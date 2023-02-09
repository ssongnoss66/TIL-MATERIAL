# 0209 THU

## 😶‍🌫️ SQL Basics

### @ Introduction

- SQL (Structure Query Language)

  - 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

  - 테이블의 형태로 **구조화**된 관계형 데이터베이스에게 요청을 **질의(요청)**

  - 컴퓨터와의 대화 -> 프로그래밍 언어 / 관계형 데이터베이스와의 대화 -> SQL

- SQL Syntax

  ```SQL
  SELECT age FROM solar_system WHERE name = 'earth';
  ```

  - SQL 키워드는 대소문자 구분 X ; but 대문자 작성 권장 (명시적 구분)

  - 각 SQL Statements 끝에는 세미콜론(;) 필요 ; 각 SQL Statements 구분하는 방법

### @ SQL Statements

- SQL 언어를 구성하는 가장 기본적인 코드 블록

  ```SQL
  SELECT column_name FROM table_name;
  ```
  - SELECT Statement

  - SELECT, FROM 2개의 keyword로 구성됨

- 유형

  - DDL (데이터 정의)

    - 데이터의 기본 구조 및 형식 변경

    - 키워드 ; CREATE, DROP, ALTER

  - DQL (데이터 검색)

    - 키워드 ; SELECT

  - DML (데이터 조작)

    - 데이터 추가, 수정, 삭제

    - 키워드 ; INSERT, UPDATE, DELETE

  - DCL (데이터 제어)

    - 데이터 및 작업에 대한 사용자 권한 제어

    - 키워드 ; COMMIT, ROLLBACK, GRANT, REVOKE

### @ 용어 정리

- Query

  - 질의, 질문

  - "데이터베이스로부터 정보를 요청" 하는 것

  - 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함

- SQL 표준

  - SQL은 미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준 채택

  - 모든 RDBMS에서 SQL 표준을 지원하나 RDBMS별로 독자적인 기능에 따라 표준 벗어나는 문법 존재

## 😕 SQL Single Table Queries

### @ Querying data

- SELECT statement ; 테이블에서 데이터를 조회

- SELECT syntax

    ```SQL
    SELECT
      select_list
    FROM
      table_name;
    ```
    - SELCT 키워드 다음에 데이터를 선택하려는 필드를 하나 이상 지정

    - FROM 키워드 다음에 데이터를 선택하려는 테이블의 이름을 지정

- SELECT examples

  - #1 테이블 employees에서 lastName 필드의 모든 데이터 조회

    ```SQL
    SELECT
      lastname
    FROM
      employees;
    ```

  - #2 테이블 employees에서 lastName, firstName 필드의 모든 데이터 조회

    ```SQL
    SELECT
      lastName, firstName
    FROM
      employees;
    ```

  - #3 테이블 employees에서 모든 필드의 데이터 조회

    ```SQL
    SELECT
      *
    FROM
      employees;
    ```

  - #4 테이블 employees에서 firstName 필드의 모든 데이터 조회 ('이름'으로 출력될 수 있도록 변경)

    - **AS keyword** ; 필드에 새로운 별칭 지정

    ```SQL
    SELECT
      firstName AS '이름'
    FROM
      employees
    ```

  - #5 테이블 orderdetails에서 productCode, 주문 총액 필드의 모든 데이터 조회 (주문 총액 필드는 quantityOrdered와 priceEach 필드를 곱한 결과값)

    - **Arithmetic Operators** ; 기본적 사칙연산 사용 가능

    ```SQL
    SELECT
      productcode,
      (quantityOrdered * priceEach) AS '주문 총액'
    FROM
      orderdetails;
    ```

## @ Sorting data

- ORDER BY clause ; 조회 결과의 레코드 정렬

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

    - FROM clause 뒤에 위치

    - 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순 정렬

      - ASC ; 오름차순 (기본 값) / DESC ; 내림차순

- ORDER BY examples

  - #1 테이블 employees에서 firstName 필드의 모든 데이터를 오름차순으로 조회

    ```SQL
    SELECT
      firstName
    FROM
      employees
    ORDER BY
      firstName;
    ```
  - #2 테이블 employees에서 firstName 필드의 모든 데이터를 낾차순으로 조회

    ```SQL
    SELECT
      firstName
    FROM
      employees
    ORDER BY
      firstName DESC;
    ```
  
  - #3 테이블 employees에서 lastName 필드를 기준으로 내림차순으로 정렬한 다음 firstName 필드 기준으로 오름차순 정렬하여 조회

    ```SQL
    SELECT
      lastName, firstName
    FROM
      employees
    ORDER BY
      lastName DESC,
      firstName;
    ```
  
  - #4 테이블 orderdetails에서 totalSales 필드를 기준으로 내림차순으로 정렬한 다음 productCode, totalSales 필드의 모든 데이터 조회 (totalSales 필드는 quantityOrdered와 priceEach 필드 곱한 값)

    ```SQL
    SELECT
      productCode,
      (quantityOrdered * priceEach) AS 'totalSales'
    FROM
      orderdetails
    ORDER BY
      totalSales DESC;
    ```
  
> SELECT statement 실행 순서 ; FROM -> SELECT -> ORDER BY

1. 테이블에서 (FROM) 2. 조회하여 (SELECT) 3. 정렬 (ORDER BY)
