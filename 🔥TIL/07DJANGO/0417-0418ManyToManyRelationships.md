- M:N 관계 맛보기 ; 병원 진료 시스템 모델 관계 만들기 (환자 - 의사)

- N:1의 한계

  1. 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계 설정

    ```python
    # hospitals/models.py
    from django.db import models

    class Doctor(models.Model):
        name = models.TextField()
        def __str__(self):
            return f'{self.pk}번 의상 {self.name}'
        
    class Patient(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        name = models.TextField()
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    ```

  2. 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약했다고 가정

    ```shell
    # shell_plus
    In [1]: doctor1 = Doctor.objects.create(name='alice')

    In [2]: doctor2 = Doctor.objects.create(name='bella')

    In [3]: patient1 = Patient.objects.create(name='carol', doctor=doctor1)

    In [4]: patient2 = Patient.objects.create(name='dane', doctor=doctor2)

    In [5]: doctor1
    Out[5]: <Doctor: 1번 의사 alice>

    In [6]: doctor2
    Out[6]: <Doctor: 2번 의사 bella>

    In [7]: patient1
    Out[7]: <Patient: 1번 환자 carol>

    In [8]: patient2
    Out[8]: <Patient: 2번 환자 dane>
    ```

  3. 1번 환자(carol)가 두 의사 모두에게 방문하려고 함

    ```shell
    # shell_plus
    patient3 = Patient.objects.create(name='carol', doctor=doctor2)
    ```
  
  4. 동시 예약 불가 (1,2 형태로 참조하는 것을 Integer 타입 아니기 때문에 불가능)

    ```shell
    In [1]: patient4 = Patient.objects.create(name='carol', doctor=doctor1, doctor2)
      Cell In[1], line 1
        patient4 = Patient.objects.create(name='carol', doctor=doctor1, doctor2)
                                                                              ^
    SyntaxError: positional argument follows keyword argument
    ```
  
  - 동일한 환자 다른 의사 예약 위해서는 객체를 하나 더 만들어서 예약 진행해야 함 > **예약 테이블을 따로 만들자**

- 중개 모델

  1. 환자 모델의 외래 키 삭제하고 별도의 예약 모델 새로 작성 > 예약 모델을 의사와 환자에 각각 N:1 관계

    ```python
    # hospitals/models.py
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```

  2. 의사와 환자 생성 후 예약 만들기

    ```shell
    In [1]: doctor1 = Doctor.objects.create(name='alice')

    In [2]: patient1 = Patient.objects.create(name='carol')

    In [3]: Reservation.objects.create(doctor=doctor1, patient=patient1)
    Out[3]: <Reservation: 1번 의사의 1번 환자>
    ```

  3. 예약 정보 조회

    ```shell
    In [4]: doctor1.reservation_set.all()
    Out[4]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

    In [5]: patient1.reservation_set.all()
    Out[5]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
    ```

  4. 1번 의사에게 새로운 환자 예약이 생성된다면

    ```shell
    In [6]: patient2 = Patient.objects.create(name='dane')

    In [7]: Reservation.objects.create(doctor=doctor1, patient=patient2)
    Out[7]: <Reservation: 1번 의사의 2번 환자>
    ```
  
  5. 1번 의사의 예약 정보 조회

    ```shell
    In [8]: doctor1.reservation_set.all()
    Out[8]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>
    ```

