"""신용카드 만들기 1"""

inptNum = int(input())
num = 0

while True:
    num += 1
    inptLi = list(map(int, input().split()))
    oddHap = 0
    evenHap = 0
    rpt = 0
    for i in inptLi:
        rpt += 1
        if rpt % 2 == 1:
            oddHap += i*2
        else:
            evenHap += i
    if ((oddHap + evenHap) % 10) == 0:
        print(f"#{num} 0")
    else:
        n = 10 - ((oddHap + evenHap) % 10)
        print(f"#{num} {n}")
    if num == inptNum:
        break