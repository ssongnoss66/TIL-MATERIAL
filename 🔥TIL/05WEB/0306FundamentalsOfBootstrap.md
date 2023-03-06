# 0306 MON

## 😏 Bootstrap

- Bootstrap ; 프론트엔드 라이브러리 / **반응형 웹  디인 & CSS 및 JS 기반의 컴포넌트와 스타일 제공

- 사용해보기

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

- Bootstrap 클래스명

  ![Bootstrap클래스명](https://user-images.githubusercontent.com/121418205/222999795-9b2cf586-c38d-446e-a2ba-9a37ace531c2.png)

  - ex) mt-5 ; {property}{sides}-{size} (margin top 48px)
  
    ```html
    <p class="mt-5">Hello, world!<p>
    ```

## 😝 Typography 및 Color

### @ Typography

- Typography ; 문서 상 제목, 본문 텍스트, 목록

- Headings ; HTML h1 ~ h6 태그와 스타일을 일치시키고 싶지만 관련 HTML 태그를 더 사용할 수 없는 경우

  ```html
  <p class="h1">h1. Bootstrap heading</p>
  <p class="h2">h2. Bootstrap heading</p>
  <p class="h3">h3. Bootstrap heading</p>
  <p class="h4">h4. Bootstrap heading</p>
  <p class="h5">h5. Bootstrap heading</p>
  <p class="h6">h6. Bootstrap heading</p>
  ```

  ![Headings](https://user-images.githubusercontent.com/121418205/223000328-a7022e0a-8331-47d6-99d2-9b1f0a078df0.png)

- Display Headings ; 기존 Heading보다 더 눈에 띄는 제목이 필요할 경우 (더 크고 약간 다른 스타일)

  ```html
  <h1 class="display-1">Display 1</h1>
  <h1 class="display-2">Display 2</h1>
  <h1 class="display-3">Display 3</h1>
  <h1 class="display-4">Display 4</h1>
  <h1 class="display-5">Display 5</h1>
  <h1 class="display-6">Display 6</h1>
  ```

  ![DisplayHeadings](https://user-images.githubusercontent.com/121418205/223000631-806129ed-a000-475a-9102-3c2bd674c42a.png)

- Inline text elements

  ```html
  <p>You can use the mark tag to <mark>highlight</mark> text.</p>
  <p><del>This line of text is meant to be treated as deleted text.</del></p>
  <p><s>This line of text is meant to be treated as no longer accurate.</s></p>
  <p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
  <p><u>This line of text willr ender as underlined.</u></p>
  <p><small>This line of text is meant to be treated as fine print.</small></p>
  <p><strong>This line rendered as bold text.</strong></p>
  <p><em>This line rendered as italicized text.</em></p>
  ```

  ![Inlinetextelements](https://user-images.githubusercontent.com/121418205/223001408-ef45a565-efff-49a7-9989-2889950243d1.png)

- List

  ```html
  <ul class="list-unstyled">
    <li>This is a list.</li>
    <li>It appears completely unstyled.</li>
    <li>Structurally, it's still a list.</li>
    <li>However, this style only applies to immediate child elements.</li>
    <li>Nested lists:
      <ul>
        <li>are unaffected by this style</li>
        <li>will still show a bullet</li>
        <li>and have appropriate left margin</li>
      </ul>
    </li>
    <li>This may still come in handy in some situations.</li>
  </ul>
  ```

  ![List](https://user-images.githubusercontent.com/121418205/223002017-add3b270-7508-4fed-ae36-f29cb46f6850.png)

### @ Bootstrap Color system

- Bootstrap Color system ; Bootstrap이 지정하고 제공하는 색상 시스템

- Text colors

  ```html
  <p class="text-primary">.text-primary</p>
  <p class="text-primary-emphasis">.text-primary-emphasis</p>
  <p class="text-secondary">.text-secondary</p>
  <p class="text-secondary-emphasis">.text-secondary-emphasis</p>
  <p class="text-success">.text-success</p>
  <p class="text-success-emphasis">.text-success-emphasis</p>
  <p class="text-danger">.text-danger</p>
  ```

  ![Color](https://user-images.githubusercontent.com/121418205/223002343-448a719a-162f-493f-b168-e778661a1b02.png)

- Background colors

  ```html
  <div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
  <div class="p-3 mb-2 bg-primary-subtle text-emphasis-primary">.bg-primary-subtle</div>
  <div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
  <div class="p-3 mb-2 bg-secondary-subtle text-emphasis-secondary">.bg-secondary-subtle</div>
  <div class="p-3 mb-2 bg-success text-white">.bg-success</div>
  <div class="p-3 mb-2 bg-success-subtle text-emphasis-success">.bg-success-subtle</div>
  <div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
  ```

  ![BackgroundColor](https://user-images.githubusercontent.com/121418205/223002495-22c8eb23-290b-49b2-8a57-66bfbb0c6d66.png)

### @ Bootstrap 실습

- 너비와 높이가 각각 200px인 정사각형 작성 (너비와 높이 제외 모두 bootstrap으로 작성)

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <style>
      .box {
        width: 200px;
        height: 200px;
      }
    </style>
  </head>
  <body>
    <div class="box border border-dark border-2 bg-info text-white m-3"></div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  <img width="239" alt="실습" src="https://user-images.githubusercontent.com/121418205/223006011-f6349bdd-af05-43e0-a6d2-790fb71f2c8f.png">


## 😃 Component

- Bootstrap Component ; Bootstrap에서 제공하는 **UI 관련 요소 (버튼, 폼, 카드, 드롭다운, 네비게이션 바 등) > 일관된 디자인, 쉬운 프로토타입 제작 및 사용자 경험**

- Alerts

  ```html
  <div class="alert alert-primary" role="alert">
    A simple primary alert—check it out!
  </div>
  <div class="alert alert-secondary" role="alert">
    A simple secondary alert—check it out!
  </div>
  <div class="alert alert-success" role="alert">
    A simple success alert—check it out!
  </div>
  <div class="alert alert-danger" role="alert">
    A simple danger alert—check it out!
  </div>
  <div class="alert alert-warning" role="alert">
    A simple warning alert—check it out!
  </div>
  <div class="alert alert-info" role="alert">
    A simple info alert—check it out!
  </div>
  <div class="alert alert-light" role="alert">
    A simple light alert—check it out!
  </div>
  <div class="alert alert-dark" role="alert">
    A simple dark alert—check it out!
  </div>
  ```

  ![alerts](https://user-images.githubusercontent.com/121418205/223006009-27971448-1a82-4402-bc0b-dec75a91343b.png)

- Badges

  ```html
  <h1>Example heading <span class="badge bg-secondary">New</span></h1>
  <h2>Example heading <span class="badge bg-secondary">New</span></h2>
  <h3>Example heading <span class="badge bg-secondary">New</span></h3>
  <h4>Example heading <span class="badge bg-secondary">New</span></h4>
  <h5>Example heading <span class="badge bg-secondary">New</span></h5>
  <h6>Example heading <span class="badge bg-secondary">New</span></h6>
  ```

  ![badges](https://user-images.githubusercontent.com/121418205/223006006-75527f1a-5270-4c2c-b641-18b834aa132d.png)

- Buttons

  ```html
  <button type="button" class="btn btn-primary">
    Notifications <span class="badge text-bg-secondary">4</span>
  </button>
  ```

  ![buttons](https://user-images.githubusercontent.com/121418205/223006005-600d3db4-9fe6-4cc7-940c-c72a4f2d62d2.png)

- Cards

  ```html
  <div class="card" style="width: 18rem;">
    <img src="..." class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
  </div>
  ```

  ![cards](https://user-images.githubusercontent.com/121418205/223005997-5bef95a5-5358-49bf-be9c-b03afcbef1ff.png)

- Navbar

  ```html
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
  ```

  ![navbar](https://user-images.githubusercontent.com/121418205/223005993-4031211c-a96c-4c16-bee2-397363e40fdb.png)

## 🤔 참고

- CND (Content Delivery Network)

  - 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술

  - 서버와 사용자 사이의 물리적 거리 줄여 콘텐츠 로딩에 소요되는 시간 최소화 (웹 페이지 로드 속도 높임)

  - 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

- Bootstrap CDN

  1. Bootstrap 홈페이지 - Download - "Compiled CSS and JS" Download

  2. CDN을 통해 가져오는 bootstrap css와 js 파일 확인

  3. bootstrap.css 파일을 참고하여, 현재까지 작성한 클래스에 적용된 스타일 직접 확인