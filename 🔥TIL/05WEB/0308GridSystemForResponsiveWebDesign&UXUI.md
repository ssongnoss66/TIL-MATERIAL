# 0308 WED

## ๐ซ  Responsive Web Design

- ๋๋ฐ์ด์ค ์ข๋ฅ๋ ํ๋ฉด ํฌ๊ธฐ์ ์๊ด์์ด, ์ด๋์์๋  ์ผ๊ด๋ ๋ ์ด์์ ๋ฐ ์ฌ์ฉ์ ๊ฒฝํ์ ์ ๊ณตํ๋ ๋์์ธ ๊ธฐ์ 

- Bootstrap grid system์ 12๊ฐ column๊ณผ **6๊ฐ breakpoints**๋ฅผ ์ฌ์ฉํ์ฌ ๋ฐ์ํ ์น ๋์์ธ ๊ตฌํ

## ๐ Grid system Breakpoints

- ์น ํ์ด์ง๋ฅผ ๋ค์ํ ํ๋ฉด ํฌ๊ธฐ์์ ์ ์ ํ๊ฒ ๋ฐฐ์นํ๊ธฐ ์ํ ๋ถ๊ธฐ์ 

- **ํ๋ฉด ๋๋น์ ๋ฐ๋ผ 6๊ฐ์ ๋ถ๊ธฐ์  ์ ๊ณต (xs, sm, md, lg, xl, xxl)**

