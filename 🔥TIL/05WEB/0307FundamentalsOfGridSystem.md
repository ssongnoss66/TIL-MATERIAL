# 0307 TUE

## ๐ Bootstrap Grid system

- ์น ํ์ด์ง์ ๋ ์ด์์์ ์กฐ์ ํ๋ ๋ฐ ์ฌ์ฉ๋๋ 12(์ ๋นํ ํฌ๊ณ  ๋ง์ ์ฝ์๋ฅผ ๊ฐ์ง ์)๊ฐ์ ์ปฌ๋ผ์ผ๋ก ๊ตฌ์ฑ๋ ์์คํ

- **๋ฐ์ํ ๋์์ธ**์ ์ง์ํด ์น ํ์ด์ง๋ฅผ ๋ชจ๋ฐ์ผ, ํ๋ธ๋ฆฟ, ๋ฐ์คํฌํ ๋ฑ ๋ค์ํ ๊ธฐ๊ธฐ์์ ์ ์ ํ๊ฒ ํ์ํ  ์ ์๋๋ก ๋์

### @ Grid system

- Grid system ํต์ฌ ํด๋์ค

  - 1๊ฐ์ row ์์ 12์นธ์ column ์์ญ์ด ๊ตฌ์ฑ

  - ๊ฐ ์์๋ 12์นธ ์ค ๋ช ๊ฐ๋ฅผ ์ฐจ์งํ  ๊ฒ์ธ์ง ์ง์ ๋จ

  ```html
  <div class="container">
    <div class="row">
      <div class="col-4"></div>
      <div class="col-4"></div>
      <div class="col-4"></div>
    </div>
  </div>
  ```

  ![GridSystem](https://user-images.githubusercontent.com/121418205/223329814-4717db24-2700-48dd-af33-a77609bd0919.png)

- Grid system ์ค์ต

  - ๊ธฐ๋ณธ

    ```html
    <div class="container">
      <div class="row">
        <div class="box col">col</div>
        <div class="box col">col</div>
        <div class="box col">col</div>
      </div>
      <div class="row">
        <div class="box col-4">col-4</div>
        <div class="box col-4">col-4</div>
        <div class="box col-4">col-4</div>
      </div>
      <div class="row">
        <div class="box col-2">col-2</div>
        <div class="box col-8">col-8</div>
        <div class="box col-2">col-2</div>
      </div>
    </div>
    ```

    ![GSแแตแฏแแณแธแแตแแฉแซ](https://user-images.githubusercontent.com/121418205/223333930-efc91fca-acf4-49ac-b8f6-ac5df3546e53.png)

  - ์ค์ฒฉ

    ```html
    <div class="container">
      <div class="row">
        <div class="box col-4">col-4</div>
        <div class="box col-8">
          <div class="row">
            <div class="box col-6">col-6</div>
            <div class="box col-6">col-6</div>
            <div class="box col-6">col-6</div>
            <div class="box col-6">col-6</div>
          </div>
        </div>
      </div>
    </div>
    ```

    ![GSแแตแฏแแณแธแแฎแผแแฅแธ](https://user-images.githubusercontent.com/121418205/223333929-66f7066a-ef06-4523-9d27-c2d626cf2902.png)

  - Offset

    ```html
    <div class="container">
      <div class="row">
        <div class="box col-4">col-4</div>
        <div class="box col-4 offset-4">col-4 offset-4</div>
      </div>
      <div class="row">
        <div class="box col-3 offset-3">col-3 offset-3</div>
        <div class="box col-3 offset-3">col-3 offset-3</div>
      </div>
      <div class="row">
        <div class="box col-6 offset-3">col-6 offset-3</div>
      </div>
    </div>
    ```

    ![GSแแตแฏแแณแธOffset](https://user-images.githubusercontent.com/121418205/223333926-5c51739a-c9b9-4e41-bc13-c2789891e1a1.png)

### @ Gutters

- Grid system์์ column ์ฌ์ด์ padding ์์ญ

  ![Gutters](https://user-images.githubusercontent.com/121418205/223333922-76ec8e2c-107e-41a6-aa39-fb646a89be94.png)

- Gutters ์ค์ต

  1.

    ```html
    <div class="container">
      <div class="row gx-5">
        <div class="col">
          <div class="box">col</div>
        </div>
        <div class="col">
          <div class="box">col</div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row gy-3">
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row g-3">
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
      </div>
    </div>
    ```

    ![Guttersแแตแฏแแณแธ](https://user-images.githubusercontent.com/121418205/223333920-e1d51de6-d72f-439c-b2a3-b51ce385efa2.png)