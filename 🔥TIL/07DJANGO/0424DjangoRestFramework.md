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
  
  - 어떠한 언어나 환경에서도 **"나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"

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