- ๊ฐ breakpoints๋ง๋ค ์ค์ ๋ ์ต๋ ๋๋น ๊ฐ **"์ด์์ผ๋ก"** ํ๋ฉด์ด ์ปค์ง๋ฉด grid system ๋์ ๋ณ๊ฒฝ

  ![breakpoints](https://user-images.githubusercontent.com/121418205/223645012-31247e04-d9ac-48cb-8703-30dd29be5de9.png)
  
- ์ค์ต

  ![breakpointsแแตแฏแแณแธ](https://user-images.githubusercontent.com/121418205/223645010-c261b598-f2a5-4687-adde-ae457f684491.png)

  ```html
  <head>
    <style>
      .box {
        border: 1px solid black;
        background-color: lightblue;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h2 class="text-center">Breakpoints</h2>
    <div class="container">
      <div class="row">
        <div classcol-12 col-sm-6 col-md-2 col-lg-3 col-xl-4>
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
      </div>
    </div>

    <h2 class="text-center">Breakpoints + offset</h2>
    <div class="row g-4">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
        <div class="box">col</div>
      </div>
    </div>
  </body>
  ```

- ์ค์  Media Query๋ก ์์ฑ๋ Grid system์ breakpoints

  ```html
  /* Small devices (landscape phones, 675px and up) */
  @media (min-width: 576px) {
    ...
  }

  /* Medium devices (tablets, 768px and up) */
  @media (min-width: 768px) {
    ...
  }

  /* Large devices (desktops, 992px and up) */
  @media (min-width: 992px) {
    ...
  }

  /* X-Laarge devices (large desktops, 1200px adn up) */
  @media (min-width: 1200px) {
    ...
  }

  /* XX-Large devices (larger desktops, 1400px and up) */
  @media (min-width: 1400px) {
    ...
  }
  ```

> Grid System์ ํ๋ฉด ํฌ๊ธฐ์ ๋ฐ๋ผ **(breakpoints)** 12๊ฐ์ ์นธ์ ๊ฐ ์์์ ๋๋์ด ์ฃผ๋ ๊ฒ

- ์ค์  ํํ์ด์ง ๋ถ์

  ![airbnb Grid System](https://user-images.githubusercontent.com/121418205/223645004-4b4d0b1a-18ee-462d-942e-6b178c22996e.png)

  ![airbnb Flexbox](https://user-images.githubusercontent.com/121418205/223644990-97f06a93-751b-41bb-8a7a-6d35d30f10af.png)

  ![airbnb Position](https://user-images.githubusercontent.com/121418205/223644971-35e5a0f3-7bee-422b-bea4-8da2d18b2bba.png)

## ๐ง ์ฐธ๊ณ 

- Grid cards ; row-cols ํด๋์ค๋ฅผ ์ฌ์ฉํ์ฌ ํ๋น ํ์ํ  ์ด (์นด๋) ์๋ฅผ ์์ฝ๊ฒ ์ ์ดํ  ์ ์์

  ![GridCards](https://user-images.githubusercontent.com/121418205/223644959-ae40242b-ce44-4498-aa61-0569ad220083.png)
  
  ```html
  <div class="container">
    <div class="row row-cols-1 row-cols-sm-3 row-cols-md-2 g-4">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">...</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  ```

## ๐ถโ๐ซ๏ธ UX & UI

### @ UX

- UX (User Experience) ; ์ ํ์ด๋ ์๋น์ค๋ฅผ ์ฌ์ฉํ๋ ์ฌ๋๋ค์ด ๋๋ผ๋ ์ ์ฒด์ ์ธ ๊ฒฝํ๊ณผ ๋ง์กฑ๋๋ฅผ ๊ฐ์ ํ๊ณ  ์ต์ ํํ๊ธฐ ์ํ ๋์์ธ๊ณผ ๊ฐ๋ฐ ๋ถ์ผ

- UX ์์

  - ๋ฐฑํ์  1์ธต์์ ๋๊ปด์ง๋ ์ข์ ํฅ์ ํฅ๊ธฐ

  - ๋ฌ์ฌ ๋งค์ฅ ๊ทผ์ฒ๋ง ๊ฐ๋ ๋งก์ ์ ์๋ ๋ฌ์ฌ ํฅ๊ธฐ

  - ์ํ๋ ์์์ ๊ฒ์ํ  ๋, ๊ฒ์ ๊ธฐ๋ฅ์ด ์ ์ ํ๊ฒ ์๋ํ๊ณ  ๊ฒ์ ๊ฒฐ๊ณผ๊ฐ ์ ํํ๊ฒ ๋์ค๋ ๊ฒ

- UX ์ค๊ณ

  - ์ฌ๋๋ค์ ๋ง์๊ณผ ์๊ฐ์ ์ดํดํ๊ณ  ์ ๋ฆฌํด์ ์ ํ์ ๋น์ฌ๋ด๋ ๊ณผ์ ์ด ํ์

  - ์ ์  ๋ฆฌ์์น, ๋ฐ์ดํฐ ์ค๊ณ ๋ฐ ์ ์ , ์ ์  ์๋๋ฆฌ์ค, ํ๋กํ ํ์ ์ค๊ณ ๋ฑ์ด ํ์

### @ UI

- UI (User Interface) ; ์๋น์ค์ ์ฌ์ฉ์ ๊ฐ์ ์ํธ์์ฉ์ ๊ฐ๋ฅํ๊ฒ ํ๋ ๋์์ธ ์์๋ค์ ๊ฐ๋ฐํ๊ณ  ๊ตฌํํ๋ ๋ถ์ผ

- UI ์์

  - ๋ฆฌ๋ชจ์ปจ ; ์ฌ์ฉ์๊ฐ ๋ฒํผ์ ๋๋ฅด๋ฉด TV๊ฐ ์ผ์ง๊ณ  ์ฑ๋์ ๋ณ๊ฒฝํ๊ฑฐ๋ ๋ณผ๋ฅจ์ ์กฐ์ ํ  ์ ์์

  - ATM ; ์ฌ์ฉ์๊ฐ ํฐ์น์คํฌ๋ฆฐ์ ํตํด ์ฌ์ฉ์ ์ ๋ณด๋ฅผ ์๋ ฅํ๊ณ , ์ํ๋ ๊ธ์ก์ ์ ํํ  ์ ์์

  - ์น ์ฌ์ดํธ ; ์ฌ์ฉ์๊ฐ ๋ก๊ทธ์ธ ๋ฒํผ์ ๋๋ฅด๋ฉด, ์ด๋ํ๋ ํ๋ฉด์ ๋์์ธ ๋ฐ ๋ ์ด์์

- UI ์ค๊ณ

  - ์์ ๋์์ธ๋ณด๋ค๋ ์ฌ์ฉ์๊ฐ ๋ ์ฝ๊ณ  ํธ๋ฆฌํ๊ฒ ์ฌ์ฉํ  ์ ์๋๋ก ๊ณ ๋ ค

  - ์ด๋ฅผ ์ํด ๋์์ธ ์์คํ, ์ค๊ฐ ์ฐ์ถ๋ฌผ, ํ๋กํ ํ์ ๋ฑ์ด ํ์

### @ ๋์์ด๋, ๊ธฐํ์, ๊ฐ๋ฐ์

- UX (์ง๋ฌด ; UX Researcher, User Researcher)

  - ๊ตฌ๊ธ ; ์ฌ์ฉ์์ ๊ฒฝํ์ ์ดํดํ๊ธฐ ์ํ ํต๊ณ ๋ชจ๋ธ ์ค๊ณ

  - MS ; ๋ฆฌ์์น ๊ธฐํ, ์ฌ์ฉ์์ ๋ํ ์งํ ์ ์

  - Meta ; ์ ์ฑ์ ์ธ ๋ฐฉ๋ฒ๊ณผ ์ ๋์ ์ธ ๋ฐฉ๋ฒ์ ์ฌ์ฉํด์ ์ฌ์ฉ์ ์กฐ์ฌ ์ค์

- UI (์ง๋ฌด ; Product Designer, Interaction Designer)

  - ๊ตฌ๊ธ ; ๋ค์ํ ๋์์ธ ํ๋กํ ํ์ดํ ํด์ ์ฌ์ฉํด์ ๊ฐ๋ฐ ๊ฐ์ด๋ ์ ๊ณต

  - MS ; ์๊ฐ ๋์์ธ์ ๊ณ ๋ คํด์ ์ฒด๊ณ์ ์ธ ๋์์ธ ์ปจ์ ๋ณด์ฌ์ค

  - Meta ; ์ ํ์ ์ดํดํ๊ณ  ๋ ๋์ UI Flow์ ์ฌ์ฉ์ ๊ฒฝํ ๋์์ธ

- ์ ํ์ UI ๋์์ธ ๊ธฐ๋ณธ ์์น https://developer.apple.com/kr/design/tips/