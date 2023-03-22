# 😎 django 프로젝트와 앱

- django project ; 애플리케이션의 집합 (DB 설정, URL 연결, 전체 앱 설정 등 처리)

- django application ; 독립적으로 작동하는 기능 단위 모듈 (각자 특정한 기능 담당하며 다른 앱들과 함께 하나의 프로젝트 구성) > **MTV 패턴에 해당하는 파일 및 폴더 담당**

- 만약 블로그를 만든다면 1. 프로젝트 ; 블로그 (전체 설정 담당) 2. 앱 ; 게시글, 댓글, 카테고리 회원 관리 등 (DB, 로직, 화면)

- 앱 생성

  ```
  $ python manage.py startapp articles
  ```

- 앱 등록 ; **반드시 앱 생성 후 등록, 반대로 등록 후 생성은 불가능**

  ```python
  #settings.py

  INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  ]
  ```

# 🙂 django 디자인 패턴

- (소프트웨어) 디자인 패턴 ; 소프트웨어 설계에서 발생하는 문제 해결을 위한 일반적 해결책 (공통적 문제 해결하는데 쓰이는 형식화된 관행)

- MVC 디자인 패턴 (Model-View-Controller)

  - 애플리케이션 구조화하는 대표적 패턴 (데이터, 사용자 인터페이스, 비즈니스 로직을 분리)

  - **시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지보수**할 수 있는 애플리케이션을 만들기 위해!

    ![MVC](https://user-images.githubusercontent.com/121418205/226498043-4bff7311-a002-4bd3-b8a8-5a4271f86e14.png)

- MTV 디자인 패턴 (Model-Template-View)

  - django에서 애플리케이션을 구조화하는 패턴 (기존 MVC와 동일하나 명칭 다르게 정의)

  - view > template / controller > view

- 프로젝트 구조

  ![프로젝트구조](https://user-images.githubusercontent.com/121418205/226500227-2b03637c-fdbd-4a20-93bf-a1d739aee9e4.png)

  - 다루게 될 파일

    - ```settings.py``` ; 프로젝트의 모든 설정 관리

    - ```urls.py``` ; URL과 이에 해당하는 적절한 views를 연결

  - 현재 단계에서 별도 수정 X

    - ```__init__.py``` ; 해당 폴더를 패키지로 인식하도록 설정

    - ```asgi.py``` ; 비동기식 웹 서버와의 연결관련 설정

    - ```wsgi.py``` ; 웹 서버와의 연결 관련 설정

    - ```manage.py``` ; Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

- 앱 구조

  ![앱구조](https://user-images.githubusercontent.com/121418205/226500223-fbd6cd41-d86b-430d-959c-0d752d47fd56.png)

  - 다루게 될 파일

    - ```admin.py``` ; 관리자용 페이지 설정

    - ```models.py``` ; DB와 관련된 Model 정의 / MTV의 M

    - ```views.py``` ; HTTP 요청을 처리하고 해당 요청에 대한 응답 반환 (url, mode, template) / MTV의 V

  - 현재 단계에서 별도 수정 X

    - ```apps.py``` ; 앱의 정보가 작성된 곳

    - ```tests.py``` ; 프로젝트 테스트 코드를 작성하는 곳

- django 프로젝트 구조

  ![DJANGO프로젝트](https://user-images.githubusercontent.com/121418205/226500325-bbd43335-c95d-4cee-86e1-28a5f5c07306.png)

# 🥲 요청과 응답

- URLs ; http://128.0.0.1:8000/**articles/** 로 요청이 왔을 때 **views** 모듈의 **index** 뷰 함수를 호출한다는 뜻

  ```python
  # urls.py

  from django.contrib import admin
  from django.urls import path
  from articles import views

  urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
  ]
  ```

- View ; 특정 경로에 있는 **template**과 **request 객체**를 결합해 응답 객체를 반환하는 index 뷰 함수 정의

  ```python
  # views.py

  from django.shortcuts import render

  def index(request):
    return render(request, 'articles/index.html')
  ```

- Template ; 반드시 **templates 폴더명이어야** 하며 개발자가 직접 생성해야

  - django에서 template 인식하는 경로 규칙 ; django는 아래 강조한 부분까지 기본 경로로 인식하기 때문에 이 지점 이후의 template 경로 작성해야 함

    - **app폴더 / templates /** articles / index.html

    - **app폴더 / templates /** example.html

  1. articles 앱 폴더 안에 templates 폴더 작성

  2. templates 폴더 안에 템플릿 페이지 작성

  ```html
  <!-- articles/index.html -->

  <!DOCTYPE html>
  <html lang="en">
  <head>
    ...
    <title>Document</title>
  </head>
  <body>
    <h1>Hello, django</h1>
  </body>
  </html>
  ```

  ![template](https://user-images.githubusercontent.com/121418205/226505050-24c60a6f-dcbf-446a-bfd9-5cb92fbee0e9.png)

> 데이터 흐름에 따른 코드 작성

  ```
  - URLs      path('articles/', views.index)
  
  - View      def index(request):
                  return render(request, 'articles/index.html')
  
  - Template  articles/templates/articles/index.html
  ```

# 🧐 참고

- render 함수 ```render(request, template_name, context)```

  - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수

  1. request ; 응답을 생성하는데 사용되는 요청 객체

  2. template_name ; 템플릿 이름의 경로

  3. context ;  템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)