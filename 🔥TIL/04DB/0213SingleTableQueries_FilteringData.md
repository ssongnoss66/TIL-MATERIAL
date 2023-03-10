# 0213 THU

## ๐ SQL Single Table Queries

### @ Introduction

**DQL (Data Query Language) ; ๋ฐ์ดํฐ ๊ฒ์ (SQL keyword ; SELECT)**

### @ Filtering data

- ๋ฐ์ดํฐ๋ฅผ ํํฐ๋งํ์ฌ ์ค๋ณต ์ ๊ฑฐ, ์กฐ๊ฑด ์ค์  ๋ฑ SQL Query๋ฅผ ์ ์ดํ๊ธฐ

- Keywords

  - Clause

    - DISTINCT clause ; ์กฐํ ๊ฒฐ๊ณผ์์ ์ค๋ณต๋ ๋ ์ฝ๋๋ฅผ ์ ๊ฑฐ

      ```SQL
      SELECT DISTINCT
        select_list
      FROM
        table_name;
      ```

      - SELECT ํค์๋ ๋ฐ๋ก ๋ค์ ์์ฑ

      - SELCT DISTINCT ํค์๋ ๋ค์์ ๊ณ ์ ํ ๊ฐ์ ์ ํํ๋ ค๋ ํ๋ ์ด์์ ํ๋ ์ง์ 

      - practice #1 ; ํ์ด๋ธ employees์์ lastName ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ ์ค๋ฆ์ฐจ์ ์กฐํ

        ```SQL
        SELECT
          lastname
        FROM
          employees
        ORDER BY
          lastName;
        ```
      
      - practice #2 ; ํ์ด๋ธ employees์์ lastName ํ๋์ ๋ชจ๋  ๋ฐ์ดํฐ ์ค๋ณต์์ด ์ค๋ฆ์ฐจ์ ์กฐํ

        ```SQL
        SELECT DISTINCT
          lastName
        FROM
          employees
        ORDER BY
          lastName;
        ```

    - WHERE clause ; ์กฐํ ์ ํน์  ๊ฒ์ ์กฐ๊ฑด์ ์ง์ 

      ```SQL
      SELECT
        select_list
      FROM
        table_name
      WHERE
        search_condition;
      ```

        - FROM clause ๋ค์ ์์น

        - search_condition์ ๋น๊ต์ฐ์ฐ์ ๋ฐ ๋ผ๋ฆฌ์ฐ์ฐ์ (AND, OR, NOT ๋ฑ) ์ฌ์ฉํ๋ ๊ตฌ๋ฌธ ์ฌ์ฉ๋จ

        - pactice #1 ; ํ์ด๋ธ employees์์ officeCode ํ๋ ๊ฐ์ด 1์ธ ๋ฐ์ดํฐ์ lastName, firstName, officeCode ์กฐํ

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode = 1;
          ```

        - practice #2 ; ํ์ด๋ธ employees์์ jobTitle ํ๋ ๊ฐ์ด 'Sales Rep'์ด ์๋ ๋ฐ์ดํฐ์ lastName, firstName, job Title ์กฐํ

          ```SQL
          SELECT
            lastName, firstName, jobTitle
          FROM
            employees
          WHERE
            jobTitle != 'Sales Rep';
          ```

        - practice #3 ; ํ์ด๋ธ employees์์ officeCode ํ๋ ๊ฐ์ด 3 ์ด์์ด๊ณ  jobTitle ํ๋ ๊ฐ์ด 'Sales Rep'์ธ ๋ฐ์ดํฐ์ lastName, firstName, officeCode, jobTitle ์กฐํ

           ```SQL
           SELECT
            lastName, firstName, officeCode, jobTitle
          FROM
            employees
          WHERE
            officeCode >= 3
            AND jobTitle = 'Sales Rep';
          ```
        
        - practice #4 ; ํ์ด๋ธ employees์์ officeCode ํ๋ ๊ฐ์ด 5 ๋ฏธ๋ง์ด๊ฑฐ๋ jobTitle ํ๋ ๊ฐ์ด 'Sales Rep'์ด ์๋ ๋ฐ์ดํฐ์ lastName, firstName, officeCode, jobTitle ์กฐํ

          ```SQL
          SELECT
            lastName, firstName, officeCode, jobTitle
          FROM
            employees
          WHERE
            officeCode < 5
            OR jobTitle != 'Sales Rep';
          ```
        
        - practice #5 ; ํ์ด๋ธ employees์์ officeCode ํ๋ ๊ฐ์ด 1 ์์ 4 ์ฌ์ด ๊ฐ์ธ ๋ฐ์ดํฐ์ lastName, firstName, officeCode ์กฐํ (1๊ณผ 4๋ฅผ ํฌํจ)

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode BETWEEN 1 AND 4;
          ```
          ๋๋
          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode >= 1
            AND officeCode <= 4;
          ```
        
        - practice #6 ; ํ์ด๋ธ employees์์ officeCode ํ๋ ๊ฐ์ด 1 ์์ 4 ์ฌ์ด ๊ฐ์ธ ๋ฐ์ดํฐ์ lastName, firstName, officeCode๋ฅผ ์ค๋ฆ์ฐจ์ ์กฐํ

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode BETWEEN 1 AND 4
          ORDER BY
            officeCode;
          ```

        - practice #7 ; ํ์ด๋ธ employees์์ officeCode ํ๋ ๊ฐ์ด 1 ๋๋ 3 ๋๋ 4 ๊ฐ์ธ ๋ฐ์ดํฐ์ lastName, firstName, officeCode ์กฐํ

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode IN (1, 3, 4);
          ```
          ๋๋
          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode = 1
            OR officeCode = 3
            OR officeCode = 4;
          ```

        - practice #8 ; ํ์ด๋ธ employees์์ officeCode ํ๋ ๊ฐ์ด 1 ๊ณผ 3 ๊ทธ๋ฆฌ๊ณ  4 ๊ฐ ์๋ ๋ฐ์ดํฐ์ lastName, firstName, officeCode ์กฐํ

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode NOT IN (1, 3, 4);
          ```

        - practice #9 ; ํ์ด๋ธ employees์์ lastName ํ๋ ๊ฐ์ด son์ผ๋ก ๋๋๋ ๋ฐ์ดํฐ์ lastName, firstName ์กฐํ

          ```SQL
          SELECT
            lastName, firstName
          FROM
            employees
          WHERE
            lastName LIKE '%son';
          ```

        - practice #10 ; ํ์ด๋ธ employees์์ firstName ํ๋ ๊ฐ์ด 4์๋ฆฌ๋ฉด์ y๋ก ๋๋๋ ๋ฐ์ดํฐ์ lastName, firstName ์กฐํ

          ```SQL
          SELECT
            lastName, firstName
          FROM
            employees
          WHERE
            firstName LIKE '___y';
          ```

    - LIMIT clause ; ์กฐํํ๋ ๋ ์ฝ๋ ์๋ฅผ ์ ํ

      ```SQL
      SELECT
        select_list
      FROM
        table_name
      LIMIT [OFFSET,] row_count;
      ```

        - LIMIT clause๋ ํ๋ ๋๋ ๋ ๊ฐ์ ์ธ์๋ฅผ ์ฌ์ฉ (0 ๋๋ ์์ ์ ์)

        - row_count๋ ์กฐํํ  ์ต๋ ๋ ์ฝ๋ ์๋ฅผ ์ง์ 

        - LIMIT & OFFSET ์์

          ![LIMIT OFFSET](https://user-images.githubusercontent.com/121418205/218443431-93712bdc-feb3-4100-9219-a0a00b046a56.jpg)

          ```SQL
          SELECT
            ..
          FROM
            ..
          LIMIT 3, 5;
          ```

        - practice #1 ; ํ์ด๋ธ customers์์ contactFirstName, creditLimit ํ๋ ๋ฐ์ดํฐ๋ฅผ creditLimit ๊ธฐ์ค ๋ด๋ฆผ์ฐจ์์ผ๋ก 7๊ฐ๋ง ์กฐํ

          ```SQL
          SELECT
            contactFirstName, creditLimit
          FROM
            customers
          ORDER BY
            creditLimit DESC
          LIMIT 7;
          ```

        - practice #2 ; ํ์ด๋ธ customers์์ contactFirstName, creditLimit ํ๋ ๋ฐ์ดํฐ๋ฅผ creditLimit ๊ธฐ์ค ๋ด๋ฆผ์ฐจ์์ผ๋ก 4๋ฒ์งธ๋ถํฐ 7๋ฒ์งธ ๋ฐ์ดํฐ๋ง ์กฐํ

          ```SQL
          SELECT
            contactFirstName, creditLimit
          FROM
            customers
          ORDER BY
            creditLimit DESC
          LIMIT 3, 4;
          ```
          ๋๋
          ```SQL
          SELECT
            contactFirstName, creditLimit
          FROM
            customers
          ORDER BY
            creditLimit DESC
          LIMIT 4 OFFSET 3;
          ```

  - Operator

    - BETWEEN

    - IN ; ๊ฐ์ด ํน์  ๋ชฉ๋ก ์์ ์๋์ง ํ์ธ

    - LIKE ; ๊ฐ์ด ํน์  ํจํด์ ์ผ์นํ๋์ง ํ์ธ with Wildcards

      - % ; **0๊ฐ ์ด์์ ๋ฌธ์์ด**๊ณผ ์ผ์นํ๋์ง ํ์ธ

      - _ ; **๋จ์ผ ๋ฌธ์**์ ์ผ์นํ๋์ง ํ์ธ

    - Comparison ; ๋น๊ต ์ฐ์ฐ์ (=, >=, <=, !=, IS, LIKE, IN, BETWEEN...AND)

    - Logical ; ๋ผ๋ฆฌ ์ฐ์ฐ์ (AND(&&), OR(::), NOT(!))

### @ Grouping data

- GROUP BY clause ; ๋ ์ฝ๋๋ฅผ ๊ทธ๋ฃนํํ์ฌ ์์ฝ๋ณธ ์์ฑ with ์ง๊ณ ํจ์ (Aggregation Functions)

    - Aggregation Functions ; ๊ฐ์ ๋ํ ๊ณ์ฐ์ ์ํํ๊ณ  ๋จ์ผํ ๊ฐ์ ๋ฐํํ๋ ํจ์ (SUM, AVG, MAX, MIN, COUNT)

    - syntax

      ```SQL
      SELECT
        c1, c2, ..., aggregate_function(ci)
      FROM
        table_name
      GROUP BY
        c1, c2, ..., cn;
      ```

        - FROM ๋ฐ WHERE ์  ๋ค์ ๋ฐฐ์น

        - GROUP BY ์  ๋ค์ ๊ทธ๋ฃนํํ  ํ๋ ๋ชฉ๋ก์ ์์ฑ

- ์ดํดํ๊ธฐ

  - jobTitle ํ๋ ๊ทธ๋ฃนํ

      ![GROUPBYแแตแแขแแกแแต1](https://user-images.githubusercontent.com/121418205/218448973-4d87fb74-2f69-48cb-bb1a-4b2b5e2cd1ed.jpg)

      ```SQL
      SELECT
        jobTitle
      FROM
        employees
      GROUP BY
        jobTitle;
      ```
  
  - COUNT ํจ์๊ฐ ๊ฐ ๊ทธ๋ฃน์ ๋ํ ์ง๊ณ๋ ๊ฐ์ ๊ณ์ฐ

      ![GROUPBYแแตแแขแแกแแต2](https://user-images.githubusercontent.com/121418205/218448965-3468ca1a-5f20-41c0-98d0-d94d7056de66.jpg)

      ```SQL
      SELECT
        jobTitle, COUNT(*)
      FROM
        employees
      GROUP BY
        jobTitle;
      ```

- practice

  - #1 ; ํ์ด๋ธ customers์์ country ํ๋๋ฅผ ๊ทธ๋ฃนํํ์ฌ ๊ฐ ๊ทธ๋ฃน์ ๋ํ creditLimit์ ํ๊ท ๊ฐ์ ๋ด๋ฆผ์ฐจ์ ์กฐํ

    ```SQL
    SELECT
      country,
      AVG(creditLimit)
    FROM
      customers
    GROUP BY
      country
    ORDER BY
      AVG(creditLimit) DESC;
    ```
    ๋๋
    ```SQL
    SELECT
      country,
      AVG(creditLimit) AS avgOfCreditLimit
    FROM
      customers
    GROUP BY
      country
    ORDER BY
      avgOfCreditLimit DESC;
    ```
  
  - #2 ; ํ์ด๋ธ customers์์ country ํ๋๋ฅผ ๊ทธ๋ฃนํํ์ฌ ๊ฐ ๊ทธ๋ฃน์ ๋ํ creditLimit์ ํ๊ท ๊ฐ์ด 80000์ ์ด๊ณผํ๋ ๋ฐ์ดํฐ๋ง ์กฐํ

    ```SQL
    SELECT
      country,
      AVG(creditLimit)
    FROM
      customers
    GROUP BY
      country
    HAVING
      AVG(creditLimit) > 80000;
    ```

      - **HAVING clause** ; ์ง๊ณ ํญ๋ชฉ์ ๋ํ ์ธ๋ถ ์กฐ๊ฑด ์ง์  (์ฃผ๋ก GROUP BY์ ํจ๊ป ์ฌ์ฉ / GROUP BY ์์ผ๋ฉด WHERE์ฒ๋ผ ๋์)

> SELECT statement ์คํ ์์ ; FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY - LIMIT

  1. ํ์ด๋ธ์์ FROM

  2. ํน์  ์กฐ๊ฑด์ ๋ง์ถฐ WHERE

  3. ๊ทธ๋ฃนํํ๊ณ  GROUP BY

  4. ๋ง์ฝ ๊ทธ๋ฃน ์ค ์กฐ๊ฑด์ด ์๋ค๋ฉด ๋ง์ถ๊ณ  HAVING

  5. ์กฐํํ์ฌ SELECT

  6. ์ ๋ ฌํ๊ณ  ORDER BY

  7. ํน์  ์์น์ ๊ฐ์ ๊ฐ์ ธ์จ๋ค LIMIT

```
์ ๋ ฌ์์์ NULL

- MySQL์์ NULL์ NULL์ด ์๋ ๊ฐ ์์ ์์น

  - NULL ๊ฐ์ด ์กด์ฌํ  ๊ฒฝ์ฐ ์ค๋ฆ์ฐจ์ ์ ๋ ฌ ์ ๊ฒฐ๊ณผ์ NULL์ด ๋จผ์  ์ถ๋ ฅ
```
```SQL
--NULL ์ ๋ ฌ ์์
SELECT
  postalCode
FROM
  customers
ORDER BY
  postalCode;
```