# 🥸 사전 준비

- app URLs 분할 및 연결

  ```python
  # articles/urls.py

  from django.urls import path

  app_name = 'articles'
  urlpatterns = [
  ]

  # firstpjt/urls.py
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls'))
  ]
  ```

- index 페이지 작성

  ```python
  # articles/urls.py
  from django.urls import path
  from . import views

  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index')
  ]

  # articles/view.py
  from django.shortcuts import render

  def index(request):
      return render(request, 'articles/index.html')
  ```

  ```html
  <!--articles/index.html-->

  {% extends 'base.html' %}
  {% block content %}
    <h1>ARTICLES</h1>
  {% endblock content %}
  ```

# 🙃 READ

- 전체 게시글 조회

  ```python
  # articles/view.py

  def index(request):
      articles = Article.objects.all()
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  ```

  ```html
  <!--articles/index.html-->

  {% extends 'base.html' %}

  {% block content %}
    <h1>ARTICLES</h1>
    <hr>
    {% for article in articles %}
      <p>글 번호: {{ article.pk }}</p>
      <p>글 제목: {{ article.title }}</p>
      <p>글 내용: {{ article.content }}</p>
    {% endfor %}
  {% endblock content %}
  ```

- 단일 게시글 조회

  ```python
  # articles/urls.py

  urlpatterns = [
      ...,
      path('<int:pk>/', views.detail, name='detail'),
  ]

  # articles/view.py

  def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
  ```

  ```html
  <!--articles/detail.html-->
  {% extends 'base.html' %}

  {% block content %}
    <h1>DETAIL</h1>
    <h3>{{ article.pk }}번째 글</h3>
    <hr>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성 시각: {{ article.created_at }}</p>
    <p>수정 시각: {{ article.updated_at }}</p>
    <hr>
  {% endblock content %}
  ```

- 제목을 누르면 해당 글의 상세 페이지로 이동

  ```html
  <!--articles/index.html-->
  {% extends 'base.html' %}

  {% block content %}
    <h1>ARTICLES</h1>
    <p>{{ articles }}</p>
    <hr>
    {% for article in articles %}
      <p>{{ article }}</p>
      <p>글 번호: {{ article.pk }}</p>
      <p>글 제목:<a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></p>
    {% endfor %}
  {% endblock content %}
  ```

# 😀 CREATE

- Create 로직 구현 위해 필요한 view 함수

  - new ; 사용자 입력 받는 페이지 렌더링

    ```python
    # articles/url.py
    urlpatterns = [
        ...,
        path('new/', views.new, name='new'),
    ]

    # articles/view.py
    def new(request):
        return render(request, 'articles/new.html')
    ```

    ```html
    <!--articles/new.html-->
    {% block content %}
      <h1>NEW</h1>
      <form action="{% url 'articles:create' %}" method="GET">
        <div>
          <label for="title">Title: </label>
          <input type="text" name="title" id="title">
        </div>
        <div>
          <label for="content">Content: </label>
          <input type="type" name="content" id="content">
        </div>
        <input type="submit">
      </form>
      <hr>
      <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}

    <!--articles/index.html에 new 페이지로 이동할 수 있는 하이퍼링크 작성-->
    {% block content %}
      <h1>ARTICLES</h1>
      <p>{{ articles }}</p>
      <hr>
      <p>새로운 입력:<a href="{% url 'articles:new' %}">NEW</a></p>
      {% for article in articles %}
        <p>{{ article }}</p>
        <p>글 번호: {{ article.pk }}</p>
        <p>글 제목:<a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></p>
      {% endfor %}
    {% endblock content %}
    ```

  - create ; 사용자 입력 데이터 받아 DB에 저장

    ```python
    # articles/urls.py
    urlpatterns = [
        ...,
        path('create/', views.create, name='create'),
    ]

    # articles/view.py
    def create(request):
        ttl = request.GET.get('title')
        cntnt = request.GET.get('content')
        article = Article(title=ttl, content=cntnt)
        article.save()
        context = {
            'ttl': ttl,
            'cntnt': cntnt,
        }
        return render(request, 'articles/create.html', context)
    ```

    ```html
    <!--articles/create.html-->
    {% block content %}
      <h1>CREATE</h1>
      <p>{{ ttl }} : {{ cntnt }}</p>
      <a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}
    ```

# 🤓 HTTP request methods

- 사용자가 게시글 작성하면 해당 데이터 저장 후 유저를 어디론가 다시 보내야 한다

- redirect() ; 인자에 작성된 주소로 다시 요청 보냄

  ```python
  # articles/views.py
  from django.shortcuts import render, redirect

  def create(request):
      ttl = request.GET.get('title')
      cntnt = request.GET.get('content')
      article = Article(title=ttl, content=cntnt)
      article.save()
      context = {
          'ttl': ttl,
          'cntnt': cntnt,
      }
      return redirect('articles:detail', article.pk)
  ```

    - create view 함수 수정 > redirect 함수 적용

