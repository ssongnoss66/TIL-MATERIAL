# 0214 TUE

## ๐ฅฒ Managing Tables

### @ Introduction

DDL (Data Definition Language) ; ๋ฐ์ดํฐ์ ๊ธฐ๋ณธ ๊ตฌ์กฐ ๋ฐ ํ์ ๋ณ๊ฒฝ (keyword ; CREATE, DROP, ALTER)

### 1. Create a table

- **CREATE TABLE** statement ; ํ์ด๋ธ ์์ฑ

  - syntax

    ```sql
    CREATE TABLE table_name (
      column_1 data_type,
      column_2 data_type,
      ...,
      constraints
    );
    ```

      - ๊ฐ ํ๋์ ์ ์ฉํ  **๋ฐ์ดํฐ ํ์ (data type)** ์์ฑ

      - ํ์ด๋ธ ๋ฐ ํ๋์ ๋ํ **์ ์ฝ์กฐ๊ฑด (constrainsts)** ์์ฑ
  
  - examples

    ![CREATETABLE](https://user-images.githubusercontent.com/121418205/218608124-8c4d37b8-d46b-49ea-84bf-90128c0919c4.jpg)

    ```sql
    CREATE TABLE examples (
      examId INT AUTO_INCREMENT,
      lastName VARCHAR(50) NOT NULL,
      firstName VARCHAR(50) NOT NULL,
      PRIMARY KEY (examId)
    )

    --Table ๊ตฌ์กฐ ํ์ธ
    SHOW COLUMNS FROM examples;
    ```

      - INT, VARCHAR(50) ; ๋ฐ์ดํฐ ํ์

      - NOT NULL, PRIMARY KEY ; ์ ์ฝ ์กฐ๊ฑด

      - AUTO_INCREMENT ; ์์ฑ

@ Data Type

  - Numeric ์ซ์ํ ; INT, FLOAT ...

  - String ๋ฌธ์ํ ; VARCHAR, TEXT ...

  - Date adn Time ๋ ์งํ ; DATE, DATETIME ...

@ Constraint

  - ๋ฐ์ดํฐ **๋ฌด๊ฒฐ์ฑ**(์ ํ์ฑ๊ณผ ์ผ๊ด์ฑ ๋ณด์ฆ)์ ์งํค๊ธฐ ์ํด ๋ฐ์ดํฐ๋ฅผ ์๋ ฅ๋ฐ์ ๋ ์คํํ๋ ๊ฒ์ฌ ๊ท์น

  - ์ข๋ฅ

    - PRIMARY KEY ; ํด๋น ํค๋ฅผ ๊ธฐ๋ณธ ํค๋ก ์ง์ 

    - NOT NULL ; ํด๋น ํ๋์ NULL ๊ฐ ์ ์ฅํ์ง ๋ชปํ๋๋ก ์ง์ 

@ Attribute

  - AUTO_INCREMENT attribute
  
    - ํ์ด๋ธ์ ๊ธฐ๋ณธ ํค์ ๋ํ ๋ฒํธ ์๋ ์์ฑ

    - ํน์ง 

      - ๊ธฐ๋ณธ ํค ํ๋์ ์ฌ์ฉ ; ๊ณ ์ ํ ์ซ์๋ฅผ ๋ถ์ฌ

      - ์์ ๊ฐ์ **1** ; ๋ฐ์ดํฐ ์๋ ฅ ์ ๊ฐ ์๋ตํ๋ฉด **์๋์ผ๋ก 1 ์ฆ๊ฐ**

      - ์ด๋ฏธ ์ฌ์ฉํ ๊ฐ ์ฌ์ฌ์ฉ X

      - ๊ธฐ๋ณธ์ ์ผ๋ก NOT NULL ์ ์ฝ ์กฐ๊ฑด ํฌํจ

### 2. Delete a table

- **DROP TABLE** statement ; ํ์ด๋ธ ์ญ์ 

  - syntax

    ```sql
    DROP TABLE table_name;
    ```

      - DROP TABLE statement ์ดํ ์ญ์ ํ  ํ์ด๋ธ ์ด๋ฆ ์์ฑ

  - examples

    ```sql
    DROP TABLE examples;
    ```

### 3. Modifying table fields

- **ALTER TABLE** statement ; ํ์ด๋ธ ํ๋ ์กฐ์ (์์ฑ, ์์ , ์ญ์ )

  - ALTER TABLE **ADD** ; ํ๋ ์ถ๊ฐ

    - syntax

      ```sql
      ALTER TABLE
        table_name
      ADD
        new_column_name column_definition;
      ```

        - ADD ํค์๋ ์ดํ ์ถ๊ฐํ๊ณ ์ ํ๋ **์ ํ๋ ์ด๋ฆ**๊ณผ **๋ฐ์ดํฐ ํ์ ๋ฐ ์ ์ฝ ์กฐ๊ฑด** ์์ฑ

    - practice #1 ; examples ํ์ด๋ธ์ country ํ๋ ์ถ๊ฐ (๋จ, ๊ฐ๋ณ๊ธธ์ด ๋ฌธ์์ด ์ต๋ 100์ / NULL ๊ฐ ํ์ฉ X)

      ```sql
      ALTER TABLE
        examples
      ADD
        country VARCHAR(100) NOT NULL;
      ```

    - practice #2 ; examples ํ์ด๋ธ์ age์ address ํ๋ ์ถ๊ฐ (๋จ, age ํ๋๋ ์ ์ ํ์ / NULL ๊ฐ ํ์ฉ X & address ํ๋๋ ๊ฐ๋ณ๊ธธ์ด ๋ฌธ์์ด ์ต๋ 100์ / NULL ๊ฐ ํ์ฉ X)

      ```sql
      ALTER TABLE
        examples
      ADD
        age INT NOT NULL,
      ADD
        address VARCHAR(100) NOT NULL;
      ```

  - ALTER TABLE **MODIFY** ; ํ๋ ์์ฑ ๋ณ๊ฒฝ

    - syntax

      ```sql
      ALTER TABLE
        table_name
      MODIFY
        column_name column_definition;
      ```

        - MODIFY ํค์๋ ์ดํ **๋ณ๊ฒฝํ๊ณ ์ ํ๋ ํ๋ ์ด๋ฆ**๊ณผ **๋ฐ์ดํฐ ํ์ ๋ฐ ์ ์ฝ ์กฐ๊ฑด** ์์ฑ

    - practice #1 ; examples ํ์ด๋ธ์ address ํ๋๋ฅผ ๊ฐ๋ณ๊ธธ์ด ๋ฌธ์์ด ์ต๋ 50์๊น์ง ๊ทธ๋ฆฌ๊ณ  NULL ๊ฐ ํ์ฉํ์ง ์๋๋ก ๋ณ๊ฒฝ

      ```sql
      ALTER TABLE
        examples
      MODIFY
        address VARCHAR(50) NOT NULL;
      ```
    
    - practice #2 ; examples ํ์ด๋ธ์ lastName, firstName ํ๋๋ฅผ ๊ฐ๋ณ๊ธธ์ด ๋ฌธ์์ด ์ต๋ 10์๊น์ง ๊ทธ๋ฆฌ๊ณ  NULL ๊ฐ ํ์ฉํ์ง ์๋๋ก ๋ณ๊ฒฝ

      ```sql
      ALTER TABLE
        examples
      MODIFY
        lastName VARCHAR(10) NOT NULL,
      MODIFY
        firstName VARCHAR(10) NOT NULL;
      ```

  - ALTER TABLE **CHANGE COLUMN** ; ํ๋ ์ด๋ฆ ๋ณ๊ฒฝ

    - syntax

      ```sql
      ALTER TABLE
        table_name
      CHANGE COLUMN
        original_name new_name column_definition;
      ```

        - CHANGE COLUMN ํค์๋ ์ดํ **๊ธฐ์กด ํ๋ ์ด๋ฆ**๊ณผ **๋ณ๊ฒฝํ๊ณ ์ ํ๋ ํ๋ ์ด๋ฆ** ๊ทธ๋ฆฌ๊ณ  **๋ฐ์ดํฐ ํ์ ๋ฐ ์ ์ฝ์กฐ๊ฑด** ์์ฑ

    - practice #1 ; examples ํ์ด๋ธ์ country ํ๋ ์ด๋ฆ์ state๋ก ๋ณ๊ฒฝ (๋จ, ๋ฐ์ดํฐ ํ์ ๋ฐ ์ ์ฝ ์กฐ๊ฑด์ ๊ธฐ์กด๊ณผ ๋์ผ)

      ```sql
      ALTER TABLE
        examples
      CHANGE COLUMN
        country state VARCHAR(100) NOT NULL;
      ```
  - ALTER TABLE **DROP COLUMN** ; ํ๋ ์ญ์ 

    - syntax

      ```sql
      ALTER TABLE
        table_name
      DROP COLUMN
        column_name;
      ```

        - DROP COLUMN ํค์๋ ์ดํ ์ญ์ ํ๊ณ ์ ํ๋ ํ๋ ์ด๋ฆ ์์ฑ

    - practice #1 ; examples ํ์ด๋ธ์ address ํ๋ ์ญ์ 

      ```sql
      ALTER TABLE
        examples
      DROP COLUMN
        address;
      ```
    
    - practice #2 ; examples ํ์ด๋ธ์ state์ age ํ๋ ์ญ์ 

      ```sql
      ALTER TABLE
        examples
      DROP COLUMN
        state,
      DROP COLUMN
        age;
      ```

> ๋ฐ๋์ NOT NULL ์ ์ฝ์ ์ฌ์ฉํ๋ ๊ฒ์ ์๋๋ค!

  - ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ์ฌ์ฉํ๋ ํ๋ก๊ทธ๋จ์ ๋ฐ๋ผ NULL์ ์ ์ฅํ  ํ์๊ฐ ์๋ ๊ฒฝ์ฐ ๋ง์์ NOT NULL๋ก ์ ์

  - ๊ฐ์ด ์๋ค๋ ํํ์ ํ์ด๋ธ์ ๊ธฐ๋กํ๋ ๊ฒ์ 0์ด๋ ๋น ๋ฌธ์์ด ๋ฑ์ ์ฌ์ฉํ๋ ๊ฒ์ผ๋ก ๋์ฒด

## ๐ฅธ Modifying Data

### @ Introduction

DML (Data Manipulation Language) ; ๋ฐ์ดํฐ ์กฐ์ (์ถ๊ฐ, ์์ , ์ญ์ ) (keyword ; INSERT, UPDATE, DELETE)

### 1. Insert data into table

- **INSERT** statement ; ํ์ด๋ธ ๋ ์ฝ๋ ์ฝ์

  - syntax

    ```sql
    INSERT INTO table_name (c1, c2, ...)
    VALUES (v1, v2, ...);
    ```

      - INSERT INTO ์  ๋ค์์ ํ์ด๋ธ ์ด๋ฆ๊ณผ ๊ดํธ ์์ ํ๋ ๋ชฉ๋ก์ ์์ฑ

      - VALUES ํค์๋ ๋ค์ ๊ดํธ ์์ ํด๋น ํ๋์ ์ฝ์ํ  ๊ฐ ๋ชฉ๋ก์ ์์ฑ

  - practice #1 ; articles ํ์ด๋ธ์ ๊ฐ ํ๋์ ์ ํฉํ ๋ฐ์ดํฐ ์๋ ฅ (createdAt ํ๋ ๊ฐ์ 2000๋ 1์ 1์ผ์ด๋ฉฐ title๊ณผ content ํ๋ ๊ฐ์ ์์จ)

    ```sql
    INSERT INTO
      articles (title, content, createdAt)
    VALUES
      ('hello', 'world', '2000-01-01');
    ```
  
  - practice #2 ; articles ํ์ด๋ธ์ ๊ฐ ํ๋์ ์ ํฉํ ๋ฐ์ดํฐ๋ฅผ 3๊ฐ ์๋ ฅ (๋ชจ๋  ํ๋ ๊ฐ์ ์์จ)

    ```sql
    INSERT INTO
      articles (title, content, createdAt)
    VALUES
      ('title1', 'content1', '1900-01-01'),
      ('title2', 'content2', '1800-01-01'),
      ('title3', 'content3', '1700-01-01');
    ```

  - practice #3 ; articles ํ์ด๋ธ์ ๊ฐ ํ๋์ ์ ํฉํ ๋ฐ์ดํฐ ์๋ ฅ (createdAt ํ๋์๋ ํ์ฌ ์์ฑํ๋ ๋ ์ง๊ฐ ์๋์ผ๋ก ์๋ ฅ ๋๋จธ์ง ํ๋ ์์จ)

    ```sql
    INSERT INTO
      articles(title, content, createdAt)
    VALUES
      ('mytitle', 'mycontent', CURDATE());
    ```

      - CURDATE() ; ํ์ฌ ๋ ์ง ๋ฐํ (MySQL ์ ๊ณต Date Functions ์ค ํ๋)
  
### 2. Update data in table

- **UPDATE** statement ; ํ์ด๋ธ ๋ ์ฝ๋ ์์ 

  - syntax

    ```sql
    UPDATE table_name
    SET column_name = expression,
    [WHERE
      condition];
    ```

      - SET ์  ๋ค์์ ์์ ํ  ํ๋์ ์ ๊ฐ ์ง์ 

      - WHERE ์ ์์ ์์ ํ  ๋ ์ฝ๋๋ฅผ ์ง์ ํ๋ ์กฐ๊ฑด ์์ฑ (์์ฑํ์ง ์์ผ๋ฉด ๋ชจ๋  ๋ ์ฝ๋ ์์ )

  - practice #1 ; articles ํ์ด๋ธ ๋ ์ฝ๋์ title ํ๋ ๊ฐ์ 'newTitle'๋ก ๋ณ๊ฒฝ

    ```sql
    UPDATE
      articles
    SET
      title = 'newTitle'
    WHERE
      id = 1;
    ```

  - practice #2 ; articles ํ์ด๋ธ 2๋ฒ ๋ ์ฝ๋์ title, content ํ๋ ๊ฐ์ ์์ ๋กญ๊ฒ ๋ณ๊ฒฝ

    ```sql
    UPDATE
      articles
    SET
      title = 'newTitle',
      content = 'newContent'
    WHERE
      id = 2;
    ```

  - practice #3 ; articles ํ์ด๋ธ ๋ชจ๋  ๋ ์ฝ๋์ content ํ๋ ๊ฐ ์ค ๋ฌธ์์ด 'content'๋ฅผ 'TEST'๋ก ๋ณ๊ฒฝ

    ```sql
    UPDATE
      articles
    SET
      content = REPLACE(content, 'contest', 'TEST');
    ```

      - REPLACE() ; ์ง์ ๋ ๋ฌธ์์ด ๋ณ๊ฒฝ (MySQL ์ ๊ณต String Functions ์ค ํ๋)

### 3. Delete data from table

- **DELETE** statement ; ํ์ด๋ธ ๋ ์ฝ๋ ์ญ์ 

  - syntax

    ```sql
    DELETE FROM table_name
    [WHERE
      condition];
    ```

      - DELETE FROM ์  ๋ค์์ ํ์ด๋ธ ์ด๋ฆ ์์ฑ

      - WHERE ์ ์์ ์ญ์ ํ  ๋ ์ฝ๋ ์ง์ ํ๋ ์กฐ๊ฑด ์์ฑ (์์ฑํ์ง ์์ผ๋ฉด ๋ชจ๋  ๋ ์ฝ๋ ์ญ์ )

  - practice #1 ; articles ํ์ด๋ธ์ 1๋ฒ ๋ ์ฝ๋ ์ญ์ 

    ```sql
    DELETE FROM
      articles
    WHERE
      id = 1;
    ```
  
  - practice #2 ; articles ํ์ด๋ธ์์ ๊ฐ์ฅ ์ต๊ทผ์ ์์ฑ๋ ๋ ์ฝ๋ 2๊ฐ ์ญ์ 

    ```sql
    DELETE FROM
      articles
    ORDER BY
      createdAt DESC
    LIMIT 2;
    ```