"""등산로 조성 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AV5PoOKKAPIDFAUq&probBoxId=AYY1F7UqkrkDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+3%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    cnt = 0
    mx = 0
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < n and 0 <= ny < n:
            if mt[nx][ny] >= mt[x][y] - k:
                cnt += 1
                # print(f"x{x} y {y} nx {nx} ny{ny} mt[nx][ny] {mt[nx][ny]} k {k} cnt {cnt}")
                dfs(nx, ny)
            if cnt > mx:
                mx = cnt
    return(mx)

for i in range(1, int(input())+1):
    n, k = map(int, input().split())
    mt = [list(map(int, input().split())) for _ in range(n)]
    hghst = max(map(max, mt))
    prnt = 0
    # print(mt)
    # print(f"hghst {hghst}")
    for x in range(n):
        for y in range(n):
            if mt[x][y] == hghst:
                func = dfs(x, y)
                print(f"hghst {hghst} x {x} y {y} dfs(x, y) {dfs(x, y)} prnt {prnt}")
                if func > prnt:
                    prnt = func
    print(f"#{i} {prnt}")