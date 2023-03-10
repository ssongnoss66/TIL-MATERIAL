# 0209 THU

## ๐ถโ๐ซ๏ธ SQL Basics

### @ Introduction

- SQL (Structure Query Language)

  - ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ ๋ณด๋ฅผ ์ ์ฅํ๊ณ  ์ฒ๋ฆฌํ๊ธฐ ์ํ ํ๋ก๊ทธ๋๋ฐ ์ธ์ด

  - ํ์ด๋ธ์ ํํ๋ก **๊ตฌ์กฐํ**๋ ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค์๊ฒ ์์ฒญ์ **์ง์(์์ฒญ)**

  - ์ปดํจํฐ์์ ๋ํ -> ํ๋ก๊ทธ๋๋ฐ ์ธ์ด / ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค์์ ๋ํ -> SQL

- SQL Syntax

  ```SQL
  SELECT age FROM solar_system WHERE name = 'earth';
  ```

  - SQL ํค์๋๋ ๋์๋ฌธ์ ๊ตฌ๋ถ X ; but ๋๋ฌธ์ ์์ฑ ๊ถ์ฅ (๋ช์์  ๊ตฌ๋ถ)

  - ๊ฐ SQL Statements ๋์๋ ์ธ๋ฏธ์ฝ๋ก (;) ํ์ ; ๊ฐ SQL Statements ๊ตฌ๋ถํ๋ ๋ฐฉ๋ฒ

### @ SQL Statements

- SQL ์ธ์ด๋ฅผ ๊ตฌ์ฑํ๋ ๊ฐ์ฅ ๊ธฐ๋ณธ์ ์ธ ์ฝ๋ ๋ธ๋ก

  ```SQL
  SELECT column_name FROM table_name;
  ```
  - SELECT Statement

  - SELECT, FROM 2๊ฐ์ keyword๋ก ๊ตฌ์ฑ๋จ

- ์ ํ

  - DDL (๋ฐ์ดํฐ ์ ์)

    - ๋ฐ์ดํฐ์ ๊ธฐ๋ณธ ๊ตฌ์กฐ ๋ฐ ํ์ ๋ณ๊ฒฝ

    - ํค์๋ ; CREATE, DROP, ALTER

  - DQL (๋ฐ์ดํฐ ๊ฒ์)

    - ํค์๋ ; SELECT

  - DML (๋ฐ์ดํฐ ์กฐ์)

    - ๋ฐ์ดํฐ ์ถ๊ฐ, ์์ , ์ญ์ 

    - ํค์๋ ; INSERT, UPDATE, DELETE

  - DCL (๋ฐ์ดํฐ ์ ์ด)

    - ๋ฐ์ดํฐ ๋ฐ ์์์ ๋ํ ์ฌ์ฉ์ ๊ถํ ์ ์ด

    - ํค์๋ ; COMMIT, ROLLBACK, GRANT, REVOKE

### @ ์ฉ์ด ์ ๋ฆฌ

- Query

  - ์ง์, ์ง๋ฌธ

  - "๋ฐ์ดํฐ๋ฒ ์ด์ค๋ก๋ถํฐ ์ ๋ณด๋ฅผ ์์ฒญ" ํ๋ ๊ฒ

  - ์ผ๋ฐ์ ์ผ๋ก SQL๋ก ์์ฑํ๋ ์ฝ๋๋ฅผ ์ฟผ๋ฆฌ๋ฌธ(SQL๋ฌธ)์ด๋ผ ํจ

- SQL ํ์ค

  - SQL์ ๋ฏธ๊ตญ ๊ตญ๋ฆฝ ํ์ค ํํ(ANSI)์ ๊ตญ์  ํ์คํ ๊ธฐ๊ตฌ(ISO)์ ์ํด ํ์ค ์ฑํ

  - ๋ชจ๋  RDBMS์์ SQL ํ์ค์ ์ง์ํ๋ RDBMS๋ณ๋ก ๋์์ ์ธ ๊ธฐ๋ฅ์ ๋ฐ๋ผ ํ์ค ๋ฒ์ด๋๋ ๋ฌธ๋ฒ ์กด์ฌ

## ๐ SQL Single Table Queries

### @ Querying data

- SELECT statement ; ํ์ด๋ธ์์ ๋ฐ์ดํฐ๋ฅผ ์กฐํ

- SELECT syntax

    ```SQL
    SELECT
      select_list
    FROM
      table_name;
    ```
    - SELCT ํค์๋ ๋ค์์ ๋ฐ์ดํฐ๋ฅผ ์ ํํ๋ ค๋ ํ๋๋ฅผ ํ๋ ์ด์ ์ง์ 

    - FROM ํค์๋ ๋ค์์ ๋ฐ์ดํฐ๋ฅผ ์ ํํ๋ ค๋ ํ์ด๋ธ์ ์ด๋ฆ์ ์ง์ 

