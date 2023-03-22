# 🤓 Transactions

- (모두 성공 혹은 모두 실패하는) 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법

- 쪼개질 수 없는 업무처리의 단위 (All or Nothing)

- 예시 ; 계좌이체 (인출 & 입금) > 송금 중 알 수 없는 문제로 인출에는 성공했는데 입금에 실패한다면? 둘 다 성공해야 거래 승인 / 문제 발생 시 없었던 거래로 만들어야 > 모두 성공 또는 모두 실패!

- Syntax

  ```sql
  START TRANSACTION;
  state_ments;
  ...
  [ROLLBACK:COMMIT];
  ```

    - START TRANSACTION ; 트랜잭션 구문의 시작 알림

    - COMMIT ; 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영

    - ROLLBACK ; 부분적으로 작업 실패 시 트랜잭션에서 진행한 모든 연산 취소 > 트랜잭션 실행 전으로 되돌림

- 원리

  ![Transaction원리](https://user-images.githubusercontent.com/121418205/220011181-db918e94-bbed-4630-9776-11443929b6c9.jpg)

- practice

  - #0 ; MySQL은 자동으로 변경 사항 COMMIT > 자동 COMMIT 하지 않도록 사전 설정

    ```sql
    -- 자동 COMMIT 비활성화
    SET autocommit = 0;

    -- users 테이블 생성
    CREATE TABLE users (
      id INT AUTO_INCREMENT,
      name VARCHAR(10) NOT NULL,
      PRIMARY KEY (id)
    );
    ```
  
  - #1 ; 트랜잭션을 사용해 users 테이블에 데이터 삽입 > ROLLBACK 했을 때와 COMMIT 했을 때 users 테이블 상태 비교

    ```sql
    -- ROLLBACK
    START TRANSACTION;

    INSERT INTO users (name)
    VALUES ('james'), ('mary');

    SELECT * FROM users;

    ROLLBACK;

    SELECT * FROM users;

    -- COMMIT
    START TRANSACTION;

    INSERT INTO users (name)
    VALUES ('james'), ('mary');

    SELECT * FROM users;

    COMMIT;

    SELECT * FROM users;
    ```

# 🫢 Triggers

- (INSERT, UPDATE, DELETE 등) 특정 이벤트에 대한 응답으로 자동으로 실행되는 것 

- 1️⃣ 을 추가/수정/삭제한 후에 **2️⃣ 하겠다 < 이게 Trigger**

- Syntax

  ```sql
  CREATE TRIGGER trigger_name
    {BEFORE : AFTER} {INSERT:UPDATE:DELETE}
    ON table_name FOR EACH ROW
    trigger_body;
  ```

    - CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름 지정

    - 각 레코드의 어느 시점에 트리거가 실행될 지 지정 (삽입, 수정, 삭제 전후)

    - ON 키워드 뒤에 트리거가 속한 테이블 이름 지정

    - 트리거 활성화될 때 실행할 코드를 trigger_body에 지정 ; 명령문 여러 개 일 때는 BEGIN END 키워드로 묶어서 사용

    - 트리거는 DML의 영향을 받는 필드 값에만 적용 가능

- practice

  - #1 ; 트리거를 사용해 기존 게시글이 수정되면, 게시글의 수정일자 필드 값을 최신 일자로 수정하기

    ```sql
    -- 사전 준비 / articles 테이블 작성 및 예시 데이터 입력
    CREATE TABLE articles (
      id INT AUTO_INCREMENT,
      title VARCHAR(100) NOT NULL,
      createdAt DATETIME NOT NULL,
      updateAt DATETIME NOT NULL,
      PRIMARY KEY (id)
    );

    INSERT INTO articles (title, createdAt, updatedAt)
    VALUES ('title1', CURRENT_TIEM(), CURRENT_TIME());

    DELIMITER //
    CREATE TRIGGER beforeArticleUpdate
      BEFORE UPDATE
      ON articles FOR EACH ROW
    BEGIN
      SET NEW.updatedAt = CURRENT_TIME();
    END//
    DELIMITER ;
    ```

      - DELIMITER // DELIMITER
      
        - SQL의 구문 문자(;)를 변경

        - BEGIN-END 구문 사이에 여러 SQL 문이 작성되기 때문에 하나의 트리거로써 작동되도록 사용
  
      - BEGIN END//

        - 하나 이상의 구문 목록 표현

        - BEGIN과 END 키워드로 둘러싸는 다중 구문 구성

      - NEW.

        - 트리거에서 특정 시점 전후의 값에 접근할 수 있도록 제공하는 키워드

        - OLD와 NEW 두 개 제공

          ![OLDNEW](https://user-images.githubusercontent.com/121418205/220036680-cb6a0687-1eec-479b-86bd-a3bcae08d535.jpg)

  - #2 ; 트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 해당 게시글이 작성되었다는 것을 기록하기

    ```sql
    -- 사전준비 / articles 테이블 작성 및 예시 데이터 입력
    CREATE TABLE articleLogs (
      id INT AUTO_INCREMENT,
      description VARCHAR(100) NOT NULL,
      createdAt DATETIME NOT NULL,
      PRIMARY KEY (id)
    );

    DELIMITER //
    CREATE TRIGGER recordLogs
      AFTER INSERT
      ON articles FOR EACH ROW
    BEGIN
      INSERT INTO articleLogs (description, createdAt)
      VALUES ('글이 작성되었습니다.', CURRENT_TIME());
    END//
    DELIMITER;

    -- 풀이 확인

    INSERT INTO articles (title, createdAt, updatedAt)
    VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

    SELECT * FROM articleLogs;
    ```
  
  - #2 심화 ; 트리거를 사용해 기존 게시글이 작성되면, 별도의 테이블에 몇 번 게시글이 작성되었다는 것을 기록하기

    ```sql
    DELIMITER //
    CREATE TRIGGER recordLogs
      AFTER INSERT
      ON articles FOR EACH ROW
    BEGIN
      INSERT INTO articleLogs (description, createdAt)
      VALUES (CONCAT(NEW.id, '번 글이 작성되었습니다.'), CURRENT_TIME());
    END//
    DELIMITER;
    ```

  - #3 ; 트리거를 사용해 기존 게시글이 삭제되면, 삭제된 게시글의 구조 그대로 별도의 테이블에 기록하기

    ```sql
    -- 사전 준비
    CREATE TABLE backupArticles (
      id INT AUTO_INCREMENT,
      title VARCHAR(100) NOT NULL,
      createdAt DATETIME NOT NULL,
      updatedAt DATETIME NOT NULL,
      PRIMARY KEY(id)
    );

    DELIMITER //
    CREATE TRIGGER backupLogs
      AFTER DELETE
      ON articles FOR EACH ROW
    BEGIN
      INSERT INTO backupArticles (title, createdAt, updatedAt)
      VALUES (OLD.title, OLD.createdAt, OLD.updatedAt);
    END//
    DELIMITER;

    -- 풀이 확인
    DELETE FROM articles
    WHERE id = 1;

    SELECT * FROM backupArticles;
    ```