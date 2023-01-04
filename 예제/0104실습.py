# 01

num = int(input("정수를 입력하세요:"))

if num == 0:
    print(0)
elif num < 0:
    print(num-(2*num))
else:
    print(num)

# 02

numList = list(map(int, input("정수 여러개를 입력하세요 : ").split()))
howMany = 0

for i in numList:
    howMany += 1

print(howMany)

# 03

numList = list(map(int, input("정수 여러개를 입력하세요 : ").split()))
total = 0

for i in numList:
    total += i

print(total)

# 04

numList = list(map(int, input("정수 여러개를 입력하세요 : ").split()))
total = 0
howMany = 0

for i in numList:
    total += i
    howMany += 1

print(total/howMany)

# 05

numList = list(map(int, input("정수 여러개 : ").split()))
time = 1

for i in numList:
    time *= i

print(time)

# 06

numList = list(map(int, input("양의 정수 여러개 : ").split()))
largest = numList[0]

for i in numList:
    if i > largest:
        largest = i

print(largest)

"""
변수 = 리스트[0] 하면 리스트에서 인덱싱 사용 가능!
"""

# 07

numList = list(map(int, input("양의정수여러개 : ").split()))
smallest = numList[0]

for i in numList:
    if i < smallest:
        smallest = i

print(smallest)