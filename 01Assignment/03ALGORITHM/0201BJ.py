"""2525 오븐시계 https://www.acmicpc.net/problem/2525"""

# teammateVer


a, b = map(int,input().split())
c = int(input())

hr = a + ((b + c) // 60)
min = (b + c) % 60

if hr >= 24:
    hour = hr % 24
    min = (b + c) % 60

print(hr, min)

# myVer

hourNow, minNow = map(int, input().split())
minCook = int(input())

if minNow + minCook > 60:
    if hourNow + ((minNow + minCook)//60) > 23:
        print(((hourNow + ((minNow + minCook)//60))%24), ((minNow + minCook)%60))
    elif hourNow + ((minNow + minCook)//60) <= 23:
        print((hourNow + ((minNow + minCook)//60)), ((minNow + minCook)%60))
elif  minNow + minCook == 60:
    if hourNow + ((minNow + minCook)//60) > 23:
        print(0, 0)
    elif hourNow + ((minNow + minCook)//60) <= 23:
        print((hourNow + ((minNow + minCook)//60)), 0)
elif minNow + minCook < 60:
    print(hourNow, (minNow + minCook))

"""2798 블랙잭 https://www.acmicpc.net/problem/2798"""

# teacherVer

def blackjack(n, m, cards):
    max_total = 0 # 현재 가장 큰 합

    # 완전탐색(Brute-force)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]

                # 현재 가장 큰 합보다는 크고, m을 넘지 않아야 갱신
                if max_total < total <= m:
                    max_total = total

                # 합과 m이 같으면 더이상 탐색하는 의미가 없으므로 종료
                if total == m:
                    return total

    return max_total

a, b = map(int, input().split())
crds = list(map(int, input().split()))

print(blackjack(a, b, crds))

""" 틀림!!!! 왜!!!!! # myVer

n, m = map(int, input().split())
inptLi = list(map(int, input().split()))
min = m

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if abs(m - (inptLi[i] + inptLi[j] + inptLi[k])) <= min:
                min = abs(m - (inptLi[i] + inptLi[j] + inptLi[k]))
                abcLi = [inptLi[i], inptLi[j], inptLi[k]]
                

print(sum(abcLi))
"""

"""9076 점수 집계 https://www.acmicpc.net/problem/9076"""

# teammateVer

t = int(input())

for i in range(t):
    score = list(map(int, input().split()))
    score.sort()
    if (score[3] - score[1]) >= 4:
        print("KIN")
    else:
        print(sum(score[1:4]))

# myVer

import sys
inpt = sys.stdin.readline

for i in range(int(inpt())):
    numLi = list(map(int, input().split()))
    mx = max(numLi)
    mn = min(numLi)
    numLi.remove(mx)
    numLi.remove(mn)
    if max(numLi) - min(numLi) >= 4:
        print("KIN")
    else:
        print(sum(numLi))

"""1526 가장 큰 금민수 https://www.acmicpc.net/problem/1526"""

# teammateVer

n = int(input())
data = ["0", "1", "2", "3", "5", "6", '8', "9"]

while True:
    n_ = str(n)
    for d in data:
        if d in n_:
            n -= 1
            break
    else:
        print(n)
        break

# myVer

# 4와 7로만 이루어진 리스트 중 가장 작은값은 4니까 시작값 strt에 4 할당해두고 시작
strt = 4

# strt에 1씩 추가하면서 while문 돌 때 중복 여부와 관계 없이 4와 7로만 이루어지면 되니까 세트 활용
strtSt = set(str(strt).strip())
idx = -1

# 4와 7로만 이루어진 리스트 채우기 위해 numLi 비워두기
numLi = []

inpt = int(input())

while True:
    # 세트가 4 / 7 / 4 7 중에 하나면 (현재 strt 4 ; 세트에 4만 들어있음)
    if strtSt == {"4"} or strtSt == {"7"} or strtSt == {"4", "7"}:
        # 리스트에 추가
        numLi.append(strt)
        idx += 1
    # strt에 1씩 추가
    strt += 1
    # strt 값이 1 추가되면서 바꼈으니까 세트도 새로 할당해야됨
    strtSt = set(str(strt).strip())
    # 리스트에서 가장 큰 값 (가장 최근에 추가된 값)이 입력받은 값보다 크면 (입력값보다 작거나 같은 값을 출력해야되니까)
    if numLi[idx] > inpt:
        # while문 종료
        break

print(numLi[idx-1])

"""엥 이건 시간 초과 뜸
strt = 4
strtSt = set(str(strt).strip())
numLi = []
inpt = int(input())

while True:
    if strtSt == {"4"} or strtSt == {"7"} or strtSt == {"4", "7"}:        
        numLi.append(strt)       
    strt += 1    
    strtSt = set(str(strt).strip())    
    if max(numLi) > inpt:        
        numLi.pop()        
        break
    
print(max(numLi))

# 4와 7로만 이루어진 리스트 중 가장 작은값은 4니까 시작값 strt에 4 할당해두고 시작
# strt에 1씩 추가하면서 while문 돌 때 중복 여부와 관계 없이 4와 7로만 이루어지면 되니까 세트 활용
# 4와 7로만 이루어진 리스트 채우기 위해 numLi 비워두기
# 세트가 4 / 7 / 4 7 중에 하나면 (현재 strt 4 ; 세트에 4만 들어있음)
# 리스트에 추가
# strt에 1씩 추가
# strt 값이 1 추가되면서 바꼈으니까 세트도 새로 할당해야됨
# 리스트에서 가장 큰 값 (가장 최근에 추가된 값)이 입력받은 값보다 크면 (입력값보다 작거나 같은 값을 출력해야되니까)
# 리스트에서 가장 큰 값 (가장 최근에 추가된 값) 삭제
# while문 종료
"""

"""1436 영화감독 숌 https://www.acmicpc.net/status?user_id=ssong66&problem_id=1436&from_mine=1"""

strt = 666
idx = 0
numLi = []
inpt = int(input())

while True:
    if "666" in str(strt):
        numLi.append(strt)
        idx += 1
    strt += 1
    if idx > inpt:
        break

print(numLi[inpt - 1])