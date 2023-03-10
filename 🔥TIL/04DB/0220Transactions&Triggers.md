# 0220 MON

## π€ Transactions

- (λͺ¨λ μ±κ³΅ νΉμ λͺ¨λ μ€ν¨νλ) μ¬λ¬ μΏΌλ¦¬λ¬Έμ λ¬Άμ΄μ νλμ μμμ²λΌ μ²λ¦¬νλ λ°©λ²

- μͺΌκ°μ§ μ μλ μλ¬΄μ²λ¦¬μ λ¨μ (All or Nothing)

- μμ ; κ³μ’μ΄μ²΄ (μΈμΆ & μκΈ) > μ‘κΈ μ€ μ μ μλ λ¬Έμ λ‘ μΈμΆμλ μ±κ³΅νλλ° μκΈμ μ€ν¨νλ€λ©΄? λ λ€ μ±κ³΅ν΄μΌ κ±°λ μΉμΈ / λ¬Έμ  λ°μ μ μμλ κ±°λλ‘ λ§λ€μ΄μΌ > λͺ¨λ μ±κ³΅ λλ λͺ¨λ μ€ν¨!

- Syntax

  ```sql
  START TRANSACTION;
  state_ments;
  ...
  [ROLLBACK:COMMIT];
  ```

    - START TRANSACTION ; νΈλμ­μ κ΅¬λ¬Έμ μμ μλ¦Ό

    - COMMIT ; λͺ¨λ  μμμ΄ μ μμ μΌλ‘ μλ£λλ©΄ νκΊΌλ²μ DBμ λ°μ

    - ROLLBACK ; λΆλΆμ μΌλ‘ μμ μ€ν¨ μ νΈλμ­μμμ μ§νν λͺ¨λ  μ°μ° μ·¨μ > νΈλμ­μ μ€ν μ μΌλ‘ λλλ¦Ό

