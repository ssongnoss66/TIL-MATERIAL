# 😗 Bootstrap Grid system

- 웹 페이지의 레이아웃을 조정하는 데 사용되는 12(적당히 크고 많은 약수를 가진 수)개의 컬럼으로 구성된 시스템

- **반응형 디자인**을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

## @ Grid system

- Grid system 핵심 클래스

  - 1개의 row 안에 12칸의 column 영역이 구성

  - 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨

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

- Grid system 실습

  - 기본

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

    ![GS실습기본](https://user-images.githubusercontent.com/121418205/223333930-efc91fca-acf4-49ac-b8f6-ac5df3546e53.png)

  - 중첩

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

    ![GS실습중첩](https://user-images.githubusercontent.com/121418205/223333929-66f7066a-ef06-4523-9d27-c2d626cf2902.png)

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

    ![GS실습Offset](https://user-images.githubusercontent.com/121418205/223333926-5c51739a-c9b9-4e41-bc13-c2789891e1a1.png)

## @ Gutters

- Grid system에서 column 사이에 padding 영역

  ![Gutters](https://user-images.githubusercontent.com/121418205/223333922-76ec8e2c-107e-41a6-aa39-fb646a89be94.png)

- Gutters 실습

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

    ![Gutters실습](https://user-images.githubusercontent.com/121418205/223333920-e1d51de6-d72f-439c-b2a3-b51ce385efa2.png)