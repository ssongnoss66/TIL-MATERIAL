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