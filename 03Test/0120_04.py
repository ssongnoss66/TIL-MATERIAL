"""소득 불균형"""

for i in range(1, (int(input())+1)):
    prnt = 0
    howMany = int(input())
    incomeLi = list(map(int, input().split()))
    for j in incomeLi:
        if j <= (sum(incomeLi) / howMany):
            prnt += 1
    print(f"#{i} {prnt}")