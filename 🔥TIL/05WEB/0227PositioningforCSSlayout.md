# 0227 MON

## 😗 Web - Positioning for CSS layout

- CSS Layout ; 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것 (Position)

### @ Position

- CSS Position ; Normal Flow(CSS 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향)에서 요소를 끄집어내서 다른 위치로 배치하는 것 

  - 다른 요소 위에 놓기, 화면 특정 위치에 고정시키기 등

  - 전체 페이지 레이아웃 구성하는 것이 아니라 **페이지의 특정 항목의 위치를 조정하는 것**과 관련되어 있다

- Position 이동 방향

  ![포지션이동방향](https://user-images.githubusercontent.com/121418205/221449108-52ee2f2d-f6bc-4902-84af-969d46c7a78b.png)

- Position 유형

  - static

    - 기본값

    - 요소를 Normal Flow에 따라 배치

  - relative

    - 요소를 Normal Flow에 따라 배치

    - 자기 자신을 기준으로 이동

    - 요소가 차지하는 공간은 **static일 때와 같음**

  - absolute

    - 요소를 Normal Flow에서 제거

    - 가장 가까운 relative 부모 요소를 기준으로 이동

    - 문서에서 요소가 차지하는 공간이 없어짐
  
  - fixed
  
    - 요소를 Normal Flow에서 제거

    - 현재 화면영역(viewport)을 기준으로 이동

    - 문서에서 요소가 차지하는 공간이 없어짐

  - sticky

    - 요소를 Normal Flow에 따라 배치

    - 가장 가까운 block 부모 요소를 기준으로 이동

    - 요소가 특정 임계정 (ex. viewport의 상단으로부터 10px)에 스크롤 될 때 그 위치에서 고정됨 (fixed)

    - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리 대체 ; 이전 요소가 고정되어 있던 위치와 다음 요소가 고정되어야 할 위치가 겹치게 되기 때문

- Position 실습

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

- 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정 ; z축 (스크린 표면으로부터 사용자 얼굴 쪽으로 향하는 라인) 기준 정렬

- 특징

  - 정수 값을 사용해 z축 순서 지정

  - 더 큰 값 가진 요소가 작은 값의 요소를 덮음

- 실습

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