# 01

a = 1
b = 1
print(a < b)

# False

# 02

a = bool("")
b = False
print(a == b)

# True

# 03

a = 1
result = ""

if a == 1:
    result = True
else:
    result = False

print(result)

# True

# 04

a = 90

if a == 90:
    a = a + 10

elif a == 100:
    a = a + 10


elif a == 110:
    a = a + 10

else:
    a = a + 10

a = a + 10

print(a)

# 110

# 05

string = "hello world!"

for element in string:
    print(element)

"""
h
e
l
l
o

w
o
r
l
d
!
"""

# 06

list_variable = [0, 1, 2, 3, 4, 5, 6]

for element in list_variable:
    print(element, end=" ")

"""
0 1 2 3 4 5 6
"""

# 07

n = 10

for element in range(-n, n):
    print(element, end= " ")

"""
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
"""

# 08

n = 10

for element in range(1, n+1, 3):
    print(element, end=" ")

"""
1 4 7 10
"""

# 09

list_variable = [6, 5, 4, 3, 2, 1, 0]

"""
enumerate()
- for 문의 in 뒷부분을 enumerate()로 감싸기
- 인덱스와 원소로 이루어진 튜플을 만들어줌
- 인덱스와 원소를 각각 다른 변수에 할당하려면 unpacking 필요
"""

for i, e in enumerate(list_variable):
    print(i, e)

"""
 0 6
 1 5
 2 4
 3 3
 4 2
 5 1
 6 0

인덱스와 원소를 동시에 출력!
"""

# 10

n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0:
        break

"""
10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9
"""

# 11

list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue

    print(element, end=" ")

"""
3 5 1 9 21

continue 이후의 코드 블록 수행 X, 다음 반복 수행
"""

# 12

N = 3
M = 4

for n in range(N):
    for m in range(M):
        print(f"{n}, {m}")

"""
0, 0
0, 1
0, 2
0, 3
1, 0
1, 1
1, 2
1, 3
2, 0
2, 1
2, 2
2, 3

for문 : 처음부터 끝까지 모두 순회
"""