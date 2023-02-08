# 1000

a, b = map(int, input().split())
print(a+b)

# 2558

a = int(input())
b = int(input())
print(a+b)

# 10950

howMany = int(input())

for i in range(1,howMany+1):
    print(sum(list(map(int, input().split()))))
    i += 1

# 10953

t = int(input())

for i in range(0, t):
    a, b = map(int, input().split(","))
    print(a + b)

# 11021

import sys
input = sys.stdin.readline

trial = int(input())

for i in range(0, trial):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")

# 11022

import sys
input = sys.stdin.readline

trial = int(input())
for i in range(0, trial):
    a,b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")