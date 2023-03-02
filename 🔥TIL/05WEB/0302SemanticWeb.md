# 0302 THU

## 😁 Web - Semantic Web

- 웹 데이터를 의미론적으로 표현하고 연결하는 개념 ; 컴퓨터가 데이터 내용과 문맥을 더 효율적으로 이해하고 지능적으로 활용할 수 있도록!

## 1. Semantics in HTML

- "이 페이지의 최상위 제목"

  ```html
  <h1>Heading</h1>
  ```

    - 페이지 최상위 제목 의미를 제공하는 semantic 요소 h1

    - 브라우저에 의해 제목처럼 보이도록 큰 글꼴로 스타일 지정됨

  ```html
  <span style="font-size: 32px;">Heading</span>
  ```

    - 모든 요소를 최상위 제목**"처럼"** 보이게 할 수는 있으나 **의미론적 가치는 없음**
  
- HTML Semantic Element

  - 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소

  - 검색엔진 및 개발자가 웹 페이지의 콘텐츠를 이해하기 쉽게 만들어줌

- "각자의 책임과 역할"

  - HTML ; 채워질 데이터를 나타내기 위한

  - CSS ; 어떻게 보여야 하는지

- 페이지 구조화를 위한 대표적인 semantic element

  - header

  - nav

  - main
  
  - article

  - section

  - aside

  - footer

- 의미론적 마크업 실습

  ```html
  <header>
    <h1>Header</h1>
  </header>
  <nav>
    <ul>
      <li><a href="#">Home</a></li>
    </ul>
  </nav>
  <main>
    <article>
      <h2>Article Title</h2>
      <p>Article content goes here ...</p>
    </article>
    <aside>
      <h3>Aside</h3>
      <ol>
        <li><a href="#">Lorem, ipsum.</a></li>
      </ol>
    </aside>
  </main>
  <footer>
    <p>&copy; All rights reserved.</p>
  </footer>
  ```

## 2. Semantics in CSS

### @ oocss 

- Object-Oriented CSS ; 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

- oocss 실습

  ```html
  <style>
    /*기본 카드 구조*/
    .card {
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 16px;
      width: 50%;
    }

    /*카드 제목*/
    .card-title {
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 8px;
    }

    /*카드 설명*/
    .card-description {
      font-size: 16px;
      margin-bottom: 16px;
    }

    /*기본 버튼 구조*/
    .btn {
      display: inline-block;
      border-radius: 4px;
      padding: 8px 16px;
      font-size: 1rem;
      font-weight: 400;
      color: #212529;
      text-align: center;
      text-decoration: none;
      cursor: pointer;
    }

    /*파란 배경*/
    .bg-blue {
      background-color: #007bff;
      color: #fff;
    }

    /*빨간 배경*/
    .bg-red {
      background-color: #cb2323;
      color: #fff;
    }
  </style>

  <body>
    <div class="card">
      <h2 class="card-title">Card Title</h2>
      <p class="card-description">This is a card description.</p>
      <button class="btn bg-blue">Learn More</button>
      <button class="btn bg-red">Learn More</button>
    </div>
  </body>
  ```

### @ BEM

- Block Element Modifier ; 블록, 요소, 수정자 사용해 클래스 이름을 구조화하는 방법론

- BEM 구성

  - Block

    - 문단 전체에 적용된 요소 또는 요소를 담고 있는 컨테이너

    - 재사용 가능한 독립적 블록, 가장 바깥쪽 상위 요소

    - 재사용을 위해 margin 또는 padding 적용 X

  - Element

    - block이 포함하고 있는 한 조각

    - 블록을 구성하는 종속적인 하위 요소

  - Modifier

    - block 또는 element의 속성

- BEM 실습

  ```html
  <head>
    <style>
      /*Block*/
      .block {
        display: flex;
        flex-direction: column;
        background-color: #eee;
        padding: 20px;
      }

      /*Element*/
      .block__title {
        font-size: 24px;
        margin-bottom: 10px;
      }

      .block__list {
        margin: 0;
        padding: 0;
      }

      .block__button {
        color: #fff;
        font-size: 16px;
        padding: 10px 20px;
      }

      /*Modifier*/
      .block__list--none {
        list-style: none;
      }

      .block__button--red {
        background-color: #ff0000;
      }
    </style>
  </head>
  <body>
    <div class="block">
      <h2 class="block__title">제목</h2>
      <ul class="block__list">
        <li class="block__list-item">항목 1</li>
        <li class="block__list-item">항목 2</li>
      </ul>
      <button class="block__button block__button--red">버튼
    </button>
    </div>
  </body>
  ```

## 참고

- 의미론적 마크업의 이점

  - 검색 엔진이 해당 웹사이트를 분석하기 쉽게 만들어 검색 순위에 영향

  - 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 때 추가적 도움

- 클래스 명의 길이

  - 클래스 이름이 무엇을 나타내는지 분명하게 전달하는 것이 가장 중요

  - 빠르고 명확한 표기를 우선적으로!

- OOCSS & BEM의 목적

  - 재사용 가능한 모듈로 분리함으로써 유지보수성과 확장성 향상

  - 개발자 간 협력 향상되어 공통 언어와 코드 이해 확립