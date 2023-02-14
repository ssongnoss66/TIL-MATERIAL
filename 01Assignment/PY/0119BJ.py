"""
2576 홀수 https://www.acmicpc.net/problem/2576
"""

oddNum = []

for i in range(7):
    num = int(input())
    if num % 2 == 1:
        oddNum.append(num)  

if len(oddNum) > 0:
    print(sum(oddNum))
    print(min(oddNum))
else:
    print(-1)
    
"""
10822 더하기 https://www.acmicpc.net/problem/10822
"""

print(sum(map(int, input().split(","))))

"""
2754 학점게산 https://www.acmicpc.net/problem/2754
"""

scoreDict = {
    "A+": 4.3,
    "A0": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B0": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C0": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D0": 1.0,
    "D-": 0.7,
    "F": 0.0,
}

print(scoreDict.get(input()))


"""
5622 다이얼 https://www.acmicpc.net/problem/5622
"""

# 34852kb 112 ms

import string
alph = list(string.ascii_uppercase)

phoneDict = {}

for i in range(2, 10):
    if i < 7 or i == 8:
        phoneDict[i+1] = alph[0:3]
        alph = alph[3::]
    if i == 7:
        phoneDict[i+1] = alph[0:4]
        alph = alph[4::]
    if i == 9:
        phoneDict[i+1] = alph

def get_key(val):
    for key, value in phoneDict.items():
         if val == value:
             return key

hap = 0
wordInpt = map(str, input().strip())

for k in wordInpt:
    for j in phoneDict.values():
        if k in j:
            num = get_key(j)
            hap += num

print(hap)

"""
2577 숫자의 개수 https://www.acmicpc.net/problem/2577
"""

# 30616kb 40ms

a = int(input())
b = int(input())
c = int(input())
abc = a*b*c
numDict = {}

for i in range(0, 10):
    numDict[i] = str(abc).count(str(i))

print("\n".join(map(str, numDict.values())))

"""
곱한 값을 str()해서 비교할거면 i도 str()해야됨
"""


"""
7785 회사에 있는 사람 https://www.acmicpc.net/problem/7785
"""

# 48464kb / 4896ms

n = int(input())
commuteDict = {}

for i in range(n):
    k, v = map(str, input().split())
    commuteDict[k] = v

print("\n".join(sorted([k for k, v in commuteDict.items() if v == "enter"], reverse = True)))

# 48060kb / 3940ms

commuteDict = {}

for i in range(int(input())):
    k, v = input().split()
    if v == "enter":
        commuteDict[k] = v
    else:
        commuteDict.pop(k)

print("\n".join(sorted(commuteDict.keys())[::-1]))

# 42260kb / 3936ms

commuteSet = set()

for i in range(int(input())):
    k, v = input().split()
    if v == "enter":
        commuteSet.add(k)
    else:
        commuteSet.remove(k)

print("\n".join(sorted(commuteSet)[::-1]))

# 50752kb / 176 ms

s = set()
_, * l = open(0)
for c in l:
    n, a = c.split()
    if a[0] == 'e':
        s.add(n)
    else:
        s.remove(n)
print(*sorted(s)[::-1], sep='\n')

"""
딕셔너리에서 값에 따른 키 값 반환 ; k for k, v in Dictionary.items() if v == value
리스트 역순 정렬 ; sorted(List, reverse = True)
세트 역순 정렬 ; sorted(Set[::-1])
리스트 개행 출력 ; print("\n".join(List))
"""
