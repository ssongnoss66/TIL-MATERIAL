# 예제 01

dict_variable = {}
dict_variable["name"] = "David"
dict_variable["birthdate"] = "19000101"
dict_variable["job"] = "hypergrowth"

print(dict_variable["name"])
print(dict_variable["birthdate"])
print(dict_variable["job"])

"""
David
19000101
hypergrowth
"""

# 예제 02

dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"])
print(dict_variable["D"])
print(dict_variable["b"])

"""
A
d
@@ KeyError: 'b'
"""

# 예제 03

dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"])

"""
6000
"""

# 예제 04

dict_variable = {
    "name": "Tom",
    "birthdate": "19000101",
    "job": "hypergrowth",
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
name Tom
birthdate 19000101
job hypergrowth
"""

# 예제 5

dict_variable = {
    "name": "David",
    "birthdate": "19000101",
    "job": "hypergrowth",
}

for key, value in dict_variable.items():
    print(key, value)

"""
name David
birthdate 19000101
job hypergrowth
"""

# 예제 6

dict_variable = {
    "name": "Tom",
    "birthdate": "19000101",
    "job": "hypergrowth",
}

print("age" in dict_variable)

"""
@@ False
"""

# 예제 7

dict_variable = {
    "name": "Jane",
    "birthdate": "19000101",
    "job": "hypergrowth",
}

if "address" not in dict_variable:
    dict_variable["address"] = "Seoul"

"""
@@딕셔너리에 주소 없으면 추가 가능 ; 키와 값의 쌍 (키 있으면 값만도 추가 가능)
"""

print(dict_variable)
"""
dict_variable = {
    "name": "Jane",
    "birthdate": "19000101",
    "job": "hypergrowth",
    "address": "Seoul",
"""

# 예제 8

list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])

except:
    print("에러발생")
    print("에러의 원인은?")

"""
@@ EOF
> SyntaxError: unexpected EOF while parsing
list_variable = [0, 1, 2]
"""

# 예제 9

try:
    number = 1
    if number == 1:
        print(number)

except:
    print("에러가 발생했습니다")
    print("에러의 원인은 무엇인가요?")

"""
invalid syntax
if ...: ; ":" 빠짐
"""

# 예제 10

n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total)

"""
100

n 1
t 4
n 2
t 4+4
n 3
t 8+6
n 4
t 14+8
n 5
t 22+8
n 6
t 30+12
n 7
t 42+10
n 8
t 52+16
n 9
t 68+12
n 10
t 80+20 = 100
"""