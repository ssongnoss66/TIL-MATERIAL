"""어디에 단어가 들어갈 수 있을까 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AYYQ-fnKCuYDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+2%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

num = int(input())

for case in range(1, num+1):
    n, k = map(int, input().split())
    matrix = []
    prntHap = 0
    for i in range(n):
        line = list(map(int, input().split()))
        lnStr = "".join(str(s) for s in line)
        lnstrLi = list(lnStr.split("0"))
        # print(lnstrLi)
        for z in lnstrLi:
            if z == ("1" * k):
                prntHap += 1
        # print(f"행렬 lnStr {lnStr} prntHap{prntHap}")
        matrix.append(line)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[j][n-i-1]
    for jLi in rotated_matrix:
        jliStr = "".join(str(s) for s in jLi)
        jlistrLi = jliStr.split("0")
        # print(lnstrLi)
        for z in jlistrLi:
            if z == ("1" * k):
                prntHap += 1
        # print(f"돌아간행렬 jliStr {jliStr} prntHap {prntHap}")
    print(f"#{case} {prntHap}")