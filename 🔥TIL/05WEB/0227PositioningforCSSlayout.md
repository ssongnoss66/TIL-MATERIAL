# 0227 MON

## ๐ Web - Positioning for CSS layout

- CSS Layout ; ๊ฐ ์์์ ์์น์ ํฌ๊ธฐ๋ฅผ ์กฐ์ ํ์ฌ ์น ํ์ด์ง์ ๋์์ธ์ ๊ฒฐ์ ํ๋ ๊ฒ (Position)

### @ Position

- CSS Position ; Normal Flow(CSS ์ ์ฉํ์ง ์์์ ๊ฒฝ์ฐ ์นํ์ด์ง ์์๊ฐ ๊ธฐ๋ณธ์ ์ผ๋ก ๋ฐฐ์น๋๋ ๋ฐฉํฅ)์์ ์์๋ฅผ ๋์ง์ด๋ด์ ๋ค๋ฅธ ์์น๋ก ๋ฐฐ์นํ๋ ๊ฒ 

  - ๋ค๋ฅธ ์์ ์์ ๋๊ธฐ, ํ๋ฉด ํน์  ์์น์ ๊ณ ์ ์ํค๊ธฐ ๋ฑ

  - ์ ์ฒด ํ์ด์ง ๋ ์ด์์ ๊ตฌ์ฑํ๋ ๊ฒ์ด ์๋๋ผ **ํ์ด์ง์ ํน์  ํญ๋ชฉ์ ์์น๋ฅผ ์กฐ์ ํ๋ ๊ฒ**๊ณผ ๊ด๋ จ๋์ด ์๋ค

