"""최빈수구하기"""

for i in range(int(input())):
    caseNum = int(input())
    scoreLi = list(map(int, input().split()))
    countLi = []
    for j in scoreLi:
        countLi.append(scoreLi.count(j))
        if max(countLi) == scoreLi.count(j):
            prnt = j
        else:
            pass
    print(f"#{caseNum} {prnt}")