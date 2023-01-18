"""9498 시험성적"""

score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

"""9093 단어뒤집기"""

t = int(input())

for i in range(t):
    sentenceLi = map(str, input().split())
    reverseLi = []
    for j in sentenceLi:
        reverseLi.append(j[::-1])
    print(" ".join(reverseLi))

# 문자열 슬라이싱 문자열[::-1]

"""11721 열개씩 끊어 출력하기"""
splitLi = list(input())

while True:
    print("".join(splitLi[:10]))
    if len(splitLi) < 10:
        break
    splitLi = splitLi[10:]

# 리스트 슬라이싱...

"""2947 나무 조각"""

numLi = list(map(int, input().split()))

while True:
    for i in range(4):
        if numLi[i] > numLi[i+1]:
            numLi[i], numLi[i+1] = numLi[i+1], numLi[i]
            print(*numLi)
            print(" ".join(map(str, numLi)))
    if numLi == [1, 2, 3, 4, 5]:
        break

# 리스트 요소 위치 변경
# map 함수 활용
# print(* ); 예쁘게 출력!