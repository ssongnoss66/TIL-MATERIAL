# 0223 THU

## 😕 구성요소

- **CSS Box Model**

  - 모든 HTML 요소를 (사각형) 박스로 표현

  - 박스에 대한 크기, 여백, 테두리 등의 스타일을 지정하는 디자인 개념

  - Box 구성

    ![box구성](https://user-images.githubusercontent.com/121418205/220822587-465ebe93-9567-4780-a20f-f6cdd337d861.png)


  - Box 구성의 방향 별 명칭

  ![box구성방향별명칭](https://user-images.githubusercontent.com/121418205/220822399-4a8ac0f4-ed10-42c3-a020-1836620d217d.png)

  - Box 요소 실습

    ```html
    <body>
      <div class="box1">box1</div>
      <div class="box2">box2</div>
    </body>

    .box1 {
      width: 300px;
      paddingleft: 25px;
      padding-bottom: 25px;
      margin-left: 25px;
      margin-top: 50px;
      border-width: 3px;
      border-color: black;
      border-style: solid;
    }

    .box2 {
      width: 300px;
      padding: 25px 50px;
      margin: 25px auto;
      border: 1px dashed black;
    }
    ```

- **width & height** 속성

  - 요소의 너비와 높이를 지정

  - 이때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함

    ![widthheight](https://user-images.githubusercontent.com/121418205/220823365-2d7289e9-5d62-4c26-b8ad-687a488eab14.png)

- **box-sizing** 속성

  - 요소의 너비와 높이를 계산하는 방법을 지정

    ![boxsizing](https://user-images.githubusercontent.com/121418205/220823452-1e954128-b65a-416f-8a93-65da7c3a056a.png)

    ```html
    /*왼쪽*/

    * {
      box-sizing: content-box;
    }

    /*오른쪽*/

    * {
      box-sizing: border-box;
    }
    ```

  - box-sizing 실습

    ```html
    <body>
      <div class="box content-box">content-box</div>
      <div class="box border-box">border-box</div>
    </body>

    .box {
      width: 100px;
      border: 2px solid black;
      apdding: 10px;
      margin: 20px;
      background-color: lightgray;
    }

    .content-box {
      box-sizing: content-box;
    }

    .border-box {
      box-sizing: border-box;
    }
    ```

## 😗 박스타입

- Block & Inline

  ```html
  /*Block*/

  .index {
    display: block;
  }

  /*Inline*/

  .index {
    display: inline;
  }
  ```

  - Normal Flow ; CSS 적용하지 않았을 경우 Block 및 Inline 요소가 기본적으로 배치되는 방향

  - Block 타입 특징

    - 항상 새로운 행으로 나뉨

    - width와 height 속성을사용하여 너비와 높이 지정 가능

    - width 속성 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함 (너비를 사용가능한 공간의 100%로 채우는 것)

    - 태그 ; h1~6, p, div
  
  - Inline 타입 특징

    - 새로운 행으로 나뉘지 않음

    - width와 height 속성을 사용할 수 없음

    - 수직 방향 ; padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음

    - 수평 방향 ; padding, margins, borders가 적용되어 다른 요소 밀어낼 수 있음

    - 태그 ; a, img, span

  - 박스 타입 실습

    ```html
    <!DOCTYPE html>
    <html>
    <style>
      a,
      span,
      img {
        border: 1px solid red;
      }

      h1,
      p,
      div {
        border: 1px solid blue;
      }
    </style>
    <body>
      <h1>Normal flow</h1>
      <p>Lorem, imsum dolor sit amet consect explicabo?</p>
      <div>
        <p>block 요소는 기본적으로 부모 요소의 너비 100% 차지, 자식 콘텐츠의 최대 높이 취함</p>
        <p>block 요소의 총 너비와 총 높이는 content + padding + borderwidth/height</p>
      </div>
      <p>block 요소는 서로 margins로 구분</p>
      <p>inline 요소는 <span>이처럼</span> 자체 콘텐츠의 너비와 높이만 차지
        그리고 inline 요소는 <a href="#">width나 height 속성 지정 불가</a>
      </p>
      <p>
        이미지도 <img src="#" alt="#"> 인라인 요소
        이미지는 다른 inline 요소와 달리 width나 height로 크기 조정 가능
      </p>
      <p>
        inline 요소의 크기 제어하려면 block 요소로 변경하거나 inline-block 요소로 설정해줘야 함
      </p>
    </body>
    </html>
    ```

## 😑 참고

- shorthand 속성

  - border ; border-width, border-style, border-color를 한번에 설정하기 위한 속성

    ```html
    /*순서는 영향을 주지 않음*/
    border: 1px solid black;
    ```

  - margin & padding ; 4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성

    ```html
    /*4개 상우하좌*/
    margin: 10px 20px 30px 40px;
    padding: 10px 20px 30px 40px;

    /*3개 상/좌우/하*/
    margin: 10px 20px 30px;
    padding: 10px 20px 30px;

    /*2개 상하/좌우*/
    margin: 10px 20px;
    padding: 10px 20px;

    /*1개 공통*/
    margin: 10px;
    padding: 10px;
    ```

- display ; inline-block

  - inline과 block 요소 사이의 중간 지점을 제공하는 display 값

  - 요소가 줄바꿈되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용

  - block 요소의 특징을 가짐

    - 너비 및 높이 속성 준수

    - 패딩, 여백 미 네두리로 인해 다른 요소가 상자에서 밀려납니다

- Margin Collapsing (마진 상쇄)

  - 두 block 타입 요소의 martin top과  bottom이 만나 큰 margin으로 결합되는 현상
  
  - 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함 ; 각 요소에 대한 상/하 margin을 각각 설정하지 않고 한 요소에 대해서만 설정할 수 있음

    ![MarginCollapsing](https://user-images.githubusercontent.com/121418205/220829732-9e7fb1a2-92d8-43b2-bac2-288cbf183278.png)