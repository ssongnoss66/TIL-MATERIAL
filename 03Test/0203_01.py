"""민석이의 과제 체크하기 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AWVl3rWKDBYDFAXm&probBoxId=AYYQ-fnKCuYDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+2%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

for tc in range(1, (int(input())+1)):
    n, k = map(int, input().split())
    arr = [i+1 for i in range(n)]
    yes = list(map(int, input().split()))
    for i in yes:
        if i in arr:
            arr.remove(i)
    print(f"#{tc}", end=" ")
    print(*arr)