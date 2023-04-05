- Django Authentication System (인증 시스템) ; 사용자 인증과 관련된 기능을 모아놓은 시스템 / 인증과 권한 부여를 함께 제공 및 처리

  ```python
  # settings.py

  INSTALLED_APPS = [
    ...,
    'django.contrib.auth',
    ...,
  ]
  ```

- Authentication (인증) ; 사용자가 자신이 누구인지 확인하는 것 / 신원 확인

- Authorization (권한, 허가) ; 인증된 사용자가 수행할 수 있는 작업 결정, 권한 부여

- 사전 설정 ; auth와 관련된 경로나 키워드들을 django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것 권장

  ```python
  # accounts/urls.py
  from django.urls import path
  from . import views

  app_name = 'accounts'
  urlpatterns = [

  ]

  # pjt/urls.py
  urlpatterns = [
    ...,
    path('accounts/', include('accounts.urls')),
  ]
  ```

# 🥲 Custom User model

- Custom User model로 대체하기

  - django가 기본적으로 제공하는 User model은 내장된 auth 모듈의 User 클래스 사용 https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405
  
  - **별도의 설정 없이 사용 가능 but 직접 수정할 수 없는 문제**

  - AbstractUser 상속받는 커스텀 User 클래스 작성 > 기존 User 클래스도 AbstractUser 상속받기 때문에 **커스텀 User 클래스도 완전히 같은 모습** 가지게 됨

    ```python
    # accounts/models.py
    from django.contrib.auth.models import AbstractUser

    class User(AbstractUser):
      pass
    ```
  
  - django 프로젝트가 사용하는 기본 User 모델을 우리가 작성한 User 모델로 지정 (수정 전 기본값은 'auth.User')

    ```python
    # settings.py
    AUTH_USER_MODEL = 'accounts.User'
    ```

  - 기본 User 모델 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

    ```python
    # accounts/admin.py
    # Register your models here.
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    admin.site.register(User, UserAdmin)
    ```
  
  > [주의] 프로젝트 중간에 AUTH_USER_MODEL 변경 불가능!! > 필요시 데이터베이스 초기화 후 진행

