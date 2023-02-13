"""창용 마을 무리의 개수 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AWngfZVa9XwDFAQU&probBoxId=AYY1F7UqkrkDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+3%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline

def dfs(start):
    stack = [start]    
    visited[start] = True               

    while stack:
        cur = stack.pop()              
        for adj in rltnLi[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
    vstd = list(map(str, visited))
    vstdSl = ("".join(s for s in vstd)).split("False")
    cnt = 0
    for i in vstdSl:
        if len(i) > 0:
            cnt += 1
    return(cnt)      

for i in range(1, int(input())+1):
    ppl, ntwrk = map(int, input().split())
    rltnLi = [[] for _ in range(ppl + 1)]
    visited = [False] * (ppl + 1)
    for j in range(ntwrk):
        x, y = map(int, input().split())
        rltnLi[x].append(y)
        rltnLi[y].append(x)
    print(f"#{i} {dfs(1)}")

"""
[[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
---------------------------------------------
[[], [2, 5], [1, 5, 4, 3], [4, 2], [3, 6, 5, 2], [2, 1, 4], [4]]
"""