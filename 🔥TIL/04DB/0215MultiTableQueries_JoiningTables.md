# 🙃 SQL - Multi Table Queries

## @ Introduction to Join

- 커뮤니티 게시판에서 권미자가 작성한 모든 게시글 조회하기 위해서

  ![커게](https://user-images.githubusercontent.com/121418205/218895811-0ad3a0d9-592d-4453-af3b-07678c9fe13b.jpg)

  ```sql
  SELECT * FROM 테이블 WHERE writer = '권미자';
  ```

  를 사용하면 ; 동명이인 있는 경우 / 특정 데이터가 수정되는 경우 **데이터 관리가 어렵다**

  - 테이블을 나눠보기

    ![커게3](https://user-images.githubusercontent.com/121418205/218896135-560a586a-ae8c-4f81-9549-f5bef740e266.jpg)

    - articles와 users 테이블에 각각 userId, roleId **외래 키** 필드 작성

      - 학생인 사람만 보고 싶다면 > roleId가 3인 데이터 조회

      - 권미자라는 사람이 권미숙으로 개명한다면 > users에서 한번만 변경하면 자동으로 모두 변경
    
    - 테이블 분리 시 관리 용이 but **다른 테이블과 연결지어 출력**해야 함

## @ Joining Tables ; **JOIN** clause

- 둘 이상의 테이블에서 데이터를 검색하는 방법

- 종류

  - **INNER JOIN** clause ; 두 테이블에서 값이 일치하는 레코드에 대해서만 결과 반환

    - syntax

      ```sql
      SELECT
        select_list
      FROM
        table1
      INNER JOIN table2
        ON table1.fk = table2.pk;
      ```

        - FROM 절 이후 메일 테이블 지정 (table1)

        - INNER JOIN 절 이후 메인 테이블과 조인할 테이블 지정 (table2)

        - ON 키워드 이후 조인 조건 작성 ; table1과 table2 간의 레코드 일치시키는 규칙 지정
    
    - 예시

      ![JOIN](https://user-images.githubusercontent.com/121418205/218897237-28cdfa62-f800-4d86-a5d7-27984cbf346b.jpg)

      ```sql
      SELECT
        *
      FROM
        articles
      INNER JOIN users
        ON articles.userId = users.id;
      ```

    - practice #1 ; productLine 값이 같은 레코드의 productCode, productName 필드 조회

      ```sql
      SELECT
        productCode, productName
      FROM
        products
      INNER JOIN productlines
        ON productLine.products = productLine.productlines;
      ```
    
    - practice #2 ; orderNumber 값이 같은 레코드의 orders 테이블 orderNumber, status 필드 조회

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
      -- 틀린 답안 ; 두 테이블 모두에 orderNumber가 존재하는 경우 AMBIGUOUS
      SELECT
        orderNumber, status
      FROM
        orders
      INNER JOIN orderdetails
        ON orderNumber.orders = orderNumber.orderNumber;
      ```
    
    - practice #3 ; 직전 조회 결과를 바탕으로 각 주문번호 별 주문상태와 총 판매액 요약 (주문번호는 orderNumber, 총 판매액은 quantityOrdered * priceEach)

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

    - **LEFT JOIN** clause ; 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환

      - syntax

        ```sql
        SELECT
          select_list
        FROM
          table1
        LEFT [OUTER] JOIN table2
          ON table1.fk = table2.pk;
        ```

          - FROM 절 이후 왼쪽 테이블 지정 (table1)

          - LEFT JOIN 절 이후 오른쪽 테이블 지정 (table2)

          - ON 키워드 이후 조인 조건 작성 ; 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴

      - 예시

        ![LEFTJOIN](https://user-images.githubusercontent.com/121418205/218907123-2cc5bd2d-598d-4dda-838c-3cb0f50d9a22.jpg)

        ```sql
        SELECT
          *
        FROM
          articles
        LEFT JOIN users
          ON articles.userId = users.id;
        ```
      
      - 특징

        - 왼쪽은 무조건 표시 후 매치되는 레코드 없으면 **NULL** 표시

        - 왼쪽 테이블 한 개의 레코드에서 여러 개의 오른쪽 테이블 레코드가 일치할 경우, 해당 **왼쪽 레코드를 여러 번 표시**

      - practice #1 ; customers 기준으로 customerNumber 필드가 일치하는 레코드와 함께 customers 테이블 contactFirstName과 orders 테이블의 orderNumber, status 필드 조회 (왼쪽 테이블은 customers, 오른쪽 테이블은 orders, 일치하지 않는 경우 NULL)

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

      - practice #2 ; 직전 조회 결과를 바탕으로 주문내역이 없는 고객의 이름과 주문번호 및 배송상태 조회 (고객의 이름은 contactFirstName 필드, 주문번호는 orderNumber, 배송상태는 status 필드)

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

    - **RIGHT JOIN** clause ; 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환

      - syntax

        ```sql
        SELECT
          select_list
        FROM
          table1
        RIGHT [OUTER] JOIN table2
          ON table1.fk = table2.pk;
        ```

          - FROM 절 이후 왼쪽 테이블 지정 (table1)

          - RIGHT JOIN 절 이후 오른쪽 테이블 지정 (table2)

          - ON 키워드 이후 조인 조건 작성 (오른쪽 테이블의 각 레코드를 왼쪽 테이블의 모든 레코드와 일치시킴)
      
      - 예시

        ![RIGHTJOIN](https://user-images.githubusercontent.com/121418205/218910146-7643fe58-bb0e-4e98-8ceb-8431f9a253c9.jpg)

        ```sql
        SELECT
          *
        FROM
          articles
        RIGHT JOIN users
          ON articles.userId = user.id;
        ```

      - 특징

        - 오른쪽은 무조건 표시하고, 매치되는 레코드 없으면 **NULL** 표시

        - 오른쪽 테이블 한 개의 레코드에 여러 개의 왼쪽 테이블 레코드가 일치할 경우, 해당 **오른쪽 레코드를 여러 번 표시**

      - practice #1 ; employees를 기준으로 employeeNumber 필드와 sales REpEmployeeNumber 필드가 일치하는 레코드와 함께 employeeNumber, firstName, customerNumber, contactFirstName 필드 조회 (왼쪽 테이블은 customers, 오른쪽 테이블은 employees, 일치하지 않는 경우 NULL)

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
      
      - practice #2 ; 고객에게 판매한 내역이 없는 직원 목록 조회 (직원 번호와 이름은 employeeNumber, contactFirstName 필드 / 고객 번호와 이름은 custoemrNumber, contactFirstName 필드)

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

![JOIN정리](https://user-images.githubusercontent.com/121418205/218911425-5ed49551-b742-4eb6-a8b7-536ccd557d8b.jpg)

> FULL OUTER JOIN

  - 한쪽 테이블이 아닌 두 테이블 모두 이 빠진 형태로 데이터를 조회해야 할 때 사용

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