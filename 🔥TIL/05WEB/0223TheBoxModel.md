# 0223 THU

## ๐ ๊ตฌ์ฑ์์

- **CSS Box Model**

  - ๋ชจ๋  HTML ์์๋ฅผ (์ฌ๊ฐํ) ๋ฐ์ค๋ก ํํ

  - ๋ฐ์ค์ ๋ํ ํฌ๊ธฐ, ์ฌ๋ฐฑ, ํ๋๋ฆฌ ๋ฑ์ ์คํ์ผ์ ์ง์ ํ๋ ๋์์ธ ๊ฐ๋

  - Box ๊ตฌ์ฑ

    ![boxแแฎแแฅแผ](https://user-images.githubusercontent.com/121418205/220822587-465ebe93-9567-4780-a20f-f6cdd337d861.png)


  - Box ๊ตฌ์ฑ์ ๋ฐฉํฅ ๋ณ ๋ช์นญ

  ![boxแแฎแแฅแผแแกแผแแฃแผแแงแฏแแงแผแแตแผ](https://user-images.githubusercontent.com/121418205/220822399-4a8ac0f4-ed10-42c3-a020-1836620d217d.png)

  - Box ์์ ์ค์ต

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

- **width & height** ์์ฑ

  - ์์์ ๋๋น์ ๋์ด๋ฅผ ์ง์ 

  - ์ด๋ ์ง์ ๋๋ ์์์ ๋๋น์ ๋์ด๋ ์ฝํ์ธ  ์์ญ์ ๋์์ผ๋ก ํจ

    ![widthheight](https://user-images.githubusercontent.com/121418205/220823365-2d7289e9-5d62-4c26-b8ad-687a488eab14.png)

- **box-sizing** ์์ฑ

  - ์์์ ๋๋น์ ๋์ด๋ฅผ ๊ณ์ฐํ๋ ๋ฐฉ๋ฒ์ ์ง์ 

    ![boxsizing](https://user-images.githubusercontent.com/121418205/220823452-1e954128-b65a-416f-8a93-65da7c3a056a.png)

    ```html
    /*์ผ์ชฝ*/

    * {
      box-sizing: content-box;
    }

    /*์ค๋ฅธ์ชฝ*/

    * {
      box-sizing: border-box;
    }
    ```

  - box-sizing ์ค์ต

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

## ๐ ๋ฐ์คํ์

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

  - Normal Flow ; CSS ์ ์ฉํ์ง ์์์ ๊ฒฝ์ฐ Block ๋ฐ Inline ์์๊ฐ ๊ธฐ๋ณธ์ ์ผ๋ก ๋ฐฐ์น๋๋ ๋ฐฉํฅ

  - Block ํ์ ํน์ง

    - ํญ์ ์๋ก์ด ํ์ผ๋ก ๋๋จ

    - width์ height ์์ฑ์์ฌ์ฉํ์ฌ ๋๋น์ ๋์ด ์ง์  ๊ฐ๋ฅ

    - width ์์ฑ ์ง์ ํ์ง ์์ผ๋ฉด ๋ฐ์ค๋ inline ๋ฐฉํฅ์ผ๋ก ์ฌ์ฉ ๊ฐ๋ฅํ ๊ณต๊ฐ์ ๋ชจ๋ ์ฐจ์งํจ (๋๋น๋ฅผ ์ฌ์ฉ๊ฐ๋ฅํ ๊ณต๊ฐ์ 100%๋ก ์ฑ์ฐ๋ ๊ฒ)

    - ํ๊ทธ ; h1~6, p, div
  
  - Inline ํ์ ํน์ง

    - ์๋ก์ด ํ์ผ๋ก ๋๋์ง ์์

    - width์ height ์์ฑ์ ์ฌ์ฉํ  ์ ์์

    - ์์ง ๋ฐฉํฅ ; padding, margins, borders๊ฐ ์ ์ฉ๋์ง๋ง ๋ค๋ฅธ ์์๋ฅผ ๋ฐ์ด๋ผ ์๋ ์์

    - ์ํ ๋ฐฉํฅ ; padding, margins, borders๊ฐ ์ ์ฉ๋์ด ๋ค๋ฅธ ์์ ๋ฐ์ด๋ผ ์ ์์

    - ํ๊ทธ ; a, img, span

  - ๋ฐ์ค ํ์ ์ค์ต

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
        <p>block ์์๋ ๊ธฐ๋ณธ์ ์ผ๋ก ๋ถ๋ชจ ์์์ ๋๋น 100% ์ฐจ์ง, ์์ ์ฝํ์ธ ์ ์ต๋ ๋์ด ์ทจํจ</p>
        <p>block ์์์ ์ด ๋๋น์ ์ด ๋์ด๋ content + padding + borderwidth/height</p>
      </div>
      <p>block ์์๋ ์๋ก margins๋ก ๊ตฌ๋ถ</p>
      <p>inline ์์๋ <span>์ด์ฒ๋ผ</span> ์์ฒด ์ฝํ์ธ ์ ๋๋น์ ๋์ด๋ง ์ฐจ์ง
        ๊ทธ๋ฆฌ๊ณ  inline ์์๋ <a href="#">width๋ height ์์ฑ ์ง์  ๋ถ๊ฐ</a>
      </p>
      <p>
        ์ด๋ฏธ์ง๋ <img src="#" alt="#"> ์ธ๋ผ์ธ ์์
        ์ด๋ฏธ์ง๋ ๋ค๋ฅธ inline ์์์ ๋ฌ๋ฆฌ width๋ height๋ก ํฌ๊ธฐ ์กฐ์  ๊ฐ๋ฅ
      </p>
      <p>
        inline ์์์ ํฌ๊ธฐ ์ ์ดํ๋ ค๋ฉด block ์์๋ก ๋ณ๊ฒฝํ๊ฑฐ๋ inline-block ์์๋ก ์ค์ ํด์ค์ผ ํจ
      </p>
    </body>
    </html>
    ```

## ๐ ์ฐธ๊ณ 

- shorthand ์์ฑ

  - border ; border-width, border-style, border-color๋ฅผ ํ๋ฒ์ ์ค์ ํ๊ธฐ ์ํ ์์ฑ

    ```html
    /*์์๋ ์ํฅ์ ์ฃผ์ง ์์*/
    border: 1px solid black;
    ```

  - margin & padding ; 4๋ฐฉํฅ์ ์์ฑ์ ๊ฐ๊ฐ ์ง์ ํ์ง ์๊ณ  ํ๋ฒ์ ์ง์ ํ  ์ ์๋ ์์ฑ

    ```html
    /*4๊ฐ ์์ฐํ์ข*/
    margin: 10px 20px 30px 40px;
    padding: 10px 20px 30px 40px;

    /*3๊ฐ ์/์ข์ฐ/ํ*/
    margin: 10px 20px 30px;
    padding: 10px 20px 30px;

    /*2๊ฐ ์ํ/์ข์ฐ*/
    margin: 10px 20px;
    padding: 10px 20px;

    /*1๊ฐ ๊ณตํต*/
    margin: 10px;
    padding: 10px;
    ```

- display ; inline-block

  - inline๊ณผ block ์์ ์ฌ์ด์ ์ค๊ฐ ์ง์ ์ ์ ๊ณตํ๋ display ๊ฐ

  - ์์๊ฐ ์ค๋ฐ๊ฟ๋๋ ๊ฒ์ ์ํ์ง ์์ผ๋ฉด์ ๋๋น์ ๋์ด๋ฅผ ์ ์ฉํ๊ณ  ์ถ์ ๊ฒฝ์ฐ์ ์ฌ์ฉ

  - block ์์์ ํน์ง์ ๊ฐ์ง

    - ๋๋น ๋ฐ ๋์ด ์์ฑ ์ค์

    - ํจ๋ฉ, ์ฌ๋ฐฑ ๋ฏธ ๋ค๋๋ฆฌ๋ก ์ธํด ๋ค๋ฅธ ์์๊ฐ ์์์์ ๋ฐ๋ ค๋ฉ๋๋ค

- Margin Collapsing (๋ง์ง ์์)

  - ๋ block ํ์ ์์์ martin top๊ณผ  bottom์ด ๋ง๋ ํฐ margin์ผ๋ก ๊ฒฐํฉ๋๋ ํ์
  
  - ์น ๊ฐ๋ฐ์๊ฐ ๋ ์ด์์์ ๋์ฑ ์ฝ๊ฒ ๊ด๋ฆฌํ  ์ ์๋๋ก ํจ ; ๊ฐ ์์์ ๋ํ ์/ํ margin์ ๊ฐ๊ฐ ์ค์ ํ์ง ์๊ณ  ํ ์์์ ๋ํด์๋ง ์ค์ ํ  ์ ์์

    ![MarginCollapsing](https://user-images.githubusercontent.com/121418205/220829732-9e7fb1a2-92d8-43b2-bac2-288cbf183278.png)