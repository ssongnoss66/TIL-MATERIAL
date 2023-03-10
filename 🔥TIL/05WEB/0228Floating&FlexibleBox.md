# 0228 TUE

## ๐ Web ; Floating for CSS layout

### @ CSS Float

- ์์๋ฅผ **๋์์** ํ์คํธ ๋ฐ ์ธ๋ผ์ธ ์์๊ฐ ๊ทธ ์ฃผ์๋ฅผ ๊ฐ์ธ๋๋ก ํ๋ ๋ฐฐ์น ; ์ผ์ชฝ ํน์ ์ค๋ฅธ์ชฝ์ผ๋ก ๋์ Normal flow์์ ๋ฒ์ด๋จ

- ํ์ ๋ฐฐ๊ฒฝ

  - ํ์คํธ ์ด ๋ด๋ถ์ ๋ ๋ค๋๋ ์ด๋ฏธ์ง๋ฅผ ํฌํจํ๋ฉด์๋ ํด๋น ์ด๋ฏธ์ง์ ์ข์ฐ์ ํ์คํธ๋ฅผ ๋๋ฌ์ธ๋ ๊ฐ๋จํ ๋ ์ด์์์ ๊ตฌํํ๊ธฐ ์ํด ๋์ ex) ์ ๋ฌธ ๋ ์ด์์

  - ์๋ ๋ชฉ์ ์์ ๋ ๋์๊ฐ ์น ํ์ด์ง ์ ์ฒด ๋ ์ด์์ ๊ตฌ์ฑํ๋ ๋ฐ ์ฌ์ฉ๋์์ผ๋ Felxbox์ Grid์ ๋ฑ์ฅ์ผ๋ก ์ธํด ์๋ ๋ชฉ์ ์ผ๋ก ๋์๊ฐ

- ์ค์ต

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

## ๐คฏ Web ; Flexible box for CSS layout

### @ CSS Flexbox

- ์์๋ฅผ ํ๊ณผ ์ด ํํ๋ก ๋ฐฐ์นํ๋ **1์ฐจ์** ๋ ์ด์์ ๋ฐฉ์