- HTTP request methods ; 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것

  - **'GET'** Method

    - 특정 리소스를 조회하는 요청 (GET으로 데이터 전달 시 Query String 형식으로 보내짐)
    
    - ```http://127.0.0.1:8000/articles/create/?title=제목&content=내용```

    - 반드시 **데이터를 가져올 때만** 사용해야 함

  - **'POST'** Method

    - 특정 리소스에 변경사항을 만드는 요청 (POST로 데이터 전달하면 HTTP Body에 담겨 보내짐)
    
    - ```http://127.0.0.1:8000/articles/create/?title=제목&content=내용```

    - POST method 적용

      ```python
      # articles/views.py

      def create(request):
          ttl = request.POST.get('title')
          cntnt = request.POST.get('content')
          ...
          return redirect('articles:detail', article.pk)
      ```

      ```html
      <!--articles/new.html-->

      {% block content %}
        <h1>NEW</h1>
        <form action="{% url 'articles:create' %}" method="POST">
          ...
      {% endblock content %}
      ```
  
    - 게시글 작성 후 403 Forbidden 응답 확인

      ![403](https://user-images.githubusercontent.com/121418205/228733487-b1e7155b-2ccf-4ab2-bca2-7ecb929c6485.png)

      - HTTP response status code ; 특정 HTTP 요청이 성공적으로 완료되었는지 알려줌 > 5개의 그룹으로 분류 (1xx, 2xx, 3xx, 4xx, 5xx) https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

      - 403 Forbidden ; 서버에 요청이 전달되었지만 **권한 때문에 거절**되었음을 의미

      - Help > Reason given for failure : CSRF token missing or incorrect.

        - CSRF(Cross-Site-Request-Forgery, "사이트 간 요청 위조") ; 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 후정, 삭제 등의 작업을 하게 만드는 공격 방법

        - Security Token(CSRF Token, "대표적인 CSRF 방어 방법")

          1. 서버는 사용자 입력 데이터에 임의의 난수 값(token)을 부여

          2. 매 요청마다 해당 token을 포함시켜 전송시키도록 함

          3. 이후 서버에서 요청을 받을 때마다 전달된 token이 유효한 지 검증

    - csrf_token 태그 ; DTL의 **csrf_token 태그**를 사용해 사용자에게 토큰 값 부여 > 요청 시 토큰 값도 함께 서버로 전송되도록 함

      ```html
      <!--articles/new.html-->

      {% block content %}
        <h1>NEW</h1>
        <form action="{% url 'articles:create' %}" method="POST">
          {% csrf_token %}
          ...
      {% endblock content %}
      ```

      ![csrf_token](https://user-images.githubusercontent.com/121418205/228733737-54ae77c0-b365-43d2-83fc-b7beef1c0c37.png)

      > POST Method는 데이터베이스에 대한 변경사항을 만드는 요청 ; 토큰을 사용해 최소한의 신원을 확인하는 것!

    - 게시글 생성 후 Form Data 전송되는 모습 확인

      <img width="1118" alt="Form Data" src="https://user-images.githubusercontent.com/121418205/228733983-304c7acb-6d77-4736-aa44-72cc622947da.png">

# 🫢 DELETE

- DELETE 로직 작성

  ```python
  # articles/urls.py
  urlpatterns = [
      ...
      path('<int:pk>/delete/', views.delete, name='delete')
  ]

  # articles/views.py
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('articles:index')
  ```

  ```html
  <!--articles/detail.html-->
  {% block content %}
    ...
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  {% endblock content %}
  ```

# 😛 UPDATE

- Update 로직 구현 위해 필요한 view 함수

  - **edit** ; 사용자의 입력을 받는 페이지 렌더링

    - edit 로직 작성

      ```python
      # articles/urls.py
      urlpatterns = [
          ...
          path('<int:pk>/edit/', views.edit, name='edit'),
      ]

      # articles/view.py
      def edit(request, pk):
          article = Article.objects.get(pk=pk)
          context = {
              'article': article,
          }
          return render(request, 'articles/edit.html', context)
      ```

      ```html
      <!--articles/edit.html-->
      {% block content %}
        <h1>Articles EDIT</h1>
        <form action="#" method="POST">
          {% csrf_token %}
          <div>
            <label for="title">Title: </label>
            <input type="text" name="title" id="title" value="{{ article.title }}">
          </div>
          <div>
            <label for="content">Content: </label>
            <input type="text" name="content" id="content" value="{{ article.content }}">
          </div>
          <input type="submit">
        </form>
        <hr>
        <a href="{% url 'articles:index' %}">[BACK]</a>
      {% endblock content %}
      ```

    - edit 페이지 이동하기 위한 하이퍼링크 작성

      ```html
      <!--articles/detail.html-->
      {% block content %}
        <a href="{% url 'articles:edit' article.pk %}">[edit]</a>
      {% endblock content %}
      ```

  - **update** ; 사용자가 입력한 데이터 받아 DB에 저장

    - update 로직 작성

      ```python
      # articles/urls.py
      urlpatterns = [
          ...,
          path('<int:pk>/update/', views.update, name='update')
      ]

      # articles/view.py
      def update(request, pk):
          article = Article.objects.get(pk=pk)
          article.title = request.POST.get('title')
          article.content = request.POST.get('content')
          article.save()
          return redirect('articles:detail', article.pk)
      ```

      ```html
      <!--articles/edit.html-->
      {% block content %}
        <form action="{% url 'articles:update' article.pk %}" method="POST">
          ...
      {% endblock content %}
      ```

# 😗 참고

- HTTP request methods 사용 예시 (TMDB API)

  ![HTTPrequestmethodsTMDB API](https://user-images.githubusercontent.com/121418205/228738742-1624f7da-92de-4bc2-8860-25eedee6ae1f.png)

- HTTP request methods 활용한 효율적인 URL 구조

  - (POST) articles/1/ ; 1번 게시글 생성!

  - (DELETE) articles/1/ ; 1번 게시글 삭제!