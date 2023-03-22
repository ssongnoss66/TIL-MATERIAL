# 😏 1. Introduction of Web page

- Web ; "Web site"와 "Web page"를 포함하는 상위 개념

- Web site ; 여러 개의 "Web page"가 모여서 구성

- Web page ; "Web site"를 구성하는 하나의 요소

  - HTML "Structure"

  - CSS "Styling"

  - Javascript "Behaviour"

# 😝 2. Structuring the Web

## 2.1 Introduction to HTML

- HTML ; HyperText Markup Language 웹 페이지의 의미와 구조를 정의하는 언어

- Hypertext

  - 웹 페이지를 다른 페이지로 연결하는 링크

  - 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- Markup Language

  - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 (HTML, Markdown)

  - 예시

    ```html
    <h1>HTML</h1>
    <p>HTML이란 Hyper Text Markup Language의 약자이다.</p>

    <h2>Hyper Text.</h2>
    <p>Hyper Text란 기존의 선형적인 텍스트가 아닌 비선형적으로 이루어진 텍스트를 의미하며, 이는 인터넷의 등장과 함께 대두되었다. 기본적으로 Hyper Link를 통해 텍스트를 이동한다.</p>
    ```

## 2.2 Structure of HTML

- Element

  ![HTMLELEMENT](https://user-images.githubusercontent.com/121418205/220529841-4ad8df5e-29fc-45a0-b528-7084c5bda99e.JPG)

    - 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성

    - 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

- Attributes

  ![HTMLattributes](https://user-images.githubusercontent.com/121418205/220530088-156f1365-4860-475c-9cdc-8cfb43a80b73.jpg)

    - 규칙

      - 요소 이름 다음 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 함

      - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함

      - 속성 값은 열고 닫는 따옴표로 감싸야 함

    - 목적

      - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용

      - CSS가 해당 요소를 선택하기 위한 값으로 활용됨

- 문서 구조

  - ```<!DOCTYPE html>``` ; 해당 문서가 html로 문서라는 것을 나타냄

  - ```<html></html>``` ; 전체 페이지의 콘텐츠를 포함

  - ```<title></title>``` ; 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용

  - ```<head></head>``` ; HTML 문서에 관련된 설명, 설정 등 / 사용자에게 보이지 않음

  - ```<body></body>``` ; 페이지에 표시되는 모든 콘텐츠

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>My page</title>
    </head>
    <body>
      <p>This is my page</p>
    </body>
    </html>
    ```

- HTML 기본 Practice

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My page</title>
  </head>
  <body>
    <p>This is my page</p>
    <a href="https://www.google.co.kr/">Google로 이동</a>
    <img src ="images/sample.png" alt="sample-img">
    <img src="https://random.imagecdn.app/500/150/" alt="sample-img">
  </body>
  </html>
  ```

## 2.3 Text Structure

- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것

  ```html
  <h1>Main Heading</h1>
  ```

    - 단순히 텍스트를 크게 만드는 것이 아닌 **해당 문서의 최상위 제목**이라는 의미 부여

- Heading & Paragraphs ; h1~6, p

- Lists ; ol, ul, li

  - Unordered

  - Ordered

- Emphasis & Importance ; em, strong

- HTML Text Practice

  ```html
  <body>
    <h1>Main Heading</h1>
    <h2>Sub Heading</h2>
    <p>This is my page</p>
    <p>This is <em>emphasis</em></p>
    <p>Hi <strong>my name</strong> is Air</p>
    <ol>
      <li>파이썬</li>
      <li>알고리즘</li>
      <li>디비</li>
    </ol>
  </body>
  ```

# 😄 3. Styling the Web

## 3.1 Introduction to CSS

- CSS (Cascading Style Sheet) ; 웹 페이지의 디자인과 레이아웃을 구성하는 언어

- 구문

  ![css구문](https://user-images.githubusercontent.com/121418205/220536075-847b01c4-ded8-4818-816c-cc9b710a054c.jpg)

- 적용 방법

  1. 인라인(Inline) 스타일

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      ...
    </head>
    <body>
      <h1 style="color: blue; background-color: yellow;">Hello World!</h1>
    </body>
    </html>
    ```

  2. 내부(Internal) 스타일 시트

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      ... 
      <title>Document</title>
      <style>
        h1 {
          color: blue;
          background-color: yellow;
        }
      </style>
    </head>
    <body>
      <h1>Hello World!</h1>
    </body>
    </html>
    ```

  3. 외부(External) 스타일 시트 ; 별도의 CSS 파일 생성 후 불러오기

    ```html
    <!DOCTYPE html>
    <html lang=""en>
    <head>
      ... 
      <link rel="stylesheet" href="style.css">
    <title>Document</title>
    </head>
    <body>
      <h1>Hello World!</h1>
    </body>
    </html>

    /* style.css */

    h1 {
      color: blue;
      background-color: yellow;
    }
    ```

## 3.2 Select elements

- CSS Selectors ; HTML 요소를 선택하여 스타일을 적용할 수 있도록 함

- 종류

  - 기본 선택자

    - 전체(*) 선택자

    - 요소(tag) 선택자
    
      - 지정한 모든 태그 선택

    - 클래스(class) 선택자

      - 주어진 클래스 속성을 가진 모든 요소 선택

      - 예) .index는 class="index"를 가진 모든 요소 선택

    - 아이디(id) 선택자

      - 주어진 아이디 속성 가진 요소 선택
      
      - 문서에는 주어진 아이디를 가진 요소가 **하나만** 있어야 함

      - 예) #index는 id="index"를 가진 요소 선택

    - 속성(attr) 선택자

  - 결합자 (Combinators)

    - 자손 결합자 (" "(space))

      - 첫 번째 요소의 **자손 요소들** 선택

      - 예) p span은 ```<p>``` 안에 있는 모든 ```<span>```를 선택 (하위 레벨 상관 X)

    - 자식 결합자 (>)

      - 첫 번째 요소의 **직계 자식**만 선택

      - 예) ul > li은 ```<ul>``` 안에 있는 모든 ```<li>```를 선택 (한단계 아래 자식들만)

