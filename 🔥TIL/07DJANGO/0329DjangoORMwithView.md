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