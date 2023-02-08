"""파리 퇴치 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV5PzOCKAigDFAUq&probBoxId=AYYQ-fnKCuYDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+2%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

for trial in range(1, (int(input())+1)):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxM = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            hapM = 0
            for di in range(m):
                for dj in range(m):
                    hapM += arr[i+di][j+dj]
            if maxM < hapM:
                maxM = hapM
    print(f"#{trial} {maxM}")

""" internetVer
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)                                                # 행렬 만들기까지는 ㅇㅋ...
    n = M-1                                                     # 파리채 크기 -1
    max_v = 0                                                   # 최대값 0으로 할당해놓고
    # N-M+1 범위의 idx만큼 순회
    for i in range(N-n):                                        # 0부터 4까지
        for j in range(N-n):
            sum_v = 0                                           # 합 0으로 할당해놓고
            #해당 인덱스에서 MxM 범위 내 원소합을 저장
            for di in range(M):                                
                for dj in range(M):                             # 행이든 열이든 증가만 하면 되니까 range로 설정
                    print(f"i {i} j {j} di {di} dj {dj} arr[i+di][j+dj] {arr[i+di][j+dj]}")
                    sum_v += arr[i+di][j+dj]
                    print(sum_v)
            #최대값과 비교하며 최대값 저장
            if sum_v > max_v:
                max_v = sum_v
    print('#{} {}'.format(tc, max_v))
"""