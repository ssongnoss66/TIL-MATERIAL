# 01

num = int(input("자연수를 입력하세요 : "))
num = num + 10
print(num)

# 02

food = input("좋아하는 음식을 입력하세요 : ")
print("좋아하는 음식 : ", food)

# 03

name = input("이름을 입력하세요 : ")
birthYear = 2023 - int(input("태어난 연도를 입력하세요 : "))
print("저의 이름은", name, "이고, 올해 나이는", birthYear, "입니다.")

# 04
sentenceA = input("첫 번째 문장을 입력해주세요 : ")
sentenceB = input("두 번째 문장을 입력해주세요 : ")
print(sentenceA + sentenceB)

# 05
num = int(input("자연수를 입력하세요 : "))
num = num - (num * 2)
print(num)

# 06
num1 = int(input("첫 번째 자연수를 입력하세요 : "))
num2 = int(input("두 번째 자연수를 입력하세요 : "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1//num2)
print(num1%num2)

# 07
num1 = int(input("첫 번째 자연수를 입력하세요 : "))
num2 = int(input("두 번째 자연수를 입력하세요 : "))
num3 = int(input("세 번째 자연수를 입력하세요 : "))
print((num1 + num2 + num3)//3)

# 08
numList = []
num1 = int(input("첫 번째 자연수를 입력하세요 : "))
num2 = int(input("두 번째 자연수를 입력하세요 : "))
num3 = int(input("세 번째 자연수를 입력하세요 : "))
num4 = int(input("네 번째 자연수를 입력하세요 : "))
num5 = int(input("다섯 번째 자연수를 입력하세요 : "))
numList = [num1, num2, num3, num4, num5]
print(numList)

# 09
string = input("문자열을 입력해주세요 : ")
num = int(input("자연수를 입력해주세요 : "))
print(string*num)

# 10
num1 = int(input("첫 번째 자연수를 입력하세요 : "))
sum1 = num1
print(sum1)
num2 = int(input("두 번째 자연수를 입력하세요 : "))
sum2 = sum1 + num2
print(sum2)
num3 = int(input("세 번째 자연수를 입력하세요 : "))
sum3 = sum2 + num3
print(sum3)
num4 = int(input("네 번째 자연수를 입력하세요 : "))
sum4 = sum3 + num4
print(sum4)
num5 = int(input("다섯 번째 자연수를 입력하세요 : "))
sum5 = sum4 + num5
print(sum5)