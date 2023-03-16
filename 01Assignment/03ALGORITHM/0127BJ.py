"""10817 세 수 https://www.acmicpc.net/problem/10817"""

inptLi = sorted(list(map(int, input().split())))

print(inptLi[(len(inptLi) - 2)])

"""20001 고무오리 디버깅 https://www.acmicpc.net/problem/20001"""

inptLi = []

while True:
    wrd = input()
    if wrd == "고무오리 디버깅 시작":
        pass
    elif wrd == "고무오리 디버깅 끝":
        if inptLi.count("문제") == 0:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break
    else:
        if wrd == "문제":
            inptLi.append(wrd)        
        elif wrd == "고무오리":
            if inptLi.count("고무오리") + 1 > inptLi.count("문제"):
                inptLi.append("문제")
                inptLi.append("문제")
            else:
                inptLi.remove(inptLi[0])



"""1269 대칭 차집합 https://www.acmicpc.net/problem/1269"""

a, b = map(int, input().split())

aSt = set(map(int, input().split()))
bSt = set(map(int, input().split()))

print((len(aSt - bSt))+(len(bSt - aSt)))

"""3052 나머지 https://www.acmicpc.net/problem/3052"""

remainderSet = set()

for i in range(10):
    remainder = (int(input())) % 42
    remainderSet.add(remainder)

print(len(remainderSet))

"""1181 단어 정렬 https://www.acmicpc.net/problem/1181"""

import heapq
heap = []
num = int(input())
for i in range(num):
    wrd = input()
    if not (len(wrd), wrd) in heap:
        heapq.heappush(heap, (len(wrd), wrd))

for j in range(num):
    try:
        print(heapq.heappop(heap)[1])
    except:
        break

"""11286 절댓값 힙  https://www.acmicpc.net/problem/11286"""

import sys
inpt = sys.stdin.readline

import heapq
heap = []

for i in range(int(inpt())):
    num = int(inpt())
    if not num == 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

# abs() ; 절댓값
# heapq.heappop(heap)[1] ; 리스트에서의 pop()과 마찬가지로 반환하고 "삭제"