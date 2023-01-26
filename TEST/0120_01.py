"""신용카드 만들기 2"""

inptNum = int(input())
num = 0

while True:
    num += 1
    numLi = list(map(int, (input().replace("-", "")).strip()))
    if numLi[0] == 3 or numLi[0] == 4 or numLi[0] == 5 or numLi[0] == 6 or numLi[0] == 9:
        if len(numLi) == 16:
            print(f"#{num} 1")
        else:
            print(f"#{num} 0")
    else:
        print(f"#{num} 0")
    if num == inptNum:
        break