- 기본 User 테이블의 변화

  ![기본유저테이블변화](https://user-images.githubusercontent.com/121418205/229664891-da2f2517-bb9f-40a5-b27a-0a5e777a0661.png)

- 반드시 User 모델을 대체해야 할까?

  - Django는 새 프로젝트 시작 시 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장

  - 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문

  - 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate 실행 전에 이 작업 마쳐야 함

# 😕 Login

- Session을 Create하는 과정

- AuthneticationForm() ; 로그인을 위한 built-in form https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L174

- 로그인 페이지 작성

  ```python
  # accounts/urls.py
  app_name = 'accounts'
  urlpatterns = [
    path('login/', views.login, name='login'),
  ]

  # accounts/views.py
  from django.shortcuts import render, redirect
  from django.contrib.auth import login as auth_login
  from django.contrib.auth.forms import AuthenticationForm

  def login(request):
    if request.method == 'POST':
      form = AuthenticationsForm(request, request.POST)
      if form.is_valid():
        auth_login(request, form.get_user())
        return redirect('articles:index')
    else:
      form = AuthenticationForm()
    context = {
      'form': form,
    }
    return render(request, 'accounts/login.html', context)
  ```

    - login(request, user) ; 인증된 사용자를 로그인하는 함수

    - get_user() ; AuthenticationForm의 인스턴스 메서드 > 유효성 검사 통과했을 경우 로그인한 사용자 객체 반환 https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L244

  ```html
  <!--accounts/login.html-->
  <h1>accounts LOGIN</h1>
  <hr>
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <div class="input-group flex-nowrap mb-3">
      <input type="submit" class="form-control border-dark" placeholder="SUBMIT" aria-label="SUBMIT" aria-describedby="addon-wrapping">
    </div>
  </form>
  ```

- 세션 데이터 확인하기

  - 로그인 후 개발자 도구와 DB에서 django로부터 발급받은 세션 확인 (로그인은 관리자 계정 만든 후 진행)

  1. django_session 테이블에서 확인

    <img width="996" alt="세션데이터확인1" src="https://user-images.githubusercontent.com/121418205/229674274-dcd0a74c-4774-4d72-9efc-4b69043d84dc.png">
  
  2. 브라우저에서 확인 > 개발자도구 - Application - Cookies

    ![세션데이터확인2](https://user-images.githubusercontent.com/121418205/229674260-52a2d7db-af9c-4a6c-a09e-4f4fde181868.png)

# 😏 Logout

- Session을 Delete하는 과정

- logout(request)

  1. 현재 요청에 대한 session data를 DB에서 삭제

  2. 클라이언트의 쿠키에서도 sessionid를 삭제

- 로그아웃 로직 작성

  ```python
  # accounts/urls.py
  urlpatterns = [
    ...,
    path('logout/', views.logout, name='logout'),
  ]

  # accounts/views.py
  from django.contrib.auth import logout as auth_logout

  def logout(request):
    auth_logout(request)
    return redirect('mainpg:index')
  ```

  ```html
  <!--articles/index.html-->
  <h1>articles INDEX</h1>
  <hr>
  <a href="{% url 'accounts:login' %}" class="btn btn-dark mb-3">login</a>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="logout" class="btn btn-dark mb-3">
  </form>
  ```

- 로그아웃 진행 및 세션 데이터 삭제 확인

  ![로그아웃세션확인](https://user-images.githubusercontent.com/121418205/229687753-a4475736-f67a-40e2-805c-9e04f8e23868.png)

# 🥸 Template with Authentication data

- 템플릿에서 인증 관련 데이터 출력하는 방법

- 현재 로그인 되어있는 유저 정보 출력하기

  ```html
  <!--articles/index,html-->
  <h3>Hello, {{ user }}</h3>
  ```

- context processors

  - 템플릿이 렌더링 될 때 호출가능한 컨텍스트 데이터 목록

  - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용가능한 변수로 포함됨

  - 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해둔 것

    ```python
    # settings.py
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates',],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

# 🙃 참고

- User 모델 상속 관계

  ![User모델상속관계](https://user-images.githubusercontent.com/121418205/229688330-c7e5fae6-520a-47d1-8f1e-91352bc0d20b.png)

- 'AbstractUser' class

  - "관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스'

  - Abstract base classes (추상 기본 클래스)

    - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

    - 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨

    - https://docs.python.org/3/library/abc.html

- 유저 모델 대체하기 Tip

  - 대체하는 과정을 외우기 어려울 경우 해당 공식문서를 보며 순서대로 진행하는 것 권장

  - https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model

# 😀 회원 가입

- User 객체를 Create 하는 것

- UserCreationForm() ; 회원가입 위한 built-in ModelForm https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L75

- 회원 가입 페이지 작성

  ```python
  # accounts/urls.py
  urlpatterns = [
    ...,
    path('signup/', views.signup, name='signup'),
  ]

  # accounts/views.py
  def signup(request):
      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('mainpg:index')
      else:
          form = UserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  ```

  ```html
  <!--accounts/signup.html-->
  <h1>accounts SIGNUP</h1>
  <hr>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <div class="input-group flex-nowrap mb-3">
      <input type="submit" class="form-control border-dark" placeholder="SUBMIT" aria-label="SUBMIT" aria-describedby="addon-wrapping">
    </div>
  </form>
  ```

- 회원 가입 페이지 작성

  ![signupPage](https://user-images.githubusercontent.com/121418205/229959719-dd0835eb-e073-48c2-aec5-867fb4b21c75.png)

- 회원 가입 진행 후 에러 페이지 확인

  ![signupError](https://user-images.githubusercontent.com/121418205/229960287-aaf3b6f7-3a96-4b83-8666-dd9f8528ad73.png)

  - 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문

  - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L106

> 커스텀 유저 모델 사용하려면 **1. UserCreationForm 2. UserChangeForm** 다시 작성해야 한다! > 두 form 모두 class Meta:model=User가 등록된 form이기 때문

- 커스텀 유저 모델 사용 과정

  1. 커스텀 form 작성

    ```python
    # account/forms.py
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm

    class CustomerUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = get_user_model()

    class CustomerUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
    ```

    - get_user_model() ; "현재 프로젝트에서 활성화된 사용자 모델(active user model)"을 반환하는 함수

    - from .models import user 구조로 **직접 참조하지 않는** 이유

      - User 모델을 get_user_model() 사용해 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문

      - Django는 User 클래스 직접 참조하는 대신 get_user_model() 사용해 참조해야한다고 강조

  2. 회원 가입 로직 수정

    ```python
    # accounts/views.py
    from .forms import CustomUserCreationForm

    def signup(request):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mainpg:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    ```

# 🤓 회원 탈퇴

- User 객체를 Delete하는 것

- 회원 탈퇴 로직 작성

  ```python
  # accounts/urls.py
  urlpatterns = [
    ...,
    path('delete/', views.delete, name='delete')
  ]

  # accounts/views.py
  def delete(request):
    request.user.delete()
    return redirect('mainpg:index')
  ```

  ```html
  <!--mainpg/index.html-->
  ...
  <form action="{% url 'accounts:delete' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="delete" class="btn btn-dark mb-3 form-control">
  </form>
  ```

# 🫢 회원정보 수정

- User 객체를 Update 하는 것

- UserChangeForm() ; 회원가입을 위한 built-in ModelForm https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L135

- 회원정보 수정 페이지 작성

  ```python
  # accounts/urls.py
  urlpatterns = [
      ...,
      path('update/', views.update, name='update'),
  ]
  # accounts/views.py
  def update(request):
      if request.method == "POST":
          form = CustomUserChangeForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('mainpg:index')
      else:
          form = CustomUserChangeForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/update.html', context)
  ```

  ```html
  <!--accounts/update.html-->
  <h1>accounts UPDATE</h1>
  <hr>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <div class="input-group flex-nowrap mb-3">
      <input type="submit" class="form-control border-dark" placeholder="SUBMIT" aria-label="SUBMIT" aria-describedby="addon-wrapping">
    </div>
  </form>

  <!--mainpg/index.html-->
  <a href="{% url 'accounts:update' %}" class="btn btn-dark mb-3">update</a>
  ```

- UserChangeForm 사용 시 **일반 사용자가 접근해서는 안 될 정보들까지 모두 수정 가능해짐** ; admin 인터페이스에 사용되는 ModelForm이기 때문 > CustomUserChangeForm에서 **접근 가능한 필드 조정**해야 함

- CustomUserChangeForm fields 재정의

  ```python
  # accounts/forms.py
  class CustomUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm.Meta):
          model = get_user_model()
          fields = ('email', 'first_name', 'last_name')
  ```

  - User Model의 필드는 AbstractUser 클래스 참고 https://github.com/django/django/blob/main/django/contrib/auth/models.py#L334

- 회원정보 수정 로직 작성

  ```python
  # accounts/views.py
  def update(request):
      if request.method == "POST":
          form = CustomUserChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('mainpg:index')
      else:
          form = CustomUserChangeForm(instance=request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/update.html', context)
  ```

# 😛 비밀번호 변경

- django는 회원정보 수정 form에서 별도 주소로 안내 (/accounts/password/)

- PasswordChangeForm() ; 비밀번호 변경을 위한 built-in Form https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L360

- 비밀번호 변경 페이지 작성

  ```python
  # accounts/urls.py
  urlpatterns = [
      ...,
      path('password/', views.change_password, name='change_password'),
  ]

  # accounts/views.py
  from django.contrib.auth.forms import PasswordChangeForm

  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              return redirect('mainpg:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/change_password', context)
  ```

  ```html
  <!--accounts/change_password.html-->
  <h1>accounts CHANGE PASSWORD</h1>
  <hr>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <div class="input-group flex-nowrap mb-3">
      <input type="submit" class="form-control border-dark" placeholder="SUBMIT" aria-label="SUBMIT" aria-describedby="addon-wrapping">
    </div>
  </form>
  ```

- PasswordChangeForm의 인자 순서 https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py

  ![PasswordChangeForm](https://user-images.githubusercontent.com/121418205/229998856-3d941778-f65c-484a-950d-3c300c4c77ff.png)

- 암호 변경 시 세션 무효화

  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 로그인 상태 유지 X

  - 비밀번호는 변경되었으나 비밀번호 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

- update_session_auth_hash(request, user) ; 암호 변경 시 세션 무효화 방지

  - 암호 변경되어도 로그아웃되지 않도록 새로운 password의 session data로 기존 session 업데이트 https://docs.djangoproject.com/en/3.2/topics/auth/default/

  - 적용

    ```python
    # accounts/views.py
    from django.contrib.auth import update_session_auth_hash

    def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('mainpg:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```

# 😗 로그인 사용자에 대한 접근 제한

1. is authenticated 속성

  - 사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성

  - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성 ; AnonymousUser에 대해서는 항상 False

  - **권한과 관련 X** ; 사용자가 활성 상태이거나 유효한 세션을 가지고 있는지도 확인 X

  - 적용

    - 로그인과 비로그인 상태에서 출력되는 링크 다르게 설정하기

      ```html
      <!--mainpg/index.html-->
      {% if request.user.is_authenticated %}
          <h2>Hello, {{ user }}</h2>
        {% else %}
          <div class="row">
            <a href="{% url 'accounts:login' %}" class="btn btn-dark mb-3">login</a>
            <a href="{% url 'accounts:signup' %}" class="btn btn-dark mb-3">signup</a>
          </div>
        {% endif %}
      ```

    - 인증된 사용자라면 로그인/회원가입 로직 수행할 수 없도록 처리하기

```python
# accounts/views.py
def login(request):
    if request.user.is_authenticated:
        return redirect('mainpg:index')
    ...

def signup(request):
    if request.user.is_authenticated:
        return redirect('mainpg:index')
    ...
```

2. login_required 데코레이터

  - 인증된 사용자에 대해서만 view 함수 실행시키는 데코레이터

  - 로그인하지 않은 사용자의 경우 /accounts/login/ 주소로 redirect 시킴

  - 적용

```python
# articles/views.py ; 인증된 사용자만 게시글 작성/수정/삭제할 수 있도록 수정
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    ...

@login_required
def delete(request, pk):
    ...

@login_required
def update(request, pk):
    ...

# accounts/views.py ; 인증된 사용자만 게시글을 로그아웃/탈퇴/수정/비밀번호 변경할 수 있도록 수정
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    ...

@login_required
def logout(request):
    ...

@login_required
def delete(request):
    ...

@login_required
def update(request):
    ...

@login_required
def change_password(request):
    ...
```

# 🫠 참고

- 데코레이터 ; 기존에 작성된 함수에 기능 추가하고 싶을 때, 해당 함수 수정하지 않고 기능만을 추가해주는 함수

  ```python
  def hello(func):
    def wrapper():
      print('HIHI')
      func()
      print('HIHI')

    return wrapper
  
  @hello
  def bye():
    print('byebye')
  
  bye()

  # 출력
  HIHI
  byebye
  HIHI
  ```

- is_authenticated https://github.com/django/django/blob/main/django/contrib/auth/base_user.py

  ![is_authenticated](https://user-images.githubusercontent.com/121418205/230009684-45381b22-5195-48ec-9594-1309f3017750.png)

- 회원가입 후 로그인까지 진행하려면

  ```python
  # accounts/views.py
  def signup(request):
      ...
          if form.is_valid():
              user = form.save()
              auth_login(request,user)
              return redirect('mainpg:index')
      ...
  ```

  ![UserCreationForm의 save 메서드](https://user-images.githubusercontent.com/121418205/230010450-9a6fa102-b546-46ef-8d1b-b818197f6b2e.png)

- 탈퇴하면서 유저의 세션 정보도 함께 지우고 싶을 경우

  ```python
  # accounts/views.py
  def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('mainpg:index')
  ```

  - **탈퇴(1) 후 로그아웃(2)**의 순서가 바뀌면 안 됨

  - 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지고 > 탈퇴에 필요한 유저 정보 또한 없어지기 때문