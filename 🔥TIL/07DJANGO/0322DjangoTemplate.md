# 😶‍🌫️ Template System

- django template system ; 데이터 **표현**을 제어하면서, **표현**과 관련된 로직 담당

- HTML의 특정 부분을 변수 값에 따라 바꾸고 싶다면?

  ```python
  # views.py
  def index(request):
    context = {
      'name': 'Sophia',
    }
    return render(request, 'articles/index.html', context)
  ```

  ```html
  <!--index.html-->
  <body>
    <h1>Hello, {{ name }}</h1>
  </body>
  ```

## @ DTL

- Django Template Language (DTL) ; Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

- DTL Syntax

  1. Variable ```{{ variable }}```

    - view 함수에서 render 함수의 세번째 인자로 딕셔너리 타입으로 넘겨 받을 수 있음

    - 딕셔너리 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨

    - dot(.)를 사용하여 변수 속성에 접근 가능

  2. Filters ```{{ variable|filter }}```

    - 표시할 변수를 수정할 때 사용

    - chained가 가능하며 일부 필터는 인자를 받기도 함 ```{{ name|truncatewords:30 }}```

    - 약 60개의 built-in template filters 제공

  3. Tags ```{% tag %}```

    - 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행

    - 일부 태그는 시작과 종료 태그가 필요 ```{% if %} {% endif %}```

    - 약 24개의 built-in template tags 제공

  4. Comments ```{# name #} 또는 {% comment %} ... {% endcomment %}```

    - 주석

      ```
      {% comment %}
        {% if name == 'Sophia' %}
        {% endif %}
      {% endcomment %}
      ```