- Position ์ด๋ ๋ฐฉํฅ

  ![แแฉแแตแแงแซแแตแแฉแผแแกแผแแฃแผ](https://user-images.githubusercontent.com/121418205/221449108-52ee2f2d-f6bc-4902-84af-969d46c7a78b.png)

- Position ์ ํ

  - static

    - ๊ธฐ๋ณธ๊ฐ

    - ์์๋ฅผ Normal Flow์ ๋ฐ๋ผ ๋ฐฐ์น

  - relative

    - ์์๋ฅผ Normal Flow์ ๋ฐ๋ผ ๋ฐฐ์น

    - ์๊ธฐ ์์ ์ ๊ธฐ์ค์ผ๋ก ์ด๋

    - ์์๊ฐ ์ฐจ์งํ๋ ๊ณต๊ฐ์ **static์ผ ๋์ ๊ฐ์**

  - absolute

    - ์์๋ฅผ Normal Flow์์ ์ ๊ฑฐ

    - ๊ฐ์ฅ ๊ฐ๊น์ด relative ๋ถ๋ชจ ์์๋ฅผ ๊ธฐ์ค์ผ๋ก ์ด๋

    - ๋ฌธ์์์ ์์๊ฐ ์ฐจ์งํ๋ ๊ณต๊ฐ์ด ์์ด์ง
  
  - fixed
  
    - ์์๋ฅผ Normal Flow์์ ์ ๊ฑฐ

    - ํ์ฌ ํ๋ฉด์์ญ(viewport)์ ๊ธฐ์ค์ผ๋ก ์ด๋

    - ๋ฌธ์์์ ์์๊ฐ ์ฐจ์งํ๋ ๊ณต๊ฐ์ด ์์ด์ง

  - sticky

    - ์์๋ฅผ Normal Flow์ ๋ฐ๋ผ ๋ฐฐ์น

    - ๊ฐ์ฅ ๊ฐ๊น์ด block ๋ถ๋ชจ ์์๋ฅผ ๊ธฐ์ค์ผ๋ก ์ด๋

    - ์์๊ฐ ํน์  ์๊ณ์  (ex. viewport์ ์๋จ์ผ๋ก๋ถํฐ 10px)์ ์คํฌ๋กค ๋  ๋ ๊ทธ ์์น์์ ๊ณ ์ ๋จ (fixed)

    - ๋ง์ฝ ๋ค์ sticky ์์๊ฐ ๋์ค๋ฉด ๋ค์ sticky ์์๊ฐ ์ด์  sticky ์์์ ์๋ฆฌ ๋์ฒด ; ์ด์  ์์๊ฐ ๊ณ ์ ๋์ด ์๋ ์์น์ ๋ค์ ์์๊ฐ ๊ณ ์ ๋์ด์ผ ํ  ์์น๊ฐ ๊ฒน์น๊ฒ ๋๊ธฐ ๋๋ฌธ

- Position ์ค์ต

  ```html
  <!DOCTYPE html>
  <html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      height: 1500px;
    }

    .container {
      position: relative;
      height: 300px;
      width: 300px;
      border: 1px solid black;
    }

    .box {
      height: 100px;
      width: 100px;
      border: 1px solid black;
    }

    .static {
      position: static;
      background-color: lightcoral;
    }

    .absolute {
      position: absolute;
      background-color: lightgreen;
      top: 0px;
      right: 0px;
    }

    .relative {
      position: relative;
      background-color: lightblue;
      top: 100px;
      left: 100px;
    }

    .fixed {
      position: fixed;
      background-color: gray;
      top: 0;
      right: 0;
    }
  </style>
  <body>
    <div class="container">
      <div class="box static">Static</div>
      <div class="box absolute">Absolute</div>
      <div class="box relative">Relative</div>
      <div class="box fixed">Fixed</div>
    </div>
  </body>
  </html>
  ```

  ![positionpr](https://user-images.githubusercontent.com/121418205/221459718-e04eaa59-568b-49dd-bb95-4b0ca89d0d42.png)

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      body {
        height: 1500px;
      }

      .sticky {
        position: sticky;
        background-color: lightblue;
        padding: 20px;
        border: 2px solid black;
        top: 0;
      }
  </style>
  </head>
  <body>
    <div>
      <div class="sticky">sticky</div>
      <div>
        <p>aa</p>
        <p>aa</p>
        <p>aa</p>
      </div>
      <div class="sticky">sticky</div>
      <div>
        <p>aa</p>
        <p>aa</p>
        <p>aa</p>
      </div>
      <div class="sticky">sticky</div>
    </div>
  </body>
  </html>
  ```

  ![positionpr2](https://user-images.githubusercontent.com/121418205/221459698-dc9c249a-9a93-4c7d-af2c-efa0f5853aa8.png)

### @ z-index

- ์์๊ฐ ๊ฒน์ณค์ ๋ ์ด๋ค ์์ ์์ผ๋ก ์์ ๋ํ๋ผ ์ง ๊ฒฐ์  ; z์ถ (์คํฌ๋ฆฐ ํ๋ฉด์ผ๋ก๋ถํฐ ์ฌ์ฉ์ ์ผ๊ตด ์ชฝ์ผ๋ก ํฅํ๋ ๋ผ์ธ) ๊ธฐ์ค ์ ๋ ฌ

- ํน์ง

  - ์ ์ ๊ฐ์ ์ฌ์ฉํด z์ถ ์์ ์ง์ 

  - ๋ ํฐ ๊ฐ ๊ฐ์ง ์์๊ฐ ์์ ๊ฐ์ ์์๋ฅผ ๋ฎ์

- ์ค์ต

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      .container {
        position: relative;
      }

      .box {
        position: absolute;
        width: 100px;
        height: 100px;
      }

      .red {
        background-color: red;
        top: 50px;
        left: 50px;
        z-index: 3;
      }

      .green {
        background-color: green;
        top: 100px;
        left: 100px;
        z-index: 2;
      }

      .blue {
        background-color: blue;
        top: 150px;
        left: 150px;
        z-index: 1;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="box red"></div>
      <div class="box green"></div>
      <div class="box blue"></div>
    </div>
  </body>
  </html>
  ```