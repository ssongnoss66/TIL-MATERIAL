"""창용 마을 무리의 개수 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AWngfZVa9XwDFAQU&probBoxId=AYY1F7UqkrkDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+3%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline



for i in range(1, int(input())+1):
    print("---------------------------")
    n, m = map(int, input().split())
    rltnLi = [[] for _ in range(n+1)]
    for j in range(m):
        x, y = map(int, input().split())
        rltnLi[x].append(y)
    print(rltnLi)
    
