# 0228 TUE

## 😎 Web ; Floating for CSS layout

### @ CSS Float

- 요소를 **띄워서** 텍스트 및 인라인 요소가 그 주위를 감싸도록 하는 배치 ; 왼쪽 혹은 오른쪽으로 띄워 Normal flow에서 벗어남

- 탄생 배경

  - 텍스트 열 내부에 떠다니는 이미지를 포함하면서도 해당 이미지의 좌우에 텍스트를 둘러싸는 간단한 레이아웃을 구현하기 위해 도입 ex) 신문 레이아웃

  - 원래 목적에서 더 나아가 웹 페이지 전체 레이아웃 구성하는 데 사용되었으나 Felxbox와 Grid의 등장으로 인해 원래 목적으로 돌아감

- 실습

  ```html
  <style>
    .box {
      width: 10rem;
      height: 10rem;
      border: 1px solid black;
      background-color: lightcoral;
    }

    .float-left {
      float: left;
    }

    .float-right {
      float: right;
    }
  </style>

  <body>
    <div class="box float-left">float left</div>
    <p>...</p>
    <div class="box float-right">float right</div>
    <p>...</p>
  </body>
  ```

## 🤯 Web ; Flexible box for CSS layout

### @ CSS Flexbox

- 요소를 행과 열 형태로 배치하는 **1차원** 레이아웃 방식

