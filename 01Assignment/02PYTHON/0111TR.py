# 1

numList = list(map(int, input().split()))

for i in numList:
    print(i, end=" ")
    
# 2

print(input())

# 3

testCase = int(input())
whatCase = 0

while whatCase < testCase:
    whatCase += 1
    inputLine = int(input())
    for i in range(0, inputLine):
        print(int(input()))

# 4

testCase = int(input())

for i in range(0, testCase):
    inputLine = int(input())
    for j in range(0, inputLine):
        numList = list(map(str, input().split()))
        print(" ".join(numList))

# 5

testCase = int(input())

for i in range(0, testCase):
    inputLine = int(input())
    whatLine = 0
    while whatLine < inputLine:
        print(input())
        whatLine += 1

# 6

testCase = int(input())
inputLine = int(input())
whatCase = 0

while whatCase < testCase:
    whatCase += 1
    whatLine = 0
    while whatLine < inputLine:
        whatLine += 1
        numList = list(map(str, input().split()))
        print(" ".join(numList))

# 7

testCase, inputLine = map(int,input().split())

for i in range(0, testCase):
    for j in range(0, inputLine):
        print(input())

# 8

a,b = map(int, input().split())

for i in range(0, a):
    for j in range(0, b):
        numList = list(map(str, input().split()))
        string = ""
        for k in numList:
            string += k
        print(" ".join(string))

# 9

a,b = map(int, input().split())

for i in range(0, a):
    for j in range(0, b):
        numList = list(map(str, input().split()))
        print(" ".join(numList))

# 리스트 내장 메소드 ; "여기 들어간 걸 기준으로 구분".joint(리스트명)