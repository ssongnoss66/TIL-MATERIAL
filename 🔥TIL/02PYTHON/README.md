@ 파이썬 특징
- 객체 지향 프로그래밍 ; 모든 것이 객체로 구현
  - **동일 이름에 다른 객체를 언제든 할당 가능**
- 동적 타입 언어로 **자료형이 맞지 않을 시 에러 발생**
  - 자료형의 중요성!

@ 자료형
- 문자열 + 문자열 = 이어붙이는 형태로 나열됨
- 음수 인덱싱은 맨 오른쪽부터 / 0이 아니라 -1부터

@ 형 변환 ; 데이터 형태는 변환 가능 (암시적 / 명시적)

@ 조건문
- 조건식은 동시에 검사 X  **순차적**으로 비교!
- 중첩 조건문 : 들여쓰기 유의

@ 레인지
- **range(n)** : 0부터 n-1까지의 숫자의 시퀀스
- **range(n,m)** : n부터 m-1까지의 숫자의 시퀀스
- **range(n, m, s)** : n부터 m-1까지 s만큼 증가시키는 숫자의 시퀀스

@ 반복문
- **특정 조건 도달 시**까지 반복되는 일련의 문장
- while 문 ; **종료조건에 해당하는 코드**를 통해
- for 문 ; **순회 가능한 객체를 모두 순회 시** 종료

@ 함수
- Abstraction & Decomposition ; 재사용성, 가독성, 생산성
- **map(function, iterable)**
  1. 첫번째 인자로 *함수*를 받아서
  2. 두번째 인자인 *반복 가능한 객체*의 **모든 요소**에 적용

@ 딕셔너리
- 키값 쌍으로 이뤄진 모음
- key를 순회하고 key를 통해 값을 활용
- 추가 메서드 활용하여 순회 가능
  - .items() ;(Key, value)의 튜플로 구성된 결과

@ 에러와 예외
- try except 예외 처리
  ```python
  # 에러 이름 알 때
  try:
      # 에러가 발생할 가능성이 있는 코드
  except Exception: # 에러 종류
      #에러가 발생 했을 경우 처리할 코드

  # 에러 이름 모를 때
  try:
    # 에러가 발생할 가능성이 있는 코드
  except Exception as ex: # 에러 종류
      print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수
  ```
- raise로 예외를 발생시키면 raise 아래에 있는 코드는 실행되지 않고 바로 except로 넘어감
- assert vs raise ; 둘 다 에러 발생을 알리고 프로그램 종료시킴
  - assert ; ```__debug__``` 상수가 False라면 동작 X > debugging이나 test 성격이 강함 > 실제 서비스코드에서는 사용 지양
  - raise ; 실제 서비스에게 상태를 알리는 목적일 때 사용
    ```python
    raise Exception # 에러 종류
    ```

@ 파일 입출력
- **open(file, mode="r", encoding=None)**

@ JSON
- 텍스트 <=> 언어별 데이터 타입
- 활용
  1. 객체를 JSON으로 변환
    ```python
    import json
    x = [1, "simple", "list"]
    json.dumps(x)
    # "[1, "simple", "list"]
    ```
  2. JSON을 객체로 변환
    ```python
    x = json.load(f)
    ```

@ 튜플
- 불변한 값들의 나열
- 순서 가짐 / 서로 다른 타입의 요소 가질 수 있음
- 변경 불가능 / 반복 가능

@ 세트
- 유일한 값들의 모음
- 순서 없음 (별도의 값에 접근 불가능) / 중복된 값 없음
- 변경 가능 / 반복 가능
- 다른 컨테이너에서 중복된 값 제거

@ 메서드
> 타입.메서드()
- 클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수
- 클래스 내부에 함수를 포함시킨 예
  ```python
  class Human( ):
    '''인간'''
    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk( self ):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

  person = Human.create("철수", 60.5)
  person.eat()    # self는 생략해도 알아서 전달되니까
  ```
- self ; 메소드의 첫번째 인자, 인스턴스의 매개변수 전달 시 self 매개변수 생략하고 전달