- Django ManyToManyField

  1. 환자 모델에 Django ManyToManyField 작성

    ```shell
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor)
        name = models.TextField()
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    
    # Reservation Class 주석 처리
    ```

  2. 중개 테이블 hospitals_patient_doctors 확인

    <img width="930" alt="중개테이블" src="https://user-images.githubusercontent.com/121418205/232458456-c2da67eb-16ae-4a75-a830-8a3ab4ae080d.png">

  3. 의사 1명과 환자 2명 생성

    ```shell
    In [1]: doctor1 = Doctor.objects.create(name='alice')

    In [2]: patient1 = Patient.objects.create(name='carol')

    In [3]: patient2 = Patient.objects.create(name='dane')
    ```

  4. 예약 생성 (환자가 의사에게 예약)

    ```shell
    # patient1이 doctor1에게 예약
    In [4]: patient1.doctors.add(doctor1)

    # patient1 - 자신이 예약한 의사 목록 확인
    In [5]: patient1.doctors.all()
    Out [5]: <QuerySet [<Doctor: 1번 의사 alice>]>
    ```

  5. 예약 생성 (의사가 환자를 예약)

    ```shell
    # doctor1이 patient2을 예약
    In [6]: doctor1.patient_set.add(patient2)

    # doctor1 - 자신의 예약 환자 목록 확인
    In [7]: doctor1.patient_set.all()
    Out [7]: <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

    # patient1,2 - 자신이 예약한 의사 목록 확인
    In [8]: patient1.doctors.all()
    Out [8]: <QuerySet [<Doctor: 1번 의사 alice>]>

    In [9]: patient2.doctors.all()
    Out [9]: <QuerySet [<Doctor: 1번 의사 alice>]>
    ```

  6. 예약 현황 중개 테이블 확인

    <img width="905" alt="예약현황중개테이블" src="https://user-images.githubusercontent.com/121418205/232461251-929c1c36-02fa-453b-8c77-805765a94668.png">

  7. 예약 취소하기 > .remove() 사용

    ```shell
    # doctor1이 patient1 진료 예약 취소
    In [10]: doctor1.patient_set.remove(patient1)

    In [11]: doctor1.patient_set.all()
    Out[11]: <QuerySet [<Patient: 2번 환자 dane>]>

    In [12]: patient1.doctors.all()
    Out[12]: <QuerySet []>

    # patient2가 doctor1 진료 예약 취소
    In [13]: patient2.doctors.remove(doctor1)

    In [14]: patient2.doctors.all()
    Out[14]: <QuerySet []>

    In [15]: doctor1.patient_set.all()
    Out[15]: <QuerySet []>
    ```

- 'through' argument

  - 중개 모델 직접 작성하는 경우 through 옵션 사용하여 사용하려는 중개 테이블 나타내는 Django 모델 지정 가능

  - **중개 테이블에 '추가 데이터' 사용해 다대다 관계와 연결하려는 경우**

  1. through 설정 및 Reservation Class 수정 > 예약 정보에 "증상"과 "예약일"이라는 추가 데이터 생김

    ```python
    # hospitals/models.py
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, through='Reservation')
        name = models.TextField()
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'

    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        symptom = models.TextField()
        reserved_at = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```

  2. 의사 1명과 환자 2명 생성

    ```shell
    In [1]: doctor1 = Doctor.objects.create(name='alice')

    In [2]: patient1 = Patient.objects.create(name='carol')

    In [3]: patient2 = Patient.objects.create(name='dane')
    ```

  3. 예약 생성 방법 1 ; Reservation class 통한 예약 생성

    ```shell
    In [4]: reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')

    In [5]: reservation1.save()

    In [6]: doctor1.patient_set.all()
    Out [6]: <QuerySet [<Patient: 1번 환자 carol>]>

    In [7]: patient1.doctors.all()
    Out [7]: <QuerySet [<Doctor: 1번 의사 alice>]>
    ```

  4. 예약 생성 방법2 ; Patient 객체를 통한 예약 생성

    ```shell
    In [8]: patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

    In [9]: doctor1.patient_set.all()
    Out[9]: <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

    In [10]: patient2.doctors.all()
    Out[10]: <QuerySet [<Doctor: 1번 의사 alice>]>
    ```

  5. 예약 삭제

    ```shell
    In [11]: doctor1.patient_set.remove(patient1)

    In [12]: patient2.doctors.remove(doctor1)
    ```

- 정리

  - M:N 관계로 맺어진 두 테이블에는 변화 없음

  - ManyToManyField는 중개 테이블을 자동으로 생성

  - ManyToManyField는 M:N 관계 맺는 두 모델 **어디에 위치해도 상관 없음** > 필드 작성 위치에 따라 참조와 역참조 방향 주의

  - N:1은 완전한 종속 관계 > M:N은 의사에게 진찰받는 환자, 환자 진찰하는 의사의 두 가지 형태로 모두 표현 가능

# 🥸 ManyToManyField

- ```ManyToManyField(to, **options)```

  - many-to-many 관계 설정 시 사용하는 모델 필드

  - 모델 필드의 RelatedManager 사용하여 관련 개체 추가, 제거 또는 생성 ; add(), remove(), create(), clear()...

