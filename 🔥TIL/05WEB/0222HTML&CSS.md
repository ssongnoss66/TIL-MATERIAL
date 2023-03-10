# 0222 WED

## ๐ 1. Introduction of Web page

- Web ; "Web site"์ "Web page"๋ฅผ ํฌํจํ๋ ์์ ๊ฐ๋

- Web site ; ์ฌ๋ฌ ๊ฐ์ "Web page"๊ฐ ๋ชจ์ฌ์ ๊ตฌ์ฑ

- Web page ; "Web site"๋ฅผ ๊ตฌ์ฑํ๋ ํ๋์ ์์

  - HTML "Structure"

  - CSS "Styling"

  - Javascript "Behaviour"

## ๐ 2. Structuring the Web

### 2.1 Introduction to HTML

- HTML ; HyperText Markup Language ์น ํ์ด์ง์ ์๋ฏธ์ ๊ตฌ์กฐ๋ฅผ ์ ์ํ๋ ์ธ์ด

- Hypertext

  - ์น ํ์ด์ง๋ฅผ ๋ค๋ฅธ ํ์ด์ง๋ก ์ฐ๊ฒฐํ๋ ๋งํฌ

  - ์ฐธ์กฐ๋ฅผ ํตํด ์ฌ์ฉ์๊ฐ ํ ๋ฌธ์์์ ๋ค๋ฅธ ๋ฌธ์๋ก ์ฆ์ ์ ๊ทผํ  ์ ์๋ ํ์คํธ

- Markup Language

  - ํ๊ทธ ๋ฑ์ ์ด์ฉํ์ฌ ๋ฌธ์๋ ๋ฐ์ดํฐ์ ๊ตฌ์กฐ๋ฅผ ๋ช์ํ๋ ์ธ์ด (HTML, Markdown)

  - ์์

    ```html
    <h1>HTML</h1>
    <p>HTML์ด๋ Hyper Text Markup Language์ ์ฝ์์ด๋ค.</p>

    <h2>Hyper Text.</h2>
    <p>Hyper Text๋ ๊ธฐ์กด์ ์ ํ์ ์ธ ํ์คํธ๊ฐ ์๋ ๋น์ ํ์ ์ผ๋ก ์ด๋ฃจ์ด์ง ํ์คํธ๋ฅผ ์๋ฏธํ๋ฉฐ, ์ด๋ ์ธํฐ๋ท์ ๋ฑ์ฅ๊ณผ ํจ๊ป ๋๋๋์๋ค. ๊ธฐ๋ณธ์ ์ผ๋ก Hyper Link๋ฅผ ํตํด ํ์คํธ๋ฅผ ์ด๋ํ๋ค.</p>
    ```

### 2.2 Structure of HTML

