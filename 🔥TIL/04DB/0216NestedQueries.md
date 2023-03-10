# 0216 THU

## ๐ Introduction to Subquery

### @ subquery

- "A query inside a query" ; ๋จ์ผ ์ฟผ๋ฆฌ๋ฌธ์ ์ฌ๋ฌ ํ์ด๋ธ์ ๋ฐ์ดํฐ๋ฅผ ๊ฒฐํฉํ๋ ๋ฐฉ๋ฒ

- ์์

  - table1์์ ๊ฐ์ฅ ๋์ด๊ฐ ์ด๋ฆฐ ์ฌ๋์ ์ญ์ ํด์ผํ๋ค๋ฉด?

    ```sql
    SELECT MIN(age)
    FROM table1;
    
    DELETE FROM table1
    WHERE age = ์์์ ์ฐพ์ ๊ฐ;
    ```
    ๋ฅผ
    ```sql
    DELETE FROM table1
    WHERE age = (
      SELECT MIN(age) FROM table1
    )
    ```
    ๋ก ํํ ๊ฐ๋ฅ (WHERE age = ์ดํ๊ฐ **SUBQUERY**)

- ํน์ง

  - ์กฐ๊ฑด์ ๋ฐ๋ผ ํ๋ ์ด์์ ํ์ด๋ธ์์ ๋ฐ์ดํฐ ๊ฒ์ํ๋๋ฐ ์ฌ์ฉ

  - SELECT, FROM, WHERE, HAVING ์  ๋ฑ์์ ๋ค์ํ ๋งฅ๋ฝ์์ ์ฌ์ฉ

- practice

  - #1 ; ํ๋ฒ์ ๊ฐ์ฅ ๋ง์ ๋์ ์๋นํ ๊ณ ๊ฐ ๋ฒํธ ์กฐํ (payments ํ์ด๋ธ ํ์ฉ)

    ```sql
    SELECT customerNumber, amount
    FROM payments
    WHERE amount = (
      SELECT MIN(amount)
      FROM payments
    );
    ```

  - #2 ; ๋ฏธ๊ตญ์ ์๋ ์ฌ๋ฌด์ค์์ ๊ทผ๋ฌดํ๋ ์ง์์ ์ฑ๊ณผ ์ด๋ฆ ์กฐํ (์ง์ ์ ๋ณด๋ employees, ์ฌ๋ฌด์ค ์ ๋ณด๋ offices ํ์ด๋ธ์ ์กด์ฌ)

    ```sql
    SELECT lastName, firstName
    FROM employees
    WHERE officode IN (
      SELECT officeCode
      FROM offices
      WEHRE country = 'USA'
    );
    ```

  - #3 ; ์ฃผ๋ฌธํ ์ ์ด ์๋ ๊ณ ๊ฐ ๋ชฉ๋ก ์กฐํ (๊ณ ๊ฐ ์ ๋ณด๋ customers, ์ฃผ๋ฌธ ์ ๋ณด๋ orders ํ์ด๋ธ์ ์กด์ฌ)

    ```sql
    SELECT customerName
    FROM customers
    WHERE customerNumber NOT IN (
      SELECT DISTINCT customerNumber
      FROM orders
    );
    ```
  
  - #ad ; ์๋น๋ฅผ ํ ๊ณ ๊ฐ๋ค ์ค ํ๋ฒ์ ์ง๋ถํ ๊ธ์ก์ด ๊ฐ์ฅ ๋์ ๊ณ ๊ฐ์ customerNumber, amount, contactFirstName์ ์กฐํ (๊ณ ๊ฐ ํ์ด๋ธ์ customers, ์ง๋ถ ํ์ด๋ธ์ payments ํ์ฉ)

    - ํ์ด ํํธ 

      - payments ํ์ด๋ธ๊ณผ customers ํ์ด๋ธ์ ์กฐ์ธํ์ฌ contactFirstName, amountm, customerNumber ํ๋๋ฅผ ํฌํจํ๋ findName์ด๋ผ๋ ์ด๋ฆ์ ์๋ธ์ฟผ๋ฆฌ ์์ฑ

      - findName ์๋ธ์ฟผ๋ฆฌ์์ amount, customerNumber, contactFirstName ํ๋ ์ ํ

      - ๋๋ค๋ฅธ ์๋ธ์ฟผ๋ฆฌ ์ฌ์ฉํด์ payments ํ์ด๋ธ์์ ๊ฐ์ฅ ๋์ amount ๊ฐ ๊ฐ์ง ๋ ์ฝ๋ ์ฐพ๊ธฐ

      - findName ์๋ธ์ฟผ๋ฆฌ์์ amount ํ๋์ ๋ค๋ฅธ ์๋ธ์ฟผ๋ฆฌ์ ๊ฒฐ๊ณผ๊ฐ ์ผ์นํ๋ ๋ ์ฝ๋ ์ ํ

      - ์ต์ข์ ์ผ๋ก customerNumber, amount, contactFirstName ํ๋ ์ถ๋ ฅ
    
    ```sql
    SELECT customerNumber, amount, contactFirstName
    FROM
      (
        SELECT contactFirstName, amount, t1.customerNumber
        FROM payments AS t1
        INNER JOIN customers AS t2
          ON t1.customerNumber = t2.customerNumber
      ) AS findName
    WHERE
      amount = (SELECT(MAX(amount) FROM payments));
    ```

      - AS findName ; FROM ์ ์์ ์ฌ์ฉํ๋ subquery๋ ๋ณ๋์ ํ์๋ ํ์ด๋ธ๋ก ๊ฐ์ฃผ > MySQL์์๋ ๋ฐ๋์ ๋ณ์นญ ์ง์  ํ์

