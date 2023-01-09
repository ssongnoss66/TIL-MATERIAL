# 1
 
word = input()
wordList = list(word)
indx = 0

for i in wordList:
    if not i == "e":
        indx += 1
        if indx == len(word):
            print(-1)
    elif i == "e":
        print(indx)
            

# 2

wordList = list(input().split())
wordDict = {}

for i in wordList:
    if i in wordDict:
        wordDict[i] += 1
    elif i not in wordDict:
        wordDict[i] = 1

for k, v in wordDict.items():
    print("{} {}".format(k, v))

# 3

wordList = list(input())

for i in wordList:
    if i == "e":
        wordList.remove("e")

for i in wordList:
    print(i, end=" ")

print("----------------------------------")

# 4

wordAlph = input().split()
wordList = list(wordAlph[0])
alphNum = 0

for i in wordList:
    if i == wordAlph[1]:
        alphNum += 1

print(alphNum)

# 5

threeWord = input().split()
print(f"{threeWord[0]}-{threeWord[1]}-{threeWord[2]}")

# 6

num = int(input())
digitSum = 0

if num <= 0:
    print(-1)
else:
    while num > 0:
        digitSum += (num%10)
        num = num//10

print(digitSum)