- Element

  ![HTMLELEMENT](https://user-images.githubusercontent.com/121418205/220529841-4ad8df5e-29fc-45a0-b528-7084c5bda99e.JPG)

    - ํ๋์ ์์๋ ์ฌ๋ ํ๊ทธ์ ๋ซ๋ ํ๊ทธ ๊ทธ๋ฆฌ๊ณ  ๊ทธ ์์ ๋ด์ฉ์ผ๋ก ๊ตฌ์ฑ

    - ๋ซ๋ ํ๊ทธ๋ ํ๊ทธ ์ด๋ฆ ์์ ์ฌ๋์๊ฐ ํฌํจ๋๋ฉฐ ๋ซ๋ ํ๊ทธ๊ฐ ์๋ ํ๊ทธ๋ ์กด์ฌ

- Attributes

  ![HTMLattributes](https://user-images.githubusercontent.com/121418205/220530088-156f1365-4860-475c-9cdc-8cfb43a80b73.jpg)

    - ๊ท์น

      - ์์ ์ด๋ฆ ๋ค์ ๋ฐ๋ก ์ค๋ ์์ฑ์ ์์ ์ด๋ฆ๊ณผ ์์ฑ ์ฌ์ด์ ๊ณต๋ฐฑ์ด ์์ด์ผ ํจ

      - ํ๋ ์ด์์ ์์ฑ๋ค์ด ์๋ ๊ฒฝ์ฐ์ ์์ฑ ์ฌ์ด์ ๊ณต๋ฐฑ์ผ๋ก ๊ตฌ๋ถํจ

      - ์์ฑ ๊ฐ์ ์ด๊ณ  ๋ซ๋ ๋ฐ์ดํ๋ก ๊ฐ์ธ์ผ ํจ

    - ๋ชฉ์ 

      - ๋ํ๋ด๊ณ  ์ถ์ง ์์ง๋ง ์ถ๊ฐ์ ์ธ ๊ธฐ๋ฅ, ๋ด์ฉ์ ๋ด๊ณ  ์ถ์ ๋ ์ฌ์ฉ

      - CSS๊ฐ ํด๋น ์์๋ฅผ ์ ํํ๊ธฐ ์ํ ๊ฐ์ผ๋ก ํ์ฉ๋จ

- ๋ฌธ์ ๊ตฌ์กฐ

  - ```<!DOCTYPE html>``` ; ํด๋น ๋ฌธ์๊ฐ html๋ก ๋ฌธ์๋ผ๋ ๊ฒ์ ๋ํ๋

  - ```<html></html>``` ; ์ ์ฒด ํ์ด์ง์ ์ฝํ์ธ ๋ฅผ ํฌํจ

  - ```<title></title>``` ; ๋ธ๋ผ์ฐ์  ํญ ๋ฐ ์ฆ๊ฒจ์ฐพ๊ธฐ ์ ํ์๋๋ ์ ๋ชฉ์ผ๋ก ์ฌ์ฉ

  - ```<head></head>``` ; HTML ๋ฌธ์์ ๊ด๋ จ๋ ์ค๋ช, ์ค์  ๋ฑ / ์ฌ์ฉ์์๊ฒ ๋ณด์ด์ง ์์

  - ```<body></body>``` ; ํ์ด์ง์ ํ์๋๋ ๋ชจ๋  ์ฝํ์ธ 

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

- HTML ๊ธฐ๋ณธ Practice

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>My page</title>
  </head>
  <body>
    <p>This is my page</p>
    <a href="https://www.google.co.kr/">Google๋ก ์ด๋</a>
    <img src ="images/sample.png" alt="sample-img">
    <img src="https://random.imagecdn.app/500/150/" alt="sample-img">
  </body>
  </html>
  ```

### 2.3 Text Structure

- HTML์ ์ฃผ์ ๋ชฉ์  ์ค ํ๋๋ ํ์คํธ ๊ตฌ์กฐ์ ์๋ฏธ๋ฅผ ์ ๊ณตํ๋ ๊ฒ

  ```html
  <h1>Main Heading</h1>
  ```

    - ๋จ์ํ ํ์คํธ๋ฅผ ํฌ๊ฒ ๋ง๋๋ ๊ฒ์ด ์๋ **ํด๋น ๋ฌธ์์ ์ต์์ ์ ๋ชฉ**์ด๋ผ๋ ์๋ฏธ ๋ถ์ฌ

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
      <li>ํ์ด์ฌ</li>
      <li>์๊ณ ๋ฆฌ์ฆ</li>
      <li>๋๋น</li>
    </ol>
  </body>
  ```

## ๐ 3. Styling the Web

### 3.1 Introduction to CSS

- CSS (Cascading Style Sheet) ; ์น ํ์ด์ง์ ๋์์ธ๊ณผ ๋ ์ด์์์ ๊ตฌ์ฑํ๋ ์ธ์ด

- ๊ตฌ๋ฌธ

  ![cssแแฎแแฎแซ](https://user-images.githubusercontent.com/121418205/220536075-847b01c4-ded8-4818-816c-cc9b710a054c.jpg)

- ์ ์ฉ ๋ฐฉ๋ฒ

  1. ์ธ๋ผ์ธ(Inline) ์คํ์ผ

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

  2. ๋ด๋ถ(Internal) ์คํ์ผ ์ํธ

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

  3. ์ธ๋ถ(External) ์คํ์ผ ์ํธ ; ๋ณ๋์ CSS ํ์ผ ์์ฑ ํ ๋ถ๋ฌ์ค๊ธฐ

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

### 3.2 Select elements

- CSS Selectors ; HTML ์์๋ฅผ ์ ํํ์ฌ ์คํ์ผ์ ์ ์ฉํ  ์ ์๋๋ก ํจ

- ์ข๋ฅ

  - ๊ธฐ๋ณธ ์ ํ์

    - ์ ์ฒด(*) ์ ํ์

    - ์์(tag) ์ ํ์
    
      - ์ง์ ํ ๋ชจ๋  ํ๊ทธ ์ ํ

    - ํด๋์ค(class) ์ ํ์

      - ์ฃผ์ด์ง ํด๋์ค ์์ฑ์ ๊ฐ์ง ๋ชจ๋  ์์ ์ ํ

      - ์) .index๋ class="index"๋ฅผ ๊ฐ์ง ๋ชจ๋  ์์ ์ ํ

    - ์์ด๋(id) ์ ํ์

      - ์ฃผ์ด์ง ์์ด๋ ์์ฑ ๊ฐ์ง ์์ ์ ํ
      
      - ๋ฌธ์์๋ ์ฃผ์ด์ง ์์ด๋๋ฅผ ๊ฐ์ง ์์๊ฐ **ํ๋๋ง** ์์ด์ผ ํจ

      - ์) #index๋ id="index"๋ฅผ ๊ฐ์ง ์์ ์ ํ

    - ์์ฑ(attr) ์ ํ์

  - ๊ฒฐํฉ์ (Combinators)

    - ์์ ๊ฒฐํฉ์ (" "(space))

      - ์ฒซ ๋ฒ์งธ ์์์ **์์ ์์๋ค** ์ ํ

      - ์) p span์ ```<p>``` ์์ ์๋ ๋ชจ๋  ```<span>```๋ฅผ ์ ํ (ํ์ ๋ ๋ฒจ ์๊ด X)

    - ์์ ๊ฒฐํฉ์ (>)

      - ์ฒซ ๋ฒ์งธ ์์์ **์ง๊ณ ์์**๋ง ์ ํ

      - ์) ul > li์ ```<ul>``` ์์ ์๋ ๋ชจ๋  ```<li>```๋ฅผ ์ ํ (ํ๋จ๊ณ ์๋ ์์๋ค๋ง)

