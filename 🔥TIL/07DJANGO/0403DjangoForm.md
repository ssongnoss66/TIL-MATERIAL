- HTML form ; 사용자로부터 form 요소 통해 데이터 받고 있으나 비정상적/악의적 요청 확인 없이 모두 수용 중 > 우우리가 원하는 데이터 형식 맞는 지 **유효성 검증** 필요

  - 유효성 검사 ; 수집한 데이터가 정확하고 유효한지 확인하는 과정 > 입력 값, 형식, 중복, 범위, 보안 등 부가적인 것들 고려해야하고 이런 과정과 기능을 제공하는 **도구** 필요

# 🫠 Django Form

- 사용자 입력 데이터를 수집, 처리 및 유효성 검증 수행 위한 도구 > **유효성 검사 단순화 / 자동화할 수 있는 기능 제공**

- Form class 선언

  ```python
  # articles/forms.py
  from django import forms

  class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
  ```

- Form class 적용한 new 로직

  ```python
  # articles/views.py
  from .forms import ArticleForm

  def new(request):
    form = ArticleForm()
    context = {
      'form': form,
    }
    return render(request, 'articles/new.html', context)
  ```

  ```html
  <!--articles/new.html-->
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
  </form>
  ```

- Form class 적용 결과

  ![FormClass](https://user-images.githubusercontent.com/121418205/229419077-078b8b90-4664-4ca4-925d-a5daa3d3eaa8.png)

- Form rendering options

  ```html
  <!--articles/new.html-->
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  ```
  ![FormClassRenderingOption](https://user-images.githubusercontent.com/121418205/229419310-b2832374-1da6-49da-a5cf-5bf36229c94b.png)

# 😫 Widgets

- HTML 'input' element의 표현을 담당 > input 요소의 속성 및 출력되는 부분을 변경하는 것

- https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets

- Widget 적용

  ```python
  # articles/forms.py
  from django import forms

  class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
  ```

  ![Widgets](https://user-images.githubusercontent.com/121418205/229419688-d50956ab-3a98-45c8-a1f6-0b68c41b2612.png)

# 🤯 Django ModelForm

- Form ; 사용자 입력 데이터를 DB에 저장하지 않을 때 (ex. 로그인)

- ModelForm ; 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 회원가입)

- ModelForm class 선언

  ```python
  # articles/forms.py
  from django import forms
  from .models import Article

  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = '__all__'
  ```

- ModelForm class 출력 결과

  ![ModelForm](https://user-images.githubusercontent.com/121418205/229420294-3c90b029-103e-4db6-a998-41cae5bef873.png)

- Meta class ; ModelForm의 정보를 작성하는 곳

- fields 및 exclude 속성 ; exclude 속성 사용하여 모델에서 포함하지 않을 필드 지정 가능

  ```python
  # articles/forms.py
  from django import forms
  from .models import Article

  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = ('title',)
  ```

  ![fields](https://user-images.githubusercontent.com/121418205/229420810-1e6b52e5-992a-4954-863f-76c28a15cf2d.png)

  ```python
  # articles/forms.py
  from django import forms
  from .models import Article

  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          exclude = ('title',)
  ```

  ![exclude](https://user-images.githubusercontent.com/121418205/229420808-fc5d8c3b-cc99-4c3f-acf2-f59e209bd6bc.png)

- ModelForm을 적용한 create 로직

  ```python
  # articles/view.py
  from .forms import ArticleForm

  def create(request):
      form = ArticleForm(request.POST)
      if form.is_valid():
          article = form.save()
          return redirect('articles:detail', article.pk)
      context = {
          'form': form,
      }
      return render(request, 'articles/new.html', context)
  ```

- ModelForm 적용 결과 ; 제목 input에 공백 입력 후 에러 메시지 확인 (유효성 검사 결과)

  ![ModelForm적용결과](https://user-images.githubusercontent.com/121418205/229422101-b019ce90-1ae7-4d4a-a1e3-bc2431d89e74.png)

- is_valid() ; 여러 유효성 검사 실행하고 데이터 유효성 여부를 boolean으로 반환

- ModelForm을 적용한 edit 로직

  ```python
  def edit(request, pk):
      article = Article.objects.get(pk=pk)
      form = ArticleForm(instance=article)
      context = {
          'article': article,
          'form': form,
      }
      return render(request, 'articles/edit.html', context)
  ```

  ```html
  <!--articles/edit.html-->
  <h1>Articles EDIT</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  ```

- ModelForm을 적용한 update 로직

  ```python
  # articles/views.py
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      form = ArticleForm(request.POST, instance=article)
      if form.is_valid():
          form.save()
          return redirect('articles:detail', article.pk)
      context = {
          'form': form,
      }
      return render(request, 'articles/edit.html', context)
  ```

- save() ; 데이터베이스 객체 만들고 저장 > 키워드 인자 instance 여부 통해 생성/수정 결정

  ```python
  # articles/view.py
  # CREATE
  form = ArticleForm(request.POST)
  form.save

  # UPDATE
  form = ArticleForm(request.POST, instance=article)
  form.save()
  ```

# 🙂 참고

- ModelForm 키워드 인자 data와 instance 살펴보기 https://github.com/django/django/blob/main/django/forms/models.py#L333

  ```python
  class BaseModelForm(BaseForm, AltersData):
    def __init__(
        self,
        data=None,
        files=None,
        auto_id="id_%s",
        prefix=None,
        initial=None,
        error_class=ErrorList,
        label_suffix=None,
        empty_permitted=False,
        instance=None,
        use_required_attribute=None,
        renderer=None,
    ):
  ```

- Widget 응용

  ```python
  # articles/forms.py
  from django import forms
  from .models import Article

  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          label='제목',
          widget=forms.TextInput(
              attrs = {
                  'class': 'my-title',
                  'placeholder': 'Enter the title',
                  'maxlength': 10,
              }
          ),
      )
      content = forms.CharField(
          label='내용',
          widget=forms.Textarea(
              attrs = {
                  'class': 'my-content',
                  'placeholder': 'Enter the content',
                  'rows': 5,
                  'cols': 50,
              }
          ),
          error_messages = {'required': '내용을 입력해주세요.'},
      )

      class Meta:
          model = Article
          fields = '__all__'
  ```

- Meta class

  - 파이썬의 문법적 개념으로 접근하지 말 것

  - 단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록 ModelForm의 설계가 이렇게 되어있을 뿐 **ModelForm의 역할과 사용법 숙지**하는 데 집중할 것!