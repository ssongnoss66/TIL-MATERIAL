- ![URLDispatcher](https://user-images.githubusercontent.com/121418205/227085501-f16f28d8-0df0-4037-aa56-239319efd4b5.png)

- URL dispatcher (운항 관리자, 분배기) ; URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

# 🤓 변수와 URL

- 템플릿의 많은 부분이 중복되고 URL의 일부만 변경되는 상황에 활용

- Variable Routing ; URL 일부에 변수 포함시키는 것 (변수는 view 함수의 인자로 전달 가능)

- Variable routing 작성법 ```path_converter:variable_name```

  - Path converters ; URL 변수의 타입을 지정 (str, int 등 5가지 타입 지원)

- Variable Routing 실습

  1. int 타입

  ```python
  # urls.py
  urlpatterns = [
    path('apps/<int:num>/', views.detail),
  ]

  # views.py
  def detail(request, num):
    context = {
      'num': num,
    }
    request render(request, 'apps/detail.html', context)
  ```

  ```html
  <!--apps/detail.html-->
  {% extends 'base.html %}

  {% block content %}
    <h1>Detail</h1>
    <h3>{{ num }}번 글 입니다.</h3>
  {% endblock content %}
  ```

  2. str 타입

  ```python
  # urls.py
  urlpatterns = [
    path('apps/<str:name>/', views.detail),
  ]

  # views.py
  def detail(request, name):
    context = {
      'name': name,
    }
    request render(request, 'apps/greeting.html', context)
  ```

  ```html
  <!--apps/greeting.html-->
  {% extends 'base.html %}

  {% block content %}
    <h1>Detail</h1>
    <h3>{{ name }}님 안녕하세요 !</h3>
  {% endblock content %}
  ```

# 🫢 App의 URL

- App URL mapping ; 각 앱에 URL을 정의하는 것 > 프로젝트와 각각의 앱이 URL을 나누어 관리하여 주소 관리를 편하게 하기 위함

- 두번째 앱 생성 후 URL 주소가 겹친다면

  - 기존 방식

    ![기존방식](https://user-images.githubusercontent.com/121418205/227089173-317ae8ff-f99c-44de-8057-0aba72b61403.png)

    ```python
    # firstpjt/urls.py
    from articles import views as articles_views
    from pages import views as pages_views

    urlpatterns = [
      ...,
      path('articles-index', articles_views.index),
      path('pages-index', pages_views.index),
    ]
    ```

  - 변경 후 방식

    - include()
    
      - 다른 URL들을 참조할 수 있도록 돕는 함수
      
      - URL의 그 시점까지 일치하는 부분 잘라내고, 남은 문자열 부분을 후속 처리 위해 include된 URL로 전달

    ![변경후방식](https://user-images.githubusercontent.com/121418205/227089281-4be1d04c-b758-41d0-99b3-cb4b5334b132.png)

    ```python
    # firstpjt/urls.py
    from django.urls import path, include

    urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('pages/', include('pages.urls')),
    ]

    # articles/urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
      path('index/', views.index),
      path('dinner/', views.dinner),
      path('search/', views.search),
      path('throw/', views.throw),
      path('catch/', views.catch),
      path('articles/<int:num>/', views.detail),
    ]

    # pages/urls.py
    from djrnago.urls import path
    from . import views

    urlpatterns = [
      path('index/', view.index),
      path('hello/<str:name>/', views.greeting),
    ]
    ```

# 😛 URL 이름 지정

- 기존 'articles/' 주소가 'articles/index/'로 변경됨 > 기존에 articles/ 주소 사용했던 모든 위치 찾아 변경해야 됨

  ```python
  # firstpjt/urls.py
  path('articles/', include('articles.urls'))

  # articles/urls.py
  path('index/', views.index, name='index')
  ```

- Naming URL patterns ; URL에 이름 지정 (path 함수의 name 인자 정의해서 사용)

- name 인자 작성

  ```python
  # articles/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('articles/<int:num>/', views.detail, name='detail'),
  ]

  # pages/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
    path('index/', views.index, name='index'),
    path('hello/<str:name>', views.greeting, name='greeting'),
  ]
  ```

- URL 표기 변화

  - 'url' tag ; 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소 반환 ```{% url 'url-name' arg1 arg2 %}```

  - url 태그 변경 후 브라우저 출력 확인

    ![url태그변경후브라우저출력확인](https://user-images.githubusercontent.com/121418205/227105774-79da18e7-2f57-4c71-9bff-0c2cb84df967.png)

  ```html
  <!--articles/index.html-->
  <!--변화 전-->
  {% extends 'base.html' %}

  {% block content %}
    <h1>Hello, {{ name }}</h1>
    <a href="/dinner/">dinner</a>
    <a href="/search/">search</a>
    <a href="/throw/">throw</a>
  {% endblock content %}

  <!--변화 후-->
  {% extends 'base.html' %}

  {% block content %}
    <h1>Hello, {{ name }}</h1>
    <a href="{% url 'dinner' %}">dinner</a>
    <a href="{% url 'search' %}">search</a>
    <a href="{% url 'throw' %}">throw</a>
    <!--href 속성 값 뿐만 아니라 form의 action 속성처럼 url을 작성하는 모든 위치에서 변경-->
  {% endblock content %}
  ```

# 😗 URL Namespace

- URL 이름 지정 후 남은 문제 ; articles 앱의 url 이름과 pages 앱의 url 이름이 같음 > 이름만으로 분리 어려움

- app_name 속성 지정 ; url 이름 + app 이름표 붙이기

  ```python
  # articles/urls,py
  app_name = 'articles'
  urlpatterns = [
    ...,
  ]

  # pages/urls.py
  app_name = 'pages'
  urlpatterns = [
    ...,
  ]
  ```

- URL tag의 변화 ```{% url 'index' %} > {% url 'articles:index' %}```

# 🫠 참고

- app_name 지정 후 주의사항

  - app_name을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용 가능 > 그렇지 않으면 NoReverseMatch 에러 발생

  - 즉, app_name 지정 후 ```{% url 'index' %}```와 같은 표기는 사용 불가

- Trailing Slashes

  - django는 URL 끝에 '/' 없으면 자동으로 붙임

  - django의 url 설계 철학 "기술적인 측면에서 foo.com/bar와 foo.com/bar/은 서로 다른 URL이다"

  - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 서로 다른 페이지로 봄 > django는 검색 엔진이 혼동하지 않게 하기 위해 사용 but 모든 프레임워크가 이렇게 동작하는 것은 X