- DTL 실습

  ```python
  # urls.py

  urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
    path('dinner/', views.dinner),
  ]

  # view.py
  import random

  def dinnner(request):
    foods = ['pizza', 'hamburger', 'bibimbap', 'bulgogi']
    picked = random.choice(foods)
    context = {
      'foods': foods,
      'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)
  ```

  ```html
  <!-- articles/dinner.html -->
  <p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다</p>

  <h2>메뉴판</h2>
  <ul>
    {% for food in foods %}
      <li>{{ food }}</li>
    {% endfor %}
  </ul>

  {% if foods|length == 0 %}
    <p>메뉴가 소진되었습니다</p>
  {% else %}
    <p>아직 메뉴가 남았습니다</p>
  {% endif %}
  ```

  ![DTL실습](https://user-images.githubusercontent.com/121418205/226904884-ade07b62-8e95-4c4e-8899-a80dc66d7d1f.png)

# 😕 템플릿 상속

- 모든 템플릿에 bootstrap 적용하기 위해 모든 템플릿에 CDN 작성?

- 템플릿 상속 (Template Inheritance) ; 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조 구축

- skeleton 역할 템플릿 작성

  ```html
  <!-- articles/base.html-->
  <!doctype html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
      <title>Document</title>
    </head>
    <body>
      {% block content %}
      {% endblock content %}
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    </body>
  </html>
  ```

- 기존 템플릿의 변화

  ```html
  <!--articles/dinner.html-->
  <!--기존-->
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1>Hello, {{ name }}</h1>
  </body>
  </html>

  <!--skeleton 활용 후-->
  {% extends 'articles/base.html' %}
  {% block content %}
    <h1>Hello, {{ name }}</h1>
  {% endblock content %}
  ```

- 'extends' tag ```{% extends 'path' %}```

  - 자식 (하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림

    > 반드시 템플릿 최상단에 작성되어야 함 (2개 이상 사용 불가)

- 'block' tag ```{% block name %}{% endblock name %}```

  - 하위 템플릿에서 재정의(overriden)할 수 있는 블록을 정의 (하위 템플릿이 작성할 수 있는 공간 지정)

    ```html
    <!--부모 템플릿-->
    <!doctype html>
    <html lang="en">
      <head>
        ...
      </head>
      <body>
        {% block content %}
        {% endblock content %}
      </body>
    </html>

    <!--자식 템플릿-->
    {% extends 'articles/base.html' %}
    {% block content %}
      <h1>Hello, {{ name }}</h1>
    {% endblock content %}
    ```

# 😏 요청과 응답 with HTML form

- 데이터를 보내고 가져오기 (Sending and Retrieving form data) ; HTML form element 통해 사용자와 애플리케이션 간의 상호작용 이해하기

- HTML form ; HTTP 요청을 서버에 보내는 가장 편리한 방법

- form 태그 구조

  ```html
  <form action="#" method="GET">
    <div>
      <label for="name">아이디 : </label>
      <input type="text" id="name">
    </div>
    <div>
      <label for="password">패스워드 : </label>
      <input type="password" name="password" id="password">
    </div>
    <input type="submit" value="로그인">
  </form>
  ```

  ![form태그](https://user-images.githubusercontent.com/121418205/226911087-c132c7e6-1c73-4cc1-b9e6-57620b8fca3b.png)

- 'form' element

  - 사용자로부터 할당된 데이터를 서버로 전송

  - 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 제공

  - 핵심 속성 ; 데이터를 어디(**action**)로 어떤 방식(**method**)으로 보낼 지"

    - action

      - 입력 데이터가 전송될 URL을 지정 (목적지)

      - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

    - method

      - 데이터를 어떤 방식으로 보낼 것인지 정의
      
      - 데이터의 HTTP request methods (GET, POST)를 지정

- 'input' element

  - 사용자의 데이터를 입력받을 수 있는 요소
  
  - type 속성 값에 따라 다양한 유형의 입력 데이터 받음

  - 핵심 속성

    - name ; 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근 가능

- 검색 페이지 실습

  ```python
  # urls.py
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search)
  ]

  # views.py
  def search(request):
      return render(request, 'articles/search.html')
  ```

  ```html
  <!--articles/search.html--> 
  {% extends 'articles/base.html' %}

  {% block content %}
    <form action="" method="GET">
      <label for="message">검색어</label>
      <input type="text" name="message" id="message"> <!-- 🥸 -->
      <input type="submit" value="submit">
    </form>
  {% endblock content %}
  ```

  - django 입력 및 제출 뒤 url 변화 확인

    > http://127.0.0.1:8000/search/?message=qwer

    - 🥸에 해당하는 message가 ? 뒤에 위치하고 input에 입력한 데이터가 = 뒤에 위치한다

- fake Naver 실습

  - Naver에서 검색 후 URL 분석

    > https://search.naver.com/search.naver?query=django

    - 목적지 URL ? input의 name = input에 입력한 데이터

  ```html
  <!--articles/search.html--> 
  {% extends 'articles/base.html' %}

  {% block content %}
    <form action="https://search.naver.com/search.naver" method="GET">
      <label for="message">검색어</label>
      <input type="text" name="query" id="message">
      <input type="submit" value="submit">
    </form>
  {% endblock content %}
  ```

- Query String Parameters

  - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 넘기는 방법

  - 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며, 기본 URL과 물음표(?)로 구분됨

  - 예시 ```http://host:port/path?key=value&key=value```

# 🙃 요청과 응답 활용

- 사용자 입력 데이터를 받아 그대로 출력하는 서비스 제작

  ![서비스페이지예시](https://user-images.githubusercontent.com/121418205/226921461-e279eff2-88d0-4d94-9d6f-6f18178d8f54.png)

  - view 함수는 2개 필요

    1. throw 작성

      ```python
      # urls.py
      urlpatterns = [
          ...,
          path('throw/', views.throw),
      ]

      # views.py
      def throw(request):
          return render(request, 'berners_lee/throw.html')
      ```
      ```html
      <!--throw.html-->
      {% extends 'berners_lee/base.html' %}

      {% block content %}
        <h1>Throw</h1>
        <form action="http://127.0.0.1:8000/catch/" method="GET">
          <input type="text" name="message">
          <input type="submit">
        </form>
      {% endblock content %}
      ```

    2. catch 작성

      ```python
      # urls.py
      urlpatterns = [
          ...,
          path('catch/', views.catch),
      ]

      # views.py
      def catch(request):
          data = request.GET.get('message')
          context = {
              'data': data,
          }
          return render(request, 'berners_lee/catch.html', context)
      ```
      ```html
      <!--catch.html-->
      {% extends 'berners_lee/base.html' %}

      {% block content %}
        <h1>Catch</h1>
        <h1>{{ data }}를 받았습니다!</h1>
      {% endblock content %}
      ```

  - form 데이터의 위치 ; 모든 요청 데이터는 **HTTP request** 객체에 들어있음 (view 함수의 첫번째 인자)

  - request 객체 살펴보기

    ```python
    print(request)                      # <WSGIRequest: GET '/catch/?message=DJANGO'>
    print(type(request))                # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(dir(request))                 # ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'headers', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
    print(request.GET)                  # <QueryDict: {'message': ['DJANGO']}>
    print(request.GET.get('message'))   # DJANGO
    ```

    ![request객체](https://user-images.githubusercontent.com/121418205/226928908-2ebe713e-e6f8-4af4-af0d-d71361acb2da.png)

# 😀 참고

- 추가 템플릿 경로 지정

  ```python
  # settings.py

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates',],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  ![추가템플릿경로지정](https://user-images.githubusercontent.com/121418205/226930542-3291bd5a-3155-4111-842f-38059174ce3c.png)

- BASE_DIR ; settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정해놓은 변수

  ```python
  # settings.py

  # Build paths inside the project like this: BASE_DIR / 'subdir'.
  BASE_DIR = Path(__file__).resolve().parent.parent
  ```

  ![BASE_DIR위치](https://user-images.githubusercontent.com/121418205/226930922-46e400a2-5ab4-4204-aa57-46010d73f5db.png)

- DTL 주의사항

  - Python처럼 일부 프로그래밍 구조(if, for 등) 사용 가능 but 명칭을 그렇게 설계했을 뿐 **Python 코드로 실행되는 것 아니며 Python과 관련 없음**

  - 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것 ; 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리

- DTL 학습 https://docs.djangoproject.com/en/3.2/ref/templates/builtins/