- SELECT examples

  - #1 ํ์ด๋ธ employees์์ lastName ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ ์กฐํ

    ```SQL
    SELECT
      lastname
    FROM
      employees;
    ```

  - #2 ํ์ด๋ธ employees์์ lastName, firstName ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ ์กฐํ

    ```SQL
    SELECT
      lastName, firstName
    FROM
      employees;
    ```

  - #3 ํ์ด๋ธ employees์์ ๋ชจ๋  ํ๋์ ๋ฐ์ดํฐ ์กฐํ

    ```SQL
    SELECT
      *
    FROM
      employees;
    ```

  - #4 ํ์ด๋ธ employees์์ firstName ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ ์กฐํ ('์ด๋ฆ'์ผ๋ก ์ถ๋ ฅ๋  ์ ์๋๋ก ๋ณ๊ฒฝ)

    - **AS keyword** ; ํ๋์ ์๋ก์ด ๋ณ์นญ ์ง์ 

    ```SQL
    SELECT
      firstName AS '์ด๋ฆ'
    FROM
      employees
    ```

  - #5 ํ์ด๋ธ orderdetails์์ productCode, ์ฃผ๋ฌธ ์ด์ก ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ ์กฐํ (์ฃผ๋ฌธ ์ด์ก ํ๋๋ quantityOrdered์ priceEach ํ๋๋ฅผ ๊ณฑํ ๊ฒฐ๊ณผ๊ฐ)

    - **Arithmetic Operators** ; ๊ธฐ๋ณธ์  ์ฌ์น์ฐ์ฐ ์ฌ์ฉ ๊ฐ๋ฅ

    ```SQL
    SELECT
      productcode,
      (quantityOrdered * priceEach) AS '์ฃผ๋ฌธ ์ด์ก'
    FROM
      orderdetails;
    ```

### @ Sorting data

- ORDER BY clause ; ์กฐํ ๊ฒฐ๊ณผ์ ๋ ์ฝ๋ ์ ๋ ฌ

- ORDER BY syntax

    ```SQL
    SELECT
      select_list
    FROM
      table_name
    ORDER BY
      column1 [ASC:DESC],
      column2 [ASC:DESC],
      ...;
    ```

    - FROM clause ๋ค์ ์์น

    - ํ๋ ์ด์์ ์ปฌ๋ผ์ ๊ธฐ์ค์ผ๋ก ๊ฒฐ๊ณผ๋ฅผ ์ค๋ฆ์ฐจ์, ๋ด๋ฆผ์ฐจ์ ์ ๋ ฌ

      - ASC ; ์ค๋ฆ์ฐจ์ (๊ธฐ๋ณธ ๊ฐ) / DESC ; ๋ด๋ฆผ์ฐจ์

- ORDER BY examples

  - #1 ํ์ด๋ธ employees์์ firstName ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ๋ฅผ ์ค๋ฆ์ฐจ์์ผ๋ก ์กฐํ

    ```SQL
    SELECT
      firstName
    FROM
      employees
    ORDER BY
      firstName;
    ```
  - #2 ํ์ด๋ธ employees์์ firstName ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ๋ฅผ ๋พ์ฐจ์์ผ๋ก ์กฐํ

    ```SQL
    SELECT
      firstName
    FROM
      employees
    ORDER BY
      firstName DESC;
    ```
  
  - #3 ํ์ด๋ธ employees์์ lastName ํ๋๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ด๋ฆผ์ฐจ์์ผ๋ก ์ ๋ ฌํ ๋ค์ firstName ํ๋ ๊ธฐ์ค์ผ๋ก ์ค๋ฆ์ฐจ์ ์ ๋ ฌํ์ฌ ์กฐํ

    ```SQL
    SELECT
      lastName, firstName
    FROM
      employees
    ORDER BY
      lastName DESC,
      firstName;
    ```
  
  - #4 ํ์ด๋ธ orderdetails์์ totalSales ํ๋๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ด๋ฆผ์ฐจ์์ผ๋ก ์ ๋ ฌํ ๋ค์ productCode, totalSales ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ ์กฐํ (totalSales ํ๋๋ quantityOrdered์ priceEach ํ๋ ๊ณฑํ ๊ฐ)

    ```SQL
    SELECT
      productCode,
      (quantityOrdered * priceEach) AS 'totalSales'
    FROM
      orderdetails
    ORDER BY
      totalSales DESC;
    ```
  
> SELECT statement ์คํ ์์ ; FROM -> SELECT -> ORDER BY

1. ํ์ด๋ธ์์ (FROM) 2. ์กฐํํ์ฌ (SELECT) 3. ์ ๋ ฌ (ORDER BY)
