"""모음이 보이지 않는 사람 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AWNcD_66pUEDFAV8&probBoxId=AYY1F7UqkrkDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+3%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline

mo = "aeiou"

for i in range(1, int(input())+1):
    prnt = ""
    strLi = list(input().strip())
    for j in strLi:
        if j not in mo:
            prnt += j
    print(f"#{i} {prnt}")