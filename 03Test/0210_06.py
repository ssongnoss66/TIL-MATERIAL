"""Flatten https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV139KOaABgCFAYh&probBoxId=AYY1F7UqkrkDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+3%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""
from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline

for i in range(1, 11):
    dump = int(input())
    boxLi = sorted(list(map(int, input().split())))
    # print(f"dump {dump} boxLi {boxLi}")
    lngth = len(boxLi) - 1
    for j in range(dump):
        boxLi[lngth] -= 1
        boxLi[0] += 1
        boxLi = sorted(boxLi)
        # print(f"boxLi {boxLi}")
        mx = boxLi[lngth]
        mn = boxLi[0]
        # print(f"mx {mx} mn {mn}")
    print(f"#{i} {mx - mn}")

"""teammateVer
for t in range(1, 11):
    cnt = int(input())
    box = sorted(map(int, input().split()))

    while cnt > 0:
        a = box.pop() -1
        b = box.pop(0) + 1

        box.append(a)
        box.append(b)
        box.sort()
        cnt -= 1

        if (max(box) - min(box)) == 0:
            break
        if (max(box) - min(box)) == 1:
            break

    print(f'#{t} {max(box) - min(box)}')
"""