- μλ¦¬

  ![Transactionαα―α«αα΅](https://user-images.githubusercontent.com/121418205/220011181-db918e94-bbed-4630-9776-11443929b6c9.jpg)

- practice

  - #0 ; MySQLμ μλμΌλ‘ λ³κ²½ μ¬ν­ COMMIT > μλ COMMIT νμ§ μλλ‘ μ¬μ  μ€μ 

    ```sql
    -- μλ COMMIT λΉνμ±ν
    SET autocommit = 0;

    -- users νμ΄λΈ μμ±
    CREATE TABLE users (
      id INT AUTO_INCREMENT,
      name VARCHAR(10) NOT NULL,
      PRIMARY KEY (id)
    );
    ```
  
  - #1 ; νΈλμ­μμ μ¬μ©ν΄ users νμ΄λΈμ λ°μ΄ν° μ½μ > ROLLBACK νμ λμ COMMIT νμ λ users νμ΄λΈ μν λΉκ΅

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

## π«’ Triggers

- (INSERT, UPDATE, DELETE λ±) νΉμ  μ΄λ²€νΈμ λν μλ΅μΌλ‘ μλμΌλ‘ μ€νλλ κ² 

- 1οΈβ£ μ μΆκ°/μμ /μ­μ ν νμ **2οΈβ£ νκ² λ€ < μ΄κ² Trigger**

- Syntax

  ```sql
  CREATE TRIGGER trigger_name
    {BEFORE : AFTER} {INSERT:UPDATE:DELETE}
    ON table_name FOR EACH ROW
    trigger_body;
  ```

    - CREATE TRIGGER ν€μλ λ€μμ μμ±νλ €λ νΈλ¦¬κ±°μ μ΄λ¦ μ§μ 

    - κ° λ μ½λμ μ΄λ μμ μ νΈλ¦¬κ±°κ° μ€νλ  μ§ μ§μ  (μ½μ, μμ , μ­μ  μ ν)

    - ON ν€μλ λ€μ νΈλ¦¬κ±°κ° μν νμ΄λΈ μ΄λ¦ μ§μ 

    - νΈλ¦¬κ±° νμ±νλ  λ μ€νν  μ½λλ₯Ό trigger_bodyμ μ§μ  ; λͺλ Ήλ¬Έ μ¬λ¬ κ° μΌ λλ BEGIN END ν€μλλ‘ λ¬Άμ΄μ μ¬μ©

    - νΈλ¦¬κ±°λ DMLμ μν₯μ λ°λ νλ κ°μλ§ μ μ© κ°λ₯

- practice

  - #1 ; νΈλ¦¬κ±°λ₯Ό μ¬μ©ν΄ κΈ°μ‘΄ κ²μκΈμ΄ μμ λλ©΄, κ²μκΈμ μμ μΌμ νλ κ°μ μ΅μ  μΌμλ‘ μμ νκΈ°

    ```sql
    -- μ¬μ  μ€λΉ / articles νμ΄λΈ μμ± λ° μμ λ°μ΄ν° μλ ₯
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
      
        - SQLμ κ΅¬λ¬Έ λ¬Έμ(;)λ₯Ό λ³κ²½

        - BEGIN-END κ΅¬λ¬Έ μ¬μ΄μ μ¬λ¬ SQL λ¬Έμ΄ μμ±λκΈ° λλ¬Έμ νλμ νΈλ¦¬κ±°λ‘μ¨ μλλλλ‘ μ¬μ©
  
      - BEGIN END//

        - νλ μ΄μμ κ΅¬λ¬Έ λͺ©λ‘ νν

        - BEGINκ³Ό END ν€μλλ‘ λλ¬μΈλ λ€μ€ κ΅¬λ¬Έ κ΅¬μ±

      - NEW.

        - νΈλ¦¬κ±°μμ νΉμ  μμ  μ νμ κ°μ μ κ·Όν  μ μλλ‘ μ κ³΅νλ ν€μλ

        - OLDμ NEW λ κ° μ κ³΅

          ![OLDNEW](https://user-images.githubusercontent.com/121418205/220036680-cb6a0687-1eec-479b-86bd-a3bcae08d535.jpg)

  - #2 ; νΈλ¦¬κ±°λ₯Ό μ¬μ©ν΄ κΈ°μ‘΄ κ²μκΈμ΄ μμ±λλ©΄, λ³λμ νμ΄λΈμ ν΄λΉ κ²μκΈμ΄ μμ±λμλ€λ κ²μ κΈ°λ‘νκΈ°

    ```sql
    -- μ¬μ μ€λΉ / articles νμ΄λΈ μμ± λ° μμ λ°μ΄ν° μλ ₯
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
      VALUES ('κΈμ΄ μμ±λμμ΅λλ€.', CURRENT_TIME());
    END//
    DELIMITER;

    -- νμ΄ νμΈ

    INSERT INTO articles (title, createdAt, updatedAt)
    VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

    SELECT * FROM articleLogs;
    ```
  
  - #2 μ¬ν ; νΈλ¦¬κ±°λ₯Ό μ¬μ©ν΄ κΈ°μ‘΄ κ²μκΈμ΄ μμ±λλ©΄, λ³λμ νμ΄λΈμ λͺ λ² κ²μκΈμ΄ μμ±λμλ€λ κ²μ κΈ°λ‘νκΈ°

    ```sql
    DELIMITER //
    CREATE TRIGGER recordLogs
      AFTER INSERT
      ON articles FOR EACH ROW
    BEGIN
      INSERT INTO articleLogs (description, createdAt)
      VALUES (CONCAT(NEW.id, 'λ² κΈμ΄ μμ±λμμ΅λλ€.'), CURRENT_TIME());
    END//
    DELIMITER;
    ```

  - #3 ; νΈλ¦¬κ±°λ₯Ό μ¬μ©ν΄ κΈ°μ‘΄ κ²μκΈμ΄ μ­μ λλ©΄, μ­μ λ κ²μκΈμ κ΅¬μ‘° κ·Έλλ‘ λ³λμ νμ΄λΈμ κΈ°λ‘νκΈ°

    ```sql
    -- μ¬μ  μ€λΉ
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

    -- νμ΄ νμΈ
    DELETE FROM articles
    WHERE id = 1;

    SELECT * FROM backupArticles;
    ```