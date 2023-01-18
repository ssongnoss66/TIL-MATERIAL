"""2789 유학금지"""

word = input()

for i in ["C", "A", "M", "B", "R", "I", "D", "G", "E"]:
    word = word.replace(i, "")

print(word)

# .strip() / .replace( , )

"""2675 문자열 반복"""

trial = int(input())

for i in range(trial):
    inputLi = list(map(str, input().split()))
    r = int(inputLi[0])
    word = inputLi[1]
    printLi = []
    for j in range(len(word)):
        printLi.append(word[j]*r)
    print("".join(printLi))
        
# "".join(리스트명)

"""10988 펠린드롬"""
 
word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)

"""17249 태보태보 총난타"""

stringLi = list(input().split("(^0^)"))
printLi = []

for string in stringLi:
    printLi.append(str(string.count("@")))

print(" ".join(printLi))

# "".join(리스트명)

"""2941 크로아티아 알파벳"""

# my ver

wordInput = input()
word = wordInput
cnt = 0
cntLi = []

for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    cnt += word.count(i)
    wordNew = word.replace(i, ".")
    word = wordNew
    
print(cnt+len(word.replace(".", "")))

# teammate ver

wordInput = input()
word = wordInput
cnt = 0
cntLi = []

for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    cnt += wordInput.count(i)
    
print(len(wordInput) - cnt)

# teammate ver

wordInput = input()
word = wordInput
cnt = 0
cntLi = []

croat = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in croat:
    word = word.replace(i,"#")
print(len(word))

"""10809 알파벳 찾기"""

# my ver

s = input()
import string 
alph = list(string.ascii_lowercase)
alphLi = []

for i in alph:
    if s.count(i) > 0:
        alphLi.append(str(s.index(i)))
    else:
        alphLi.append("-1")

print(" ".join(alphLi))

# teammate ver

for i in alph:                      # 알파벳 순회
    alphLi.append(s.find(i))        # 비워둔 리스트에 순회한 알파벳 (a, b, c ...)이 몇 개 있는지 반환 (find 매서드는 없으면 -1 반환)

print(*alphLi)

"""
import string 
alph = list(string.ascii_lowercase)

for i in alph:
    print(S.find(chr(i))) 
"""

# import string 
# string.ascii_lowercase
# .find()