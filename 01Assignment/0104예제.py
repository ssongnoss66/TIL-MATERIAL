# 01

list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
    # [0, 1, 2, 3, 4, 5]
list_variable.append(7)
    # [0, 1, 2, 3, 4, 5, 7]
list_variable.append(8)
    # [0, 1, 2, 3, 4, 5, 7, 8]

for element in list_variable[2:]:
    print(element, end=" ")

"""
2 3 4 5 7 8

.pop() ; 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제
[2:] ; (슬라이싱) 인덱스 2부터 끝까지 뽑아낸다
"""

# 02

for element in range(-2, 10, 2):
    print(element, end=" ")

"""
-2 0 2 4 6 8
"""

# 03

a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1
        # 0 2 4 6 8 
    if number % 3 == 0:
        b = b + 1
        # 0 3 6 9
    if number % 4 == 0:
        c = c + 1
        # 0 4 8
    if number % 5 == 0:
        d = d + 1
        # 0 5
print(a, b, c, d)

"""
5 4 3 2

elif 아니고 if! 모든 if문에 들러서 돌고 다음 if문으로
"""

# 04

i = 0
while i <= 10:
    print(i)
    i = i + 1

"""
0
1
2
3
4
5
6
7
8
9
10
"""

# 05

i = 0
while i <= 10:
    i = i + 1
    print(i)

"""
1
2
3
4
5
6
7
8
9
10
11
"""

# 06

i = 0
while i <= 10:
    i = i + 2
    print(i)

"""
2
4
6
8
10
12
"""

# 07

i = 0
while True:
    print(i)
    i = i + 1
    if i > 10:
        break

"""
0
1
2
3
4
5
6
7
8
9
10
"""

# 08

i = 0
while True:
    print(i)
    if i > 10:
        break
    i = i + 1

"""
0
1
2
3
4
5
6
7
8
9
10
11
"""

# 09

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable))

"""
7
"""

# 10

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable))

"""
21
"""

# 11

list_variable = [3, 1, 4, -3, -9, -7]
print(min(list_variable) - max(list_variable))

"""
-13
"""