- ManyToManyField's Arguments

  1. related_name ; 역참조시 사용하는 manager name을 변경

    ```python
    # hospitals/models.py
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, related_name='patients')
        name = models.TextField()
    ```

    ```shell
    # 변경 전
    doctors.patient_set.all()

    # 변경 후
    doctors.patients.all()
    ```

  2. through ; 중개 테이블 직접 작성하는 경우, through 옵션 사용하여 중개 테이블 나타내는 Django 모델 지정 > 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 사용됨

  3. symmetrical ; ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용 > 기본 값 : True

    ```python
    # hospitals/models.py
    class Person(models.Model):
        friends = models.ManyToManyField('self')
        # friends = models.ManyToManyField('self', sy,,etrical=False)
    ```

    - True일 경우

      - _set 매니저 추가 X

      - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)

      - 즉, 내가 당신의 친구라면 당신도 내 친구가 됨

    - 대칭을 원하지 않는 경우 False로 설정 ; Follow 기능 구현에서 다시 확인할 예정

- M:N에서의 methods

  - add() ; **"지정된 객체를 관련 객체 집합에 추가"** > 이미 존재하는 관계에 사용하면 관계가 복제되지 않음

  - remove() ; **"관련 객체 집합에서 지정된 모델 개체를 제거"**

# 🙃 Article & User

- Many to many relationships (N:M or M:N) ; 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우 **양쪽 모두에서 N:1 관계를 가짐**

- Article(M) - User(N) ; 0개 이상의 게시글은 0명 이상의 회원과 관련됨 > 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고 / 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다

- 모델 관계 설정

  1. ManyToManyField

    ```python
    # articles/models.py
    class Article(models.Model):
        ...
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
        ...
    ```

  2. Migration 진행 후 에러 확인

    ```
    # terminal
    python manage.py makemigrations
    SystemCheckError: System check identified some issues:

    ERRORS:
    articles.Article.like_users: (fields.E304) Reverse accessor for 'articles.Article.like_users' clashes with reverse accessor for 'articles.Article.user'.
            HINT: Add or change a related_name argument to the definition for 'articles.Article.like_users' or 'articles.Article.user'.
    articles.Article.user: (fields.E304) Reverse accessor for 'articles.Article.user' clashes with reverse accessor for 'articles.Article.like_users'.
            HINT: Add or change a related_name argument to the definition for 'articles.Article.user' or 'articles.Article.like_users'.
    ```

  - like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨 > but 이전 N:1(Article-User) 관계에서 이미 해당 매니저 사용 중 (user.article_set.all() ; 해당 유저가 작성한 모든 게시글 조회)

  - user가 작성한 글들(user.article_set)과 user가 좋아요 누른 글(user.article_set) 구분 불가

  - user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함

  - user.article_set ; related manager 이름이 충돌

    - N:1 ; 유저가 작성한 게시글

    - M:N ; 유저가 좋아요한 게시글

  3. related_name 작성 후 migration

    ```python
    # articles/models.py
    class Article(models.Model):
        ...
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    ```

  4. 생성된 중개 테이블 확인

    <img width="893" alt="article중개테이블" src="https://user-images.githubusercontent.com/121418205/232642079-95acc91e-dc85-42ed-908f-fd5d29a02072.png">

- User-Article 간 사용 가능한 related manager 정리

  - article.user ; 게시글을 작성한 유저 N:1

  - user.article_set ; 유저가 작성한 게시글(역참조) N:1

  - article.like_users ; 게시글을 좋아요한 유저 M:N

  - user.like_articles ; 유저가 좋아요한 게시글(역참조) M:N

- 좋아요 구현

  1. url 및 view 함수 작성

    ```python
    # articles/urls.py
    urlpatterns = [
        ...
        path('<int:article_pk>/likes/', views.likes, name='likes'),
    ]

    # articles/views.py
    @login_required
    def likes(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    ```
  
  2. index 템플릿에서 각 게시글에 좋아요 버튼 출력

    ```html
      {% for article in articles %}
        ...
        <form action="{% url 'articles:likes' article.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in article.like_users.all %}
            <input type="submit" value="좋아요 취소">
          {% else %}
            <input type="submit" value="좋아요">
          {% endif %}
        </form>
      {% endfor %}
    ```

