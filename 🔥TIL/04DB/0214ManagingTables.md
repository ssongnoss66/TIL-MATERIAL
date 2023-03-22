# 🥲 Managing Tables

## @ Introduction

DDL (Data Definition Language) ; 데이터의 기본 구조 및 형식 변경 (keyword ; CREATE, DROP, ALTER)

## 1. Create a table

- **CREATE TABLE** statement ; 테이블 생성

  - syntax

    ```sql
    CREATE TABLE table_name (
      column_1 data_type,
      column_2 data_type,
      ...,
      constraints
    );
    ```

      - 각 필드에 적용할 **데이터 타입 (data type)** 작성

      - 테이블 및 필드에 대한 **제약조건 (constrainsts)** 작성
  
  - examples

    ![CREATETABLE](https://user-images.githubusercontent.com/121418205/218608124-8c4d37b8-d46b-49ea-84bf-90128c0919c4.jpg)

    ```sql
    CREATE TABLE examples (
      examId INT AUTO_INCREMENT,
      lastName VARCHAR(50) NOT NULL,
      firstName VARCHAR(50) NOT NULL,
      PRIMARY KEY (examId)
    )

    --Table 구조 확인
    SHOW COLUMNS FROM examples;
    ```

      - INT, VARCHAR(50) ; 데이터 타입

      - NOT NULL, PRIMARY KEY ; 제약 조건

      - AUTO_INCREMENT ; 속성

@ Data Type

  - Numeric 숫자형 ; INT, FLOAT ...

  - String 문자형 ; VARCHAR, TEXT ...

  - Date adn Time 날짜형 ; DATE, DATETIME ...

@ Constraint

  - 데이터 **무결성**(정확성과 일관성 보증)을 지키기 위해 데이터를 입력받을 때 실행하는 검사 규칙

  - 종류

    - PRIMARY KEY ; 해당 키를 기본 키로 지정

    - NOT NULL ; 해당 필드에 NULL 값 저장하지 못하도록 지정

@ Attribute

  - AUTO_INCREMENT attribute
  
    - 테이블의 기본 키에 대한 번호 자동 생성

    - 특징 

      - 기본 키 필드에 사용 ; 고유한 숫자를 부여

      - 시작 값은 **1** ; 데이터 입력 시 값 생략하면 **자동으로 1 증가**

      - 이미 사용한 값 재사용 X

      - 기본적으로 NOT NULL 제약 조건 포함

## 2. Delete a table

- **DROP TABLE** statement ; 테이블 삭제

  - syntax

    ```sql
    DROP TABLE table_name;
    ```

      - DROP TABLE statement 이후 삭제할 테이블 이름 작성

  - examples

    ```sql
    DROP TABLE examples;
    ```

## 3. Modifying table fields

- **ALTER TABLE** statement ; 테이블 필드 조작 (생성, 수정, 삭제)

  - ALTER TABLE **ADD** ; 필드 추가

    - syntax

      ```sql
      ALTER TABLE
        table_name
      ADD
        new_column_name column_definition;
      ```

        - ADD 키워드 이후 추가하고자 하는 **새 필드 이름**과 **데이터 타입 및 제약 조건** 작성

    - practice #1 ; examples 테이블에 country 필드 추가 (단, 가변길이 문자열 최대 100자 / NULL 값 허용 X)

      ```sql
      ALTER TABLE
        examples
      ADD
        country VARCHAR(100) NOT NULL;
      ```

    - practice #2 ; examples 테이블에 age와 address 필드 추가 (단, age 필드는 정수 타입 / NULL 값 허용 X & address 필드는 가변길이 문자열 최대 100자 / NULL 값 허용 X)

      ```sql
      ALTER TABLE
        examples
      ADD
        age INT NOT NULL,
      ADD
        address VARCHAR(100) NOT NULL;
      ```

  - ALTER TABLE **MODIFY** ; 필드 속성 변경

    - syntax

      ```sql
      ALTER TABLE
        table_name
      MODIFY
        column_name column_definition;
      ```

        - MODIFY 키워드 이후 **변경하고자 하는 필드 이름**과 **데이터 타입 및 제약 조건** 작성

    - practice #1 ; examples 테이블의 address 필드를 가변길이 문자열 최대 50자까지 그리고 NULL 값 허용하지 않도록 변경

      ```sql
      ALTER TABLE
        examples
      MODIFY
        address VARCHAR(50) NOT NULL;
      ```
    
    - practice #2 ; examples 테이블의 lastName, firstName 필드를 가변길이 문자열 최대 10자까지 그리고 NULL 값 허용하지 않도록 변경

      ```sql
      ALTER TABLE
        examples
      MODIFY
        lastName VARCHAR(10) NOT NULL,
      MODIFY
        firstName VARCHAR(10) NOT NULL;
      ```

  - ALTER TABLE **CHANGE COLUMN** ; 필드 이름 변경

    - syntax

      ```sql
      ALTER TABLE
        table_name
      CHANGE COLUMN
        original_name new_name column_definition;
      ```

        - CHANGE COLUMN 키워드 이후 **기존 필드 이름**과 **변경하고자 하는 필드 이름** 그리고 **데이터 타입 및 제약조건** 작성

    - practice #1 ; examples 테이블의 country 필드 이름을 state로 변경 (단, 데이터 타입 및 제약 조건은 기존과 동일)

      ```sql
      ALTER TABLE
        examples
      CHANGE COLUMN
        country state VARCHAR(100) NOT NULL;
      ```
  - ALTER TABLE **DROP COLUMN** ; 필드 삭제

    - syntax

      ```sql
      ALTER TABLE
        table_name
      DROP COLUMN
        column_name;
      ```

        - DROP COLUMN 키워드 이후 삭제하고자 하는 필드 이름 작성

    - practice #1 ; examples 테이블의 address 필드 삭제

      ```sql
      ALTER TABLE
        examples
      DROP COLUMN
        address;
      ```
    
    - practice #2 ; examples 테이블의 state와 age 필드 삭제

      ```sql
      ALTER TABLE
        examples
      DROP COLUMN
        state,
      DROP COLUMN
        age;
      ```

> 반드시 NOT NULL 제약을 사용하는 것은 아니다!

  - 데이터베이스를 사용하는 프로그램에 따라 NULL을 저장할 필요가 없는 경우 많아서 NOT NULL로 정의

  - 값이 없다는 표현을 테이블에 기록하는 것은 0이나 빈 문자열 등을 사용하는 것으로 대체

# 🥸 Modifying Data

## @ Introduction

DML (Data Manipulation Language) ; 데이터 조작 (추가, 수정, 삭제) (keyword ; INSERT, UPDATE, DELETE)

## 1. Insert data into table

- **INSERT** statement ; 테이블 레코드 삽입

  - syntax

    ```sql
    INSERT INTO table_name (c1, c2, ...)
    VALUES (v1, v2, ...);
    ```

      - INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성

      - VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성

  - practice #1 ; articles 테이블에 각 필드에 적합한 데이터 입력 (createdAt 필드 값은 2000년 1월 1일이며 title과 content 필드 값은 자율)

    ```sql
    INSERT INTO
      articles (title, content, createdAt)
    VALUES
      ('hello', 'world', '2000-01-01');
    ```
  
  - practice #2 ; articles 테이블에 각 필드에 적합한 데이터를 3개 입력 (모든 필드 값은 자율)

    ```sql
    INSERT INTO
      articles (title, content, createdAt)
    VALUES
      ('title1', 'content1', '1900-01-01'),
      ('title2', 'content2', '1800-01-01'),
      ('title3', 'content3', '1700-01-01');
    ```

  - practice #3 ; articles 테이블에 각 필드에 적합한 데이터 입력 (createdAt 필드에는 현재 작성하는 날짜가 자동으로 입력 나머지 필드 자율)

    ```sql
    INSERT INTO
      articles(title, content, createdAt)
    VALUES
      ('mytitle', 'mycontent', CURDATE());
    ```

      - CURDATE() ; 현재 날짜 반환 (MySQL 제공 Date Functions 중 하나)
  
## 2. Update data in table

- **UPDATE** statement ; 테이블 레코드 수정

  - syntax

    ```sql
    UPDATE table_name
    SET column_name = expression,
    [WHERE
      condition];
    ```

      - SET 절 다음에 수정할 필드와 새 값 지정

      - WHERE 절에서 수정할 레코드를 지정하는 조건 작성 (작성하지 않으면 모든 레코드 수정)

  - practice #1 ; articles 테이블 레코드의 title 필드 값을 'newTitle'로 변경

    ```sql
    UPDATE
      articles
    SET
      title = 'newTitle'
    WHERE
      id = 1;
    ```

  - practice #2 ; articles 테이블 2번 레코드의 title, content 필드 값을 자유롭게 변경

    ```sql
    UPDATE
      articles
    SET
      title = 'newTitle',
      content = 'newContent'
    WHERE
      id = 2;
    ```

  - practice #3 ; articles 테이블 모든 레코드의 content 필드 값 중 문자열 'content'를 'TEST'로 변경

    ```sql
    UPDATE
      articles
    SET
      content = REPLACE(content, 'contest', 'TEST');
    ```

      - REPLACE() ; 지정된 문자열 변경 (MySQL 제공 String Functions 중 하나)

## 3. Delete data from table

- **DELETE** statement ; 테이블 레코드 삭제

  - syntax

    ```sql
    DELETE FROM table_name
    [WHERE
      condition];
    ```

      - DELETE FROM 절 다음에 테이블 이름 작성

      - WHERE 절에서 삭제할 레코드 지정하는 조건 작성 (작성하지 않으면 모든 레코드 삭제)

  - practice #1 ; articles 테이블의 1번 레코드 삭제

    ```sql
    DELETE FROM
      articles
    WHERE
      id = 1;
    ```
  
  - practice #2 ; articles 테이블에서 가장 최근에 작성된 레코드 2개 삭제

    ```sql
    DELETE FROM
      articles
    ORDER BY
      createdAt DESC
    LIMIT 2;
    ```