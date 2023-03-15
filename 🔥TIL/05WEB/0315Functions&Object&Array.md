# 0315 WED

# Functions

## 😛 Functions

- Function ; 참조 자료형에 속하며 모든 함수는 Function object

- 함수의 구조

  - 함수의 이름

  - 함수의 매개변수

  - 함수의 body를 구성하는 statement

  ```html
  <script>
    function name ([param, [param, [..., param]]]) {
      statements
      return value  //return 없으면 undefined 반환
    }
  </script>
  ```

## 😗 함수의 정의

### @ 선언식과 표현식

- 선언식 function declaration

  ```html
  <script>
    function funcName () {
      statements
    }
  ```

  ```html
  //예시
  <script>
    function add (num1, num2) {
      return num1 + num2
    }

    add(2, 7) //9
  ```

- 표현식 function expression

  ```html
  <script>
    const funcName = function () {
      statements
    }
  ```

  ```html
  <script>
    const sub = function (num1, num2) {
      return num1 - num2
    }

    sub(7, 2) //5
  ```

  - 특징

    - 함수 이름이 없는 '익명 함수' 사용 가능

    - 선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 코드에서 나타나기 전에 먼저 사용 불가

      ```html
      <script>
        //선언식
        add(2, 7) //9

        function add (num1, num2) {
          return num1 + num2
        }

        //표현식
        sub(7, 2) //ReferenceError: cannot access 'sub' before initialization

        const sub = function (num1, num2) {
          return num1 - num2
        }
      ```