- 요소 간 **'공간 배열'과 '정렬'**

  ![CSSflexbox](https://user-images.githubusercontent.com/121418205/222118484-f85ba649-7d8f-4fce-819f-b41387dd7065.png)

- 기본 사항

  ![CSSflexbox기본사항](https://user-images.githubusercontent.com/121418205/222118637-55bf8fdb-0420-4af2-9e01-fd5fbe1b41e3.png)

  - Main Axis (주 축)

    - flex item들이 배치되는 기본 축

    - main satrt에서 시작하여 main end 방향으로 배치

  - Cross Axis (교차 축)

    - main axis에 수직인 축

    - cross start에서 시작하여 cross end 방향으로 배치

  - Flex Container

    - display: flex; 혹은 display: inline-flex;가 설정된 부모 요소

    - 이 컨테이너의 1차 자식 요소들이 flex item이 됨
    
    - flexbox 속성 값들을 사용하여 자식 요소 flex item들을 배치

  - Flex Item

    - flex container 내부에 레이아웃되는 항목

- Flexbox 속성

  - Flex Container 관련 속성

    [1] Flex Container 지정

      - flex item은 행으로 나열

      - flex item은 주축의 시작 선에서 시작

      - flex item은 교차축의 크기를 채우기 위해 늘어남

        ```html
        <style>
        .container {
          height: 500px;
          border: 1px solid black;
          display: flex;
        }
        ```

        ![FlexContainer지정](https://user-images.githubusercontent.com/121418205/222121436-e8d7ba73-ecef-4e8d-aa36-6aaa4ba96a0d.png)

    [2] flex-direction 지정

      - flex item이 나열되는 방향 지정

      - column으로 지정할 경우 주 축이 변경됨

      - -reverse로 지정하면 시작 선과 끝 선이 서로 바뀜

        ```html
        <style>
        .container {
          /*flex-direction: row;*/
          flex-direction: column;
          /*flex-direction: row-reverse;*/
          /*flex-direction: column-reverse;*/
        }
        ```

        ![FlexDirection지정](https://user-images.githubusercontent.com/121418205/222121983-9a9cd258-843c-459a-bcb2-212ea1061a59.png)

    [3] flex-wrap

      - flex item 목록이 flex container의 하나의 행에 들어가지 않을 경우 다른 행에 배치 여부 설정

        ```html
        <style>
        .container {
          /*flex-wrap: nowrap;*/
          flex-wrap: wrap;
        }
        ```

        ![FlexWrap지정](https://user-images.githubusercontent.com/121418205/222122359-0b112635-0ada-4c9a-845d-7b79562db1e9.png)

    [4] justify-content

      - 주 축을 따라 flex item과 주위에 공간을 분배

        ```html
        <style>
        .container {
          /*justify-content: flex-start;*/
          justify-content: center;
          /*justify-content: flex-end;*/
        }
        ```

          ![justifycontent](https://user-images.githubusercontent.com/121418205/222122996-2ccec9f8-bad9-4f52-81e1-f6ed5e214ea1.png)

    [5] align-content

      - 교차 축을 따라 flex item과 주위 공간 분배

      - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨

      - 한줄짜리 행에는 (flex-wrap이 nowrap으로 설정된 경우) 효과 없음

        ```html
        <style>
        .container {
          flex-wrap: wrap;

          /*align-content: flex-satrt;*/
          align-content: center;
          /*align-content: flex-end;*/
        }
        ```

        ![aligncontent](https://user-images.githubusercontent.com/121418205/222123572-449634c7-d6cb-432f-9ea3-acf1333f7176.png)

    [6] align-items

      - 교차 축을 따라 flex item을 정렬

        ```html
        <style>
        .container {
          align-items: center;
        }
        ```

        ![alignitems](https://user-images.githubusercontent.com/121418205/222123872-cf9c6ba1-722a-4b34-a7c8-758c7c1875d9.png)

  - Flex Item 관련 속성

    [7] align-self

      - 교차 축을 따라 개별 flex item을 정렬

        ```html
        <style>
        .item1 {
          align-self: center;
        }

        .item2 {
          align-self: flex-end;
        }
        ```

        ![alignself](https://user-images.githubusercontent.com/121418205/222124165-f7f5c1f7-a92b-4224-8b27-4c9e2ab79582.png)

    [8] flex-grow (flex-shrink)

      - 남는 행 여백을 비율에 따라 각 flex item에 분배

      - flex-grow의 반대는 flex-shrink ; 넘치는 너비를 분배해서 줄임

        ```html
        <style>
          .container {
            display: flex;
            width: 100%;
          }

          .item {
            height: 100px;
            color: white;
            font-size: 3rem;
          }

          .item-1 {
            background-color: red;
            flex-grow: 1;
          }

          .item-2 {
            background-color: green;
            flex-grow: 2;
          }

          .item-3 {
            background-color: blue;
            flex-grow: 3;
          }
        </style>

        <body>
          <div class="container">
            <div class="item item-1">1</div>
            <div class="item item-2">2</div>
            <div class="item item-3">3</div>
          </div>
        </body>
        ```

        ![flexgrow](https://user-images.githubusercontent.com/121418205/222128064-e58c26a5-f591-4e76-a54c-d815ea143a56.png)

        ![flexgrow2](https://user-images.githubusercontent.com/121418205/222128192-1a880d5e-1b44-4597-a8f1-8775350a4f08.png)

    [9] flex-basis

      - flex item의 초기 크기 값 지정

      - flex-basis와 width 값을 동시에 적용한 경우 flex-basis가 우선

        ```html
        <style>
          .container {
            display: flex;
            width: 100%;
          }

          .item {
            height: 100px;
            color: white;
            font-size: 3rem;
          }

          .item-1 {
            background-color: red;
            flex-basis: 300px;
          }

          .item-2 {
            background-color: green;
            flex-basis: 600px;
          }

          .item-3 {
            background-color: blue;
            flex-basis; 300px;
          }
        </style>

        <body>
          <div class="container">
            <div class="item item-1">1</div>
            <div class="item item-2">2</div>
            <div class="item item-3">3</div>
        </body>
        ```

        ![flexbasis](https://user-images.githubusercontent.com/121418205/222129973-41c6cea8-4d07-4ff2-b3c2-3628e6100464.png)

    [목적에 따른 분류]

      - 배치 설정 ; flex-direction / flex-wrap

      - 공간 분배 ; justify-content / align-content

      - 정렬 ; align-items / align-self

    [속성명 TIP]

      - justify 주축

      - align 교차축

- Flexbox 반응형 레이아웃 ; flex-wrap을 사용해 반응형 레이아웃 작성 (flex-grow & flex-basis)

  ```html
  <style>
    .card {
      width: 80%;
      border: 1px solid black;
      /* 1 */
      display: flex;
      /* 2 */
      flex-wrap: wrap;
    }

    img {
      width; 100%
    }

    .thumbnail {
      /* 3 */
      flex-basis: 700px;
      /* 4 */
      flex-grow: 1;
      /* flex: 1 700px */
    }

    .content {
      /* 3 */
      flex-basis: 350px;
      /* 4 */
      flex-grow: 1;
      /* flex: 1 350px; */
    }
  </style>

  <body>
    <div class="card">
      <img class="thumbnail" src="#" alt="#">
      <div class="content">
        <h2>Heading</h2>
        <p>..</p>
      </div>
    </div>
  </body>
  ```

  ![반응형레이아웃](https://user-images.githubusercontent.com/121418205/222131720-fd5f68d5-84ae-46c8-8e50-3a84c9f9a9e3.png)

### @ 참고

- flex-direction

  ![flexdirection](https://user-images.githubusercontent.com/121418205/222133606-37a0ce21-08b7-4c67-ab56-2879a429a732.png)

- flex-wrap

  ![flexwrap](https://user-images.githubusercontent.com/121418205/222133603-f79bf7af-3df8-446d-919e-dec596ba970d.png)

- justify-content

  ![justifycontent2](https://user-images.githubusercontent.com/121418205/222133601-75d2e9fd-59d0-4af7-862c-6e479dbf4a97.png)

- align-content

  ![aligncontent2](https://user-images.githubusercontent.com/121418205/222133595-66f8a761-1241-4b58-b131-4e3cba555abe.png)

- align-items

  ![alignitems2](https://user-images.githubusercontent.com/121418205/222133591-50302d38-2dee-4568-8c05-5c7bbf7e3a05.png)

- align-self

  ![alignself2](https://user-images.githubusercontent.com/121418205/222133585-185a7038-8d76-4d31-b89d-710f650ad8b1.png)

- justify-items 및 justify-self 속성이 없는 이유

  - 필요없기 때문

  - margin auto 통해 정렬 및 배치 가능

- Shorthand 

  - "flex-flow"

    ```html
    <style>
      .container {
        flex-flow: flex-direction flex-wrap;
      }
    ```

  - "flex"

    ```html
    <style>
      /* One value, unitless number: flex-grow */
      flex: 2;

      /* One value, length or percentage: flex-basis */
      flex: 10rem;
      flex: 30%;

      /* Two values: flex-grow : flex-basis */
      flex: 1 30px;

      /* Two values: flex-grow : flex-shrink */
      flex: 2 2;

      /* Three values: flex-grow : flex-shrink : flex-basis */
      flex: 2 2 10%
      ```