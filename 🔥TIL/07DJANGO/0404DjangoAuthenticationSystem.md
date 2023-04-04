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