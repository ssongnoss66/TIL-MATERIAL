"""10101 삼각형 외우기 https://www.acmicpc.net/problem/10101"""

a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b or b == c or c == a:
        if a == b == c == 60:
                print("Equilateral")
        else:
            print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")        

"""2720 세탁소 사장 동혁 https://www.acmicpc.net/problem/2720

1달러 = 100센트
0.25달러 = 25센트 = 1쿼터
0.10달러 = 10센트 = 1다임
0.05달러 = 5센트 = 1니켈
0.01달러 = 1센트 = 1페니
"""

# myVer

for i in range(int(input())):
    chng = int(input())
    q = chng // 25
    chng = chng % 25
    d = chng // 10
    chng = chng % 10
    n = chng // 5
    p = chng % 5
    print(f"{q} {d} {n} {p}")

# teamVer

n = int(input())

for _ in range(n):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money // i, end=' ')
        money = money % i

"""1453 피시방 알바 https://www.acmicpc.net/problem/1453"""

# myVer

guestN = int(input())
seatNum = list(map(int, input().split()))
seatStack = []
rfs = 0

for i in seatNum:
    if i in seatStack:
            rfs += 1
    else:
        seatStack.append(i)

print(rfs)

# googleVer

N = int(input())
seats = list(map(int, input().split()))
s = len(list(set(seats)))
print(N - s)

"""10773 제로 https://www.acmicpc.net/problem/10773"""

numLi = []

for k in range(int(input())):
    num = int(input())
    if num == 0:
        numLi.pop()
    else:
        numLi.append(num)

print(sum(numLi))

"""2161 카드1 https://www.acmicpc.net/problem/2161"""

# ssaemVer ; Deque

from collections import deque

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    print(queue.popleft(), end=" ")
    queue.append(queue.popleft())

print(queue[0])

# myVer
n = int(input())
numLi = list(range(1, n+1))

prntLi = []

while True:
    if len(numLi) == 1:
        break
    prntLi.append(numLi[0])
    del numLi[0]
    numLi.append(numLi[0])
    del numLi[0]
    

prntLi.append(numLi[0])
print(*prntLi)

"""9012 괄호 https://www.acmicpc.net/problem/9012"""

for i in range(int(input())):
    stack = []
    inpt = input()
    for j in inpt:
        if j == "(":
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")