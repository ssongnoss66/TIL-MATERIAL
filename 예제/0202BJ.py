"""1547 공 https://www.acmicpc.net/problem/1547"""

import sys
inpt = sys.stdin.readline

ballLi = [0, 1, 1]

for _ in range(int(inpt())):
    x, y = map(int, inpt().split())
    ballLi[x - 1], ballLi[y - 1] = ballLi[y - 1], ballLi[x - 1]

print(ballLi.index(0) + 1)

# 리스트 자리바꾸기 ; 리스트[인덱스a], 리스트[인덱스b] = 리스트[인덱스b], 리스트[인덱스a]

"""5576 콘테스트 https://www.acmicpc.net/problem/5576"""

import sys
inpt = sys.stdin.readline
numLia = []

for i in range(10):
    num = int(inpt())
    if len(numLia) >= 3:
        if min(numLia) < num:
            idx = numLia.index(min(numLia))
            numLia.pop(idx)
            numLia.insert(idx, num)
    else:
        numLia.append(num)

numLib = []

for i in range(10):
    num = int(inpt())
    if len(numLib) >= 3:
        if min(numLib) < num:
            idx = numLib.index(min(numLib))
            numLib.pop(idx)
            numLib.insert(idx, num)
    else:
        numLib.append(num)

print(f"{sum(numLia)} {sum(numLib)}")

"""2846 오르막길 https://www.acmicpc.net/problem/2846"""

import sys
inpt = sys.stdin.readline
num = int(inpt())
numLi = list(map(int, input().split()))

"""1251 단어나누기 https://www.acmicpc.net/problem/1251"""
import sys
inpt = sys.stdin.readline
wrd = input()

# 사전순으로 정리하기 위해 리스트에 받기 위해 dictLi 비워둡니다
dictLi = []

# 적어도 길이가 1 이상이어야 하기 때문에 범위는 단어 길이에서 -2로 설정합니다
for i in range(len(wrd) - 2):
    # 입력받은 문자열의 첫번째 요소부터 i번째 요소까지 슬라이싱한 뒤 > 뒤집어서 a에 할당합니다
    a = (wrd[0:(i + 1)])[::-1]

    # 범위는 a가 끝난 다음부터 시작해야 하고 길이가 1 이상이어야 하기 때문에 i+1 부터 단어 길이 -1 까지로 설정합니다
    for j in range((i + 1), (len(wrd) - 1)):
        b = (wrd[(i + 1):(j + 1)])[::-1]
        for k in range((j + 1), (len(wrd))):
            c = (wrd[(j + 1)::])[::-1]
            # 비워둔 리스트 dictLi에 a, b, c를 순서대로 합쳐서 넣어줍니다
            dictLi.append(a + b + c)

# 리스트를 알파벳 순으로 나열한 후 첫번째 요소를 출력합니다
print(sorted(dictLi)[0])