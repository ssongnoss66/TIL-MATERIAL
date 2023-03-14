# 0314 TUE

- 코딩스타일 가이드 https://standardjs.com/rules-kokr.html

## 🥰 변수

- 식별자(변수면) 작성 규칙

  - 반드시 문자, 달러($) 또는 밑줄(_)로 시작

  - 대소문자 구분, 클래스명 외에는 모두 소문자로 시작

  - 예약어 사용 불가

  1. 카멜 케이스 (camelCase) ; 변수, 객체, 함수에 사용

  2. 파스칼 케이스 (PascalCase) ; 클래스, 생성자에 사용

  3. 대문자 스네이크 케이스 (SNAKE_CASE) ; 상수(개발자의 의도와 상관없이 변경될 가능성이 없는 값)에 사용

- 변수 선언 키워드

  - 기본적으로 const 사용 권장

  - 재할당해야하는 경우에만 let 사용

  - 실습에서는 편의를 위해 재할당이 가능한 let을 기본적으로 사용

  - 블록 스코프 (block scope)

    - if, for, 함수 등의 **중괄호({}) 내부**를 가리킴

    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

      ```html
      <script>
        let x = 1

        if (x === 1) {
          let x = 2
          console.log(x) //2
        }

        console.log(x) //1
      </script>
      ```

  - let

    - 블록 스코프를 갖는 지역 변수 선언

    - 재할당 가능 & 재선언 불가능

      ```html
      <script>
        let number = 10 //1. 선언 및 초기값 할당
        number = 20 //2. 재할당

        let number = 10 //1. 선언 및 초기값 할당
        let number = 20 //2. 재선언 불가능
      </script>
      ```

  - const

    - 블록 스코프를 갖는 지역 변수 선언

    - 재할당 불가능 & 재선언 불가능

      ```html
      <script>
        const number = 10 //1. 선언 및 초기값 할당
        number = 10 //2. 재할당 불가능

        const number = 10 //1. 선언 및 초기값 할당
        const number = 20 //2. 재선언 불가능

        const number //const' declarations must be initialized. 선언 시 반드시 초기값 설정 필요
      </script>
      ```

  - var

    - 재할당 가능 & 재선언 가능

    - ES6 이전에 변수 선언할 때 사용되던 키워드

    - 함수 스코프(function scope) 가짐

      - 함수의 중괄호 내부

      - 함수 스코프를 가지는 변수는 **함수 바깥에서 접근 불가능**

    - 변수 선언 시 var const let 키워드 중 하나 사용하지 않으면 자동으로 var 선언됨

    - "호이스팅"되는 특성으로 인해 예기치 못한 문제 발생 가능 (따라서 const let 사용 권장)

      - 변수를 선언 이전에 참조할 수 있는 현상

      - 변수 선언 이전의 위치에서 접근 시 undefined 반환

        ```html
        <script>
          console.log(name) //undefined > 선언 이전에 참조

          var name = '홍길동' //선언

          //위 코드를 암묵적으로 아래와 같이 이해함
          var name //undefined로 초기화
          console.log(name)

          var name = '홍길동'
        </script>
        ```

      - JavaScript에서 변수들은 실제 실행시에 코드 최상단으로 끌어올려지게되며 (hoisted) 이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 일어남

      - 반면 let, const는 호이스팅 일어나면 에러 발생

        ```html
        <script>
          console.log(uesrname) //undefined
          var username = '홍길동'

          console.log(email) //Uncaught ReferenceError
          let email = 'gildong@gmail.com'

          console.log(age) //Uncaught ReferenceError
          const age = 50
        </script>
        ```

## 🙃 데이터 타입

