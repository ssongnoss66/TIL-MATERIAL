- HTTP Request Methods ; 리소스(resource, 자원)에 대한 행위(수행하고자 하는 동작)를 정의 (HTTP verbs라고도 함)

  1. GET ; 서버에 리소스의 표현을 요청 / GET을 사용하는 요청은 **데이터만 검색**해야 함

  2. POST ; 데이터를 지정된 리소스에 제출 / **서버의 상태**를 변경

  3. PUT ; 요청한 주소의 리소스 수정

  4. DELETE ; 지정된 리소스 삭제

- HTTP response status codes ; 특정 HTTP 요청이 성공적으로 완료되었는지를 나타냄 https://http.cat/

  1. Informational responses (100-199)

  2. Successful responses (200-299)

  3. Redirection messages (300-399)

  4. Client error responses (400-499)

  5. Server error responses (500-599)

# 😎 REST API

- API (Application Programming Interface) ; 애플리케이션과 프로그래밍으로 소통하는 방법 > 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문 제공 ```우리는 가전제품에 직접 배선을 하지 않는다```

- Web API

  - 웹 서버 또는 웹 브라우저를 위한 API > 웹 개발은 여러 Open API를 활용하는 추세

  - 대표적인 Third Party Open API 서비스 ; YoutubeAPI, Naver Papago API, Kakao Map API

  - API는 다양한 타입의 데이터를 응담 ; HTML, JSON 등

- REST (Representational State Transfer)

  - API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론 ; 2000년 로이 필딩의 박사학위 논문에서 처음으로 소개된 후 네트워킹 문화에 널리 퍼짐

  - '소프트웨어 아키텍쳐 디자인 제약 모음' (a group of software architecture design constraints)

  - REST 원리를 따르는 시스템을 **RESTful** 하다고 부름

  - **"자원을 정의"**하고 **"자원에 대한 주고를 지정"**하는 전반적인 방법을 서술

- REST에서 자원을 정의하고 주소를 지정하는 방법

  1. 자원의 식별 ; URI

  2. 자원의 행위 ; HTTP Methods

  3. 자원의 표현

    - 궁극적으로 표현되는 결과물

    - JSON으로 표현된 데이터 제공