- ์์ ๊ฐ **'๊ณต๊ฐ ๋ฐฐ์ด'๊ณผ '์ ๋ ฌ'**

  ![CSSflexbox](https://user-images.githubusercontent.com/121418205/222118484-f85ba649-7d8f-4fce-819f-b41387dd7065.png)

- ๊ธฐ๋ณธ ์ฌํญ

  ![CSSflexboxแแตแแฉแซแแกแแกแผ](https://user-images.githubusercontent.com/121418205/222118637-55bf8fdb-0420-4af2-9e01-fd5fbe1b41e3.png)

  - Main Axis (์ฃผ ์ถ)

    - flex item๋ค์ด ๋ฐฐ์น๋๋ ๊ธฐ๋ณธ ์ถ

    - main satrt์์ ์์ํ์ฌ main end ๋ฐฉํฅ์ผ๋ก ๋ฐฐ์น

  - Cross Axis (๊ต์ฐจ ์ถ)

    - main axis์ ์์ง์ธ ์ถ

    - cross start์์ ์์ํ์ฌ cross end ๋ฐฉํฅ์ผ๋ก ๋ฐฐ์น

  - Flex Container

    - display: flex; ํน์ display: inline-flex;๊ฐ ์ค์ ๋ ๋ถ๋ชจ ์์

    - ์ด ์ปจํ์ด๋์ 1์ฐจ ์์ ์์๋ค์ด flex item์ด ๋จ
    
    - flexbox ์์ฑ ๊ฐ๋ค์ ์ฌ์ฉํ์ฌ ์์ ์์ flex item๋ค์ ๋ฐฐ์น

  - Flex Item

    - flex container ๋ด๋ถ์ ๋ ์ด์์๋๋ ํญ๋ชฉ

- Flexbox ์์ฑ

  - Flex Container ๊ด๋ จ ์์ฑ

    [1] Flex Container ์ง์ 

      - flex item์ ํ์ผ๋ก ๋์ด

      - flex item์ ์ฃผ์ถ์ ์์ ์ ์์ ์์

      - flex item์ ๊ต์ฐจ์ถ์ ํฌ๊ธฐ๋ฅผ ์ฑ์ฐ๊ธฐ ์ํด ๋์ด๋จ

        ```html
        <style>
        .container {
          height: 500px;
          border: 1px solid black;
          display: flex;
        }
        ```

        ![FlexContainerแแตแแฅแผ](https://user-images.githubusercontent.com/121418205/222121436-e8d7ba73-ecef-4e8d-aa36-6aaa4ba96a0d.png)

    [2] flex-direction ์ง์ 

      - flex item์ด ๋์ด๋๋ ๋ฐฉํฅ ์ง์ 

      - column์ผ๋ก ์ง์ ํ  ๊ฒฝ์ฐ ์ฃผ ์ถ์ด ๋ณ๊ฒฝ๋จ

      - -reverse๋ก ์ง์ ํ๋ฉด ์์ ์ ๊ณผ ๋ ์ ์ด ์๋ก ๋ฐ๋

        ```html
        <style>
        .container {
          /*flex-direction: row;*/
          flex-direction: column;
          /*flex-direction: row-reverse;*/
          /*flex-direction: column-reverse;*/
        }
        ```

        ![FlexDirectionแแตแแฅแผ](https://user-images.githubusercontent.com/121418205/222121983-9a9cd258-843c-459a-bcb2-212ea1061a59.png)

    [3] flex-wrap

      - flex item ๋ชฉ๋ก์ด flex container์ ํ๋์ ํ์ ๋ค์ด๊ฐ์ง ์์ ๊ฒฝ์ฐ ๋ค๋ฅธ ํ์ ๋ฐฐ์น ์ฌ๋ถ ์ค์ 

        ```html
        <style>
        .container {
          /*flex-wrap: nowrap;*/
          flex-wrap: wrap;
        }
        ```

        ![FlexWrapแแตแแฅแผ](https://user-images.githubusercontent.com/121418205/222122359-0b112635-0ada-4c9a-845d-7b79562db1e9.png)

    [4] justify-content

      - ์ฃผ ์ถ์ ๋ฐ๋ผ flex item๊ณผ ์ฃผ์์ ๊ณต๊ฐ์ ๋ถ๋ฐฐ

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

      - ๊ต์ฐจ ์ถ์ ๋ฐ๋ผ flex item๊ณผ ์ฃผ์ ๊ณต๊ฐ ๋ถ๋ฐฐ

      - flex-wrap์ด wrap ๋๋ wrap-reverse๋ก ์ค์ ๋ ์ฌ๋ฌ ํ์๋ง ์ ์ฉ๋จ

      - ํ์ค์ง๋ฆฌ ํ์๋ (flex-wrap์ด nowrap์ผ๋ก ์ค์ ๋ ๊ฒฝ์ฐ) ํจ๊ณผ ์์

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

      - ๊ต์ฐจ ์ถ์ ๋ฐ๋ผ flex item์ ์ ๋ ฌ

        ```html
        <style>
        .container {
          align-items: center;
        }
        ```

        ![alignitems](https://user-images.githubusercontent.com/121418205/222123872-cf9c6ba1-722a-4b34-a7c8-758c7c1875d9.png)

  - Flex Item ๊ด๋ จ ์์ฑ

    [7] align-self

      - ๊ต์ฐจ ์ถ์ ๋ฐ๋ผ ๊ฐ๋ณ flex item์ ์ ๋ ฌ

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

      - ๋จ๋ ํ ์ฌ๋ฐฑ์ ๋น์จ์ ๋ฐ๋ผ ๊ฐ flex item์ ๋ถ๋ฐฐ

      - flex-grow์ ๋ฐ๋๋ flex-shrink ; ๋์น๋ ๋๋น๋ฅผ ๋ถ๋ฐฐํด์ ์ค์

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

      - flex item์ ์ด๊ธฐ ํฌ๊ธฐ ๊ฐ ์ง์ 

      - flex-basis์ width ๊ฐ์ ๋์์ ์ ์ฉํ ๊ฒฝ์ฐ flex-basis๊ฐ ์ฐ์ 

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

    [๋ชฉ์ ์ ๋ฐ๋ฅธ ๋ถ๋ฅ]

      - ๋ฐฐ์น ์ค์  ; flex-direction / flex-wrap

      - ๊ณต๊ฐ ๋ถ๋ฐฐ ; justify-content / align-content

      - ์ ๋ ฌ ; align-items / align-self

    [์์ฑ๋ช TIP]

      - justify ์ฃผ์ถ

      - align ๊ต์ฐจ์ถ

- Flexbox ๋ฐ์ํ ๋ ์ด์์ ; flex-wrap์ ์ฌ์ฉํด ๋ฐ์ํ ๋ ์ด์์ ์์ฑ (flex-grow & flex-basis)

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

  ![แแกแซแแณแผแแงแผแแฆแแตแแกแแฎแบ](https://user-images.githubusercontent.com/121418205/222131720-fd5f68d5-84ae-46c8-8e50-3a84c9f9a9e3.png)

### @ ์ฐธ๊ณ 

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

- justify-items ๋ฐ justify-self ์์ฑ์ด ์๋ ์ด์ 

  - ํ์์๊ธฐ ๋๋ฌธ

  - margin auto ํตํด ์ ๋ ฌ ๋ฐ ๋ฐฐ์น ๊ฐ๋ฅ

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