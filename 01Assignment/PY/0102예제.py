# 예제01
number1 = 1
number2 = number1 + 1
print(number1, number2)

# 1 2
# ()는 print()코드의 일부; 출력되지 않음

# 예제02
number1 = 10
number2 = 5
number3 = str(number1) + str(number2)
number4 = number1 + number2
print(number1, number2, number3, number4)

# 10 5 105 15
# str은 문자열 ; 문자열 + 문자열 하면 이어서 나열된 형식으로 출력

# 예제03
string1 = "Hello"
string2 = string1
string3 = "World" + "!"
print(string2, "?", string3)

# Hello?World!

# 예제04
string = "Hello?"
n = 5
print(string * n)

# Hello?Hello?Hello?Hello?Hello?

# 예제05
string = "abc hello def"
sub_string1 = string[4:10]
sub_string2 = string[1:4]
sub_string3 = string[-1]
print(sub_string1)
print(sub_string2)
print(sub_string3)

# hello 
# bc 
# f
# 음수 인덱싱은 맨오른쪽부터 / -1부터! (0부터 아님)

# 예제06
number1 = 5
number2 = 10.0 + number1
number1 - 5
number3 = number1 * (number2 + 10)
print(number1, number2, number3)

# 5 15.0 125.0

# 예제07
list_variable = [1, 2, 3, [1, 2, 3]]
sub_list = list_variable[3][-1]
print(sub_list)

# 3

# 예제08
list_variable = []
list_variable.append(1)
list_variable.append("a")
list_variable[0] = 0
print(list_variable)

# [0, 'a']
# list_variable[0]으로 인덱스의 0에 해당하는 변수를 0으로 **바꾸는 것** (맨앞에 0 갖다붙이는 것 아님!)

# 예제09
name = input("너의 이름은?")
print(name)

# 김소은
# input() 하면 입력창 뜸 입력창에 김소은이라고 치면 name이라는 변수에 김소은이라는 객체가 할당됨

# 예제10
age = int(input("너의 나이는?"))
print("올해 나이 : ", age)
print("내년 나이 : ", age + 1)

# 올해 나이 : 26
# 내년 나이 : 27
# int(input()) 하면 입력창 뜸 입력창에 26이라고 치면 age라는 변수에 26이라는 객체가 할당됨