"""조교의 성적 매기기 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV5PwGK6AcIDFAUq&probBoxId=AYYQ-fnKCuYDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+2%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

for i in range(1, (int(input()) + 1)):
    scoreDict = {}
    n, k = map(int, input().split())
    # print(n//10, 2*n//10, 3*n//10, 4*n//10, 5*n//10, 6*n//10, 7*n//10, 8*n//10, 9*n//10, n)
    for j in range(1, n+1):
        m, f, a = (map(int, input().split()))
        ttl = (m * 35 / 100) + (f * 45 / 100) + (a * 20 / 100)
        scoreDict[ttl] = j
    srtdDict = dict(sorted(scoreDict.items(), reverse=True))
    # print(srtdDict)
    for index, (key, val) in enumerate(srtdDict.items()):
        if val == k:
            # print(f"val {val} index {index}")
            if index < n//10:
                print(f"#{i} A+")
            elif index < 2*n//10:
                print(f"#{i} A0")
            elif index < 3*n//10:
                print(f"#{i} A-")
            elif index < 4*n//10:
                print(f"#{i} B+")
            elif index < 5*n//10:
                print(f"#{i} B0")
            elif index < 6*n//10:
                print(f"#{i} B-")
            elif index < 7*n//10:
                print(f"#{i} C+")
            elif index < 8*n//10:
                print(f"#{i} C0")
            elif index < 9*n//10:
                print(f"#{i} C-")
            elif index <= n:
                print(f"#{i} D0")