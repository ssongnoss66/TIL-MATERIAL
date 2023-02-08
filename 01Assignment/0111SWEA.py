"""
2047

신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.

입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.

[예제 풀이]

The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.

위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.

THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.


[제약 사항]

문자열의 최대 길이는 80 bytes 이다.


[입력]

입력으로 80 bytes 이하의 길이를 가진 문자열이 주어진다.


[출력]

문자열의 소문자를 모두 대문자로 변경한 결과를 출력한다.
"""

print(input().upper())

"""
2025

1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

단, 주어질 숫자는 10000을 넘지 않는다.


[예제]

주어진 숫자가 10 일 경우 출력해야 할 정답은,

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
"""

print(sum(range(1,(int(input())+1))))

"""
1936

A와 B가 가위바위보를 하였다.

가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.

A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

 

[입력]

입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.

 
 

[출력]

A가 이기면 A, B가 이기면 B를 출력한다.
"""

abDict = {
    (1, 2): 'B', 
    (2, 3): 'B', 
    (3, 1): 'B', 
    (2, 1): 'A', 
    (3, 2): 'A', 
    (1, 3): 'A'
}

abList = list(map(int, input().split()))
result = abDict.get(tuple(abList))
print(result)

# dict.get(key, default=None) ; 딕셔너리 메소드, 딕셔너리에 키가 있으면 해당 키에 대한 값을 반환
# tuple(list) ; list to tuple

"""
2027

주어진 텍스트를 그대로 출력하세요.
"""

for i in range(1, 6):
    print("+"*(i-1)+"#"+"+"*(5-i))
"""
2058

하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.


[제약 사항]

자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)


[입력]

입력으로 자연수 N이 주어진다.


[출력]

각 자릿수의 합을 출력한다.
"""

num = int(input())
hap = 0

while num > 0:
    hap += (num % 10)
    num = num//10

print(hap)

"""
2019

1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

주어질 숫자는 30을 넘지 않는다.
"""

num = int(input())
 
for i in range(0, num+1):
    i = 2 ** i
    print(i, end=" ")