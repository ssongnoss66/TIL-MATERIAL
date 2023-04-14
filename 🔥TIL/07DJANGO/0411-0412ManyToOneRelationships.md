- 관계형 데이터베이스의 N:1 관계

  ![관계형데이터베이스ManyToOne](https://user-images.githubusercontent.com/121418205/231651796-2d7e60f7-92c4-4452-8787-a07510b76515.png)

  - Foreign Key (위 표에서는 고객 ID) ; 테이블 필드 중 다른 테이블의 레코드를 식별할 수 있는 키 > 각 레코드에서 서로 다른 테이블 간의 '관계'를 만드는 데 사용

# 🧐 Comment & Article 

## @ 모델 관계 설정

- Many to one relationships (N:1 or 1:N) ; 한 테이블의 0개 이상의 레코드가 다른 테입르의 레코드 한 개와 관련된 관계

- Comment(N) - Article(1) ; '0개 이상의 댓글은 1개의 게시글에 작성될 수 있다'

- 두 모델의 관계

  ![두 모델의 관계](https://user-images.githubusercontent.com/121418205/231652573-45a70163-c125-4519-9a23-5fb97dd43ae9.png)

- ForeignKey() ; django에서 N:1 관계 설정 모델 필드

- Comment 모델 정의

  ```python
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

  - ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

  - ForeignKey 클래스를 작성하는 위치와 관계없이 필드 마지막에 생성됨

  > ForeignKey(to, on_delete)

  - to ; 참조하는 모델 class 이름
  
  - on_delete
  
    - 참조하는 모델 class가 삭제될 때 연결된 하위 객체의 동작 결정

    - 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정 (데이터 무결성)

    - "CASCADE" ; 부모 객체(참조된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제 https://docs.djangoproject.com/en/3.2/ref/models/fields/#arguments

- Migration 진행 후 Comment 테이블 확인

  <img width="1351" alt="Comment테이블" src="https://user-images.githubusercontent.com/121418205/231654245-f8987117-d638-45ee-8f48-24142801cc7f.png">

  - article_id 필드 확인 ; 참조하는 클래스 이름의 소문자(단수형) 작성 권장 이유

- 댓글 생성 연습

  ```shell
  > terminal
  # 1. shell_plus 실행 및 게시글 작성
  python manage.py shell_plus

  # 게시글 생성
  Article.objects.create(title='title', content='content')


  # 2. 댓글 생성
  # Comment 클래스의 인스턴스 comment 생성
  comment = Comment()

  # 인스턴스 변수 저장
  comment.conetnt = 'first comment'

  # DB에 댓글 저장
  comment.save()

  # 에러 발생 ; articles_comment 테이블의 ForeignKeyFireld, article_id 값이 저장 시 누락되었기 때문
  django.db.utils.IntegrityError: NOT NULL constraint failed: articles_comment.article_id

  # 게시글 조회
  article = Article.objects.get(pk=1)

  # 외래 키 데이터 입력
  comment.article = article
  # 또는 comment.article_id = article.pk처럼 pk 값을 직접 외래 키 컬럼에 넣어줄 수도 있지만 권장 X

  # DB에 댓글 저장 및 확인
  comment.save()

  # 3. comment 인스턴스를 통한 article 값 접근하기

  comment.pk
  => 1

  comment.content
  => 'first comment'

  # 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
  comment.article
  => <Article: Article object (1)>

  # article_pk는 존재하지 않는 필드이기 때문에 사용 불가
  comment.article_id
  => 1

  # 4. 댓글 생성
  # 1번 댓글이 작성된 게시물의 pk 조회
  comment.article.pk
  => 1

  # 1번 댓글이 작성된 게시물의 content 조회
  comment.article.content
  => 'content'

  # 두번째 댓글 작성해보기
  comment = Comment(content = 'second comment', article=article)
  comment.save()

  comment.pk
  => 2

  comment
  => <Comment: Comment object (2)>

  comment.article.pk
  => 1
  ```

  - 작성된 댓글 확인

  <img width="1222" alt="작성된댓글" src="https://user-images.githubusercontent.com/121418205/231657097-7cf11305-bcc1-4b1d-8f8f-7dfa8065f201.png">

## @ 관계 모델 참조

- 역참조 ; 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것 > N:1 관계에서는 1이 N을 참조하는 것 > **BUT Article에는 Comment를 참조할 어떠한 필드도 없다**

- ```article.comment_set.all()```

  ![article comment_set all()](https://user-images.githubusercontent.com/121418205/231657457-f24c29fa-b86e-41e6-9120-0f717c1c3cc1.png)

  - related manager ; N:1 혹은 M:N 관계에서 역참조 시에 사용하는 manager > objects라는 매니저 통해 queryset api 사용했던 것처럼 related manager 통해 queryset api 사용할 수 있게 됨

    - related manager가 필요한 이유

      - article.comment 형식으로는 댓글 객체 참조 불가 > 실제 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않기 때문

      - Django가 역참조할 수 있는 'comment_set' manager 자동으로 생성해 article.comment_set 형태로 댓글 객체 참조 가능

      - N:1 관계에서 생성되는 Related manager의 이름은 참조하는 **"모델면_set"** 이름 규칙으로 만들어짐

    - Related manager 연습하기

      ```shell
      # terminal
      # 1. shell_plus 실행 및 1번 게시글 조회
      python manage.py shell_plus

      article = Article.objects.get(pk=1)


      # 2. 1번 게시글에 작성된 모든 댓글 조회하기 (역참조)
      article.comment_set.all()
      <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>


      # 3. 1번 게시글에 작성된 모든 댓글 출력하기
      comments = article.comment_set.all()

      for comment in comments:
          print(comment.content)
      ```

## @ 댓글 기능 구현

- Comment CREATE

  - 사용자로부터 댓글 데이터 입력받기 위한 CommentForm 작성 > detail 페이지에서 CommentForm 출력

    ```python
    # articles/forms.py
    from .models import Article, Comment

    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = '__all__'

    # articles/views.py
    from .forms import ArticleForm, CommentForm

    def detail(request, pk):
        ...
        comment_form = CommentForm()
        context = {
            ...,
            'comment_form': comment_form,
        }
    ```

  - detail 페이지에서 CommentForm 출력

    ```html
    <!--articles/detail.html-->
      <form action="#" method = "POST">
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit" class="btn btn-dark">
      </form>
    ```

    ![CommentForm](https://user-images.githubusercontent.com/121418205/231663283-6c19693e-f69d-49b7-8645-be7f001818ff.png)

    - Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문에 출력되고 있음 > but 외래 키 필드는 **사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장**되어야 함

    ```python
    # articles/forms.py
    from .models import Article, Comment

    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('content', )
    ```

    - 출력에서 제외된 외래 키 데이터는 detail 페이지의 url에서 사용되는 해당 게시글의 pk값 활용

    ```python
    # articles/urls.py
    urlpatterns = [
        ...,
        path('<int:pk>/comments/', views.comments_create, name='comments_create')
    ]

    # articles/views.py
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save(commit=False)
            comment.article = article
            comment_form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'article': article,
            'comment_form': comment_form,
        }
        return render(request, 'articles/detail.html', context)
    ```

    - ```save(commit=False)``` ; "create but don't save the new instance" > DB에 저장하지 않고 인스턴스만 반환 https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method

    ```html
    <!--articles/detail.html-->
    <form action="{% url 'articles:comments_create' article.pk %}" method = "POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit" class="btn btn-dark">
    </form>
    ```

- Comment READ

  - 전체 댓글 출력

    ```python
    # articles/views.py
    from .models import Article, Comment

    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comments = article.comment_set.all()
        comment_form = CommentForm()
        context = {
            'article': article,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'articles/detail.html', context)
    ```

    ```html
    <!--articles/detail.html-->
    <p>댓글 목록</p>
    <ul>
      {% for comment in comments %}
        <li>댓글 {{ comment.pk }}: {{comment.content }}</li>
      {% endfor %}
    </ul>
    ```

- Comment DELETE

  - 댓글 삭제 url / view 함수 작성

    ```python
    # articles/urls.py
    urlpatterns = [
        ...,
        path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete')
    ]

    # articles/views.py
    from .models import Article, Comment

    def comments_delete(request, article_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles: detail', article_pk)
    ```

  - 댓글 삭제 버튼 작성

    ```html
    <!--articles/detail.html-->
      <ul>
        {% for comment in comments %}
          <li>댓글 {{ comment.pk }}: {{comment.content }}</li>
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE" class="btn btn-dark"> 
          </form>
        {% endfor %}
      </ul>
    ```

# 😶‍🌫️ 참고

- 댓글 갯수 출력하기

  - DTL filter-length 사용

    ```html
    {{ comments|length }}
    {{ article.comment_set.all|length }}
    ```

  - Queryset API-count() 사용

    ```html
    {{ article.comment_set.count }}
    ```

- 댓글이 없는 경우 대체 컨텐츠 출력 ; DTL tag-for empty 사용

  ```html
  <!--articles/detail.html-->
  <ul>
    {% for comment in comments %}
      <li>댓글 {{ comment.pk }}: {{comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE" class="btn btn-dark"> 
        </form>
      </li>
    {% empty %}
      <p>댓글이 없습니다.</p>
    {% endfor %}
  </ul>
  ```

- 댓글 수정을 구현하지 않는 이유

  - 일반적으로 댓글 수정은 수정 페이지 이동 없이 현재 페이지에서 댓글 작성 Form 부분만 변경되어 수정

  - 페이지 일부 내용만 업데이트 하는 것은 JS 영역

# 🥲 Article & User

- Article(N) - User(1) ; 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음

## @ 모델 관계 설정

- User 외래 키 정의

  ```python
  # articles/modesl.py
  from django.conf import settings

  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      ...
  ```

- User 모델을 참조하는 2가지 방법

  - get_user_model() ; 반환 값 'User Object' (객체) > **models.py가 아닌 다른 모든 곳에서 참조할 때**

  - settings.AUTH_USER_MODEL ; 반환 값 'accounts.User' (문자열) > **models.py의 모델 필드에서 참조할 때**

- Migrations 진행

  ```
  # terminal
  python manage.py makemigrations

  You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
  Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit, and let me add a default in models.py
  Select an option:
  ```

  - 기본적으로 모든 컬럼은 NOT NULL 제약조건 있기 때문에 데이터 없이는 새로 추가되는 외래 키 필드 user_id 생성 X

  - 기본값 어떻게 작성할 것인지 선택 > 1 입력 후 Enter 진행

  ```
  # terminal
  Select an option: 1
  Please enter the default value now, as valid Python
  The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
  Type 'exit' to exit this prompt
  >>> 1

  python manage.py migrate
  ```

  - article의 user_id에 어떤 데이터 넣을 것인지 직접 입력해야 함 > 1 입력 후 Enter 진행

  - 기존에 작성된 게시글 있다면 1번 회원이 작성한 것으로 처리됨

  - migrations 파일 생성 후 migrate 진행

## @ CRUD 구현

- Article CREATE

  1. ArticleForm 출력 확인

    ![ArticleForm 출력 확인](https://user-images.githubusercontent.com/121418205/231941593-82d9e294-d393-4da9-8811-6c500706aa7f.png)

  2. ArticleForm 출력 필드 수정

    ```python
    # articles/forms.py
    class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = ('title', 'content',)
    ```

  3. 게시글 작성 시 user_id 필드 데이터 누락되어 에러 발생 
  
    ```
    IntegrityError at /articles/create/
    NOT NULL constraint failed: articles_article.user_id)
    ```

  4. 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용

    ```python
    # articles/views.py
    @login_required
    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:detail', article.pk)
        else:
            ...
    ```

  5. 게시글 작성 후 테이블 확인

    <img width="1688" alt="게시글 작성 후 테이블 확인" src="https://user-images.githubusercontent.com/121418205/231942414-948adff4-b78d-4eab-b819-fe9f72b3a02b.png">

- Article READ

  1. index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력 및 확인

    ```html
    <!--articles/index.html-->
    {% for article in articles %}
      <p>{{ article }}</p>
      <p>작성자 : {{ article.user }} </p>
      <p>글 번호: {{ article.pk }}</p>
      <p>글 제목:<a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></p>
    {% endfor %}

    <!--articles/detail.html-->
    <h3>{{ article.pk }}번째 글</h3>
    <hr>
    <p>작성자: {{ article.user }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>댓글 목록</p>
    ```

- Article UPDATE

  1. 수정 요청하려는 사람과 게시글 작성한 사람 비교하여 본인 게시글만 수정할 수 있도록 함

    ```python
    # articles/views.py
    @login_required
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.user == article.user:    # 수정요청한 사람 == 게시글 작성자라면
            if request.method == 'POST':
                form = ArticleForm(request.POST, request.FILES, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('articles:detail', article.pk)
            else:
                form = ArticleForm(instance=article)
        else:                               # 같은 사람 아니면 초기화면으로 돌아가기
            return redirect('articles:index')
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    ```

  2. 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼 출력하지 않도록 함

    ```html
    <!--articles/detail.html-->
    {% if request.user == article.user %}
      <a href="{% url 'articles:update' article.pk %}" class="btn btn-secondary">EDIT</a>
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE" class="btn btn-secondary">
      </form>
    {% endif %}
    ```

- Article DELETE ; 삭제 요청하려는 사람과 게시글 작성한 사람 비교하여 본인 게시글만 삭제할 수 있도록 함

    ```python
    # articles/views.py
    @login_required
    def delete(request, pk):
        article = Article.objects.get(pk=pk)
        if request.user == article.user:      # 삭제요청한 사람 == 게시글 작성자라면
            article.delete()
        return redirect('articles:index')
    ```

# 😕 Comment & User

- Comment(N) - User(1) ; 0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음

## @ 모델 관계 설정

- User 외래 키 정의

  ```python
  # articles/models.py
  class Comment(models.Model):
      ...
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      ...
  ```

- Migration 진행 ; 기존에 존재하던 테이블에 새로운 컬럼 추가 > migrations 파일 바로 생성 X

## @ CRD 구현

- Comment CREATE

  1. 댓글 작성 시 user_id 필드 데이터 누락되어 에러 발생

    ```
    IntegrityError at /articles/1/comments/
    NOT NULL constraint failed: articles_comment.user_id
    ```

  2. 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용

    ```python
    # articles/views.py
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment_form.save()
            return redirect('articles:detail', article.pk)
        ...
    ```

- Comment READ ; detail 템플릿에서 각 댓글의 작성자 출력 및 확인

    ```html
    <!--articles/detail.html-->
    ```

- Comment DELETE

  1. 삭제 요청하려는 사람과 댓글 작성한 사람 비교하여 본인 댓글만 삭제할 수 있도록 함

    ```python
    # articles/views.py
    def comments_delete(request, article_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    ```

  2. 해당 댓글 작성자 아니라면, 댓글 삭제 버튼 출력하지 않도록 함

    ```html
    <!--articles/detail.html-->
    {% if request.user == comment.user %}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE" class="btn btn-dark"> 
      </form>
    {% endif %}
    ```

# 😏 참고

- 인증된 사용자인 경우만 댓글 작성/삭제

  ```python
  # articles/views.py
  @login_required
  def comments_create(request, pk):
      ...

  @login_required
  def comments_delete(request, article_pk, comment_pk):
      ...
  ```