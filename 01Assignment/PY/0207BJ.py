"""17608 막대기 https://www.acmicpc.net/problem/17608"""

import sys
input = sys.stdin.readline

num = int(input())
stckLi = []

for i in range(num):
    stckLi.append(int(input()))

stndrd = stckLi.pop()
stckLi = list(reversed(stckLi))
prnt = 1
mx = 0

# print(f"stndrd {stndrd} stckLi {stckLi}")

for j in stckLi:
    if stndrd < j and mx < j:
        prnt += 1
        mx = j

print(prnt)

"""7568 덩치 https://www.acmicpc.net/problem/7568"""

dcLi = []
num = int(input())

for i in range(num):
    dcLi.append(list(map(int, input().split())))

# print(dcLi)
# [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]

j = 0
prntLi = [0 for _ in range(num)]

while True:
    if j == num:
        break
    cnt = 0
    for k in range(num):
        if j == k:
            pass
        elif dcLi[j][0] < dcLi[k][0] and dcLi[j][1] < dcLi[k][1]:
            cnt += 1
    prntLi[j] = cnt + 1
    # print(f"j {j} prntLi {prntLi}")
    j += 1

print(*prntLi)

"""1063 킹 https://www.acmicpc.net/problem/1063"""

k, s, n = input().split()
kPlace = list(map(int, [ord(k[0]) - 64, k[1]]))
sPlace = list(map(int, [ord(s[0]) - 64, s[1]]))

dm = {
    "R" : [1, 0],
    "L" : [-1, 0],
    "B" : [0, -1],
    "T" : [0, 1],
    "RT" : [1, 1],
    "LT" : [-1, 1],
    "RB" : [1, -1],
    "LB" : [-1, -1]
}
        
for _ in range(int(n)):
    i = input()
    kx = kPlace[0] + dm[i][0]
    ky = kPlace[1] + dm[i][1]
    if 0 < kx <= 8 and 0 < ky <= 8:
        if [kx, ky] == sPlace:
            # print(f"돌이랑 자리 같아서 돌 이동 전 sPlace {sPlace} kPlace {kPlace}")
            sx = sPlace[0] + dm[i][0]
            sy = sPlace[1] + dm[i][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                sPlace = [sx, sy]
                kPlace = [kx, ky]
                # print(f"돌 이동 후 sPlace {sPlace} kPlace {kPlace}")
            # else:
            #     print(f"체스판 밖으로 나가서 킹돌 이동 없이 sPlace {sPlace} kPlace {kPlace}")
        else:
            kPlace = [kx, ky]
            # print(f"돌이랑 자리 달라서 돌 이동 없이 sPlace {sPlace} kPlace {kPlace}")
    # else:
    #     print(f"체스판 밖으로 나가서 킹돌 이동 없이 sPlace {sPlace} kPlace {kPlace}")

print(f"{chr(kPlace[0] + 64)}{kPlace[1]}")
print(f"{chr(sPlace[0] + 64)}{sPlace[1]}")