### @ EXISTS operator

- ์ฟผ๋ฆฌ ๋ฌธ์์ ๋ฐํ๋ ๋ ์ฝ๋์ ์กด์ฌ ์ฌ๋ถ ํ์ธ

- syntax

  ```sql
  SELECT
    select_list
  FROM
    table
  WHERE
    [NOT] EXISTS (subquery);
  ```
  
    - subquery๊ฐ ํ๋ ์ด์์ ํ์ ๋ฐํํ๋ฉด EXISTS ์ฐ์ฐ์๋ true ๋ฐํํ๊ณ  ๊ทธ๋ ์ง ์์ผ๋ฉด false ๋ฐํ

    - ์ฃผ๋ก WHERE ์ ์์ subquery์ ๋ฐํ ๊ฐ ์กด์ฌ ์ฌ๋ถ ํ์ธํ๋๋ฐ ์ฌ์ฉ

- practice

  - #1 ; ์ ์ด๋ ํ๋ฒ ์ด์ ์ฃผ๋ฌธ์ ํ ๊ณ ๊ฐ๋ค์ ๋ฒํธ์ ์ด๋ฆ ์กฐํ (๊ณ ๊ฐ ํ์ด๋ธ์ customers, ์ฃผ๋ฌธ ํ์ด๋ธ์ orders์ด๋ฉฐ ๋ ํ์ด๋ธ์ customerNumber ํ๋๋ฅผ ๊ธฐ์ค์ผ๋ก ๋น๊ต)

    ```sql
    SELECT customerNumber, customerName
    FROM customers
    WHERE
      EXISTS (
        SELECT * 
        FROM orders
        WHERE customers.customerNumber = orders.customerNumber
    );
    ```
  
  - #2 ; Paris์ ์๋ ์ฌ๋ฌด์ค์์ ์ผํ๋ ๋ชจ๋  ์ง์์ ๋ฒํธ, ์ด๋ฆ, ์ฑ์ ์กฐํ (์ง์ ํ์ด๋ธ์ employees, ์ฌ๋ฌด์ค ํ์ด๋ธ์ offices์ด๋ฉฐ ๋ ํ์ด๋ธ์ officeCode ํ๋๋ฅผ ๊ธฐ์ค์ผ๋ก ๋น๊ต)

    ```sql
    SELECT employeeNumber, firstName, lastName
    FROM employees
    WHERE
      EXISTS (
        SELECT *
        FROM offices
        WHERE city = 'Paris' AND offices.officeCode = employees.officeCode
    );
    ```

## ๐ซ Conditional Statements

### @ CASE statement

- SQL ๋ฌธ์์ ์กฐ๊ฑด๋ฌธ์ ๊ตฌ์ฑ

- syntax

  ```sql
  CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value2 THEN statements
    ...
    [ELSE else-statements]
  END CASE;
  ```

    - case_value๊ฐ when_value์ ๋์ผํ ๊ฒ์ ์ฐพ์ ๋๊น์ง ์์ฐจ์ ์ผ๋ก ๋น๊ต

    - when_value์ ๋์ผํ case_value๋ฅผ ์ฐพ์ผ๋ฉด ํด๋น THEN ์ ์ ์ฝ๋ ์คํ

    - ๋์ผํ ๊ฐ ์ฐพ์ง ๋ชปํ๋ฉด ELSE ์ ์ ์ฝ๋ ์คํ ; ELSE ์  ์์ ๋ ๋์ผํ ๊ฐ ์ฐพ์ง ๋ชปํ๋ฉด ์ค๋ฅ ๋ฐ์

- practice

  - #1 ; ๊ณ ๊ฐ๋ค์ creditLimit์ ๋ฐ๋ผ VIP, Platinum, Bronze ๋ฑ๊ธ์ ๋งค๊ฒจ ์กฐํ (VIP 100000 ์ด๊ณผ, Platinum์ 70000 ์ด๊ณผ ๊ทธ ์ธ๋ Bronze๋ก ์ง์ )

    ```sql
    SELECT contactFirstName, creditLimit,
      CASE
        WHEN creditLimit >= 100000.00 THEN 'VIP'
        WHEN creditLimit >= 70000.00 THEN 'Platinum'
        ELSE 'Bronze'
      END AS grade
    FROM customers;
    ```
  
  - #2 ; orders ํ์ด๋ธ์ status์ ๋ฐ๋ผ ์์ธ ์ ๋ณด๋ฅผ ๋งค๊ฒจ ์กฐํ ('In Process'๋ '์ฃผ๋ฌธ์ค', 'Shipped'๋ '๋ฐ์ฃผ์๋ฃ', 'Cancelled'๋ '์ฃผ๋ฌธ์ทจ์', ๊ทธ ์ธ๋ '๊ธฐํ์ฌ์ '๋ก ์ง์ )

    ```sql
    SELECT orderNumber, status,
      CASE
        WHEN status = 'In Process' THEN '์ฃผ๋ฌธ์ค'
        WHEN status = 'Shipped' THEN '๋ฐ์ฃผ์๋ฃ'
        WHEN status = 'Cancelled' THEN '์ฃผ๋ฌธ์ทจ์'
        ELSE '๊ธฐํ์ฌ์ '
      END AS details
    FROM orders;
    ```
    