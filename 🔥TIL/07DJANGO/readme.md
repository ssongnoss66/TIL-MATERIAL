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