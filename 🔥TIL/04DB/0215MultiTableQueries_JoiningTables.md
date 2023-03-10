# 0215 WED

## ๐ SQL - Multi Table Queries

### @ Introduction to Join

- ์ปค๋ฎค๋ํฐ ๊ฒ์ํ์์ ๊ถ๋ฏธ์๊ฐ ์์ฑํ ๋ชจ๋  ๊ฒ์๊ธ ์กฐํํ๊ธฐ ์ํด์

  ![แแฅแแฆ](https://user-images.githubusercontent.com/121418205/218895811-0ad3a0d9-592d-4453-af3b-07678c9fe13b.jpg)

  ```sql
  SELECT * FROM ํ์ด๋ธ WHERE writer = '๊ถ๋ฏธ์';
  ```

  ๋ฅผ ์ฌ์ฉํ๋ฉด ; ๋๋ช์ด์ธ ์๋ ๊ฒฝ์ฐ / ํน์  ๋ฐ์ดํฐ๊ฐ ์์ ๋๋ ๊ฒฝ์ฐ **๋ฐ์ดํฐ ๊ด๋ฆฌ๊ฐ ์ด๋ ต๋ค**

  - ํ์ด๋ธ์ ๋๋ ๋ณด๊ธฐ

    ![แแฅแแฆ3](https://user-images.githubusercontent.com/121418205/218896135-560a586a-ae8c-4f81-9549-f5bef740e266.jpg)

    - articles์ users ํ์ด๋ธ์ ๊ฐ๊ฐ userId, roleId **์ธ๋ ํค** ํ๋ ์์ฑ

      - ํ์์ธ ์ฌ๋๋ง ๋ณด๊ณ  ์ถ๋ค๋ฉด > roleId๊ฐ 3์ธ ๋ฐ์ดํฐ ์กฐํ

      - ๊ถ๋ฏธ์๋ผ๋ ์ฌ๋์ด ๊ถ๋ฏธ์์ผ๋ก ๊ฐ๋ชํ๋ค๋ฉด > users์์ ํ๋ฒ๋ง ๋ณ๊ฒฝํ๋ฉด ์๋์ผ๋ก ๋ชจ๋ ๋ณ๊ฒฝ
    
    - ํ์ด๋ธ ๋ถ๋ฆฌ ์ ๊ด๋ฆฌ ์ฉ์ด but **๋ค๋ฅธ ํ์ด๋ธ๊ณผ ์ฐ๊ฒฐ์ง์ด ์ถ๋ ฅ**ํด์ผ ํจ

### @ Joining Tables ; **JOIN** clause

- ๋ ์ด์์ ํ์ด๋ธ์์ ๋ฐ์ดํฐ๋ฅผ ๊ฒ์ํ๋ ๋ฐฉ๋ฒ

- ์ข๋ฅ

  - **INNER JOIN** clause ; ๋ ํ์ด๋ธ์์ ๊ฐ์ด ์ผ์นํ๋ ๋ ์ฝ๋์ ๋ํด์๋ง ๊ฒฐ๊ณผ ๋ฐํ

    - syntax

      ```sql
      SELECT
        select_list
      FROM
        table1
      INNER JOIN table2
        ON table1.fk = table2.pk;
      ```

        - FROM ์  ์ดํ ๋ฉ์ผ ํ์ด๋ธ ์ง์  (table1)

        - INNER JOIN ์  ์ดํ ๋ฉ์ธ ํ์ด๋ธ๊ณผ ์กฐ์ธํ  ํ์ด๋ธ ์ง์  (table2)

        - ON ํค์๋ ์ดํ ์กฐ์ธ ์กฐ๊ฑด ์์ฑ ; table1๊ณผ table2 ๊ฐ์ ๋ ์ฝ๋ ์ผ์น์ํค๋ ๊ท์น ์ง์ 
    
    - ์์

      ![JOIN](https://user-images.githubusercontent.com/121418205/218897237-28cdfa62-f800-4d86-a5d7-27984cbf346b.jpg)

      ```sql
      SELECT
        *
      FROM
        articles
      INNER JOIN users
        ON articles.userId = users.id;
      ```

    - practice #1 ; productLine ๊ฐ์ด ๊ฐ์ ๋ ์ฝ๋์ productCode, productName ํ๋ ์กฐํ

      ```sql
      SELECT
        productCode, productName
      FROM
        products
      INNER JOIN productlines
        ON productLine.products = productLine.productlines;
      ```
    
    - practice #2 ; orderNumber ๊ฐ์ด ๊ฐ์ ๋ ์ฝ๋์ orders ํ์ด๋ธ orderNumber, status ํ๋ ์กฐํ

      ```sql
      SELECT
        t1.orderNumber,
        t1.status
      FROM
        orders AS t1
      INNER JOIN orderdetails AS t2
        ON t1.orderNumber = t2.orderNumber;
      ```

      ```sql
      -- ํ๋ฆฐ ๋ต์ ; ๋ ํ์ด๋ธ ๋ชจ๋์ orderNumber๊ฐ ์กด์ฌํ๋ ๊ฒฝ์ฐ AMBIGUOUS
      SELECT
        orderNumber, status
      FROM
        orders
      INNER JOIN orderdetails
        ON orderNumber.orders = orderNumber.orderNumber;
      ```
    
    - practice #3 ; ์ง์  ์กฐํ ๊ฒฐ๊ณผ๋ฅผ ๋ฐํ์ผ๋ก ๊ฐ ์ฃผ๋ฌธ๋ฒํธ ๋ณ ์ฃผ๋ฌธ์ํ์ ์ด ํ๋งค์ก ์์ฝ (์ฃผ๋ฌธ๋ฒํธ๋ orderNumber, ์ด ํ๋งค์ก์ quantityOrdered * priceEach)

      ```sql
      SELECT
        t1.orderNumber,
        t1.status,
        SUM(quantityOrdered * priceEach) AS totalSales
      FROM
        orders AS t1,
      iNNER JOIN orderdetails AS t2
        ON t1.orderNumber = t2.orderNumber
      GROUP BY orderNumber;
      ```

  - **OUTER** JOIN

    - **LEFT JOIN** clause ; ์ค๋ฅธ์ชฝ ํ์ด๋ธ์ ์ผ์นํ๋ ๋ ์ฝ๋์ ํจ๊ป ์ผ์ชฝ ํ์ด๋ธ์ ๋ชจ๋  ๋ ์ฝ๋ ๋ฐํ

      - syntax

        ```sql
        SELECT
          select_list
        FROM
          table1
        LEFT [OUTER] JOIN table2
          ON table1.fk = table2.pk;
        ```

          - FROM ์  ์ดํ ์ผ์ชฝ ํ์ด๋ธ ์ง์  (table1)

          - LEFT JOIN ์  ์ดํ ์ค๋ฅธ์ชฝ ํ์ด๋ธ ์ง์  (table2)

          - ON ํค์๋ ์ดํ ์กฐ์ธ ์กฐ๊ฑด ์์ฑ ; ์ผ์ชฝ ํ์ด๋ธ์ ๊ฐ ๋ ์ฝ๋๋ฅผ ์ค๋ฅธ์ชฝ ํ์ด๋ธ์ ๋ชจ๋  ๋ ์ฝ๋์ ์ผ์น์ํด

      - ์์

        ![LEFTJOIN](https://user-images.githubusercontent.com/121418205/218907123-2cc5bd2d-598d-4dda-838c-3cb0f50d9a22.jpg)

        ```sql
        SELECT
          *
        FROM
          articles
        LEFT JOIN users
          ON articles.userId = users.id;
        ```
      
      - ํน์ง

        - ์ผ์ชฝ์ ๋ฌด์กฐ๊ฑด ํ์ ํ ๋งค์น๋๋ ๋ ์ฝ๋ ์์ผ๋ฉด **NULL** ํ์

        - ์ผ์ชฝ ํ์ด๋ธ ํ ๊ฐ์ ๋ ์ฝ๋์์ ์ฌ๋ฌ ๊ฐ์ ์ค๋ฅธ์ชฝ ํ์ด๋ธ ๋ ์ฝ๋๊ฐ ์ผ์นํ  ๊ฒฝ์ฐ, ํด๋น **์ผ์ชฝ ๋ ์ฝ๋๋ฅผ ์ฌ๋ฌ ๋ฒ ํ์**

      - practice #1 ; customers ๊ธฐ์ค์ผ๋ก customerNumber ํ๋๊ฐ ์ผ์นํ๋ ๋ ์ฝ๋์ ํจ๊ป customers ํ์ด๋ธ contactFirstName๊ณผ orders ํ์ด๋ธ์ orderNumber, status ํ๋ ์กฐํ (์ผ์ชฝ ํ์ด๋ธ์ customers, ์ค๋ฅธ์ชฝ ํ์ด๋ธ์ orders, ์ผ์นํ์ง ์๋ ๊ฒฝ์ฐ NULL)

        ```sql
        SELECT
          contactFirstName,
          orderNumber,
          status
        FROM
          customers
        LEFT JOIN orders
          ON customers.customerNumber = orders.customerNumber;
        ```

      - practice #2 ; ์ง์  ์กฐํ ๊ฒฐ๊ณผ๋ฅผ ๋ฐํ์ผ๋ก ์ฃผ๋ฌธ๋ด์ญ์ด ์๋ ๊ณ ๊ฐ์ ์ด๋ฆ๊ณผ ์ฃผ๋ฌธ๋ฒํธ ๋ฐ ๋ฐฐ์ก์ํ ์กฐํ (๊ณ ๊ฐ์ ์ด๋ฆ์ contactFirstName ํ๋, ์ฃผ๋ฌธ๋ฒํธ๋ orderNumber, ๋ฐฐ์ก์ํ๋ status ํ๋)

        ```sql
        SELECT
          contactFirstName,
          orderNumber,
          status
        FROM
          customers
        LEFT JOIN orders
          ON customers.customerNumber = orders.customerNumber
        WHERE
          orders.orderNumber IS NULL;
        ```

    - **RIGHT JOIN** clause ; ์ผ์ชฝ ํ์ด๋ธ์ ์ผ์นํ๋ ๋ ์ฝ๋์ ํจ๊ป ์ค๋ฅธ์ชฝ ํ์ด๋ธ์ ๋ชจ๋  ๋ ์ฝ๋ ๋ฐํ

      - syntax

        ```sql
        SELECT
          select_list
        FROM
          table1
        RIGHT [OUTER] JOIN table2
          ON table1.fk = table2.pk;
        ```

          - FROM ์  ์ดํ ์ผ์ชฝ ํ์ด๋ธ ์ง์  (table1)

          - RIGHT JOIN ์  ์ดํ ์ค๋ฅธ์ชฝ ํ์ด๋ธ ์ง์  (table2)

          - ON ํค์๋ ์ดํ ์กฐ์ธ ์กฐ๊ฑด ์์ฑ (์ค๋ฅธ์ชฝ ํ์ด๋ธ์ ๊ฐ ๋ ์ฝ๋๋ฅผ ์ผ์ชฝ ํ์ด๋ธ์ ๋ชจ๋  ๋ ์ฝ๋์ ์ผ์น์ํด)
      
      - ์์

        ![RIGHTJOIN](https://user-images.githubusercontent.com/121418205/218910146-7643fe58-bb0e-4e98-8ceb-8431f9a253c9.jpg)

        ```sql
        SELECT
          *
        FROM
          articles
        RIGHT JOIN users
          ON articles.userId = user.id;
        ```

      - ํน์ง

        - ์ค๋ฅธ์ชฝ์ ๋ฌด์กฐ๊ฑด ํ์ํ๊ณ , ๋งค์น๋๋ ๋ ์ฝ๋ ์์ผ๋ฉด **NULL** ํ์

        - ์ค๋ฅธ์ชฝ ํ์ด๋ธ ํ ๊ฐ์ ๋ ์ฝ๋์ ์ฌ๋ฌ ๊ฐ์ ์ผ์ชฝ ํ์ด๋ธ ๋ ์ฝ๋๊ฐ ์ผ์นํ  ๊ฒฝ์ฐ, ํด๋น **์ค๋ฅธ์ชฝ ๋ ์ฝ๋๋ฅผ ์ฌ๋ฌ ๋ฒ ํ์**

      - practice #1 ; employees๋ฅผ ๊ธฐ์ค์ผ๋ก employeeNumber ํ๋์ sales REpEmployeeNumber ํ๋๊ฐ ์ผ์นํ๋ ๋ ์ฝ๋์ ํจ๊ป employeeNumber, firstName, customerNumber, contactFirstName ํ๋ ์กฐํ (์ผ์ชฝ ํ์ด๋ธ์ customers, ์ค๋ฅธ์ชฝ ํ์ด๋ธ์ employees, ์ผ์นํ์ง ์๋ ๊ฒฝ์ฐ NULL)

        ```sql
        SELECT
          employeeNumber,
          firstName,
          customerNumber,
          contactFirstName
        FROM
          customers
        RIGHT JOIN employees
          ON salesRepEmployeeNumber = employeeNumber;
        ```
      
      - practice #2 ; ๊ณ ๊ฐ์๊ฒ ํ๋งคํ ๋ด์ญ์ด ์๋ ์ง์ ๋ชฉ๋ก ์กฐํ (์ง์ ๋ฒํธ์ ์ด๋ฆ์ employeeNumber, contactFirstName ํ๋ / ๊ณ ๊ฐ ๋ฒํธ์ ์ด๋ฆ์ custoemrNumber, contactFirstName ํ๋)

        ```sql
        SELECT
          employeeNumber,
          firstName,
          customerNumber,
          contactFirstName
        FROM
          customers
        RIGHT JOIN employees
          ON salesRepEmployeeNumber = employeeNumber
        WHERE
          salesRepEmployeeNumber IS NULL;
        ```

![JOINแแฅแผแแต](https://user-images.githubusercontent.com/121418205/218911425-5ed49551-b742-4eb6-a8b7-536ccd557d8b.jpg)

> FULL OUTER JOIN

  - ํ์ชฝ ํ์ด๋ธ์ด ์๋ ๋ ํ์ด๋ธ ๋ชจ๋ ์ด ๋น ์ง ํํ๋ก ๋ฐ์ดํฐ๋ฅผ ์กฐํํด์ผ ํ  ๋ ์ฌ์ฉ

    ```sql
    SELECT
      *
    FROM
      A
    LEFT JOIN B
    UNION
    SELECT
      *
    FROM A
    RIGHT JOIN B;
    ```