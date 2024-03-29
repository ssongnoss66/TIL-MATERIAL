# 🙂 String Formatting

## @ String Interpolation

- 변수 활용하여 문자열 만드는 법

  - %-formatting

    ```python
    name = "Kim"
    score = 4.5

    print("Hello, %s" % name)
    print("내 성적은 %d" % score)
    print("내 성적은 %f" % score)

    # Hello, Kim
    # 내 성적은 4
    # 내 성적은 4.500000
    ```
  
  - f-string

    ```python
    name = "Kim"
    score = 4.5
    print(f"Hello, {name}! 성적은 {score}")
    # Hello, Kim! 성적은 4.5

    pi = 3.141592
    print(f"원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}")
    # 원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368

# 🧐 형 변환 (Typecasting)

## @ 자료형 변환 

- 파이썬에서 데이터 형태는 서로 변환 가능

  - 암시적 형 변환 (Implicit) 

    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우

    - bool, Numeric type (int, float, complex)

      ```python
      True + 3
      # 4
      3 + 5.0
      # 8.0
      3 + 4j + 5
      # (8+4j)
      ```

  - 명시적 형 변환 (Explicit)

    - int ; str*, float -> int

    - float ; str*, int -> float

    - str ; int, float, list, tuple, dict -> str

      ```python
      '3' + 4           #(X)
      int('3') + 4      #(O) 7
      int('3.0') + 4    #(O) 7
      int('3.5') + 4    #(X)
      float('3.5') + 4  #(O) 7.5

      # 문자열은 암시적 타입 변환이 되지 않음
      # 명시적 타입 변환이 필요함
      # 정수 형식이 아닌 경우 타입 변환할 수 없음
      ```

# 😕 제어문 (Control Statement)

## 정의

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령 수행

- 특정 상황에 따라 코드를 선택적으로 **실행(분기/조건)하거나 계속하여 실행(반복)하는 제어**가 필요

- 순서도(flow chart)로 표현 가능

# 😏 조건문 (Conditional Statement)

## @ 조건문 기본 정의

- 참 / 거짓을 판단할 수 있는 조건식과 함께 사용

  ![조건문](https://user-images.githubusercontent.com/121418205/210301865-57181801-d071-494d-9695-28609d020a3e.jpg)

- 기본 형식 : expression에는 참 / 거짓에 대한 조건식

  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행

  - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행

    - else는 선택적으로 활용 가능

      ```python
      if < expression >:
        # Run this Code block
      else:
        # Run this Code block
      ```

- 예제 : 아래의 순서도 두개를 코드로 나타내세요

  ![조건문예제](https://user-images.githubusercontent.com/121418205/210302574-eb000cfb-8dc4-4b54-ade8-2f4310f9f1b6.jpg)

  ![조건문예제2](https://user-images.githubusercontent.com/121418205/210303018-704e992a-4711-429b-80f3-42e314c1c8f8.jpg)

  ```python
  a = -10
  if a >= 0
    print("양수")
  else:
    print("음수")
  print(a)
  # 음수 
  # -10

  a = 10
  if a >= 0
    print("양수")
  else:
    print("음수")
  print(a)
  # 양수
  # 10
  ```

- 실습 문제 : 조건문을 통해 변수 num의 값의 홀짝 여부 출력

  - num은 input을 통해 사용자로부터 입력받을 것

  ```python
  num = int(input())
  if num % 2 == 0:
    print("짝수")
  else:
    print("홀수")
  ```

## @ 복수 조건문

- elif 활용

  ```python
  if < expression >:
    # Code block
  elif < expression >:
    # Code block
  else:
    # Code block
  ```

- 실습 문제 : dust 값에 따라 등급을 출력하는 조건식 작성

  ![미세먼지 농도 등급](https://user-images.githubusercontent.com/121418205/210303672-d41218ed-8520-4992-bb5e-7d24b6abcc63.jpg)

    ```python
    mimun = int(input())
    if mimun > 150:
      print("매우나쁨")
    elif mimun > 80
      print("나쁨")
    elif mimun > 30
      print("보통")
    else:
      print("좋음")
    print("미세먼지 확인 완료")
    
    # 굳이 mimun > 80 and mimun <= 150 으로 안하는 이유
    # 조건식을 동시에 검사하는게 아니라 순차적으로 비교!
    ```

## @ 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용 가능

  - 들여쓰기 유의!

  ```python
  if <expression>:
    # Code block
    if <expression>:
      #Code block
  else:
    # Code block
  ```

- 실습 문제 : 300 넘을 때 '실외 활동 자제' 음수일 때 '잘못된 값' 출력

  ![미세먼지 농도 등급](https://user-images.githubusercontent.com/121418205/210303672-d41218ed-8520-4992-bb5e-7d24b6abcc63.jpg)

    ```python
    mimun = int(input())
    if mimun > 150:
      print("매우나쁨")
      if mimun > 300:
        print("실외 활동 자제")
    elif mimun > 80:
      print("나쁨")
    elif mimun > 30:
      print("보통")
    elif mimun > 0:
      print("좋음")
    else:
      print("잘못된 값")
    ```

# 🙃 레인지

## @ range(n=0, m ,s=1)

- 숫자의 시퀀스를 나타내기 위해 사용

  - 기본형 *range(n)* ; 0부터 n-1까지의 숫자의 시퀀스

  - 범위 지정 *range(n, m)* ; n부터 m-1까지의 숫자의 시퀀스

  - 범위 및 스텝 지정 *range(n, m, s)* ; n부터 m-1까지 s만큼 증가시키는 숫자의 시퀀스

- **변경 불가능**(immutable)하고 **반복 가능**(iterable)함.

  ```python
  range(4)
  # range(0, 4)
  list(range(4))
  # [0, 1, 2, 3]
  typer(range(4))
  # <class 'range'>

  list(range(3))
  # 0부터 3-1까지 ; [0, 1, 2]
  list(range(1, 5))
  # 1부터 5-1까지 ; [1, 2, 3, 4]
  list(range(1, 5, 2))
  # 1부터 5-1까지 2만큼 증가 ; [1, 3]

  list(range(6, 1, -1))
  # 6부터 1+1까지 역순으로 ; [6, 5, 4, 3, 2]
  list(range(6, 1, 1))
  # 스텝에서 역순 명시하지 않음 ; []
  ```

# 🥲 반복문

## @ 정의

- 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

  ![반복문](https://user-images.githubusercontent.com/121418205/210305492-9b1cc64a-ec78-4d5f-9709-55a13af3ca45.jpg)

## @ 종류

- while 문 ; 종료조건에 해당하는 코드를 통해 반복문 종료

  - 조건식이 참인 경우 반복적으로 모드를 실행

  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행

  - *무한 루프 하지 않도록* **종료조건**이 반드시 필요

    ```python
    while <expression>:
        # Code block
    ```

  - 아래의 순서도를 코드로 나타내시오

    ![while문순서도](https://user-images.githubusercontent.com/121418205/210305775-65dab4e2-619c-4106-8e2d-1fdb83dc75e3.jpg)

      ```python
      a = 0
      while a < 5:
          print(a)
          a += 1
      print("END")
      ```
  
  - 실습 : 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드

    ```python
    a = 0
    sum = 0
    b = int(input())
    while a < b:
      sum += a
      a += 1
    print(sum)
    ```

- for 문 ; 반복가능한 객체를 모두 순회하면 종료 (별도의 종료조건이 필요 없음)

  - 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회

    - 처음부터 끝까지 모두 순회 ; **별도의 종료조건 필요 X**

    - 순회 가능한 객체 ; 컨테이너형(문자열, 리스트, 튜플, range, set, dictionary) 등

      ```python
      for <변수명> in <iterable>:
        # Code block
      ```

  - 아래의 순서도를 코드로 나타내시오

    ![for문 순서도](https://user-images.githubusercontent.com/121418205/210306901-37d45ca8-3ccc-4c01-83a4-87757d312d75.jpg)

      ```python
      fruits = ["딸기", "바나나", "키위", "사과"]
      for fruit in fruits:
        print(fruit)
      print("END")
      ```
  
  - 문자열 순회 : 사용자가 입력한 문자를 한글자씩 세로로 출력

    ```python
    chars = input()
    for char in chars:
      print(char)

    for i in range(len(chars)):
      print(chars[i])

    # range 활용
    ```

- 반복문 제어 ; break, continue, for-else

  - break ; 반복문 종료

    ```python
    n = 0
    while True:
      if n ==3:
        break
      print(n)
      n += 1

    # 0
    # 1
    # 2

    for i in range(10)
      if i > 1:
        print("0과 1만 필요해!")
        break
      print(i)

    # 0
    # 1
    # 0과 1만 필요해!
    ```

  - continue ; continue 이후의 코드 블록 수행 X, 다음 반복 수행

    ```python
    for i in range(6):
      if i % 2 == 0 :
        contine
      print(i)

    # 1
    # 3
    # 5
    # continue 만나면 이후 코드인 print(i) 실행되지 않고 바로 다음 반복 실행
    ```    

  - for-else ; 끝까지 반복문 실행한 이후에 else문 실행

    - break 통해 중간에 종료되는 경우 else문 실행 X

    ```python
    for char in "apple":
      if char == "b":
        print("b!")
        break
    else:
      print("b가 없습니다")

    # b가 없습니다

    for char in "banana":
      if char == "b":
        print("b!")
        break
    else:
      print("b가 없습니다")
     # b!
     ```

  - 기본 형식

    ![반복문 제어 기본 형식](https://user-images.githubusercontent.com/121418205/210308384-d53c6efc-960a-4ab8-98b2-43ad02a630da.jpg)