@ 사용자 정의 함수
    ```python
    def function(parameter):
      return parameter
  
    function(argument)
    ```
- 값을 하나만 return / return과 동시에 실행 종료
- argument
  - positional arguments ; 위치에 따라 함수 내에 전달
  - keyword arguments ; 변수의 이름으로 특정 argument 전달
  - default arguments values ; 기본값 지정하여 함수 호출 시 argument 설정 X
  - 정해지지 않은 개수의 arguments ; 튜플로 묶여 처리
    ```python
    def add(*args):
      for arg in args:
        print(arg)
    add(2)
    add(2, 3, 4, 5)
    ```
  -정해지지 않은 개수의 keyword arguments ; 딕셔너리로 묶여 처리
    ```python
    def family(**kwargs):
      for k, v in kwargs:
        print(k, ":", v)

    family(father = "John", mother = "Jane")
    ```
- 객체 수명주기
  - built-in scope ; 파이썬 실행 후 영원히
  - global scope ; 모듈 호출 시 / 인터프리터 끝날 때까지
  - local scope ; 함수 호출 시 생성 / 함수 종료될 때까지

@ 객체 지향 vs 절차 지향
- 객체 지향 ; 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악
- 절차 지향 ; 데이터와 함수로 인한 변화

@ 사용자 정의 클래스  
- 객체는 모두 특정 타입의 인스턴스
- 특징
  - 클래스 ; **객체들의 분류**, 함수나 변수들을 모아 놓은 집합체
  - 인스턴스 ; **하나하나의 실체**, 클래스에 의해 생성된 객체 > 인스턴스 각자 자신의 값을 가지고 있다
  ```python
  list1 = [1, 2, 3]
  list2 = [1, 2, 3]

  if list1 is list1:
      print("당연히 list1과 list1은 같은 인스턴스입니다.")

  if list1 == list2:
      print("list1과 list2의 값은 같습니다.")
      if list1 is list2:
          print("그리고 list1과 list2는 같은 인스턴스입니다.")
      else:
          print("하지만 list1과 list2는 다른 인스턴스입니다.")

  # 출력 결과
  # 당연히 list1과 list1은 같은 인스턴스입니다.
  # list1과 list2의 값은 같습니다.
  # 하지만 list1과 list2는 다른 인스턴스입니다.
  ```
  - 속성(attribute) ; 특정 데이터 타입이나 클래스의 *객체*들이 가지게 될 *상태 또는 데이터*
  - 메소드 ; 특정 데이터 타입이나 클래스의 *객체*에 *공통 적용 가능*한 행위(함수)
- 인스턴스
  - 인스턴스 변수 ; 인스턴스가 개인적으로 가지고 있는 속성, 생성자 메소드에서 self.으로 정의 > 생성된 이후 .으로 접근 및 할당
  - 인스턴스 메소드 ; 인스턴스 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메소드, 호출 시 첫번 째 인자로 self 전달됨

- 특수한 메소드
  ```python
  class Human( ):
      '''인간'''
      def __init__( self, name, weight ):
          '''초기화 함수'''
          self.name = name
          self.weight = weight

      def __str__( self )
          '''문자열화 함수
          return "{} ( 몸무게 {}kg )".format( self.name, self.weight )

    person = Human( "사람", 60.5 ) # 초기화 함수 사용
    print( person ) # 문자열화 함수 사용
    ```
  - self ; 인스턴스 자기자신, 함수 정의 공간에서 이름붙이기 위해 사용
  - 생성자 메소드 ; 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드, 인스턴스 생성 및 ```__init__``` 메소드 자동 호출
  - 소멸자 메소드 ; 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드, ```__del__```
  - 매직 메소드 ; 특수한 동작을 위해 자동으로 불리는 메소드
    - ```__str__``` ; 해당 객체의 출력 형태 지정, 인스턴스 출력 시 ```__str__```의 return 값이 출력
    - ```__gt___``` ; 부등호 연산자(>, greater than)