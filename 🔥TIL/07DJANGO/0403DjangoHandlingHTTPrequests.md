- HTTP requests 처리에 따른 view 함수 구조 변화

- new & create view 함수 ; 둘 다 데이터 생성 로직 구현하기 위해 사용하지만 **new는 GET method** 요청만을, **create는 POST method** 요청만을 처리

# 😎 view 함수의 변화

- new와 view 함수 결합 > 새로운 create view 함수 작성 후 articles/urls.py에서 불필요해진 new url 제거 > 기존 new 관련 코드 수정

  ```python
  # articles/views.py

  def create(request):
      if request.method == 'POST':                            # request 객체의 method값을 사용한 분기
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)  # POST일 때는 과거 create 함수의 로직 처리
      else:
          form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/new.html', context)    # POST가 아닐 때는 과거 new 함수의 로직
  ```

> (GET) articles/create/ 게시글 생성 페이지를 줘! (POST) articles/create/ 게시글을 생성해줘!

- 새로운 update view 함수 작성 후 articles/urls,py에서 불필요해진 edit url 제거 > 기존 edit 관련 코드 수정

  ```python
  # articles/views.py
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, instance=article)
          if form.is_valid():
              form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm(instance=article)
      context = {
          'article': article,
          'form': form,
      }
      return render(request, 'articles/update.html', context)
  ```