- 선언식과 표현식

  ![선언식과표현식](https://user-images.githubusercontent.com/121418205/225174573-1a6d588c-a955-4c4a-bf7c-e3437ee43857.png)

- 화살표 함수 표현식 Arrow function expressions

  - 함수 표현식의 간결한 표현법

  - 작성 순서

    1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성

    2. 함수의 매개변수가 하나 뿐이라면 매개변수의 '()' 제거 가능

    3. 함수 본문의 표현식이 한 줄이라면 '{}'와 'return' 제거 가능

      ```html
      <script>
        const arrow1 = function (name) {
          return `hello, ${name}`
        }

        //1. function 키워드 삭제 후 화살표 작성
        const arrow2 = (name) => {return `hello, ${name}`}

        //2. 인자가 한 개일 경우에만 () 생략 가능
        const arrow3 = name => {return `hello, ${name}`}

        //3. 함수 바디가 return을 포함한 표현식 한 개일 경우에 {} & return 삭제 가능
        const arrow4 = name => `hello, ${name}`
      ```
    
  - 응용

      ```html
      <script>
        //1. 인자가 없다면 () or _로 표시 가능
        const noArgs1 = () => 'No args'
        const noArgs2 = _ => 'No args'

        //2-1. object를 return한다면 return을 명시적으로 작성해야 함
        const returnObject1 = () => {return {key: 'value'}}

        //2-2. return을 적지 않으려면 소괄호로 감싸야 함
        const returnObject2 = () => ({key: 'value'})

### @ 매개변수

- 기본 함수 매개변수 (Default function parameter) ; 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

  ```html
  <script>
    const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
    }
  
  greeting() //Hi Anonymous
  ```

  ```html
  <script>
    //매개변수 개수 < 인자 개수
    const noArgs = function () {
      return 0
    }
    noArgs(1, 2, 3) //0

    const twoArgs = function (param1, param2) {
      return [param1, param2]
    }
    twoArgs(1, 2, 3) //[1, 2]

    //매개변수 개수 > 인자 개수
    const threeArgs = function (param1, param2, param3) {
      return [param1, param2, param3]
    }

    threeArgs() //[undefined, undefined, undefined]
    threeArgs(1) //[1, undefined, undefined]
    threeArgs(2, 3) //[2, 3, undefined]
  ```

- 나머지 매개변수 (Rest parameters) ; 무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법

  - 함수 정의에는 하나의 나머지 매개변수만 있을 수 있음

  - 나머지 매개변수는 함수 정의에서 마지막 매개변수여야 함

  ```html
  <script>
    const myFunc = function (param1, param2, ...restPrams) {
      return [param1, param2, restPrams]
    }

    myFunc(1, 2, 3, 4, 5) //[1, 2, [3, 4, 5]]
    myFunc(1, 2) //[1, 2, []]
  ```

# Object

## 🫠 Object

- (plain) Object ; 키로 구분된 데이터 집합(data collection)을 저장하는 자료형

- 객체의 구조

  - 중괄호를 이용해 작성

  - 중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개 넣을 수 있음
  
  - key는 문자형, value는 모든 자료형이 허용

    ```html
    <script>
      const user = {
        name: 'Sophia',
        age: 30,
        'key with space': true, //"trailing comma" 속성을 추가, 삭제, 이동하기가 용이해짐
      }
    ```

## 😎 객체의 속성

- Property 활용

  ```html
  <script>
    //조회
    console.log(user.age) //30
    console.log(user['key with space']) //true

    //추가
    user.address = 'korea'
    console.log(user) //{name: 'Sophia', age: 30, key with space: true, address: 'korea'}

    //수정
    user.age = 20
    console.log(user.age) //20

    //삭제
    delete user.address
    console.log(user) //{name: 'Sophia', age: 20, key with space; true}
  ```

- Property 존재 여부 확인 - "in"

  ```html
  <script>
    console.log('age' in user) //true
    console.log('country' in user) //false
  ```

- 단축 Property ; 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문 사용 가능

  ```html
  <script>
    const age = 30
    const address = 'korea'

    const oldIser = {
      age: age,
      address: address,
    }

    const newUser = {
      age, address,
    }
  ```

- 계산된 Property ; 키가 대괄호([])로 둘러싸여 있는 프로퍼티 > 고정된 값이 아닌 변수 값을 사용할 수 있음

  ```html
  <script>
    const product = promt('물건 이름을 입력해주세요')
    const prefix = 'my'
    const suffix = 'property'

    const bag = {
      [product]: 5,
      [prefix + suffix]: 'value',
    }

    console.log(bag) //{연필: 5, myproperty: 'value'}
  ```

## 🤯 객체와 함수

- Method

  - 객체 속성에 정의된 함수

  - 'this' 키워드 사용해 객체에 대한 특정한 작업 수행 가능

    - 'this' keyword ; 함수나 메서드를 호출한 객체를 가리키는 키워드 (함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용)

- Method 예시 ; object.method() > 메서드는 객체를 '행동'할 수 있게 함

  ```html
  <script>
    const person = {
      name: 'Sophia',
      greeting: function () {
        return 'Hello'
      },
    }

    //greeting 메서드 호출
    console.log(person.greeting()) //Hello
  ```

- Method + this 예시

  ```html
  <script>
    const person = {
      name: 'Sophia',
      greeting: function () {
        return `Hello my name is ${this.name}`
      },
    }

    console.log(person.greeting()) //Hello my name is Sophia
  ```

> JS에서 this는 함수를 **호출하는 방법**에 따라 가리키는 대상이 다르다!

  1. 단순 호출 시 > 전역 객체

    ```html
    <script>
      const myFunc = function () {
        return this
      }

      console.log(myFunc()) //window
    ```

  2. 메서드 호출 시 > 메서드를 호출한 객체

    ```html
    <script>
      const myObj = {
        data: 1,
        myFunc: function () {
          return this
        },
      }

      console.log(myObj.myFunc()) //myObj
    ```

- Nested 함수에서의 문제접과 해결책

  - forEach의 인자로 들어간 함수는 일반 함수 호출이기 때문에 **this가 전역 객체 가리킴**

    ```html
    <script>
      const myObj2 = {
        numbers: [1, 2, 3],
        myFunc: function () {
          this.numbers.forEach(function (number) {
            console.log(number) //1 2 3
            console.log(this) //window
          })
        }
      }
    ```

  - **화살표 함수**는 자신만의 this를 가지지 않기 때문에 외부 함수에서 this 값을 가져옴

    ```html
    <script>
      const myObj3 = {
        numbers: [1, 2, 3],
        myFunc: function () {
          this.numbers.forEach((number) => {
            console.log(number) //1 2 3
            console.log(this) //myObj3
          })
        }
      }
    ```

## 🙂 참고

- 유용한 객체 메서드  

  ```html
  <script>
    const profile = {
      name: 'Sophia',
      age: 30
    }

    console.log(Object.keys(profile)) //['name', 'age']
    console.log(Object.values(profile)) //['Sophia', 30]
  ```

- JavaScript 'this' 특징

  - JavaScript에서 this는 함수가 "호출되는 방식"에 따라 결정되는 현재 객체를 나타냄

  - Python의 self와 Java의 this는 선언 시 값이 이미 정해지는 것에 비해 JavaScript의 this는 **함수가 호출되기 전까지 값이 할당되지 않고 호출 시 결정된 (동적)**

- JSON (JavaScript Object Notation)

  - Key-Value 형태로 이루어진 자료 표기법

  - JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 "문자열"

  - JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함

- JSON <-> Object 변환하기

  ```html
  <script>
    const jsObject = {
      coffee: 'Americano',
      iceCream: 'Cookie and Cream',
    }

    //Object > JSON

    const objToJson = JSON.stringify(jsObject)

    console.log(objToJson) //{"coffee";"Americano", "iceCream":"Cookie and Cream"}
    console.log(typeof objToJson) //string

    //JSON > Object

    const jsonToObj = JSON.parse(objToJson)

    console.log(jsonToObj) //{coffee: 'Americano', iceCream: 'Cookie and Cream'}
    console.log(typeof jsonToObj) //object
  ```

# Array

## 🧐 Array

- Object ; 키로 구분된 데이터 집합을 저장하는 자료형 > 이제는 **순서가 있는 collection**이 필요하다!

- Array ; 순서가 있는 데이터 집합(data collection)을 저장하는 자료구조

- 배열의 구조

  - 대괄호 이용해 작성

  - length를 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음

  - 배열 요소의 자료형엔 제약 없음

  - 배열의 마지막 요소는 객체와 마찬가지로 쉼표로 끝날 수 있음

    ```html
    <script>
      const fruits = ['apple', 'banana', 'coconut']

      console.log(fruits[0])
      console.log(fruits[1])
      console.log(fruits[2])

      console.log(fruits.length)
    ```

- 배열과 반복

  ```html
  <script>
    //for
    for (let i = 0; i < fruits.length; i++) {
      console.log(fruits[i])
    }

    //for...of
    for (const fruit of fruits) {
      console.log(fruit)
    }
  ```

## 😶‍🌫️ 배열과 메서드

![배열과메서드](https://user-images.githubusercontent.com/121418205/225227575-b009819a-d81e-41b1-8da1-96e644a887f4.png)

- pop ; 배열 끝 요소를 제거하고 제거한 요소 반환

  ```html
  <script>
    const fruits = ['apple', 'banana', 'coconut']
    
    console.log(fruits.pop()) //coconut
    console.log(fruits) //['apple', 'banana']
  ```

- push ; 배열 끝 요소 추가

  ```html
  <script>
    const fruits = ['apple', 'banana']

    fruits.push('orange')
    console.log(fruits) //['apple', 'banana', 'orange']
  ```

- shift ; 배열 앞 요소를 제거하고 제거한 요소 반환

  ```html
  <script>
    const fruits = ['apple', 'banana', 'orange']

    console.log(fruits.shift()) //apple
    console.log(fruits) //['banana', 'orange']
  ```

- unshift ; 배열 앞 요소 추가

  ```html
  <script>
    const fruits = ['banana', 'orange']

    fruits.unshift('melon')
    console.log(fruits) //['melon', 'banana', 'orange']
  ```

- forEach ; 인자로 주어진 함수(콜백 함수)를 배열 요소 각각에 대해 실행

  - 구조

    ```html
    <script>
      array.forEach(function (item, index, array) {
        //do something
      })
    ```

    - 콜백함수는 3가지 매개변수로 구성

      - 콜백 함수 ; 다른 함수에 인자로 전달되는 함수 > 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행

      1. item ; 배열의 요소

      2. index ; 배열 요소의 인덱스

      3. array ; 배열

    - 반환 값 ; undefined
  
  - 예시

    ```html
    <script>
      const fruits = ['apple', 'banana', 'coconut']

      fruits.forEach(function (item, index, array) {
        console.log(`${item} / ${index} / ${array}`)
      })

      fruits.forEach((item, index, array) => {
        console.log(`${item} / ${index} / ${array}`)
      })
    ```

- map ; 배열 요소 전체를 대상으로 함수(콜백 함수)를 호출하고, 함수 호출 결과를 모아 **새로운 배열 반환**

  - 구조 ; forEach 동작 원리와 같지만 **새로운 배열 반환**

    ```html
    <script>
      const result = array.map(function (item, index, array) {
        //do something
      })

  - 예시

    ```html
    <script>
      //1
      const fruits = ['apple', 'banana', 'coconut']

      const result = fruits.map(function (fruit) {
        return fruit.length
      })

      const result2 = fruits.map((fruit => {
        return fruit.length
      }))
      
      console.log(result) //[5, 6, 7]

      //2
      
      const numbers = [1, 2, 3]

      const doubleNumber = numbers.map((number) => {
        return number * 2
      })

      console.log(doubleNumber) //[2, 4, 6]
    ```