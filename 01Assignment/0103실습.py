# 01

if int(input("자연수를 입력하세요 : ")) > 0:
    print(True)
else:
    print(False)

# 02

(a, b) = map(int, input("두 개의 정수를 입력하세요 : ").split())
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(False)

# 03

num = int(input("정수를 입력하세요 : "))
if num > 1 and num < 10:
    print(True)
else:
    print(False)

# 04

num = int(input("정수를 입력하세요 : "))
if num > 0 and num % 2 == 0:
    print(True)
else: print(False)

# 05

num = int(input("정수를 입력하세요 : "))
if num > 100 or num < 0:
    print("에러")
elif num >= 60:
    print("합격")
elif num < 60:
    print("불합격")

# 06

chars = input("문자열을 입력하세요 : ")
for char in range(len(chars)-1, -1, -1):
    print(chars[char])

"""
index 0 1 2 3 4 5 6 7 8 9 10
char  h e l l o   w o r l d
range(11-1, -1, -1) ; 인덱스의 11-1에 해당하는 문자부터 인덱스의 -1+1에 해당하는 문자까지 역순으로 출력
"""

# 07

(a, b) = map(int, input("두 개의 정수를 입력하세요 : ").split())
if a > b:
    for i in range(b+1, a):
        print(i)
elif b > a:
    for j in range(a+1, b):
        print(j)
else:
    print(False)

# 08

(a, b) = map(int, input("두 개의 정수를 입력하세요 : ").split())
if a > b:
    for i in range(a-1, b, -1):
        print(i)
elif b > a:
    for j in range(b-1, a, -1):
        print(j)
else:
    print(False)

# 09

num = int(input("정수를 입력하세요 : "))

if num > 0:
    for i in range(1,num):
        if i % 2 == 1:
            print(i, end=" ")
else:
    print(False)

print("-----------------------------------------")

# 10

for i in range(2, 10):
    for j in range(2, 10):
        print(i,"x", j, "=", i*j)