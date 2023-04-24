- 비동기(Asynchronous)

  - 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것 (병렬적 수행)

  - 시간이 필요한 작업들은 요청 보낸 뒤 응답이 빨리 오는 작업부터 처리

  - 예시
  
    1. Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨

    2. 작업 flow

      ```
      function slowRequest(callBack) {
          console.log('1. 오래 걸리는 작업 시작 ...')
          setTimeout(function() {
              callBack()
          }, 3000)
      }

      function myCallBack() {
          console.log('2. 콜백함수 실행됨')
      }

      slowRequest(myCallBack)
      console.log('3. 다른 작업 실행')

      # 출력결과
      # 1. 오래 걸리는 작업 시작 > 3. 다른 작업 실행 > 2. 콜백함수 실행됨
      ```

  - Ajax (Aynchrounous JavaScript And XML) ; 비동기적 웹 애플리케이션 개발 위한 프로그래밍 기술명 > **사용자의 요청에 대한 즉각적인 반응을 제공**하면서 페이지 전체를 다시 로드하지 않고 **필요한 부분만 업데이트하는 것이 목표**

    - 응답의 변화

      1. 기존

        ![Ajax사용전](https://user-images.githubusercontent.com/121418205/233309757-279981c0-9692-42f7-b9ee-f94fe4252b79.png)

      2. Ajax

        ![Ajax사용후](https://user-images.githubusercontent.com/121418205/233309744-c98e7e89-ab58-4ee2-9213-6a1ea96ff575.png)

  - XMLHttpRequest ; **JavaScript 객체**로, 클라이언트와 서버 간에 데이터를 **비동기적**으로 주고받을 수 있도록 해주는 객체 > **JavaScript 코드에서 서버에 요청을 보내고 서버로부터 응답을 받을 수 있음**

# 🫠 비동기 요청

- Axios ; JavaScript에서 HTTP 요청을 보내는 라이브러리 > 주로 프론트엔드 프레임워크에서 사용

  - 기본 문법

    ```html
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js></script>
    <script>
        axios({
            method: 'HTTP 메서드',
            url: '요청 URL',
        })
            .then(성공하면 수행할 콜백함수)
            .catch(실패하면 수행할 콜백함수)
    </script>
    ```

      - get, post 등 여러 method 사용 가능

      - then 이용해서 성공하면 수행할 로직 작성

      - catch 이용해서 실패하면 수행할 로직 작성

  - 고양이 사진 가져오기 Python vs JS

    - 동기식 코드 (Python) ; 위에서부터 순서대로 처리 > 첫번째 print 출력 후 이미지 가져오는 처리 기다렸다가 다음 print 출력

    - 비동기식 코드 (JavaScript) ; 바로 처리가 가능한 작업(console.log)은 바로 처리 / 오래 걸리는 작업인 이미지 요청하고 가져오는 일은 요청 보내놓고 **기다리지 않고 다음 코드로 진행 후** 완료된 시점에 결과 출력 진행

    ```python
    # PYTHON
    import requests

    print('고양이는 야옹')

    cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(cat_image_search_url)

    if response.status_code == 200:
        print(response.json())
    else:
        print('실패했다옹')
    print('야옹야옹')
    
    # 결과
    고양이는 야옹
    [{'id': 'egr', 'url': 'https://cdn2.thecatapi.com/images/egr.png', 'width': 500, 'height': 390}]
    야옹야옹
    ```

    ```html
    <!--JAVASCRIPT-->
    <body>
      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      <script>
        console.log('고양이는 야옹')
        const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'

        axios({
          method: 'get',
          url: catImageSearchURL,
        })
          .then((response) => {
            console.log(response.data)
          })
          .catch((error) => {
            console.log('실패했다옹')
          })
        console.log('야옹야옹')
      </script>
    </body>

    <!--결과-->
    고양이는 야옹                         cat_api_1.html:14 
    야옹야옹                              cat_api_1.html:27 
    Array(1)                             cat_api_1.html:22 
        0 : {id: 'dg8', url: 'https://cdn2.thecatapi.com/images/dg8.jpg', width: 800, height: 517}
        length : 1
        [[Prototype]] : Array(0)
    ```

  - 고양이 사진 가져오기 완성

    ```html
    <button>야옹이 버튼</button>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
      const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
      const btn = document.querySelector('button')

      btn.addEventListener('click', function () {
        axios({
          method: 'get',
          url: catImageSearchURL,
        })
          .then((response) => {
            imgElem = document.createElement('img')
            imgElem.setAttribute('src', response.data[0].url)
            document.body.appendChild(imgElem)
          })
          .catch((error) => {
            console.log('실패했다옹')
          })
      })
    </script>
    ```
  
# 😫 팔로우 with ajax

- 팔로우 구현

  1. axios CDN 작성

    ```html
    <!--accounts/profile.html-->
    <body>
      ...
      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      <script>
      </script>
    </body>
    ```

  2. form 요소 선택 위해 id 속성 지정 및 선택 > 불필요해진 action과 method 속성은 삭제 (요청은 axios로 대체되기 때문)

    ```html
    <!--accounts/profile.html-->
    <form id="follow-form">
      ...
    </form>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
      const form = document.querySelector('#follow-form')
    </script>
    ```

  3. axios 요청 준비

    ```html
    <!--accounts/profile.html-->
    <script>
      const form = document.querySelector('#follow-form')
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        axios({
          method: 'post',
          url: '/accounts/${???}/follow/',
        })
      })
    </script>
    ```

    - axios로 POST 요청을 보내기 위해 필요한 것

      1. url에 작성할 user pk는 어떻게 작성해야 할까?

      2. csrftoken은 어떻게 보내야 할까?

  4. url에 작성할 user pk 가져오기 (HTML > JavaScript)

    - 'data-*' attributes ; 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에 교환할 수 있는 방법
    
    - data-test-value라는 이름의 특성을 지정했다면 JS에서는 element.dataset.testValue로 접근 가능 https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*

    ```html
    <!--accounts/profile.html-->
    <form id="follow-form" data-user-id="{{ person.pk }}">
      ...
    </form>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
      const form = document.querySelector('#follow-form')
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const userId = event.target.dataset.userId
        ...
      })
    </script>
    ```

  5. 요청 url 작성 마치기

    ```html
    <!--accounts/profile.html-->
    <script>
      const form = document.querySelector('#follow-form')
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const userId = event.target.dataset.userId
        axios({
          method: 'post',
          url: '/accounts/${userId}/follow/',
        })
      })
    </script>
    ```

  6. hidden 타입으로 숨어있는 csrf 값을 가진 input 태그 선택 https://docs.djangoproject.com/en/3.2/ref/csrf/

    ![ajax_csrf_input](https://user-images.githubusercontent.com/121418205/233903796-276756d8-ec85-4de1-962f-2d3f7ba0fea8.png)

    ```html
    <!--accounts/profile.html-->
    <script>
      const form = document.querySelector('#follow-form')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    ```

  7. AJAX로 csrftoken을 보내는 방법 https://docs.djangoproject.com/en/3.2/ref/csrf/#setting-the-token-on-the-ajax-request

    ```html
    <!--accounts/profile.html-->
    <script>
      const form = document.querySelector('#follow-form')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const userId = event.target.dataset.userId
        axios({
          method: 'post',
          url: '/accounts/${userId}/follow/',
          headers: {'X-CSRFToken': csrftoken,}
        })
      })
    </script>
    ```

  8. 팔로우 관계 확인 위한 is_followed 변수 작성 및 JSON 응답
  
    - 팔로우 버튼 토글하기 위해 현재 팔로우가 된 상태인지 확인 필요 > axios 요청 통해 받는 response 객체 활용해 view 함수 통해서 팔로우 관계 여부 파악할 수 있는 변수를 담아 JSON 타입으로 응답하기

    ```python
    # accounts/views.py
    from django.http import JsonResponse

    @login_required
    def follow(request, user_pk):
        User = get_user_model()
        you = User.objects.get(pk=user_pk)
        me = request.user
        if you != me:
            if me in you.followers.all():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
            }
            return JsonResponse(context)
        return redirect('accounts:profile, you.username, context')
    ```

  9. view 함수에서 응답한 is_followed를 사용해 버튼 토글하기

    ```html
    <!--accounts/profile.html-->
    <script>
      ...
        axios({
          method: 'post',
          url: '/accounts/${userId}/follow/',
          headers: {'X-CSRFToken': csrftoken,}
        })
          .then((response) => {
            const isFollowed = response.data.is_followed
            const followBtn = document.querySelector('#follow-form > input[type=submit]')
            if (isFollowed === true) {
              followBtn.value = '언팔로우'
            } else {
              followBtn.value = '팔로우'
            }
          })
      })
    </script>
    ```

- 팔로잉 & 팔로워 수 비동기 적용

  1. 해당 요소 선택할 수 있도록 span 태그와 id 속성 작성

    ```html
    <!--accounts/profile.html-->
    <div>
      팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span> /
      팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
    </div>
    ```

  2. 직전에 작성한 span 태그를 각각 선택

    ```html
    <!--accounts/profile.html-->
    <script>
      ...
          .then((response) => {
            const isFollowed = response.data.is_followed
            const followBtn = document.querySelector('#follow-form > input[type=submit]')
            if (isFollowed === true) {
              followBtn.value = 'Unfollow'
            } else {
              followBtn.value = 'Follow'
            }
            const followingsCountTag = document.querySelector('#followings-count')
            const followersCountTag = document.querySelector('#followers-count')
          })
      })
    </script>
    ```

  3. 팔로잉, 팔로워 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

    ```python
    # accounts/views.py
    def follow(request, user_pk):
        ...
            context = {
                'is_followed': is_followed,
                'followings_count': you.followings.count(),
                'followers_count': you.followers.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    ```

  4. view 함수에서 계산된 결과를 응답에서 찾아 적용

    ```html
    <!--accounts/profile.html-->
    <script>
      ...
          .then((response) => {
            ...
            const followingsCountTag = document.querySelector('#followings-count')
            const followersCountTag = document.querySelector('#followers-count')
            const followingsCountData = response.data.followings_count
            const followersCountData = response.data.followers_count
            followingsCountTag.textContent = followingsCountData
            followersCountTag.textContent = followersCountData
          })
      })
    </script>
    ```

# 🤯 좋아요 with ajax

- 좋아요 비동기 적용 ; 팔로우와 동일한 흐름 + forEach() + querySelectorAll()

  - index 페이지 각 게시글에 각각 좋아요 버튼이 있기 때문

  - 반복 + 목록 선택

  ```python
  # articles/views.py
  @login_required
  def likes(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      if request.user in article.like_users.all():
          article.like_users.remove(request.user)
          is_liked = False
      else:
          article.like_users.add(request.user)
          is_liked = True
      context = {
          'is_liked': is_liked,
      }
      return JsonResponse(context)
  ```

  ```html
  <!--articles/index.html-->
  ...
    <form class="like-forms" data-article-id="{{ article.pk }}">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
      {% else %}
        <input type="submit" value="좋아요" id="like-{{ article.pk }}">
      {% endif %}
    </form>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const forms = document.querySelectorAll('.like-forms')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    forms.forEach((form) => {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const articleId = event.target.dataset.articleId
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/articles/${articleId}/likes/`,
          headers: {'X-CSRFToken': csrftoken},
        })
        .then((response) => {
          const isLiked = response.data.is_liked
          const likeBtn = document.querySelector(`#like-${articleId}`)
          if (isLiked === true) {
            likeBtn.value = '좋아요 취소'
          } else {
            likeBtn.value = '좋아요'
          }
        })
        .catch((error) => {
          console.log(error.response)
        })
      })
    })
  </script>
  ```

# 🙂 참고

- 비동기를 사용하는 이유 ; **"사용자 경험"**

  - 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때 > 동기로 처리하면 데이터 불러온 뒤에야 앱의 실행 로직이 수행되므로 앱이 멈춘 것과 같은 경험을 하게 됨

  - 즉, 동기식 처리는 **특정 로직이 실행되는 동안 다른 로직 실행을 차단**하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험 만들게 됨

  - 비동기로 처리한다면 **먼저 처리되는 부분부터** 보여줄 수 있으므로, 사용자 경험에 긍정적 효과 > 많은 웹 기능은 비동기 로직 사용해서 구현되어 있음