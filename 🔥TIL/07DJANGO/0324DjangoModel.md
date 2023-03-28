![장고모델](https://user-images.githubusercontent.com/121418205/228101522-5072d984-b43a-4001-9099-ade542f38091.png)

- SQLite ; 오픈소스 RDBMS 중 하나, django의 기본 DB (DB가 파일로 존재하며 가볍고 호환성 좋음)

# 🤯 Model

- django Model

  - DB의 테이블 정의하고 데이터를 조작할 수 있는 기능 제공

  - 테이블 구조를 설계하는 **'청사진(blueprint)'**

- model 클래스 작성

  ```python
  # articles/model.py

  class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
  ```

- model 클래스 이해하기

  ```python
  # articles/models.py

  class Article(models.Model):
      # 필드 이름 / 데이터 타입 / 제약조건
      title = models.CharField(max_length=10)
      content = models.TextField()
  ```

    - id 필드는 자동 생성

    - 아래와 같은 테이블 만들기 위한 설계도 > '모델 클래스 == 테이블 스키마'

      ![테이블](https://user-images.githubusercontent.com/121418205/228103602-8f152ac4-215b-493f-a4f4-31d8d9d2a466.png)

    - ```(models.Model)```

      - django.db.models 모듈의 Model이라는 부모 클래스 상속 받아 작성

      - model 기능에 관련된 모든 설정이 담긴 클래스 > https://github.com/django/django/blob/main/django/db/models/base.py

      - 개발자는 테이블 구조를 어떻게 설계할 지에 대한 코드만 작성하도록 하기 위해 사용

    - ```title = / content =```

      - 클래스 변수명 ; 테이블의 각 "필드 이름"

    - ```.CharField / .TextField```

      - model Field 클래스 ; 테이블 필드의 "데이터 타입" > https://docs.djangoproject.com/en/3.2/ref/models/fields/

      - CharField ; 길이 제한 있는 문자열 넣을 때 사용 (max_length는 필수 인자)

      - TextField ; 글자 수 많을 때 사용

    - ```(max_length=10)```

      - model Field 클래스의 키워드 인자 (필드 옵션) ; 테이블 필드의 "제약조건" 관련 설정 > https://docs.djangoproject.com/en/3.2/ref/models/fields/

# 😫 Migrations

- Migrations ; model 클래스의 변경사항(필드 생성, 추가 수정 등)을 DB에 최종 반영하는 방법

- Migrations 과정

  ![Migrations](https://user-images.githubusercontent.com/121418205/228104441-faba5e82-c347-4d77-baba-ed731df01a95.png)

- Migrations 핵심 명령어

  - ```$ python manage.py makemigrations``` ; model class를 기반으로 설계도(migration) 작성

  - ```$ python manage.py migrate``` ; 만들어진 설계도를 DB에 전달하여 반영

- migrate 후 DB 내에 생성된 테이블 확인

  <img width="1142" alt="Migration완료후" src="https://user-images.githubusercontent.com/121418205/228104877-b3c1eef3-002c-4f0d-a1e0-2c4ddf9a26f4.png">

- 추가 모델 필드 작성 ; 이미 생성된 테이블에 필드 추가

  1. python 파일 작성

    ```python
    # articles/models.py

    class Article(models.Model):
        # 필드 이름 / 데이터 타입 / 제약조건
        title = models.CharField(max_length=10)
        content = models.TextField()
        # 추가 모델 필드 작성
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```

    - ```.DateTimeField()``` ; 날짜와 시간 넣을 때 사용

      - 선택인자

        - ```(auto_now)``` ; 데이터가 저장될 때마다 자동으로 현재 날짜시간 저장

        - ```(auto_now_add)``` ; 데이터가 처음 생성될 때만 자동으로 현재 날짜시간 저장

  2. 터미널 makemigrations
  
    ```$ python manage.py makemigrations```

    ![makemigrations](https://user-images.githubusercontent.com/121418205/228105773-91d4e154-979c-4406-adc8-faec2ed92bb3.png)

    - 이미 기존 테이블 존재하기 때문에 필드 추가 시 필드의 기본값 설정 필요

    - **1번** 직접 기본 값 입력

    - 2번 현재 대화에서 나간 후 models.py에 기본 값 관련 설정 하는 방법

    ![makemigrations2](https://user-images.githubusercontent.com/121418205/228106164-e295977e-650b-47ea-93ac-5bd4f77d46bd.png)

    - 추가하는 필드의 기본값 입력해야하는 상황

    - 날짜 데이터이기 때문에 직접 입력보다는 django 제안 기본값 사용 권장

    - **아무것도 입력하지 않고 enter** 누르면 django 제안 기본값으로 설정됨

    ![makemigrations3](https://user-images.githubusercontent.com/121418205/228106417-ab809202-5085-4bd8-bffc-eac53189d405.png)

    <img width="408" alt="makemigrations4" src="https://user-images.githubusercontent.com/121418205/228106496-5e1f0cf9-d296-4387-81ce-b44c3346f5ee.png">

    - migrations 과정 종료 후 두번째 migration 파일 생성 확인

    - django는 설계도를 쌓아두면서 추후 문제 생기면 복구용으로 사용

  3. 터미널 migrate

    ```$ python manage.py migrate```

    <img width="1362" alt="migrate" src="https://user-images.githubusercontent.com/121418205/228106875-d69ea4c6-3c04-4120-8e49-c6294e689855.png">

    - migrate 후 필드 추가 확인

> model class에 변경사항 생겼다면, 새로운 설계도 생성하고 이를 DB에 반영!

  1. model class 작성 및 수정

  2. makemigrations

  3. migrate

# 🙂 Admin Site

- Automatic admin interface

  - django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스 제공

  - **데이터 관련 테스트 및 확인에 유용**

- admin 계정 생성 ```$ python manage.py createsuperuser```

  - email은 선택사항 ; 입력하지 않고 진행 가능

  - 비밀번호 생성 시 보안상 터미널 출력 X > 무시하고 입력 이어갈 것

- DB에 생성된 admin 계정 확인

  <img width="1157" alt="DBadmin" src="https://user-images.githubusercontent.com/121418205/228108911-eb766367-b0ad-423f-9c3e-816eac95ee2a.png">

- admin에 모델 클래스 등록 ; admin.py에 등록하지 않으면 admin site에서 확인 불가능

  ```python
  # articles/admin.py

  from django.contrib import admin
  from .models import Article

  # Register your models here.
  admin.site.register(Article)
  ```

- 로그인 후 등록된 모델 클래스 확인

  ![로그인후등록된모델클래스](https://user-images.githubusercontent.com/121418205/228109625-c5e823cb-72a2-492d-9e0c-022814e7dbd2.png)

- 데이터 CRUD 테스트

  ![CRUD테스트1](https://user-images.githubusercontent.com/121418205/228109909-bb2cfcbb-79b7-4b73-b3b7-e73e5f227599.png)

  ![CRUD테스트2](https://user-images.githubusercontent.com/121418205/228109908-61db045f-acc0-4c22-9880-c2c29e4432cd.png)

  ![CRUD테스트3](https://user-images.githubusercontent.com/121418205/228109905-074c915f-df77-414b-a609-ea64bf8658dc.png)

- 실제 테이블 저장 확인

  <img width="1312" alt="실제테이블저장" src="https://user-images.githubusercontent.com/121418205/228110060-df0b4197-c69b-4236-8d80-eae35334ba42.png">

# 😎 참고

- 데이터베이스 초기화

  1. migration 파일 삭제 (**폴더 지우지 않도록 주의**)

  2. db.sqlite3 파일 삭제

- Migrations 기타 명령어

  - ```$ python manage.py showmigrations```

    - migrations 파일들의 migrate 여부 확인하는 용도

    - [X] 표시가 있으면 migrate 완료되었음을 의미

  - ```$ python manage.py sqlmigrate articles 0001```

    - 해당 migrations 파일이 SQL 문으로 어떻게 해석되어 DB에 전달되는지 확인하는 용도

- 첫 migrate 시 출력 내용 많은 이유 ; 기본적으로 Django 프로젝트가 동작하기 위해 작성되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate 되기 때문