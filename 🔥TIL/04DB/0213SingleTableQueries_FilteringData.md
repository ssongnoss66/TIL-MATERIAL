# 😏 SQL Single Table Queries

## @ Introduction

**DQL (Data Query Language) ; 데이터 검색 (SQL keyword ; SELECT)**

## @ Filtering data

- 데이터를 필터링하여 중복 제거, 조건 설정 등 SQL Query를 제어하기

- Keywords

  - Clause

    - DISTINCT clause ; 조회 결과에서 중복된 레코드를 제거

      ```SQL
      SELECT DISTINCT
        select_list
      FROM
        table_name;
      ```

      - SELECT 키워드 바로 뒤에 작성

      - SELCT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드 지정

      - practice #1 ; 테이블 employees에서 lastName 필드의 모든 데이터 오름차순 조회

        ```SQL
        SELECT
          lastname
        FROM
          employees
        ORDER BY
          lastName;
        ```
      
      - practice #2 ; 테이블 employees에서 lastName 필드의 모든 데이터 중복없이 오름차순 조회

        ```SQL
        SELECT DISTINCT
          lastName
        FROM
          employees
        ORDER BY
          lastName;
        ```

    - WHERE clause ; 조회 시 특정 검색 조건을 지정

      ```SQL
      SELECT
        select_list
      FROM
        table_name
      WHERE
        search_condition;
      ```

        - FROM clause 뒤에 위치

        - search_condition은 비교연산자 및 논리연산자 (AND, OR, NOT 등) 사용하는 구문 사용됨

        - pactice #1 ; 테이블 employees에서 officeCode 필드 값이 1인 데이터의 lastName, firstName, officeCode 조회

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode = 1;
          ```

        - practice #2 ; 테이블 employees에서 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 lastName, firstName, job Title 조회

          ```SQL
          SELECT
            lastName, firstName, jobTitle
          FROM
            employees
          WHERE
            jobTitle != 'Sales Rep';
          ```

        - practice #3 ; 테이블 employees에서 officeCode 필드 값이 3 이상이고 jobTitle 필드 값이 'Sales Rep'인 데이터의 lastName, firstName, officeCode, jobTitle 조회

           ```SQL
           SELECT
            lastName, firstName, officeCode, jobTitle
          FROM
            employees
          WHERE
            officeCode >= 3
            AND jobTitle = 'Sales Rep';
          ```
        
        - practice #4 ; 테이블 employees에서 officeCode 필드 값이 5 미만이거나 jobTitle 필드 값이 'Sales Rep'이 아닌 데이터의 lastName, firstName, officeCode, jobTitle 조회

          ```SQL
          SELECT
            lastName, firstName, officeCode, jobTitle
          FROM
            employees
          WHERE
            officeCode < 5
            OR jobTitle != 'Sales Rep';
          ```
        
        - practice #5 ; 테이블 employees에서 officeCode 필드 값이 1 에서 4 사이 값인 데이터의 lastName, firstName, officeCode 조회 (1과 4를 포함)

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode BETWEEN 1 AND 4;
          ```
          또는
          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode >= 1
            AND officeCode <= 4;
          ```
        
        - practice #6 ; 테이블 employees에서 officeCode 필드 값이 1 에서 4 사이 값인 데이터의 lastName, firstName, officeCode를 오름차순 조회

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

        - practice #7 ; 테이블 employees에서 officeCode 필드 값이 1 또는 3 또는 4 값인 데이터의 lastName, firstName, officeCode 조회

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode IN (1, 3, 4);
          ```
          또는
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

        - practice #8 ; 테이블 employees에서 officeCode 필드 값이 1 과 3 그리고 4 가 아닌 데이터의 lastName, firstName, officeCode 조회

          ```SQL
          SELECT
            lastName, firstName, officeCode
          FROM
            employees
          WHERE
            officeCode NOT IN (1, 3, 4);
          ```

        - practice #9 ; 테이블 employees에서 lastName 필드 값이 son으로 끝나는 데이터의 lastName, firstName 조회

          ```SQL
          SELECT
            lastName, firstName
          FROM
            employees
          WHERE
            lastName LIKE '%son';
          ```

        - practice #10 ; 테이블 employees에서 firstName 필드 값이 4자리면서 y로 끝나는 데이터의 lastName, firstName 조회

          ```SQL
          SELECT
            lastName, firstName
          FROM
            employees
          WHERE
            firstName LIKE '___y';
          ```

    - LIMIT clause ; 조회하는 레코드 수를 제한

      ```SQL
      SELECT
        select_list
      FROM
        table_name
      LIMIT [OFFSET,] row_count;
      ```

        - LIMIT clause는 하나 또는 두 개의 인자를 사용 (0 또는 양의 정수)

        - row_count는 조회할 최대 레코드 수를 지정

        - LIMIT & OFFSET 예시

          ![LIMIT OFFSET](https://user-images.githubusercontent.com/121418205/218443431-93712bdc-feb3-4100-9219-a0a00b046a56.jpg)

          ```SQL
          SELECT
            ..
          FROM
            ..
          LIMIT 3, 5;
          ```

        - practice #1 ; 테이블 customers에서 contactFirstName, creditLimit 필드 데이터를 creditLimit 기준 내림차순으로 7개만 조회

          ```SQL
          SELECT
            contactFirstName, creditLimit
          FROM
            customers
          ORDER BY
            creditLimit DESC
          LIMIT 7;
          ```

        - practice #2 ; 테이블 customers에서 contactFirstName, creditLimit 필드 데이터를 creditLimit 기준 내림차순으로 4번째부터 7번째 데이터만 조회

          ```SQL
          SELECT
            contactFirstName, creditLimit
          FROM
            customers
          ORDER BY
            creditLimit DESC
          LIMIT 3, 4;
          ```
          또는
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

    - IN ; 값이 특정 목록 안에 있는지 확인

    - LIKE ; 값이 특정 패턴에 일치하는지 확인 with Wildcards

      - % ; **0개 이상의 문자열**과 일치하는지 확인

      - _ ; **단일 문자**와 일치하는지 확인

    - Comparison ; 비교 연산자 (=, >=, <=, !=, IS, LIKE, IN, BETWEEN...AND)

    - Logical ; 논리 연산자 (AND(&&), OR(::), NOT(!))

## @ Grouping data

- GROUP BY clause ; 레코드를 그룹화하여 요약본 생성 with 집계 함수 (Aggregation Functions)

    - Aggregation Functions ; 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수 (SUM, AVG, MAX, MIN, COUNT)

    - syntax

      ```SQL
      SELECT
        c1, c2, ..., aggregate_function(ci)
      FROM
        table_name
      GROUP BY
        c1, c2, ..., cn;
      ```

        - FROM 및 WHERE 절 뒤에 배치

        - GROUP BY 절 뒤에 그룹화할 필드 목록을 작성

- 이해하기

  - jobTitle 필드 그룹화

      ![GROUPBY이해하기1](https://user-images.githubusercontent.com/121418205/218448973-4d87fb74-2f69-48cb-bb1a-4b2b5e2cd1ed.jpg)

      ```SQL
      SELECT
        jobTitle
      FROM
        employees
      GROUP BY
        jobTitle;
      ```
  
  - COUNT 함수가 각 그룹에 대한 집계된 값을 계산

      ![GROUPBY이해하기2](https://user-images.githubusercontent.com/121418205/218448965-3468ca1a-5f20-41c0-98d0-d94d7056de66.jpg)

      ```SQL
      SELECT
        jobTitle, COUNT(*)
      FROM
        employees
      GROUP BY
        jobTitle;
      ```

- practice

  - #1 ; 테이블 customers에서 country 필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균값을 내림차순 조회

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
    또는
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
  
  - #2 ; 테이블 customers에서 country 필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균값이 80000을 초과하는 데이터만 조회

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

      - **HAVING clause** ; 집계 항목에 대한 세부 조건 지정 (주로 GROUP BY와 함께 사용 / GROUP BY 없으면 WHERE처럼 동작)

> SELECT statement 실행 순서 ; FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY - LIMIT

  1. 테이블에서 FROM

  2. 특정 조건에 맞춰 WHERE

  3. 그룹화하고 GROUP BY

  4. 만약 그룹 중 조건이 있다면 맞추고 HAVING

  5. 조회하여 SELECT

  6. 정렬하고 ORDER BY

  7. 특정 위치의 값을 가져온다 LIMIT

```
정렬에서의 NULL

- MySQL에서 NULL은 NULL이 아닌 값 앞에 위치

  - NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
```
```SQL
--NULL 정렬 예시
SELECT
  postalCode
FROM
  customers
ORDER BY
  postalCode;
```