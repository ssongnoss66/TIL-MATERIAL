# 0208 WED

## 🫠 Intro

### @ Why Database

- 데이터

  - 저장이나 처리에 효율적인 형태로 변환된 정보(information)

  - 전세계적으로 데이터량이 증가하며 데이터 센터 역시 성장

  > 무한히 증가하고 있는 데이터를 저장하고 잘 관리하여 활용할 수 있는 기술이 필요하다!

- 데이터를 저장하자

  - 과거에는 파일(어디에서나 쉽게 사용 가능 but 데이터 구조적 관리 어려움)이나 스프레드 시트(열과 행으로 데이터 구조적 관리 가능 but 데이터가 방대하다면?) 이용하여 데이터 관리

  - 스프레드 시트의 한계

    - 크기 ; 일반적으로 약 100만 행까지만 저장 가능

    - 보안 ; 파일 및 링크 소유 여부에 따라 접근 권한 설정 > 다양한 권한 설정 제공 X

    - 정확성 ; 데이터 변경 시 여러 시트에 분산되어 있다면 변경에 누락 및 추가 문제 발생 가능

### @ What is Database

- 데이터베이스 ; 체계적인 데이터 모음 > 데이터를 저장하고 조작하는 역할

- 거대하고 복잡한 데이터를 다루기 위해 고안된 도구 > 많은 기능 제공

- **CRUD (Create Read Update Delete)**

## 🧐 The Relation

### @ Relational Database

- 관계형 데이터베이스 ; 데이터 간에 **관계**가 있는 데이터 항목들의 모음

  - 테이블, 행, 열의 정보를 **구조화**하는 방식

  - **서로 관련된 데이터 포인트를 저장**하고 이에 대한 **액세스** 제공

    ![관계형디비](https://user-images.githubusercontent.com/121418205/217442075-a22bd616-6ec8-41fd-a246-d9b8fe13b096.png)

- 관계 ; 여러 테이블 간의 (논리적) 연결

  - 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회 가능 (특정 날짜 구매 고객 전체 조회, 지난 달 배송 지연 고객 조회 등)

- 예시

  - 다음과 같이 각 고객이 주문한 주문데이터가 테이블에 저장되어 있다고 가정
    
    ![관계형디비2](https://user-images.githubusercontent.com/121418205/217446013-0c44c670-14ee-413e-bf39-219e6da1bb83.png)

    - 기본 키 (Primary Key) ; (고객 테이블) 각 데이터에 고유한 식별 값 부여

    - 외래 키 (Foreign Key) ; (주문 테이블) 고객의 고유한 식별 값 저장

- 용어

  - Table (Rlation) ; 데이터 기록하는 **최종 위치**

  - Field (Column, Attribute) ; 각 필드에는 고유한 데이터 형식(타입) 지정됨

  - Record (Row, Tuple) ; 각 레코드에는 구체적 데이터 값 저장

  - Database (Schema) ; 테이블의 집합 (Set of tables)

  - Primary Key ; 각 레코드의 고유한 값 / 관계형 데이터베이스에서 **레코드의 식별자**로 활용

  - Foreign Key ; 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키 / 각 레코드에서 서로 다른 테이블 간의 **관계를 만드는 데** 사용

### @ RDBMS

- DBMS (Database Management System) ; 데이터베이스를 관리하는 소프트웨어 프로그램

- **R**DBMS (**Relational** Database Management System) ;  **관계형** 데이터베이스를 관리하는 소프트웨어 프로그램 (MySQL, PostgreSQL, Oracle Database, MS SQL Server 등)

- 데이터 저장 및 관리를 요이하게 하는 시스템

- 데이터베이스와 사용자 간의 인터페이스 역할 ; 사용자가 데이터 구성, 업데이트 모니터링, 백업, 복구 등을 할 수 있도록 도움

- MySQL

  - 가장 널리 사용되는 오픈 소스 RDBMS

  - 특징 

    - 다양한 운영체제에서 실행 가능

    - 여러 프로그래밍 언어를 위한 다양한 API 제공

    - MySQL Workbench Tool 통해 그래픽 인터페이스(GUI) 제공

  - 구조

    - **Table ⊂ Database ⊂ Database Server (MySQL)**

    ![MySQL구조](https://user-images.githubusercontent.com/121418205/217448843-217c8fe2-b3ad-49ca-8e6b-52b5a01d2834.png)
    