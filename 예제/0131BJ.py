"""2441 별 찍기 -4 https://www.acmicpc.net/problem/2441"""

n = int(input())

for i in range(n):
    print(" "*i+"*"*(n - i))

"""2592 대표값 https://www.acmicpc.net/problem/2592"""

numLi = []

for _ in range(10):
    numLi.append(int(input()))

mxCnt = 0
mxLi = []

for i in set(numLi):
    if numLi.count(i) > mxCnt:
        mxCnt = numLi.count(i)

for j in numLi:
    if numLi.count(j) == mxCnt:
        mxLi.append(j)


print(sum(numLi) // 10)
print(*set(mxLi))

"""10798 세로읽기 https://www.acmicpc.net/problem/10798"""

garo = [input().rstrip() for _ in range(5)]

if not len(min(garo, key=len)) == len(max(garo, key=len)):
    for i in garo:
        mxLn = len(max(garo, key=len))
        if mxLn > len(i):
            indx = garo.index(i)
            for j in range(mxLn - len(i)):
                i = i + "*"
            garo[indx] = i

sero = ["".join(i) for i in zip(*garo)]

print(("".join(sero)).replace("*",""))

# 리스트를 문자열로 합치는 경우 "".join(리스트)
# 문자열에서 특정 문자 제거 문자열.replace(대체하고싶은놈, 대체할놈)

"""9455 박스 https://www.acmicpc.net/problem/9455"""

for i in range(int(input())):
    m, n = map(int, input().split())
    garo = [input().rstrip() for _ in range(m)]
    sero = ["".join(i) for i in zip(*garo)]
    hap = 0
    for j in sero:
        li = list(j)
        cnt = li.count("1")
        num = (len(li) - cnt)
        # print(f"li {li}일 때 리스트 안에 1은 {cnt}개 있고 리스트의 길이인 5에서 1의 갯수 {cnt}를 뺀 {num}으로 인덱스 위치를 바꿔준다")
        for k in range(len(li)):
            if li[k] == "1":
                hap += (num - k)
                # print(f"k의 인덱스 {k}를 {num}으로 옮기기 위해서 {num - (k)}칸을 움직여야 하고 지금까지 {hap} 칸 움직임")
                num += 1
    print(hap)

# 문자열 한 글자씩 분리하여 리스트 저장할 때는 걍 list(문자열)하면 됨

"""1652 누울 자를 찾아라 https://www.acmicpc.net/problem/1652"""

# internetVer

import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
# print(f"arr {arr}")
arr_h = [''.join(i) for i in zip(*arr)]
# print(f"arr_h {arr_h}")
h, v = 0, 0

for i in range(n): 
    for j in arr[i].split('X'):
        if '..' in j:
            h += 1
    for j in arr_h[i].split('X'):
        if '..' in j:
            v += 1

print(h,v)

# zip() ; 리스트 여러개에서 같은 인덱스에 해당하는 요소들끼리 묶어줌

""" 반례가 있는데...못찾겠음............
n = int(input())
matrix = []
garo = 0
sero = 0

for i in range(n):
    inptLn = input()                            # 문자열로 입력받음
    line = list(map(str, inptLn.strip()))       # 쪼개서 리스트로 넣기
    if line.count("X") > 0:                     # X가 하나라도 있으면
        newLi = inptLn.split("X")               # X 기준으로 쪼개기
        for j in newLi:                         
            if len(j) >= 2:                     # "."로 이루어진 쪼개진 리스트의 길이가 2와 같거나 크면
                garo += 1                       # 누울 자리 += 1
                print(f"{inptLn}일 때 쪼개면 {newLi}되니까 누울 자리는 {garo}")
    else:
        garo += 1
    matrix.append(line)

rotatedMtrx = [[0]*n for _ in range(n)]         

for i in range(n):
    for j in range(n):
        rotatedMtrx[i][j] = matrix[j][n-i-1]

print(rotatedMtrx)

for i in rotatedMtrx:
    ln = i
    seroLn = "".join(str(s) for s in ln)
    if ln.count("X") > 0:
        nLi = seroLn.split("X")
        for j in nLi:
            if len(j) >= 2:
                sero += 1
    else:
        sero += 1

print(garo, sero)
"""