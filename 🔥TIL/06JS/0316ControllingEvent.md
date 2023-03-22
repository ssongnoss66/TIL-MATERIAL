# 😏 Controlling Event

- 웹에서의 이벤트

  - 버튼을 클릭했을 때 모달 출력

  - 마우스 커서의 위치에 따라 그래그 앤 드롭하는 것

  - 사용자가 입력한 값에 따라 새로운 요소 생성하는 것

# 🥸 이벤트

- event ; 무언가 일어났다는 신호, 사건 (모든 DOM 요소는 이러한 신호를 만들어 냄)

- event 종류 ; 마우스, 인풋, 키보드, 터치 등

> DOM 요소는 event를 받고 받은 event를 '처리'(이벤트 핸들러)할 수 있음

## @ 이벤트 핸들러

- event handler ; 이벤트가 발생했을 때 실행되는 함수 (사용자의 행동에 어떻게 반응할 지를 JS 코드로 표현한 것)

- .addEventListner() ; 대표적인 이벤트 핸들러 중 하나 (특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수 호출)

  ![addEventListener](https://user-images.githubusercontent.com/121418205/225479226-173a5f04-a5d8-436c-a5bd-007f165749b4.png)

  - type

    - 이벤트 이름 (ex. 'click')

    - https://developer.mozilla.org/en-US/docs/Web/Events
  
  - handler

    - 발생한 이벤트 객체를 수신하는 콜백 함수

    - 콜백 함수는 발생한 Event object를 유일한 매개변수로 받음

- 이벤트 핸들러 기초 실습

  ```html
  <body>
    <button id="btn">버튼</button>

    <script>
      //id가 버튼인 요소 선택
      const btn = document.querySelector('#btn')
      console.log(btn)

      //선택한 버튼에 이벤트 핸들러 부착
      //버튼에서 click 이벤트가 발생될때마다 함수 실행
      //1. 표현식 함수
      btn.addEventListener('click', function (event) {
        //이벤트 객체
        console.log(event)

        //이벤트가 발생한 대상
        console.log(event.target)
        console.log(this)
      })

      //2. 화살표 함수
      btn.addEventListener('click', (event) => {
        //이벤트 객체
        console.log(event)

        //이벤트가 발생한 대상
        console.log(event.target) 
        console.log(this) //주의사항; 화살표 함수에는 this 존재 X
      })
    </script>
  </body>
  ```

  ![이벤트핸들러](https://user-images.githubusercontent.com/121418205/225482487-1385abc1-85be-4393-8511-ecf1a1c46cd5.png)

# 🙃 이벤트 핸들러 활용

- click 이벤트 ; 버튼을 클릭하면 숫자를 1씩 증가

  ```html
  <body>
    <button id = "btn">버튼</button>
    <p id = "counter">0</p>

    <script>
      //초기값
      let counterNum = 0
      //id가 btn인 요소 선택
      const btn = document.querySelector('#btn')

      //선택한 버튼에 이벤트 핸들러 부착
      //버튼에서 click 이벤트 발생될때마다 함수 실행
      btn.addEventListener('click', (event) => {
        //countNumber 증가시키고
        counterNum += 1
        //id가 counter인 요소의 컨텐츠 변경
        const pTag = document.querySelector('#counter')
        pTag.textContent = counterNum
      }) 
    </script>
  </body>
  ```

  ![클릭이벤트](https://user-images.githubusercontent.com/121418205/225488859-7f84e1ed-1048-41e4-aa8b-b2ce3b06a28a.png)

- input 이벤트 ; 사용자의 입력 값을 실시간으로 출력하기

  ```html
  <body>
    <input type="text" id="text-input">
    <p></p>

    <script>
      //1. input 요소 선택
      const textInput = document.querySelector('#text-input')
      //2. 이벤트 핸들러 부착
      textInput.addEventListener('input', (event) => {
        //console.log(event)
        //console.log(event.target)
        console.log(event.target.value)

        //3. input에 작성한 value를 p태그의 컨텐츠로 출력
        const pTag = document.querySelector('p')
        pTag.textContent = event.target.value
      })
    </script>
  </body>
  ```

  ![인풋이벤트](https://user-images.githubusercontent.com/121418205/225489534-7204351b-baef-4555-9235-90e6584fd5c4.png)

- click & input 이벤트 ; 사용자의 입력 값을 실시간으로 출력하기 > 버튼을 클릭하면 출력한 값의 스타일을 변경하기

  ```html
  <head>
    <style>
      .blue {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1></h1>
    <button id="btn">클릭</button>
    <input type="text" id="text-input">

    <script>
      //인풋
      const textInput = document.querySelector('#text-input')
      textInput.addEventListener('input', function (event) {
        const h1Tag = document.querySelector('h1')
        h1Tag.textContent = event.target.value
      })
      //버튼
      const btn = document.querySelector('#btn')
      btn.addEventListener('click', function () {
        const h1 = document.querySelector('h1')
        //클래스 blue를 토글하기
        h1.classList.toggle('blue')
      })
    </script>
  </body>
  ```

  ![클릭인풋이벤트](https://user-images.githubusercontent.com/121418205/225491414-e603dd5d-bd7c-4753-ab32-f7ddc6a818ed.png)

- 이벤트 취소하기
  
  - .preventDefault() ; 현재 Event의 기본 동작을 중단

  ```html
  <body>
    <h1>정말 중요한 내용</h1>

    <script>
      const h1 = document.querySelector('h1')
      h1.addEventListener('copy', function (event) {
        //copy event 취소
        event.preventDefault()
        alert('삐빅 복사할 수 없습니다')
      })
    </script>
  </body>
  ```

  ![이벤트취소하기](https://user-images.githubusercontent.com/121418205/225493040-e4ab9ec4-8bd8-46b9-a96b-909af77ec2ab.png)

- todo 실습 ; 할 일을 입력하고 버튼을 클릭하면 할 일 요소를 생성 > input 컨텐츠를 작성하지 않는다면 경고 알림 출력

  ```html
  <body>
    <input type="text" class="input-text">
    <button id="btn">+</button>
    <ul></ul>

    <script>
      
      //1.필요한 요소 모두 선택
      const inputTag = document.querySelector('.input-text')
      const btnTag = document.querySelector('#btn')
      const ulTag = document.querySelector('ul')

      //2.투두 추가 함수
      const addTodo = (event) => {

        //2.1.사용자 입력 데이터 저장
        const inputData = inputTag.value

        //2.6.사용자 입력 데이터 공백 제거 후 확인해서 참이라면(데이터가 있다면)
        if (inputData.trim()) {

          //2.2.데이터 저장할 리스트 요소 생성
          const liTag = document.createElement('li')

          //2.3.리스트 요소 컨텐츠에 데이터 입력
          liTag.textContent = inputData
          console.log(liTag)

          //2.4.리스트 요소를 부모 ul 요소의 자식 요소로 추가
          ulTag.appendChild(liTag)

          //2.5.todo 추가 후 input의 입력 데이터는 초기화
          inputTag.value = ''

      //2.7.거짓이라면(데이터가 없다면)
      } else {
        alert('할 일을 입력하세요')
      }}
      
      //3.버튼에 이벤트 핸들러 부착
      btnTag.addEventListener('click', addTodo)
    </script>
  </body>
  ```

  ![투두실습](https://user-images.githubusercontent.com/121418205/225497206-56bf57ee-bda5-495e-9f56-20b938ea6b79.png)

- 로또 번호 생성기 실습

  - lodash

    - 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리

    - array, object 등 자료구조 다룰 때 사용하는 유용하고 간편한 함수들을 제공

    - https://lodash.com/

  ```html
  <body>
    <h1>로또 추천 번호</h1>
    <button id="btn">행운 번호 받기</button>
    <div></div>

    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
    <script>
      //1.필요한 모든 요소 선택
      const h1Tag = document.querySelector('h1')
      const btnTag = document.querySelector('#btn')
      const divTag = document.querySelector('div')

      //2.버튼 요소에 이벤트 핸들러 부착
      btnTag.addEventListener(('click'), (event) => {
        //2.1.1부터 45까지의 값이 필요
        const allNumbers = _.range(1, 46)

        //2.2.45개의 요소가 있는 배열에서 6개 번호 추출
        const sixNumbers = _.sampleSize(allNumbers, 6)

        //2.5.6개의 li 요소를 담을 ul 요소 생성
        const ulTag = document.createElement('ul')

        //2.3.추출한 번호 배열을 "반복"하면서 li 요소 생성
        sixNumbers.forEach((number) => {

          //2.4.번호를 담을 li 요소 생성 후 입력
          const liTag = document.createElement('li')
          liTag.textContent = number

          //2.6.만들어진 li를 ul 요소에 추가
          ulTag.appendChild(liTag)
        })
        //2.7.완성한 ul 요소를 div 요소에 추가
        divTag.appendChild(ulTag)      
      })
    </script>
  </body>
  ```

  ![로또번호생성기실습](https://user-images.githubusercontent.com/121418205/225529980-17bdd81e-1358-45d4-a283-477aa860deff.png)

# 😀 참고

- addEventListner와 this ; addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상(event.target)을 뜻함

  ```html
  <body>
    <button id="function">function</button>
    <button id="arrow">arrow function</button>

    <script>
      const functionButton = document.querySelector('#function')
      const arrowButton = document.querySelector('#arrow')

      functionButton.addEventListener('click', function () {
        console.log(this) //<button id="function">function</button>
      })

      arrowButton.addEventListener('click', () => {
        console.log(this) //window
      })
    </script>
  </body>
  ```

  ![addEventListener와this](https://user-images.githubusercontent.com/121418205/225531253-b02de42b-d07f-4d4d-9842-320cc4bc680f.png)