- 원시 자료형 (Primitive type)

  - 변수에 값이 직접 저장되는 자료형 (불변, 값이 복사)

    ```html
    <script>
      const bar = 'baz'
      console.log(bar) //baz

      bar.toUpperCase()
      console.log(bar) //baz

      let a = 10
      let b = a
      b = 20
      console.log(a) //10
      console.log(b) //20
    </script>
    ```

  - Number ; 정수 또는 실수형 숫자를 표현하는 자료형

    ```html
    <script>
      const a = 13
      const b = -5
      const c = 3.14 //float ;  숫자 표현
      const d = 2.998e8 //2.998 * 10^8 = 299,800,000
      const 3 = Infinity
      const f = -Infinity
      const g = NaN //Not a Number를 나타내는 값
    </script>
    ```
  
  - String ; 문자열 

    ```html
    <script>
      //덧셈 통해 문자열 붙일 수 있음
      const firstName = 'Tony'
      const lastName = 'Stark'
      const fullName = firstName + lastName

      //"Template Literal" 사용하여 문자열 사이 변수 삽입 가능
      const age = 0
      const message = '홍길동은 @{age}세입니다.'
      console.log(message)
    </script>
    ```
  
  - null ; 변수의 값이 없음을 의도적으로 표현할 때 사용

    ```html
    <script>
      const lastName = null
      console.log(lastName) //null
    </script>
    ```
  
  - undefined ; 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

    ```html
    <script>
      const firstName
      console.log(firstName) //undefined
    </script>
    ```
    > null과 undefined
    
      - 동일한 역할을 하는 두 개의 키워드가 존재하는 이유는 **JavaScript의 설계 실수**

      - null이 원시 자료형임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 해결하지 못한 것 (이미 null 타입에 의존성 가지는 프로그램들이 망가질 수 있기 때문에 하위 호환 유지)

        ```html
        <script>
          typeof null //"object"
          typeof undefined //"undefined"
        </script>
        ```

  - Boolean ; true와 false

    - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형 변환 규칙에 따라 true 또는 false로 변환됨

    - ToBoolean Conversions (자동 형변환)

      ![ToBooleanConversions](https://user-images.githubusercontent.com/121418205/224877676-6ddde5d2-cc3f-4bfa-97d6-c68c3fd79d07.png)

- 참조 자료형 (Reference type)

  - 객체의 주소가 저장되는 자료형 (가변, 주소가 복사)

    ```html
    <script>
      const obj1 = {name: 'Alice', age: 30}
      const obj2 = obj1
      obj2.age = 40
      console.log(obj1.age) //40
      console.log(obj2.age) //40
    </script>
    ```

  - Objects (Obect, Array, Function)

## 😀 연산자

- 할당 연산자

  - 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

  - 다양한 연산에 대한 단축 연산자 지원

  - Increment(++) ; 피연산자의 값을 1 증가시키는 연산자

  - Decrement(--) ; 피연산자의 값을 1 감소시키는 연산자

  - += 또는 -=와 같이 더 분명한 표현으로 적을 것을 권장

  ```html
  <script>
    let c = 0 

    c += 10
    console.log(c) //10

    c -= 3
    console.log(c) //7

    c *= 10
    console.log(c) //70

    c++
    console.log(c) //71

    c--
    console.log(c) //70
  </script>
  ```

- 비교 연산자 ; 피연산자들을 비교하고 결과값을 boolean으로 반환하는 연산자

  ```html
  <script>
    3 > 2 //true
    3 < 2 //false

    'A' < 'B' //true
    'Z' < 'a' //true
    '가' <script '나' //true
  </script>
  ```

- 동등 연산자 (==)

  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값 반환

  - 비교할 때 암묵적 타입 변환 통해 타입 일치시킨 후 같은 값인지 비교

  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

  - **예상치 못한 결과가 발생할 수 있으므로 특별한 경우 제외하고 사용 X**

  ```html
  <script>
    const a = 1
    const b = '1'
    console.log(a == b) //true
    console.log(a == true) //true

    //자동형변환예시
    console.log(8 * null) //0, null은 0
    console.log('5' - 1) //4
    console.log('5' + 1) //'51'
    console.log('five' * 2) //NaN
  </script>
  ```

- 일치 연산자 (===)

  - 두 피연산자의 값과 타입이 모두 같은 경우 true 반환

  - 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지 비교

  - 엄격한 비교가 이뤄지며 **암묵적 타입 변환 발생 X**

  ```html
  <script>
    const a = 1
    const b = '1'

    console.log(a === b) //false
    console.log(a === Number(b)) //true
  </script>
  ```

- 논리 연산자

  - and 연산은 '&&' 연산자

  - or 연산은 '||' 연산자

  - not 연산은 '!' 연산자

  - 단축 평가 지원

    ex) false && true => false

    ex) true || false => true
  
  ```html
  <script>
    true && false //false
    true && true //true

    false || true //true
    false || false //false

    !true //false

    1 && 0 //0
    0 && 1 //0
    4 && 7 //7
    1 || 0 //1
    0 || 1 //1
    4 || 7 //4
  </script>
  ```

## 😫 조건문

- if ; 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓 판단

  ```html
  <script>
    if (조건문) {
      명령문
    } else if (조건문) {
      명령문
    } else {
      명령문
    }
  </script>
  ```

  ```html
  <예시>

  <script>
    const name = 'manager'

    if (name === 'admin') {
      console.log('관리자님 환영합니다.')
    } else if (name === 'manager') {
      console.log('매니저님 환영합니다.')
    } else {
      console.log('${name}님 환영합니다.')
    }
  </script>
  ```