- CSS Selectors Practice

  ```html
  <body>
    <h1 class="green">Heading</h1>
    <h2>์ ํ์ ์ฐ์ต</h2>
    <h3>Hello</h3>
    <h4>Nice to meet you</h4>
    <p id="purple">๊ณผ๋ชฉ ๋ชฉ๋ก</p>
    <ul class="green">
      <li>ํ์ด์ฌ</li>
      <li>์๊ณ ๋ฆฌ์ฆ</li>
      <li>์น
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
    /*์ ์ฒด ์ ํ์*/
    * {
      color: red;
    }

    /*ํ์ ์ ํ์*/
    h2 {
      color: orange;
    }

    h3,
    h4 {
      color: blue;
    }

    /*ํด๋์ค ์ ํ์*/
    .green {
      color: green;
    }

    /*id ์ ํ์*/
    #purple {
      color: purple;
    }

    /*์์ ๊ฒฐํฉ์*/
    .green > span {
      font-size: 50px;
    }

    /*์์ ๊ฒฐํฉ์*/
    .green li {
      color: brown;
    }
  </style>
  ```

  ![CSSselectorsPractice](https://user-images.githubusercontent.com/121418205/220540966-d8ac332f-5c1a-4ccd-858c-1c1506958a2c.jpg)

### 3.2 Cascade & Specificity

- ๋์ผํ ์์์ ์ ์ฉ ๊ฐ๋ฅํ ๊ฐ์ ์คํ์ผ์ ๋ ๊ฐ์ง ์ด์ ์์ฑํ์ ๋ ์ด๋ค ๊ท์น์ด ์ด๊ธฐ๋ ์ง ๊ฒฐ์ ํ๋ ๊ฒ

- Cascade (๊ณ๋จ์)

  - ๋์ผํ ์ฐ์ ์์๋ฅผ ๊ฐ๋ ๊ท์น์ด ์ ์ฉ๋  ๋ **CSS์์ ๋ง์ง๋ง์ ๋์ค๋ ๊ท์น**์ด ์ฌ์ฉ

    ```html
    h1 {
      color: red;
    }

    h1 {
      color: blue;
    }
    ```

      - ์ด ๊ฒฝ์ฐ h1 ํ๊ทธ ๋ด์ฉ์ ์์ blue๊ฐ ์ ์ฉ๋จ

- Specificity (์ฐ์ ์์)

  - ์ ํ์๋ณ๋ก ์ ํด์ง ์ฐ์ ์์ ์ ์์ ๋ฐ๋ผ ์ ์๊ฐ ๋์ ๊ท์น์ด ์ฌ์ฉ

    ```html
    .make-red {
      color: red;
    }

    h1 {
      color: blue;
    }
    ```

      - ์ด ๊ฒฝ์ฐ h1 ํ๊ทธ ๋ด์ฉ์ ์์ red๊ฐ ์ ์ฉ๋จ

  - ์ฐ์ ์์๊ฐ ๋์ ์

    1. Importance ```!important``` ; Cascade ๊ตฌ์กฐ๋ฅผ ๋ฌด์ํ๊ณ  ๋ชจ๋  ์ฐ์ ์์ ์ ์ ๊ณ์ฐ์ **๋ฌดํจํ**

    2. ์ฐ์  ์์ ; ์ธ๋ผ์ธ ์คํ์ผ > id ์ ํ์ > class ์ ํ์ > ์์ ์ ํ์

    3. ์์ค ์ฝ๋ ์์

  - ์ฐ์ ์์ practice

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

- ์์

  - CSS๋ ์์์ ํตํด ๋ถ๋ชจ ์์์ ์์ฑ์ ์์์๊ฒ ์์ํ๊ณ  ์ด๋ฅผ ์ด์ฉํด ์ฝ๋์ **์ฌ์ฌ์ฉ์ฑ**์ ๋์

  - ์์๋๋ ์์ฑ ; Text ๊ด๋ จ ์์ (font, color, text-align), opacity, visibility ๋ฑ

  - ์์๋์ง ์๋ ์์ฑ ; Box model ๊ด๋ จ ์์ (width, height, margin, padding, border, box-sizing, display), Position ๊ด๋ จ ์์ (position, top/right/bottom/left, z-index) ๋ฑ

  - ์์ practice

    ```html
    <html>
    <style>
      .parent {
        /* ์์ O */
        color: red;
        /* ์์ X */
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

    ![แแกแผแแฉแจpractice](https://user-images.githubusercontent.com/121418205/220547108-87584b9e-653c-4600-8667-ec980fda1f38.jpg)

## ๐ค ์ฐธ๊ณ 

- HTML ๊ด๋ จ ์ฌํญ

  - HTML ์์ ์ด๋ฆ์ ๋์๋ฌธ์๋ฅผ ๊ตฌ๋ถํ์ง ์์ง๋ง **์๋ฌธ์** ์ฌ์ฉ ๊ถ์ฅ

  - HTML ์์ฑ์ ๋ฐ์ดํ๋ ์์ ๋ฐ์ดํ์ ํฐ ๋ฐ์ดํ๋ฅผ ๊ตฌ๋ถํ์ง ์์ง๋ง **ํฐ ๋ฐ์ดํ** ๊ถ์ฅ

  - HTML์ ํ๋ก๊ทธ๋๋ฐ ์ธ์ด์ ๋ฌ๋ฆฌ **์๋ฌ๋ฅผ ๋ฐํํ์ง ์๊ธฐ** ๋๋ฌธ์ ์์ฑ ์ ์ฃผ์

- CSS ์ธ๋ผ์ธ ์คํ์ผ ์ฌ์ฉํ์ง ๋ง ๊ฒ

  - ๋ฌธ์ ์ ์ง๋ณด์ ํ๋ค์ด์ง

  - CSS์ HTML ๊ตฌ์กฐ ์ ๋ณด๊ฐ ํผํฉ๋์ด ์์ฑ๋๊ธฐ ๋๋ฌธ์ ์ฝ๋ ์ดํด ์ด๋ ต๊ฒ ๋ง๋ฆ

- CSS ๋ชจ๋  ์์ฑ ์๊ธฐํ๋ ๊ฒ ์๋ ; ์ฃผ๋ก ํ์ฉํ๋ ์์ฑ ์์ฃผ๋ก ํ์ต

- ์์ฑ์ ๋๋๋ก class๋ง ์ฌ์ฉํ๋๋ก ํจ

  - ์ฌ๋ฌ ์ ํ์๋ค๊ณผ ํจ๊ป ์ฌ์ฉํ  ๊ฒฝ์ฐ ์ฐ์ ์์ ๊ท์น์ ๋ฐ๋ผ ์๊ธฐ์น ๋ชปํ ์คํ์ผ ๊ท์น์ด ์ ์ฉ๋์ด ์ ๋ฐ์  ์ ์ง๋ณด์ ์ด๋ ค์์ง ์ ์์

  - ๋ฌธ์์์ ๋จ ํ ๋ฒ ์ ์ผํ๊ฒ ์ ์ฉ๋  ์คํ์ผ์ ๊ฒฝ์ฐ์๋ง id ์ ํ์ ์ฌ์ฉ ๊ณ ๋ ค

- CSS ์์ ์ฌ๋ถ๋ MDN ๋ฌธ์์์ ํ์ธ ; MDN ๊ฐ ๋ฌธ์ ํ๋จ์ ์์ฑ๋ณ๋ก ์์ ์ฌ๋ถ ํ์ธ ๊ฐ๋ฅ