# 😀 참고

- ```.exists()``` ; QuerySet에 결과가 포함되어 있으면 True 반환하고 그렇지 않으면 False 반환 > 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

  ```python
  # articles/views.py
  # exists() 적용 전
  def likes(request, article_pk):
      ...
      if request.user in article.like_users.all():
          ...

  # exists() 적용 후
  def likes(request, article_pk):
      ...
      if article.like_users.filter(pk=request.user.pk).exists():
          ...
  ```

- Profile 구현

  1. 자연스러운 follow 흐름 위한 프로필 페이지 작성

    ```python
    # accounts/urls.py
    urlpatterns = [
        ...,
        path('profile/<username>/', views.profile, name='profile'),
    ]

    # accounts/views.py
    from django.contrib.auth import get_user_model

    def profile(request, username):
        User = get_user_model()
        person = User.objects.get(username=username)
        context = {
            'person': person,
        }
        return render(request, 'accounts/profile.html', context)
    ```

  2. profile 템플릿 작성

    ```html
    <!--accounts/profile.html-->
    {% block content %}
      <h1>accounts PROFILE</h1>
      <hr>
      <h2>{{ person.username }}님의 프로필</h2>
      <hr>
      <h3>{{ person.username }}'s 게시글</h3>
      {% for article in person.article_set.all %}
        <div>{{ article.title }}</div>
      {% endfor %}
      <hr>
      <h3>{{ person.username }}'s 댓글</h3>
      {% for comment in person.comment_set.all %}
        <div>{{ comment.content }}</div>
      {% endfor %}
      <hr>
      <h3>{{ person.username}}'s 좋아요한 게시글</h3>
      {% for article in person.like_articles.all %}
        <div>{{ article.title }}</div>
      {% endfor %}
    {% endblock content %}
    ```

  3. Profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성

    ```html
    <!--articles/index.html-->
    {% block content %}
      <h1>ARTICLES</h1>
      <p>{{ articles }}</p>
      <hr>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
      {% for article in articles %}
        <p>{{ article }}</p>
        <p>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></p>
        ...
    {% endblock content %}
    ```

# 🫢 User & User

- User(M) - User(N) ; 유저는 0명 이상의 다른 유저와 관련된다 > 유저는 다른 유저로부터 0개 이상의 팔로우를 받을 수 있고, 유저는 0명 이상의 다른 유저들에게 팔로잉 걸 수 있다

- Follow 구현

  1. ManyToManyField 작성 및 Migration 진행 후 중개테이블 필드 확인

    ```python
    # accounts/models.py
    class User(AbstractUser):
        followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    ```

    <img width="995" alt="accounts중개테이블" src="https://user-images.githubusercontent.com/121418205/232943453-187931ef-77b4-4975-a6a5-5b8d77ca3aa9.png">

  2. url 및 view 함수 작성

    ```python
    # accounts/urls.py
    urlpatterns = [
        ...,
        path('<int:user_pk>/follow/', views.follow, name='follow'),
    ]

    # accounts/views.py
    @login_required
    def follow(request, user_pk):
        User = get_user_model()
        person = User.objects.get(pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    ```

  3. 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성 > 팔로우 버튼 클릭 후 팔로우 버튼 변화 및 중개 테이블 데이터 확인

    ```html
    <!--accounts/profile.html-->
    {% block content %}
    {% load bootstrap5 %}
      <h1>accounts PROFILE</h1>
      <hr>
      ...
      <div>
        <div>
          팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
        </div>
        {% if request.user != person %}
        <div>
          <form action="{% url 'accounts:follow' person.pk%}" method="POST">
            {% csrf_token %}
            {% if request.user in person.followers.all %}
            <input type="submit" value="Unfollow">
            {% else %}
            <input type="submit" value="Follow">
            {% endif %}
          </form>
        </div>
        {% endif %}
      </div>
    {% endblock content %}
    ```

    <img width="893" alt="follow중개테이블" src="https://user-images.githubusercontent.com/121418205/232945225-b8f87c3c-3eb7-41b2-959d-6e5e444bcaa4.png">