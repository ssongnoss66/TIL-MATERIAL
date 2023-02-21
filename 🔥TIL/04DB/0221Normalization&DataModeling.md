# 0221 TUE

## 😛 Normalization 정규화

- RDB 설계 단계에서 중복 최소화하여 데이터 **구조화**하는 과정

  - 구조화 ; 크고, 제대로 조직되지 않은 테이블들과 관계들을 작고 잘 조직된 테이블과 관계들로 나누는 것

- 목적 ; **데이터를 쉽게 관리하기 위해**

  - 하나의 데이터를 무조건 한 곳에만 위치하도록

  - 테이블 간의 관계는 키를 통해 형성

  - 데이터를 변경하더라도 한 곳만 변경하는 구조 확립

- 1 ~ 3 정규화 진행

  ![1_3정규화](https://user-images.githubusercontent.com/121418205/220217235-ed3ce024-0152-4f0b-9b7e-5669a23b4fc2.jpg)

  - 제 1 정규화

    - 데이터베이스의 각 필드에는 하나의 값만 저장해야 함

    - 유사하게 정보를 저장하는 두 개의 필드가 있어서는 안 됨 ; 반복되는 부분을 찾아 테이블 분할 > 기본키가 될 필드 작성

      ![제1정규화](https://user-images.githubusercontent.com/121418205/220217367-d6f42318-2389-4950-a98d-d1ee7282d521.jpg)

  - 제 2 정규화

    - 키 값을 이용해 데이터를 특정 지을 수 있는 것(함수 종속성)을 찾아 테이블 분할

      ![제2정규화](https://user-images.githubusercontent.com/121418205/220217472-dd2c9d1f-1080-41bf-8100-2b0fdbd3f5ad.jpg)

  - 제 3 정규화

    - 기본 키 이외의 부분에서 중복이 없는 지 조사하여 테이블 분할

      ![제3정규화](https://user-images.githubusercontent.com/121418205/220217579-c2cfa8d2-9108-48f3-8a40-954971ce2e80.jpg)

## 😗 Data Modeling

- 데이터베이스 시스템을 시각적으로 표현하는 프로세스 ; for 데이터 유형, 데이터 간의 관계 및 분석 등을 통해 비즈니스 요구사항을 만들어 낼 수 있도록 도움

- 데이터 모델링의 중요성

  - 데이터베이스 소프트웨어 개발 오류 감소

  - 데이터베이스 설계 및 생성 속도와 효율성 촉진

  - 조직 전체에서 데이터 문서화 및 시스템 설계의 일관성 조성

  - 데이터 엔지니어와 비즈니스 팀 간의 커뮤니케이션 촉진
  
- ER (Entity-Relationship) Diagram ; 다이어 그램을 사용하여 데이터베이스의 Entity 간 관계를 나타내는 방법

  - 구성 요소

    ![ERDiagram구성요소](https://user-images.githubusercontent.com/121418205/220220621-ed0a03bc-c98f-4718-8b57-9689c50c9fa8.jpg)

  - 작성 예시

    - Entity 정의

      ![Entity](https://user-images.githubusercontent.com/121418205/220220850-79604358-38ed-4b02-b37d-8cbf9770c303.jpg)

    - Attribute + 식별자 정의

      ![Attribute](https://user-images.githubusercontent.com/121418205/220220836-4479fcf9-286f-4bdf-a83a-af1939b050bf.jpg)

    - Relationship 정의

      ![Relationship](https://user-images.githubusercontent.com/121418205/220220832-b95c81ed-0bac-42a0-b95c-00081178c1c1.jpg)
    
      - 표현 방법

        - Cardinality (기수)

          - 1:1 관계

          - 1:N 관계

          - M:N 관계

        - Optionality (선택 가능성)

          - 1:N 관계라면 회원은 "필수" & 글은 "선택"
        
        > Cardinality와 Optionality을 조합

          - "하나의 회원은 여러 개의 글을 작성할 수 있고 하나의 글은 한 명의 회원이 작성할 수 있다"

          - 회원과 글의 관계는 **1:N** / 글은 **필수적**으로 회원과 연결 / 회원은 **선택적**으로 글과 연결