## 🤓 반복문

![반복문 정리](https://user-images.githubusercontent.com/121418205/224907006-44680d81-3c1c-4316-8ef4-cf773f8990c9.png)

- while ; 조건문이 참이기만 하면 문장을 계속해서 수행

  ```html
  <script>
    while (조건문) {
      //do something
    }
  </script>
  ```

  ```html
  <예시>
  
  <script>
    let i = 0

    while (i < 6) {
      console.log(i)
      i += 1
    }
  </script>
  ```

- for ; 특정한 조건이 거짓으로 판별될 때까지 반복

  ```html
  <script>
    for ([초기문]; [조건문]; [증감문]) {
      //do something
    }
  </script>
  ```

  ```html
  <예시>
  
  <script>
    for (let i = 0; i < 6; i++) {
      console.log(i)
    }
  </script>
  ```

  ![for동작원리](https://user-images.githubusercontent.com/121418205/224880991-5a898b8e-8dfe-4e18-ae4f-227939b139a0.png)

- for ... in ; 객체(object)의 속성을 순회할 때 사용

  ```html
  <script>
    for (variable in object) {
      statements
    }
  </script>
  ```

  ```html
  <예시>
  
  <script>
    const fruits = {a: 'apple', b: 'banana'}

    for (const key in fruits) {
      console.log(key) //a, b
      console.log(fruits[key]) //apple, banana
    }

    // 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장 X ; 권장 X
  </script>
  ```

- for ... of ; 반복 가능한 객체(배열, 문자열 등)를 순회할 때 사용

  ```html
  <script>
    for (variable of objects) {
      statements
    }
  </script>
  ```

  ```html
  <예시>
  
  <script>
    const numbers = [0, 1, 2, 3]

    for (const number of numbers) {
      console.log(number) //0, 1, 2, 3
    }
  </script>
  ```

> for ... in 과 for ... of

  - for ... in은 **"속성 이름"** 통해 반복

  - for ... of는 **"속성 값"** 통해 반복

  ```html
  <script>
    const arr = [3, 5, 7]

    for (const i in arr) {
      console.log(i) //0 1 2
    }

    for (const i off arr) {
      console.log(i) //3 5 7
    }

    //for...in ; 순서에 따라 인덱스 반환하는 것 보장 X > 인덱스의 순서가 중요한 배열에서 사용 X
    //Array
    const numbers = [10, 20, 30]

    for (const number in numbers) {
      console.log(number) //0 1 2
    }

    //Object
    const capitals = {
      korea: '서울',
      france: '파리',
      japan: '도쿄'
    }

    for (const capital in capitals) {
      console.log(capital) //korea france japan
    }

    //for...of
    //Array
    const numbers = [10, 20, 30]
    for (const number of numbers) {
      console.log(number) //10 20 30
    }

    //Object
    const capitals = {
      korea: '서울',
      france: '파리',
      japan: '도쿄'
    }
    for (const capital of capitals) {
      console.log(capital) //TypeError: capitals is not iterable
    }
  </script>
  ```

## 🫢 참고

- 세미콜론 (semicolon)

  - 자바스크립트는 세미콜론 선택적 사용 가능

  - 세미콜론 없으면 ASI에 의해 자동으로 세미콜론 삽입됨

- Template literals (템플릿 리터럴)

  - 내장된 표현식을 허용하는 문자열 작성 방식

  - ES6+부터 지원

  - Backtik(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있는 이점 생김

  - 표현식은 ```$```와 ```중괄호(${expression})```로 표기

    ```html
    <script>
      const age = 10
      const message = `홍길동은 ${age}세입니다.`
    </script>
    ```

- 반복문 사용 시 const 및 let

  - for문 ; 최초 정의한 i를 **재할당**하면서 사용하기 때문에 **const 사용하면 에러 발생**

  - for...in, for...of ; 재할당이 아니라 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 **const를 사용해도 에러 발생 X**

- NaN을 반환하는 경우

  1. 숫자로서 읽을 수 없음 (Number(undefined))

  2. 결과가 허수인 수학 계산식 (Math.sqrt(-1))

  3. 피연산자가 NaN (7**NaN)

  4. 정의할 수 없는 계산식 (0*Infinity)

  5. 문자열을 포함하면서 덧셈이 아닌 계산식 ('가'/3)