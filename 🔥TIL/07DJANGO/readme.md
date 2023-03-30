- model 형태 

  ```python
  # model.py
  class AppName(models.Model):
    colName = models.modelField(limitation)
  ```

- model.py 작성 > python manage.py makemigrations > python manage.py migrate

- ORM with View 사전 준비 ; app URLs 분할 및 연결

  ```python
  # firstpjt/urls.py
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls'))
  ]
  # articles/urls.py

  from django.urls import path
  from . import views

  app_name = 'articles'
  urlpatterns = [
    path('', views.index, name='index')
  ]
  ```

- 데이터 객체 생성 시 권장 방식

  ```
  >>> article = Article(title='second', content='django!')

  # 아직 저장 X
  >>> article
  <Article: Article object (None)>

  # save 호출해야 저장됨
  >>> article.save()
  >>> article
  <Article: Article object (2)>
  >>> Article.objects.all()
  <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>

  # 값 확인
  >>> article.pk
  2
  >>> article.title
  'second'
  >>> article.content
  'django!'
  ```

- 할 일 클릭 시 해당 할 일 단일 조회 페이지 이동 **url 구조**

  ```html
  <!--articles/index.html-->
  {% block content %}
    {% for todo in todos %}
      <p>{{ todo }}</p>
      <p>할 일 번호: {{ todo.pk }}</p>
      <p>할 일 제목: <a href="{%url 'todos:detail' todo.pk %}">{{ todo.title }}</a></p>
      <p>할 일 내용: {{ todo.content }}</p>
    {% endfor %}
  {% endblock content %}
  ```

- 할 일 단일 조회 **GET**

  ```python
  # articles/view.py
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

- 사용자로부터 입력받은 정보 DB에 추가

  ```python
  # articles/view.py
  def create(request):
      title = request.GET.get('title')
      content = request.GET.get('content')
      priority = request.GET.get('priority')
      deadline = request.GET.get('deadline')
      todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
      todo.save()
      context = {
          'title': title,
          'content': content,
          'priority': priority,
          'deadline': deadline,
      }
      return render(request, 'todos/create.html', context)
  ```

https://wikidocs.net/71445#_6

- HTTP request methods ; 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것

  - 'POST' Method ; 특정 리소스에 변경사항을 만드는 요청 (POST로 데이터 전달하면 HTTP Body에 담겨 보내짐)
  
    - POST method 적용

      ```python
      # articles/views.py

      def create(request):
          ttl = request.POST.get('title')
          cntnt = request.POST.get('content')
          ...
          return redirect('articles:detail', article.pk)
      ```

- DELETE

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

- UPDATE

  - edit ; 사용자의 입력을 받는 페이지 렌더링

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
      edit 페이지 이동하기 위한 하이퍼링크 작성
      ```

      ```html
      <!--articles/detail.html-->
      {% block content %}
        <a href="{% url 'articles:edit' article.pk %}">[edit]</a>
      {% endblock content %}
      ```

  - update ; 사용자가 입력한 데이터 받아 DB에 저장

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