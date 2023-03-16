"""
1110

문제
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

출력
첫째 줄에 N의 사이클 길이를 출력한다.
"""
# SSAEM ver

inputNum = str(input())
N = inputNum

cnt = 0
while True:
    if int(N) < 10:
        N = "0" + N
    first = N[-1]
    second = N[0]
    sum_number = int(first) + int(second)

    new_number = N[-1] + str(sum_number)[-1]
    print(new_number)

    cnt +=1

    if new_number == inputNum:
        break

    N = new_number

print(cnt)

# my ver

inputNum = int(input())
num = inputNum
circ = 0

while True:
    leftNum = num // 10
    if num < 10:
        leftNum = 0
    rightNum = num % 10
    if rightNum + leftNum >= 10:
        newNum = (rightNum * 10) + ((rightNum + leftNum) % 10)
    elif rightNum + leftNum < 10:
        newNum = (rightNum * 10) + (rightNum + leftNum)
    circ += 1
    if inputNum == newNum:
        break
    num = newNum

print(circ)

# 부등호로 조건 걸 때..... = 빠지지 않았는지 확인.......

"""
10952

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

입력의 마지막에는 0 두 개가 들어온다.

출력
각 테스트 케이스마다 A+B를 출력한다.
"""

while True:
    hap = sum(int(i) for i in map(int, input().split()))
    if hap == 0:
        break
    print(hap)

# while문 순서... 변수를 정의하고 > break 조건 걸고 > 출력문 설정
  
"""
3009

문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
"""
aLi = []
bLi = []

for i in range(3):
    a, b = map(int, input().split())
    aLi.append(a)
    bLi.append(b)

for j in range(3):
    if aLi.count(aLi[j]) == 1:
        aPrint = aLi[j]
    if bLi.count(bLi[j]) == 1:
        bPrint = bLi[j]

print(f"{aPrint} {bPrint}")
    

"""
10824

문제
네 자연수 A, B, C, D가 주어진다. 이때, A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구하는 프로그램을 작성하시오.

두 수 A와 B를 합치는 것은 A의 뒤에 B를 붙이는 것을 의미한다. 즉, 20과 30을 붙이면 2030이 된다.

입력
첫째 줄에 네 자연수 A, B, C, D가 주어진다. (1 ≤ A, B, C, D ≤ 1,000,000)

출력
A와 B를 붙인 수와 C와 D를 붙인 수의 합을 출력한다.
"""

a, b, c, d = map(str, input().split())
print(int(a + b) + int(c + d))

"""
9085

문제
10보다 작거나 같은 자연수 N개를 주면 합을 구하는 프로그램을 작성하시오.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 첫 줄에 자연수의 개수 N(1 ≤ N ≤ 100)이 주어지고, 그 다음 줄에는 N개의 자연수가 주어진다. 
각각의 자연수 사이에는 하나씩의 공백이 있다.

출력
각 테스트 케이스에 대해서 주어진 자연수의 합을 한 줄에 하나씩 출력한다.
"""

t = int(input())

for i in range(t):
    n = int(input())
    print(sum(i for i in map(int, input().split())))