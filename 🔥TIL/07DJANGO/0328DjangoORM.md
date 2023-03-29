![ORM](https://user-images.githubusercontent.com/121418205/228127653-22cad3c7-95c1-444a-afd3-757aa084c690.png)

- ORM (Object-Relational-Mapping) ; 객체 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

# 🧐 QuerySet API

- QuerySet API ; ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화하는데 사용하는 도구 (API를 사용하여 SQL이 아닌 Python 코드로 데이터 처리)

- QuerySet API 구문

  - ```Article.objects.all() (ModelClass.Manager.QuerySetAPI의 구조)```

    ![QuerySetAPI구조](https://user-images.githubusercontent.com/121418205/228128340-869ba648-55c5-44f5-b1f0-41066efa5537.png)

- Query

  - 데이터베이스에 특정한 데이터를 보여달라는 요청

  - "쿼리문 작성" = 원하는 데이터 얻기 위해 데이터베이스에 요청 보낼 코드를 작성 ; 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달됨 > 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

- QuerySet

  - 데이터베이스에게서 전달받은 객체 목록 (데이터 모음) ; 순회 가능한 데이터 > 1개 이상의 데이터 불러와 사용 가능

  - Django ORM 통해 만들어진 자료형

  - 데이터베이스가 단일한 객체 반환할 때는 QuerySet 아닌 모델의 인스턴스로 반환

# 🥲 ORM CREATE

- QuerySet API 실습 사전 준비 ; 외부 라이브러리 설치 및 설정

  ```
  $ pip install ipython
  $ pip install django-extensions
  ```
  ```python
  # settings.py
  INSTALLED_APPS = [
    'articles',
    'django_extensions',
    ...,
  ]
  ```
  ```
  $ pip freeze > requirements.txt
  ```

- Django shell ; django 환경 안에서 실행되는 python shell (입력하는 QuerySet API 구문이 django 프로젝트에 영향 미침) > ```python manage.py shell_plus```

- 데이터 객체 만드는 세가지 방법

  > save() ; 객체를 데이터베이스에 저장하는 메서드

  1.

    ```
    # 특정 테이블에 새로운 행 추가하여 데이터 추가

    >>> article = Article()           # Article(class)로부터 article(instance)
    >>> article
    <Article: Article object (None)>

    >>> article.title = 'first'       # 인스턴스 변수(title)에 값을 할당
    >>> article.content = 'django!'   # 인스턴스 변수(content)에 값을 할당

    # save하지 않으면 아직 DB에 값 저장 X

    >>> article
    <Article: Article object (None)>

    >>> Article.objects.all()
    <QuerySet []>

    # save하고 확인하면 저장된 것 확인 가능

    >>> article.save()
    >>> article
    <Article: Article object (1)>
    >>> article.id
    1
    >>> article.pk
    1
    >>> Article.objects.all()
    <QuerySet [Article: Article object (1)]>
    ```

    > save 메서드 호출해야 비로소 DB에 데이터가 저장 (레코드 생성)

  2. 

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

  3.

    ```
    # 위 두가지 방법과는 다르게 바로 생성된 데이터가 반환됨

    >>> Article.objects.create(title='third', content='django!')
    <Article: Article object (3)>
    ```

    > QuerySet API 중 create() 메서드 활용

# 😶‍🌫️ ORM READ

- 전체 데이터 조회 ; all() 메서드

  ```
  >>> Article.objects.all()
  ```

- 단일 데이터 조회 ; get() 메서드

  ```
  >>> Article.objects.get(pk=1)
  <Article: Article object (1)>

  >>> Article.objects.get(pk=100)
  DoesNotExist: Article matching query does not exist.

  >>> Article.objects.get(content='django!')
  MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
  ```
  - 객체를 찾을 수 없으면 DoesNotExist 예외 발생

  - 둘 이상의 객체 찾으면 MultipleObjectsReturned 예외 발생

  - **따라서 primary key와 같이 고유성 보장하는 조회에서 사용

- 특정 조건 데이터 조회 ; filter() 메서드

  ```
  >>> Article.objects.filter(content='django!')
  <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

  >>> Article.objects.filter(title='a')
  <QuerySet []>

  >>> Article.objects.filter(title='first')
  <Que4rySet [<Article: Article object (1)>]>
  ```

# 🥰 참고

- QuerySet API 관련 문서 

  https://docs.djangoproject.com/en/3.2/ref/models/querysets/

  https://docs.djangoproject.com/en/3.2/topics/db/queries/

- Field lookups

  - 특정 레코드에 대한 조건 설정하는 방법
  
  - QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨 https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups

  ```
  # Field lookups dPtl

  # "content 컬럼에 'dj'가 포함된 모든 데이터 조회"
  Article.objects.filter(content__contains='dj')
  ```

- ORM, QuerySet API 사용하는 이유

  - 데이터베이스 쿼리 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함

  - 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움

# 😕 ORM UPDATE

- 데이터 수정

  ```
  # 수정할 인스턴스 조회
  >>> article = Article.objects.get(pk=1)

  # 인스턴스 변수 변경
  >>> article.title = 'byebye'

  # 저장
  >>> article.save()

  # 정상적으로 변경된 것을 확인
  >>> article.title
  'byebye'
  ```

# 😏 ORM DELETE

- 데이터 삭제

  ```
  # 삭제할 인스턴스 조회
  >>> article = Article.objects.get(pk=1)

  # delete 메서드 호출 (삭제된 객체가 반환됨)
  >>> article.delete()
  (1, {'articles.Article' : 1})

  # 삭제한 데이터는 더이상 조회할 수 없음
  >>> Article.objects.get(pk=1)
  DoesNotExist: Article matching query does not exist.
  ```

