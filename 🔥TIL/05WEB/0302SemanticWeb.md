# 0302 THU

## ๐ Web - Semantic Web

- ์น ๋ฐ์ดํฐ๋ฅผ ์๋ฏธ๋ก ์ ์ผ๋ก ํํํ๊ณ  ์ฐ๊ฒฐํ๋ ๊ฐ๋ ; ์ปดํจํฐ๊ฐ ๋ฐ์ดํฐ ๋ด์ฉ๊ณผ ๋ฌธ๋งฅ์ ๋ ํจ์จ์ ์ผ๋ก ์ดํดํ๊ณ  ์ง๋ฅ์ ์ผ๋ก ํ์ฉํ  ์ ์๋๋ก!

## 1. Semantics in HTML

- "์ด ํ์ด์ง์ ์ต์์ ์ ๋ชฉ"

  ```html
  <h1>Heading</h1>
  ```

    - ํ์ด์ง ์ต์์ ์ ๋ชฉ ์๋ฏธ๋ฅผ ์ ๊ณตํ๋ semantic ์์ h1

    - ๋ธ๋ผ์ฐ์ ์ ์ํด ์ ๋ชฉ์ฒ๋ผ ๋ณด์ด๋๋ก ํฐ ๊ธ๊ผด๋ก ์คํ์ผ ์ง์ ๋จ

  ```html
  <span style="font-size: 32px;">Heading</span>
  ```

    - ๋ชจ๋  ์์๋ฅผ ์ต์์ ์ ๋ชฉ**"์ฒ๋ผ"** ๋ณด์ด๊ฒ ํ  ์๋ ์์ผ๋ **์๋ฏธ๋ก ์  ๊ฐ์น๋ ์์**
  
- HTML Semantic Element

  - ๊ธฐ๋ณธ์ ์ธ ๋ชจ์๊ณผ ๊ธฐ๋ฅ ์ด์ธ์ ์๋ฏธ๋ฅผ ๊ฐ์ง๋ HTML ์์

  - ๊ฒ์์์ง ๋ฐ ๊ฐ๋ฐ์๊ฐ ์น ํ์ด์ง์ ์ฝํ์ธ ๋ฅผ ์ดํดํ๊ธฐ ์ฝ๊ฒ ๋ง๋ค์ด์ค

- "๊ฐ์์ ์ฑ์๊ณผ ์ญํ "

  - HTML ; ์ฑ์์ง ๋ฐ์ดํฐ๋ฅผ ๋ํ๋ด๊ธฐ ์ํ

  - CSS ; ์ด๋ป๊ฒ ๋ณด์ฌ์ผ ํ๋์ง

- ํ์ด์ง ๊ตฌ์กฐํ๋ฅผ ์ํ ๋ํ์ ์ธ semantic element

  - header

  - nav

  - main
  
  - article

  - section

  - aside

  - footer

- ์๋ฏธ๋ก ์  ๋งํฌ์ ์ค์ต

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

- Object-Oriented CSS ; ๊ฐ์ฒด ์งํฅ์  ์ ๊ทผ๋ฒ์ ์ ์ฉํ์ฌ CSS๋ฅผ ๊ตฌ์ฑํ๋ ๋ฐฉ๋ฒ๋ก 

- oocss ์ค์ต

  ```html
  <style>
    /*๊ธฐ๋ณธ ์นด๋ ๊ตฌ์กฐ*/
    .card {
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 16px;
      width: 50%;
    }

    /*์นด๋ ์ ๋ชฉ*/
    .card-title {
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 8px;
    }

    /*์นด๋ ์ค๋ช*/
    .card-description {
      font-size: 16px;
      margin-bottom: 16px;
    }

    /*๊ธฐ๋ณธ ๋ฒํผ ๊ตฌ์กฐ*/
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

    /*ํ๋ ๋ฐฐ๊ฒฝ*/
    .bg-blue {
      background-color: #007bff;
      color: #fff;
    }

    /*๋นจ๊ฐ ๋ฐฐ๊ฒฝ*/
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

- Block Element Modifier ; ๋ธ๋ก, ์์, ์์ ์ ์ฌ์ฉํด ํด๋์ค ์ด๋ฆ์ ๊ตฌ์กฐํํ๋ ๋ฐฉ๋ฒ๋ก 

- BEM ๊ตฌ์ฑ

  - Block

    - ๋ฌธ๋จ ์ ์ฒด์ ์ ์ฉ๋ ์์ ๋๋ ์์๋ฅผ ๋ด๊ณ  ์๋ ์ปจํ์ด๋

    - ์ฌ์ฌ์ฉ ๊ฐ๋ฅํ ๋๋ฆฝ์  ๋ธ๋ก, ๊ฐ์ฅ ๋ฐ๊นฅ์ชฝ ์์ ์์

    - ์ฌ์ฌ์ฉ์ ์ํด margin ๋๋ padding ์ ์ฉ X

  - Element

    - block์ด ํฌํจํ๊ณ  ์๋ ํ ์กฐ๊ฐ

    - ๋ธ๋ก์ ๊ตฌ์ฑํ๋ ์ข์์ ์ธ ํ์ ์์

  - Modifier

    - block ๋๋ element์ ์์ฑ

- BEM ์ค์ต

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
      <h2 class="block__title">์ ๋ชฉ</h2>
      <ul class="block__list">
        <li class="block__list-item">ํญ๋ชฉ 1</li>
        <li class="block__list-item">ํญ๋ชฉ 2</li>
      </ul>
      <button class="block__button block__button--red">๋ฒํผ
    </button>
    </div>
  </body>
  ```

## ์ฐธ๊ณ 

- ์๋ฏธ๋ก ์  ๋งํฌ์์ ์ด์ 

  - ๊ฒ์ ์์ง์ด ํด๋น ์น์ฌ์ดํธ๋ฅผ ๋ถ์ํ๊ธฐ ์ฝ๊ฒ ๋ง๋ค์ด ๊ฒ์ ์์์ ์ํฅ

  - ์๊ฐ ์ฅ์  ์ฌ์ฉ์๊ฐ ์คํฌ๋ฆฐ ๋ฆฌ๋๊ธฐ๋ก ์น ํ์ด์ง๋ฅผ ์ฌ์ฉํ  ๋ ์ถ๊ฐ์  ๋์

- ํด๋์ค ๋ช์ ๊ธธ์ด

  - ํด๋์ค ์ด๋ฆ์ด ๋ฌด์์ ๋ํ๋ด๋์ง ๋ถ๋ชํ๊ฒ ์ ๋ฌํ๋ ๊ฒ์ด ๊ฐ์ฅ ์ค์

  - ๋น ๋ฅด๊ณ  ๋ชํํ ํ๊ธฐ๋ฅผ ์ฐ์ ์ ์ผ๋ก!

- OOCSS & BEM์ ๋ชฉ์ 

  - ์ฌ์ฌ์ฉ ๊ฐ๋ฅํ ๋ชจ๋๋ก ๋ถ๋ฆฌํจ์ผ๋ก์จ ์ ์ง๋ณด์์ฑ๊ณผ ํ์ฅ์ฑ ํฅ์

  - ๊ฐ๋ฐ์ ๊ฐ ํ๋ ฅ ํฅ์๋์ด ๊ณตํต ์ธ์ด์ ์ฝ๋ ์ดํด ํ๋ฆฝ