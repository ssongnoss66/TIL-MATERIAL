"""창용 마을 무리의 개수 https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYWfkNk6EggDFAQK&contestProbId=AWngfZVa9XwDFAQU&probBoxId=AYY1F7UqkrkDFARc&type=PROBLEM&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+3%EC%A3%BC%EC%B0%A8+%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC&problemBoxCnt=6"""

# 10개 중 6개
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

# 창용마을

# teammateVer

def dfs(people, c, check):
    check[c] = True
    for i in people[c]:
        if not check[i]:
            dfs(people, i, check)
   
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))    #N:사람수, M:간선
   
    people = [[] for _ in range(N+1)]
    for _ in range(M):
        num1, num2 = map(int, input().split())
        people[num1].append(num2)
        people[num2].append(num1)
    
    check = [False] * (N + 1)
    cnt = 0
    for b in range(1, N + 1):
        if check[b] == False:
            dfs(people, b, check)
            cnt += 1
    
    print(f'#{t} {cnt}')

"""internetVer
from collections import defaultdict
from sys import stdin as s
input = open("/Users/e_o_n_l_a_/Desktop/패캠)TIL&MATERIAL/03Test/input.txt","rt").readline

def dfs(start, stack):
    num = stack.pop()
    check[num] = start
    for link_node in people[num]:
        if check[link_node] == 0:
            stack.append(link_node)
            dfs(start, stack)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(M))
    answer = 0

    people = defaultdict(list)
    check = [0] * (N + 1)
    for i in range(M):
        people[arr[i][0]].append(arr[i][1])
        people[arr[i][1]].append(arr[i][0])

    for i in range(1, N+1):
        if check[i] == 0:
            dfs(i, [i])
            answer += 1
    
    print(f"#{tc} {answer}")
"""