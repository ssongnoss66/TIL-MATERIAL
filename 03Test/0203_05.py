"""암호 생성기 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV14uWl6AF0CFAYD&probBoxId=AYYQ-fnKCuYDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+2%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

for j in range(1, 11):
    inpt = int(input())
    inptLi = list(map(int, input().split()))
    while True:
        for i in range(1, 6):
            n = inptLi[0]
            del inptLi[0]
            if n - i <= 0:
                inptLi.append(0)
                print(f"#{j}", end=" ")
                print(*inptLi)
                break
            else:
                inptLi.append(n-i)
        if inptLi[-1] == 0:
            break