- CSS Selectors Practice

  ```html
  <body>
    <h1 class="green">Heading</h1>
    <h2>선택자 연습</h2>
    <h3>Hello</h3>
    <h4>Nice to meet you</h4>
    <p id="purple">과목 목록</p>
    <ul class="green">
      <li>파이썬</li>
      <li>알고리즘</li>
      <li>웹
        <ol>
          <li>HTML</li>
          <li>CSS</li>
          <li>JS</li>
        </ol>
      </li>
    </ul>
    <p class="green">Lorem, <span>ipsum</span> dolor.</p>
  </body>

  <style>
    /*전체 선택자*/
    * {
      color: red;
    }

    /*타입 선택자*/
    h2 {
      color: orange;
    }

    h3,
    h4 {
      color: blue;
    }

    /*클래스 선택자*/
    .green {
      color: green;
    }

    /*id 선택자*/
    #purple {
      color: purple;
    }

    /*자식 결합자*/
    .green > span {
      font-size: 50px;
    }

    /*자손 결합자*/
    .green li {
      color: brown;
    }
  </style>
  ```

  ![CSSselectorsPractice](https://user-images.githubusercontent.com/121418205/220540966-d8ac332f-5c1a-4ccd-858c-1c1506958a2c.jpg)

## 3.2 Cascade & Specificity

- 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성했을 때 어떤 규칙이 이기는 지 결정하는 것

- Cascade (계단식)

  - 동일한 우선순위를 갖는 규칙이 적용될 때 **CSS에서 마지막에 나오는 규칙**이 사용

    ```html
    h1 {
      color: red;
    }

    h1 {
      color: blue;
    }
    ```

      - 이 경우 h1 태그 내용의 색을 blue가 적용됨

- Specificity (우선순위)

  - 선택자별로 정해진 우선순위 점수에 따라 점수가 높은 규칙이 사용

    ```html
    .make-red {
      color: red;
    }

    h1 {
      color: blue;
    }
    ```

      - 이 경우 h1 태그 내용의 색은 red가 적용됨

  - 우선순위가 높은 순

    1. Importance ```!important``` ; Cascade 구조를 무시하고 모든 우선순위 점수 계산을 **무효화**

    2. 우선 순위 ; 인라인 스타일 > id 선택자 > class 선택자 > 요소 선택자

    3. 소스 코드 순서

  - 우선순위 practice

    ```html
    <html>
    <style>
    h2 {
      color: darkviolet !important;
    }

    p {
      color: orange;
    }

    .blue {
      color: blue;
    }

    .green {
      color: green;
    }

    #red {
      color: red;
    } 
    </style>
    <body>
    <p>1</p>
    <p class="blue">2</p>
    <p class="blue green">3</p>
    <p class="green blue">4</p>
    <p id="red" class="blue">5</p>
    <h2 id="red" class="blue">6</h2>
    <p id="red" class="blue" style="color: brown;">7</p>
    <h2 id="red" class="blue" style="color: brown;">8</h2>
    </body>
    </html>
    ```

- 상속

  - CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속하고 이를 이용해 코드의 **재사용성**을 높임

  - 상속되는 속성 ; Text 관련 요소 (font, color, text-align), opacity, visibility 등

  - 상속되지 않는 속성 ; Box model 관련 요소 (width, height, margin, padding, border, box-sizing, display), Position 관련 요소 (position, top/right/bottom/left, z-index) 등

  - 상속 practice

    ```html
    <html>
    <style>
      .parent {
        /* 상속 O */
        color: red;
        /* 상속 X */
        border: 1px solid black;
      }
    </style>
    <body>
      <ul class="parent">
        <li class="child">Hello</li>
        <li class="child">Bye</li>
      </ul>
    </body>
    </html>
    ```

    ![상속practice](https://user-images.githubusercontent.com/121418205/220547108-87584b9e-653c-4600-8667-ec980fda1f38.jpg)

# 🤔 참고

- HTML 관련 사항

  - HTML 요소 이름은 대소문자를 구분하지 않지만 **소문자** 사용 권장

  - HTML 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 **큰 따옴표** 권장

  - HTML은 프로그래밍 언어와 달리 **에러를 반환하지 않기** 때문에 작성 시 주의

- CSS 인라인 스타일 사용하지 말 것

  - 문서 유지보수 힘들어짐

  - CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드 이해 어렵게 만듦

- CSS 모든 속성 암기하는 것 아님 ; 주로 활용하는 속성 위주로 학습

- 속성은 되도록 class만 사용하도록 함

  - 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적 유지보수 어려워질 수 있음

  - 문서에서 단 한 번 유일하게 적용될 스타일의 경우에만 id 선택자 사용 고려

- CSS 상속 여부는 MDN 문서에서 확인 ; MDN 각 문서 하단에 속성별로 상속 여부 확인 가능