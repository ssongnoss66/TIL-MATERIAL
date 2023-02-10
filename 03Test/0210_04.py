"""퍼펙트 셔플 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AWGsRbk6AQIDFAVW&probBoxId=AYY1F7UqkrkDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+3%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline

for i in range(1, int(input()) + 1):
    n = int(input())
    if n % 2 == 0:
        crdLi = list(input().split())
        crdLi = [crdLi[0:n//2], crdLi[n//2:n]]
        prntLi = []
        for j in range(n//2):
            prntLi.append(crdLi[0][j])
            prntLi.append(crdLi[1][j])
        print(f"#{i}", end=" ")
        print(*prntLi)
    else:
        crdLi = list(input().split())
        crdLi = [crdLi[0:(n//2)+1], crdLi[(n//2)+1:n]]
        prntLi = []
        for j in range(n//2):
            prntLi.append(crdLi[0][j])
            prntLi.append(crdLi[1][j])
        prntLi.append(crdLi[0][n//2])
        print(f"#{i}", end=" ")
        print(*prntLi)