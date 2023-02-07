"""파리 퇴치 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV5PzOCKAigDFAUq&probBoxId=AYYQ-fnKCuYDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+2%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

from pprint import pprint

for _ in range(1, (int(input())+1)):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        line = list(map(int, input().split()))
        matrix.append(line)
    