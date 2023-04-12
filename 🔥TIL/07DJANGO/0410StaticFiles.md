- Static Files ; 서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS 파일 등)

- 웹 서버와 정적 파일

  - 웹 서버의 기본 동작은 **특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서 > 응답(HTTP response)을 처리하고 제공(serving)**하는 것

  - "자원에 접근 가능한 주소가 있다"는 의미

  - 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원(static resource) 제공

  - **정적 파일 제공하기 위한 경로(URL)가 있어야 함**

# 😫 Static files 제공하기

- 경로에 따른 Static file 제공하기

  - 기본 경로 ```app/static/```

    - ```articles/static/articles/``` 경로에 이미지 파일 배치

    - static tag 사용해 이미지 파일에 대한 url 제공

      ```html
      <!--articles/index.html-->
      {% load static %}

      <img src="{% static 'articles/sample-1.png' %}" alt="img">
      ```

    - STATIC_URL ; 기본 경로 및 추가 경로에 위치한 정적 파일 참조하기 위한 URL > 실제 파일이나 디렉토리가 아니며 URL로만 존재 > 비어 있지 않은 값으로 설정 시 **반드시 slash(/)로 끝나야** 함

      ```python
      # settings.py
      STATIC_URL = '/static/'
      ```

      - URL + STATIC_URL + 정적파일 경로 ```http://127.0.0.1:8000/static/articles/sample-1.png```

  - 추가 경로 ```STATICFILES_DIRS```

    - 추가 경로에 이미지 파일 배치

      ```python
      # settings.py
      STATICFILES_DIRS = [
        BASE_DIR / 'static',
      ]
      ```

      ![추가경로staticfile](https://user-images.githubusercontent.com/121418205/231354495-bc91d5e4-2938-4487-b4f6-f6cc503dd5bd.png)

    - static tag 사용해 이미지 파일에 대한 url 제공

      ```html
      <!--articles/index.html-->
      <img src="{% static 'sample-2.png' %}" alt="img>
      ```

    - STATICFILES_DIRS ; 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

> 정적 파일 제공하기 위해서는 요청할 URL이 필요하다!

# 🤯 Media Files

- Media Files ; 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)

- ImageField() ; 이미지 업로드에 사용하는 모델 필드 > 이미지 객체가 직접 저장되는 것이 아닌 **'이미지 파일의 경로 문자열'이 DB에 저장**

- 미디어 파일 제공하기 전 준비

  1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

    - MEDIA_ROOT ; 미디어 파일들이 위치하는 디렉토리의 절대 경로
    
    - MEDIA_URL ; MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소 생성 (STATIC_URL과 동일한 역할)

      ```python
      # settings.py
      MEDIA_ROOT = BASE_DIR / 'media'
      MEDIA_URL = '/media/'
      ```

  2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

    - 업로드된 파일의 URL == settings.MEDIA_URL

    - 위 URL 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT

      ```python
      # crud/urls.py
      from django.conf import settings
      from django.conf.urls.static import static

      urlpatterns = [
          ...,
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```

# 🙂 이미지 업로드 및 제공하기

## @ 이미지 업로드

1. blanck=True 속성 작성해 빈 문자열 저장될 수 있도록 설정 > 기존 필드 사이에 작성해도 실제 테이블 생성시에는 **가장 우측(뒤)에 추가됨**

  ```python
  class Article(models.Model):
      ...
      image = models.ImageField(blank=True)
      ...
  ```

2. migration 진행 > **ImageField 사용하려면 Pillow 라이브러리 필요**

  ```
  # terminal
  pip install pillow
  python manage.py makemigrations
  python manage.py migrate
  pip freeze > requirements.txt
  ```

3. form 요소의 enctype 속성 추가

  ```html
  <!--articles/create.html-->
  {% block content %}
    <h1>CREATE</h1>
    <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
      ...
  {% endblock content %}
  ```

4. view 함수에서 업로드 파일에 대한 추가 코드 작성

  ```python
  # articles/views.py
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
          ...
  ```

5. 이미지 업로드 결과 > 파일 자체가 아닌 **"경로"가 저장되는 것**

  <img width="1946" alt="이미지업로드결과" src="https://user-images.githubusercontent.com/121418205/231377259-91c54bbe-7636-4b47-802a-5559d1482100.png">

## @ 업로드 이미지 제공하기

1. url 속성 통해 업로드 파일의 경로 값 얻을 수 있음

  ```html
  <!--articles/detail.html-->
  {% block content %}
    <h1>DETAIL</h1>
    ...
    <img src="{{ article.image.url }}" alt="img">
  {% endblock content %}
  ```

  - article.image.url ; 업로드 파일의 경로

  - article.image ; 업로드 파일의 파일 이름

2. 업로드 출력 확인 및 MEDIA_URL 확인

  ![업로드 출력확인](https://user-images.githubusercontent.com/121418205/231378405-d4f5398a-e995-43cf-9db2-f4f4dcca35ee.png)

3. 이미지 업로드하지 않은 게시물은 detail 템플릿 출력할 수 없는 문제 해결 > 이미지 데이터가 있는 경우만 이미지 출력할 수 있도록 처리

  ```html
  <!--articles/detail.html-->
  {% block content %}
    <h1>DETAIL</h1>
    ...
    {% if article.image %}
      <img src="{{ article.image.url }}" alt="img">
    {% endif %}
    ...
  {% endblock content %}
  ```

## @ 업로드 이미지 수정

1. 수정 페이지 form 요소에 enctype 속성 추가

  ```html
  <!--articles/update.html-->
  {% block content %}
    <h1>Articles EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
      ...
  {% endblock content %}
  ```

2. view 함수에서 업로드 파일에 대한 추가 코드 작성

  ```python
  # articles/views.py
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES, instance=article)
          ...
  ```

# 😎 참고

- 'upload_to' argument ; ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정

  ```
  # 1
  image = models.ImageField(blank=True, upload_to='images/')

  # 2
  image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

  # 3
  def articles_image_path(instance, filename):
      return f'images/{instance.user.username}/{filename}'

  image = models.ImageField(blank=Tre, upload_to=articles_image_path)
  ```

- request.FILES가 두번째 위치 인자인 이유 > ModelForm 상위 클래스의 생성자 함수 참고

  ![ModelForm상위클래스생성자함수](https://user-images.githubusercontent.com/121418205/231382627-1109cf06-e957-4730-a312-b160bdfa0242.png)