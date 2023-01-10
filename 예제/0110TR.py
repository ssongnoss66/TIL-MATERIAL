"""
문제 1

# 정수를 출력하세요.
5
"""

print(int(input()))

print("------------------------------------")
"""
문제 2

# 단어를 구분해서 출력하세요.
hello python world
"""

wordList = input().split()

def printWord(word):
    return word

for word in wordList:
    result = printWord(word)
    print(result, end=" ")

print("------------------------------------")
"""
문제 3

문제 3
# 테스트 케이스마다 입력 값을 그대로 출력하세요.
3 # 테스트 케이스 수
1 
2 
3 
"""

trial = int(input())

for i in range(0, trial):
    print(int(input()))

print("------------------------------------")
"""
문제 4

# 2개 이상의 정수를 출력하세요.
2 0 3 92 3
"""

numTuple = tuple(map(int, input().split()))

for i in numTuple:
    print(i, end=" ")

print("------------------------------------")
"""
문제 5

# 2개의 정수를 출력하세요.
2 3

for k, v in Dictionary.items():
    print("{} : {}".format(k, v))

"""

a, b = map(int, input().split())
print(f"{a} {b}")

print("------------------------------------")
"""
문제 6

# 단어를 구분해서 출력하세요.
I am Programmer
"""

strList = list(input().split())

for i in strList:
    print(i, end=" ")

print("------------------------------------")
"""
문제 7

# 테스트 케이스마다 입력 값을 그대로 출력하세요.
5 # 테스트 케이스 수
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
"""

trial = int(input())
t = 0

while t < trial:
    numList = list(map(int, input().split()))
    t += 1
    for i in range(0, len(numList)):
        print(numList[i], end=" ")

print("------------------------------------")
"""
문제 8

# 테스트 케이스마다 입력 값을 그대로 출력하세요.
5 # 테스트 케이스 수
1 38 108 29 3 2 39
1 9 12 3 5 1
28 39 1 20 9 1
34 5 6 8
9 3 2 10 1 2 4
"""

trial = int(input())

for i in range(0,5):
    numList = map(int, input().split())
    for j in numList:
        print(j, end=" ")