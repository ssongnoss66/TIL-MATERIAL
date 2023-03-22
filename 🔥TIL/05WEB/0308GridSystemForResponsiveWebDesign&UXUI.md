# 🫠 Responsive Web Design

- 디바이스 종류나 화면 크기에 상관없이, 어디에서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

- Bootstrap grid system의 12개 column과 **6개 breakpoints**를 사용하여 반응형 웹 디자인 구현

# 🙂 Grid system Breakpoints

- 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점

- **화면 너비에 따라 6개의 분기점 제공 (xs, sm, md, lg, xl, xxl)**

- 각 breakpoints마다 설정된 최대 너비 값 **"이상으로"** 화면이 커지면 grid system 동작 변경

  ![breakpoints](https://user-images.githubusercontent.com/121418205/223645012-31247e04-d9ac-48cb-8703-30dd29be5de9.png)
  
- 실습

  ![breakpoints실습](https://user-images.githubusercontent.com/121418205/223645010-c261b598-f2a5-4687-adde-ae457f684491.png)

  ```html
  <head>
    <style>
      .box {
        border: 1px solid black;
        background-color: lightblue;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h2 class="text-center">Breakpoints</h2>
    <div class="container">
      <div class="row">
        <div classcol-12 col-sm-6 col-md-2 col-lg-3 col-xl-4>
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
      </div>
    </div>

    <h2 class="text-center">Breakpoints + offset</h2>
    <div class="row g-4">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
        <div class="box">col</div>
      </div>
    </div>
  </body>
  ```

- 실제 Media Query로 작성된 Grid system의 breakpoints

  ```html
  /* Small devices (landscape phones, 675px and up) */
  @media (min-width: 576px) {
    ...
  }

  /* Medium devices (tablets, 768px and up) */
  @media (min-width: 768px) {
    ...
  }

  /* Large devices (desktops, 992px and up) */
  @media (min-width: 992px) {
    ...
  }

  /* X-Laarge devices (large desktops, 1200px adn up) */
  @media (min-width: 1200px) {
    ...
  }

  /* XX-Large devices (larger desktops, 1400px and up) */
  @media (min-width: 1400px) {
    ...
  }
  ```

> Grid System은 화면 크기에 따라 **(breakpoints)** 12개의 칸을 각 요소에 나누어 주는 것

- 실제 홈페이지 분석

  ![airbnb Grid System](https://user-images.githubusercontent.com/121418205/223645004-4b4d0b1a-18ee-462d-942e-6b178c22996e.png)

  ![airbnb Flexbox](https://user-images.githubusercontent.com/121418205/223644990-97f06a93-751b-41bb-8a7a-6d35d30f10af.png)

  ![airbnb Position](https://user-images.githubusercontent.com/121418205/223644971-35e5a0f3-7bee-422b-bea4-8da2d18b2bba.png)

# 🧐 참고

- Grid cards ; row-cols 클래스를 사용하여 행당 표시할 열 (카드) 수를 손쉽게 제어할 수 있음

  ![GridCards](https://user-images.githubusercontent.com/121418205/223644959-ae40242b-ce44-4498-aa61-0569ad220083.png)
  
  ```html
  <div class="container">
    <div class="row row-cols-1 row-cols-sm-3 row-cols-md-2 g-4">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  ```

# 😶‍🌫️ UX & UI

## @ UX

- UX (User Experience) ; 제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야

- UX 예시

  - 백화점 1층에서 느껴지는 좋은 향수 향기

  - 러쉬 매장 근처만 가도 맡을 수 있는 러쉬 향기

  - 원하는 음악을 검색할 때, 검색 기능이 적절하게 작동하고 검색 결과가 정확하게 나오는 것

- UX 설계

  - 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정이 필요

  - 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요

## @ UI

- UI (User Interface) ; 서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야

- UI 예시

  - 리모컨 ; 사용자가 버튼을 누르면 TV가 켜지고 채널을 변경하거나 볼륨을 조절할 수 있음

  - ATM ; 사용자가 터치스크린을 통해 사용자 정보를 입력하고, 원하는 금액을 선택할 수 있음

  - 웹 사이트 ; 사용자가 로그인 버튼을 누르면, 이동하는 화면의 디자인 및 레이아웃

- UI 설계

  - 예쁜 디자인보다는 사용자가 더 쉽고 편리하게 사용할 수 있도록 고려

  - 이를 위해 디자인 시스템, 중간 산출물, 프로토타입 등이 필요

## @ 디자이너, 기획자, 개발자

- UX (직무 ; UX Researcher, User Researcher)

  - 구글 ; 사용자의 경험을 이해하기 위한 통계 모델 설계

  - MS ; 리서치 기획, 사용자에 대한 지표 정의

  - Meta ; 정성적인 방법과 정량적인 방법을 사용해서 사용자 조사 실시

- UI (직무 ; Product Designer, Interaction Designer)

  - 구글 ; 다양한 디자인 프로토타이핑 툴을 사용해서 개발 가이드 제공

  - MS ; 시각 디자인을 고려해서 체계적인 디자인 컨셉 보여줌

  - Meta ; 제품을 이해하고 더 나은 UI Flow와 사용자 경험 디자인

- 애플의 UI 디자인 기본 원칙 https://developer.apple.com/kr/design/tips/