# 문제 01

word = input("문자열 입력 : ")
howManyword = 0

for char in word:
  if char == "e":
    howManyword += 1

print(f"e: {howManyword}")

"""
for 문으로 word 문자열의 인덱스 당 문자 한하나 돈다
if char == "e" ; 할당연산자가 아니라 비교연산자!!
문자열 앞에 f" 붙이면 f-string 됨 ; 중괄호 사용하면 f-string 안에 파이썬 표현식 삽입 가능
"""

# 문제 02

word = input("문자열 입력 : ")
vowel = "aeiouAEIOU"
howmanyVowel = 0

for char in word:
    if char in vowel:
        howmanyVowel += 1

print(howmanyVowel)

"""
모음이 뭔지 정의할 때 리스트가 아니라 그냥 문자열 ""형태로
"""

# 문제 03

dictInfo = {
    "name": "Tom",
    "birthdate": "20000101",
    "job": "hypergrowth",
}

age = 2023 - (int(dictInfo["birthdate"])//10000) + 1
print("나이 : ", age, "세")

# 문제 04

dictInfo = {
    "name": input("이름을 입력하세요 : "),
    "number": input("전화번호를 입력하세요 : "),
    "address": input("거주지를 입력하세요 : "),
}

print(dictInfo)
print("name", ":", dictInfo["name"])
print("number", ":", dictInfo["number"])
print("address", ":", dictInfo["address"])

# 문제 05

name = input("이름을 입력하세요 : ")

infoDict = {
    "number" : input("전화번호를 입력하세요 : "),
    "email" : input("이메일을 입력하세요 : "),
    "address" : input("거주지를 입력하세요 : "),
}

print(name, ":", infoDict)

# 문제 06

# 문제 06

word = input("문자열 입력 : ")
howmanyWord = {}

for char in word:
    if char in howmanyWord:
        howmanyWord[char] += 1
    else:
        howmanyWord[char] = 1

for char, count in howmanyWord.items():
    print(f"{char}: {count}")

"""
for char in word:                   # e
    else:                           
        howmanyWord[char] = 1       # e: 1
for char in word:                   # l
    else:
        howmanyWord[char] = 1       # l: 1
for char in word:                   # e
    if char in howmanyWord:         
        howmanyWord[char] += 1      # e: 2
for char in word:                   # m
    else:
        howmanyWord[char] = 1       # m: 1
        for char in word:           # e
    if char in howmanyWord:         
        howmanyWord[char] += 1      # e: 3
for char in word:                   # n
    else:
        howmanyWord[char] = 1       # n: 1
for char in word:                   # t
    else:
        howmanyWord[char] = 1       # t: 1
"""