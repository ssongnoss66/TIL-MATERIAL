# 😀 Introduction to Subquery

## @ subquery

- "A query inside a query" ; 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법

- 예시

  - table1에서 가장 나이가 어린 사람을 삭제해야한다면?

    ```sql
    SELECT MIN(age)
    FROM table1;
    
    DELETE FROM table1
    WHERE age = 위에서 찾은 값;
    ```
    를
    ```sql
    DELETE FROM table1
    WHERE age = (
      SELECT MIN(age) FROM table1
    )
    ```
    로 표현 가능 (WHERE age = 이하가 **SUBQUERY**)

- 특징

  - 조건에 따라 하나 이상의 테이블에서 데이터 검색하는데 사용

  - SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용

- practice

  - #1 ; 한번에 가장 많은 돈을 소비한 고객 번호 조회 (payments 테이블 활용)

    ```sql
    SELECT customerNumber, amount
    FROM payments
    WHERE amount = (
      SELECT MIN(amount)
      FROM payments
    );
    ```

  - #2 ; 미국에 있는 사무실에서 근무하는 직원의 성과 이름 조회 (직원 정보는 employees, 사무실 정보는 offices 테이블에 존재)

    ```sql
    SELECT lastName, firstName
    FROM employees
    WHERE officode IN (
      SELECT officeCode
      FROM offices
      WEHRE country = 'USA'
    );
    ```

  - #3 ; 주문한 적이 없는 고객 목록 조회 (고객 정보는 customers, 주문 정보는 orders 테이블에 존재)

    ```sql
    SELECT customerName
    FROM customers
    WHERE customerNumber NOT IN (
      SELECT DISTINCT customerNumber
      FROM orders
    );
    ```
  
  - #ad ; 소비를 한 고객들 중 한번에 지불한 금액이 가장 높은 고객의 customerNumber, amount, contactFirstName을 조회 (고객 테이블은 customers, 지불 테이블은 payments 활용)

    - 풀이 힌트 

      - payments 테이블과 customers 테이블을 조인하여 contactFirstName, amountm, customerNumber 필드를 포함하는 findName이라는 이름의 서브쿼리 생성

      - findName 서브쿼리에서 amount, customerNumber, contactFirstName 필드 선택

      - 또다른 서브쿼리 사용해서 payments 테이블에서 가장 높은 amount 값 가진 레코드 찾기

      - findName 서브쿼리에서 amount 필드와 다른 서브쿼리의 결과가 일치하는 레코드 선택

      - 최종적으로 customerNumber, amount, contactFirstName 필드 출력
    
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

      - AS findName ; FROM 절에서 사용하는 subquery는 별도의 파생된 테이블로 간주 > MySQL에서는 반드시 별칭 지정 필요

## @ EXISTS operator

- 쿼리 문에서 반환된 레코드의 존재 여부 확인

- syntax

  ```sql
  SELECT
    select_list
  FROM
    table
  WHERE
    [NOT] EXISTS (subquery);
  ```
  
    - subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true 반환하고 그렇지 않으면 false 반환

    - 주로 WHERE 절에서 subquery의 반환 값 존재 여부 확인하는데 사용

- practice

  - #1 ; 적어도 한번 이상 주문을 한 고객들의 번호와 이름 조회 (고객 테이블은 customers, 주문 테이블은 orders이며 두 테이블의 customerNumber 필드를 기준으로 비교)

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
  
  - #2 ; Paris에 있는 사무실에서 일하는 모든 직원의 번호, 이름, 성을 조회 (직원 테이블은 employees, 사무실 테이블은 offices이며 두 테이블의 officeCode 필드를 기준으로 비교)

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

# 😫 Conditional Statements

## @ CASE statement

- SQL 문에서 조건문을 구성

- syntax

  ```sql
  CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value2 THEN statements
    ...
    [ELSE else-statements]
  END CASE;
  ```

    - case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교

    - when_value와 동일한 case_value를 찾으면 해당 THEN 절의 코드 실행

    - 동일한 값 찾지 못하면 ELSE 절의 코드 실행 ; ELSE 절 없을 때 동일한 값 찾지 못하면 오류 발생

- practice

  - #1 ; 고객들의 creditLimit에 따라 VIP, Platinum, Bronze 등급을 매겨 조회 (VIP 100000 초과, Platinum은 70000 초과 그 외는 Bronze로 지정)

    ```sql
    SELECT contactFirstName, creditLimit,
      CASE
        WHEN creditLimit >= 100000.00 THEN 'VIP'
        WHEN creditLimit >= 70000.00 THEN 'Platinum'
        ELSE 'Bronze'
      END AS grade
    FROM customers;
    ```
  
  - #2 ; orders 테이블의 status에 따라 상세 정보를 매겨 조회 ('In Process'는 '주문중', 'Shipped'는 '발주완료', 'Cancelled'는 '주문취소', 그 외는 '기타사유'로 지정)

    ```sql
    SELECT orderNumber, status,
      CASE
        WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
      END AS details
    FROM orders;
    ```
    