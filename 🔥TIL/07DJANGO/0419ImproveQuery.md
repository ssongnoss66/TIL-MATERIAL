- Improve query ; 같은 결과에 대한 쿼리 개수를 줄여 조회하기

- 사전준비 ; migrate 및 fixtures 데이터 load

  ```
  # terminal
  $ python manage.py migrate
  $ python manage.py loaddata users.json articles.json comments.json

  Installed 115 object(s) from 3 fixture(s)
  ```

- annotate ; SQL의 GROUP BY 절 활용

  ![annotate_1](https://user-images.githubusercontent.com/121418205/233296422-48715fae-8461-4ac1-ab4a-6c4040070f2f.png)
  
  ![annotate_문제](https://user-images.githubusercontent.com/121418205/233298413-630558f3-33a7-438b-a1d1-f948c6130331.png)

  1. "11 queries including 10 similar" > 원인 ; 각 게시글 별 댓글 개수를 반복 평가

    ```python
    # articles/views.py
    def index_1(request):
        articles = Article.objects.order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_1.html', context)
    ```

    ```html
    <!--articles/index_1.html-->
    <p>댓글 갯수 : {{ article.comment_set.count }}</p>
    ```
  
  2. "11 queries including 10 similar" -> "1 query" > 해결 ; annotate 사용해 첫 조회 시 댓글 갯수까지 한번에 조회

    ```python
    # articles/views.py
    def index_1(request):
        articles = Article.objects.annotate(Count('comment')).order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_1.html', context)
    ```

    ```html
    <!--articles/index_1.html-->
    <p>댓글 갯수 : {{ article.comment__count }}</p>
    ```

    ![annotate_해결](https://user-images.githubusercontent.com/121418205/233299796-3f768f89-4244-49c4-bd65-ad02b688944a.png)

- select_related ; 1:1 또는 N:1 참조 관계에서 사용 > SQL의 INNER JOIN 절 활용

  ![select_related](https://user-images.githubusercontent.com/121418205/233300333-3dc8d823-6ec6-41b2-92cb-8266828c2854.png)

  ![selsect_related_문제](https://user-images.githubusercontent.com/121418205/233300345-4b08939a-9d5b-432d-b4bb-9f0f43c37a02.png)

  1. "11 queries including 10 similar and 8 duplicates" > 원인 ; 각 게시글 출력 후 게시글을 작성한 유저의 이름까지 반복 평가

    ```python
    # articles/views.py
    def index_2(request):
        articles = Article.objects.order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_2.html', context)
    ```

    ```html
    <!--articles/index_2.html-->
    {% for article in articles %}
      <h3>작성자 : {{ article.user.username }}</h3>
      <p>제목 : {{ article.title }}</p>
      <hr>
    {% endfor %}
    ```

  2. "11 queries including 10 similar and 8 duplicates" -> "1 query" > 해결 ; select_related 사용해 article 조회하면서 user까지 한번에 조회

    ```python
    # articles/views.py
    def index_2(request):
        articles = Article.objects.select_related('user').order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_2.html', context)
    ```

    ![selected_related_해결](https://user-images.githubusercontent.com/121418205/233301584-42780d51-b917-4b98-926d-ae2a2a8ed19a.png)

- prefetch_related ; M:N 또는 N:1 역참조 관계에서 사용 > SQL이 아닌 Python 사용한 JOIN 진행됨
  
  ![prefetch_related](https://user-images.githubusercontent.com/121418205/233302198-e514c427-0b6e-454d-928d-b0c2ef0cd56f.png)

  ![prefetch_related_문제](https://user-images.githubusercontent.com/121418205/233302190-1c9799a9-30ab-4f60-98dd-c4853c25d9fa.png)

  1. "11 queries including 10 similar" > 원인 ; 각 게시글 출력 후 각 게시글의 댓글 목록을 개별적으로 모두 조회

    ```python
    # articles/views.py
    def index_3(request):
        articles = Article.objects.order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_3.html', context)
    ```

    ```html
    <!--artiels/index_3.html-->
    {% for article in articles %}
        <p>제목 : {{ article.title }}</p>
        <p>댓글 목록</p>
        {% for comment in article.comment_set.all %}
          <p>{{ comment.content }}</p>
        {% endfor %}
        <hr>
      {% endfor %}
    ```

  2. "11 queries including 10 similar" -> "2 queries" > 해결 ; prefetch_related 사용해 article 조회하면서 comment까지 한번에 조회

    ```python
    # articles/views.py
    def index_3(request):
        articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_3.html', context)
    ```

    ![prefetch_related_해결](https://user-images.githubusercontent.com/121418205/233303370-39d0c8ff-95bb-497d-a1ae-e778f8d78c67.png)

- select_related & prefetch_related

  ![select_related   prefetch_related](https://user-images.githubusercontent.com/121418205/233304953-8de5d657-d7ff-485b-a929-5d94f3fa0d6a.png)

  ![select_related   prefetch_related_문제](https://user-images.githubusercontent.com/121418205/233304947-86233c8f-09c9-41ea-b4b8-0b771913db4a.png)

  1. "111 queries including 110 similar and 100 duplicates" > 원인 ; 게시글 출력 + 각 게시글의 댓글 목록 + 댓글의 작성자를 단계적으로 평가

    ```python
    # articles/views.py
    def index_4(request):
        articles = Article.objects.order_by('-pk')
        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_4.html', context)
    ```

    ```html
    <!--articles/index_4.html-->
    {% for article in articles %}
      <p>제목 : {{ article.title }}</p>
      <p>댓글 목록</p>
      {% for comment in article.comment_set.all %}
        <p>{{ comment.user.username }} : {{ comment.content }}</p>
      {% endfor %}
      <hr>
    {% endfor %}
    ```

  2. "111 queries including 110 similar and 100 duplicates" -> "2 queries" > 해결 ; 게시글 출력 + 각 게시글의 댓글 목록 + 댓글 작성자를 한 번에 조회

    ```python
    # articles/views.py
    def index_4(request):
        articles = Article.objects.prefetch_related(
            Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
        ).order_by('-pk')

        context = {
            'articles': articles,
        }
        return render(request, 'articles/index_4.html', context)
    ```

    ![select_related   prefetch_related_해결](https://user-images.githubusercontent.com/121418205/233304938-864205f5-ccfc-4234-8937-6cd5dfa19ee8.png)

> 섣부른 최적화 금지