- REST API ; REST라는 API 디자인 아키텍처를 지켜 구현한 API

  ![REST API](https://user-images.githubusercontent.com/121418205/234483904-b979a14c-93e2-4a55-b43c-08fe7a6b1d69.png)

# 🧐 Response JSON

- 서버가 응답하는 것

  - 지금까지 Django로 작성한 서버는 사용자에게 페이지(html)만 응답하고 있었음

  - 하지만 서버가 응답할 수 있는 것은 페이지뿐만 아니라 **다양한 데이터 타입**을 응답할 수 있음

  - 페이지(html)를 응답하는 서버에서 JSON 데이터를 응답하는 서버로의 변환

  - Django는 더 이상 Template 부분에 대한 역할을 담당하지 않게 되며 Front-end와 Back-end가 분리되어 구성됨

    ![서버가 응답하는 것](https://user-images.githubusercontent.com/121418205/234484451-d993e2be-3029-4a78-9d31-6484e9b4398f.png)

- 사전 준비 ; 사전 제공된 99_json_response 프로젝트 준비 > 가상 환경 생성, 활성화 및 패키지 설치 > migrate 진행 > 준비된 fixtures 파일을 load하여 실습용 초기 데이터 입력 > http://127.0.0.1:8000/api/v1/articles/ 요청 테스트

- Django REST framework (DRF) ; Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리 https://www.django-rest-framework.org/

- python에서 json 응답 받아보기

  1. 준비된 python_sample.py 확인

    ```python
    import requests
    from pprint import pprint


    response = requests.get('http://127.0.0.1:8000/api/v1/articles/')

    # json을 python 타입으로 변환
    result = response.json()

    # print(type(result))
    # pprint(result)
    # pprint(result[0])
    pprint(result[0].get('title'))
    ```

  2. 준비된 python_sample.py 실행

    <img width="1593" alt="python에서 json 응답 받아보기" src="https://user-images.githubusercontent.com/121418205/234486828-13cdf7fa-af4f-4481-b83a-098f1cf253a8.png">

# 😶‍🌫️ Serialization

- Serialization "직렬화"

  - 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
  
  - 어떠한 언어나 환경에서도 **"나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"**

  - 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

    ![Serialization](https://user-images.githubusercontent.com/121418205/234487720-f0b95403-16dc-4636-ba04-cd3e9597918f.png)

- Serializers in DRF ; 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

  ![Serializers](https://user-images.githubusercontent.com/121418205/234487950-546ca5dc-1f98-4678-95b5-a2459953ea1c.png)

# 🥲 DRF - Single Model

- 사전 준비 ; 사전 제공된 drf 프로젝트 준비 > 가상환경 생성, 활성화 및 패키지 설치 > migrate 진행 > 준비된 fixtures 파일 load하여 실습용 초기 데이터 입력 > Postman 설치 https://www.postman.com/downloads/

- Postman

  - API 구축하고 사용하기 위한 플랫폼 > API를 빠르게 만들 수 있는 여러 도구 및 기능 제공

    ![Postman](https://user-images.githubusercontent.com/121418205/234541177-b02f87fb-c3f9-4b0d-8183-ee2461074ce2.png)

- ModelSerializer 

  - 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만듦

    1. Model 정보에 맞춰 자동으로 필드 생성

    2. serializer에 대한 유효성 검사기 자동으로 생성

    3. .create() 및 .update()의 기본 구현 메서드가 포함됨

  - 작성 ; articles/serializers.py 생성 (위치나 파일명은 자유롭게 작성 가능)

    ```python
    # articles/serializers.py
    from rest_framework import serializers
    from .models import Article, Comment


    class ArticleListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title', 'content',)
    ```

- URL과 HTTP requests methods 설계

  ![URL HTTP requests](https://user-images.githubusercontent.com/121418205/234546055-7447cc56-db55-494c-9ddc-710c1e836307.png)

- GET

  - List

    1. 게시글 데이터 목록 조회하기

      - 'api_view' decorator

        - DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음

        - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

        - DRF view 함수에서는 필수로 작성

      ```python
      # articles/urls.py
      from django.urls import path
      from articles import views


      urlpatterns = [
          path('articles/', views.article_list),
      ]

      # articles/views.py
      from rest_framework.response import Response
      from rest_framework.decorators import api_view

      from .models import Article
      from .serializers import ArticleListSerializer

      @api_view(['GET'])
      def article_list(request):
          articles = Article.objects.all()
          serializer = ArticleListSerializer(articles, many=True)
          return Response(serializer.data)
      ```

    2. http://127.0.0.1:8000/api/v1/articles/ 응답 확인

  - Detail

    1. 단일 게시글 데이터 조회하기 > 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의

      ```python
      # articles/serializers.py
      class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = '__all__'
      ```

    2. url 및 view 함수 작성

      ```python
      # articles/urls.py
      urlpatterns = [
          ...
          path('comments/<int:comment_pk>/', views.comment_detail),
      ]

      # articles/views.py
      from .serializers import ArticleListSerializer, ArticleSerializer

      @api_view(['GET'])
      def article_detail(request, article_pk):
          article = Article.objects.get(pk=article_pk)
          serializer = ArticleSerializer(article)
          return Response(serializer.data)
      ```

- POST ; 게시글 데이터 새성하기 > 요청에 대한 데이터 생성이 성공했을 경우 201 Created 상태 코드 응답하고 실패했을 경우 400 Bad request 응답

  - view 함수 작성
    
    - raise_exception ; is_valid()는 유효성 검사 오류 있는 경우 ValidationError 예외 발생시키는 선택적 raise_exception 인자 사용 가능 > DRF에서 제공하는 기본 예외처리기에 의해 자동 처리되며 기본적으로 HTTP 400 응답 반환

    ```python
    # articles/views.py
    from rest_framework import status

    @api_view(['GET', 'POST'])
    def article_list(request):
        if request.method == 'GET':
            # 1. 제공할 게시글 목록 조회
            articles = Article.objects.all()
            # 2. 게시글 목록 데이터를 직렬화(serialization)
            serializer = ArticleListSerializer(articles, many=True)
            # 3. DRF의 Response로 직렬화된 데이터를 json 데이터로 응답
            return Response(serializer.data)
        
        elif request.method == 'POST':
            # 사용자 데이터를 받아서 serializer로 직렬화
            serializer = ArticleSerializer(data=request.data)
            # 유효성 검사
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # 생성 성공 시 201 응답
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # 생성 실패 시 400 응답
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

- DELETE

  - 게시글 데이터 삭제하기 > 요청에 대한 데이터 삭제가 성공했을 경우 204 No Content 상태 코드 응답

    ```python
    # articles/views.py
    @api_view(['GET', 'DELETE'])
    def article_detail(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        if request.method == 'GET':
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

        elif request.method == 'DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    ```

- PUT

  - 게시글 데이터 수정하기 > 요청에 대한 데이터 수정 성공했을 경우 200 OK 상태 코드 응답

    ```python
    # articles/views.py
    @api_view(['GET', 'DELETE', 'PUT'])
    def article_detail(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        ...
        elif request.method == 'PUT':
            # 사용자 데이터를 받아서 serializer로 직렬화 + 기존 데이터
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            # 수정에 실패했을 때
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    ```

# 😕 N:1 Relation

- 사전 준비 ; Comment 모델 작성 및 데이터베이스 초기화 > Migration 및 fixtures 데이터 로드

- GET

  - List ; 댓글 데이터 목록 조회하기

    ```python
    # articles/serializers.py
    from .models import Article, Comment

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    # articles/urls.py
    urlpatterns = [
        ...,
        path('comments/', views.comment_list)
    ]

    # articles/views.py
    from .models import Article, Comment
    from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

    @api_view(['GET'])
    def comment_list(request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    ```

  - Detail ; 단일 댓글 데이터 조회하기

    ```python
    # articles/urls.py
    urlpatterns = [
        ...,
        path('comments/<int:comment_pk>/', views.comment_detail),
    ]

    # articles/views.py
    @api_view(['GET'])
    def comment_detail(request, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    ```

- POST

  1. 단일 댓글 데이터 생성

    ```python
    # articles/urls.py
    urlpatterns = [
        ...,
        path('articles/<int:article_pk>/comments/', views.comment_create),
    ]

    # articles/views.py
    @api_view(['POST'])
    def comment_create(request, article_pk):
        article = Article.obejcts.get(pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    ```

  2. save() 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음 > CommentSerialize되는 과정에서 Parameter로 넘어온 article_pk에 해당하는 article 객체를 추가적인 데이터 넘겨 저장

    ```python
    # articles/views.py
    @api_view['POST']
    def comment_create(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    ```

    <img width="447" alt="GET not allowed" src="https://user-images.githubusercontent.com/121418205/235682737-f2eba601-9a45-4d55-ac93-f3c3d285d2dc.png">

    - 읽기 전용 필드 설정 ; ```read_only_fields``` 사용해 외래 키 필드를 읽기 전용 필드로 설정 > 데이터 전송하는 시점에 '**해당 필드를 유효성 검사에서 제외시키고, 데이터 조회 시에는 출력**'하도록 함

- DELETE & PUT

  ```python
  # articles/views.py
  @api_view(['GET', 'DELETE', 'PUT'])
  def comment_detail(request, comment_pk):
      comment = Comment.objects.get(pk=comment_pk)
      if request.method == 'GET':
          serializer = CommentSerializer(comment)
          return Response(serializer.data)
      elif request.method == 'DELETE':
          comment.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      elif request.method == 'PUT':
          serializer = CommentSerializer(comment, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  ```

# 😏 N:1 역참조 데이터 조회

- 두가지 역참조 상황 작성해보기

- 특정 게시글에 작성된 댓글 목록 출력하기 ; 기존 필드 override > 1. PrimaryKeyRelatedField() 2. Nested relationships

  1. PrimaryKeyRelatedField() ; "게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력하기"
  
    - Serializer는 기존 필드를 override하거나 추가적인 필드 구성 가능

      ```python
      # articles/serializers.py
      class ArticleSerializer(serializers.ModelSerializer):
          comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
          class Meta:
              model = Article
              fields = '__all__'
      ```

    - models.py에서 related_name 통해 역참조 매니저명 변경 가능

      ```python
      # articles/models.py
      class Comment(models.Model):
          article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
          content = models.TextField()
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
      ```

  2. Nested relationships

    - 모델 관계 상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩될 수 있음 > 이러한 중첩 관계는 serializers를 필드로 사용하여 표현 가능

      ```python
      # articles/serializers.py
      class CommentSerializer(serializer.ModelSerializer):
          class Meta:
              model = Comment
              fields = '__all__'
              read_only_fields = ('article',)

      class ArticleSerializer(serializers.ModelSerializer):
          comment_set = CommentSerializer(many=True, read_only=True)
          class Meta:
              model = Article
              fields = '__all__'
      ```

- 특정 게시글에 작성된 댓글의 개수 출력하기 ; 새로운 필드 추가

  1. 새로운 필드 추가 Article Detail
  
    - "게시글 조회 시 해당 게시글의 댓글 갯수까지 함께 출력"

      ```python
      # articles/serializers.py
      class ArticleSerializer(serializers.ModelSerializer):
          comment_set = CommentSerializer(many=True, read_only=True)
          comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
          class Meta:
              model = Article
              fields = '__all__'
      ```

  2. source

    - 필드를 채우는 데 사용할 속성의 이름

    - 점 표기법(dotted notation)을 사용하여 속성을 탐색할 수 있음

      ```python
      # articles/serializers.py
      class ArticleSerializer(serializers.ModelSerializer):
          comment_set = CommentSerializer(many=True, read_only=True)
          comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
          class Meta:
              model = Article
              fields = '__all__'
      ```

- [주의] 읽기 전용 필드 지정 이슈 ; 특정 필드를 override 혹은 추가한 경우 read_only_fields가 동작하지 않음

  ```python
  # articles/serializers.py

  # 사용 불가능
  class ArticleSerializer(serializers.ModelSerializer):
      comment_set = CommentSerializer(many=True)
      comment_count = serializers.IntegerField(source='comment_set.count')
      class Meta:
          model = Article
          fields = '__all__'
          read_only_fields = ('comment_set', 'comment_count')
  ```

- 댓글 조회 시 게시글 출력 변경해보기 ; 필요한 Serializer는 **내부에서 추가 선언** 가능

  ```python
  # articles/serializers.py
  class CommentSerializer(serializers.ModelSerializer):
      class ArticleTitleSerializer(serializers.ModelSerializer):
          class Meta:
              model = Article
              fields = ('title',)
      article = ArticleTitleSerializer(read_only=True)
      class Meta:
          model = Comment
          fields = '__all__'
  ```

# 🥸 API 문서화

- API 구조를 안내하는 문서 만들기 > Swagger ; REST 웹 서비스를 설계, 빌드, 문서화 등을 도와주는 오픈 소스 소프트웨어 프레임워크

- Swagger 라이브러리 사용 ; 설치 및 등록 https://drf-yasg.readthedocs.io/en/stable/

  ```$ pip install drf-yasg```

  ```python
  # settings.py
  INSTALLED_APPS = [
      'articles',
      'rest_framework',
      'drf_yasg',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]

  # drf/urls.py
  from rest_framework import permissions
  from drf_yasg.views import get_schema_view
  from drf_yasg import openapi

  schema_view = get_schema_view(
    openapi.Info(
        title="나만의 API 서비스",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
  )

  urlpatterns = [
      ...,
      path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
  ]
  ```

# 🙃 참고

- Django shortcuts functions

  - get_object_or_404() ; 모델 manager objects에서 get()을 호출하지만, 해당 객체가 **없을 땐** 기존 DoesNotExist 예외 대신 **Http404**를 raise 함

    ```python
    # articles/views.py
    from django.shortcuts import get_object_or_404

    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)

    # 위 코드를 모두 다음과 같이 변경
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    ```

  - get_list_or_404() ; 모델 manager objects에서 filter()의 결과를 반환하고 해당 객체 목록이 없을 땐 Http404를 raise 함

    ```python
    # articles/views.py
    from django.shortcuts import get_object_or_404, get_list_or_404

    articles = Article.objects.all()
    comments = Comment.objects.all()

    # 위 코드를 모두 다음과 같이 변경
    articles = get_list_or_404(Article)
    comments = get_list_or_404(Comment)
    ```

  - 사용하는 이유 ; 클라이언트 입장에서 서버 오류(500)라는 원인이 정확하지 않은 에러를 마주하기보다는, **서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것** 또한 중요한 요소이기 때문