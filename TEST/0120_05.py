"""직사각형 길이 찾기"""

for i in range(1, (int(input())+1)):
    numLi = list(map(int, input().split()))
    a = numLi[0]
    if numLi.count(a) == 1 or numLi.count(a) == 3:
        print(f"#{i} {numLi[0]}")
    else:
        while True:
            numLi.remove(a)
            if not numLi[0] == a:
                print(f"#{i} {numLi[0]}")
                break