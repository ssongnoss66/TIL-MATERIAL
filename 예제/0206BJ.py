"""10769 행복한지 슬픈지 https://www.acmicpc.net/problem/10769"""

inpt = input()

hpp = inpt.count(":-)")
sd = inpt.count(":-(")

if hpp == sd == 0:
    print("none")
elif hpp == sd:
    print("unsure")
elif hpp > sd:
    print("happy")
else:
    print("sad")

"""2455 지능형 기차 https://www.acmicpc.net/problem/2455"""

max = 0
curr = 0

for i in range(4):
    leave, enter = map(int, input().split())
    curr = curr - leave + enter
    if curr > max:
        max = curr

print(max)

"""2606 바이러스 https://www.acmicpc.net/problem/2606"""

comp = int(input())
ntwrk = int(input())

arr = [[] for _ in range(comp+1)]

for _ in range(ntwrk):
    m, n = map(int, input().split())
    arr[m].append(n)
    arr[n].append(m)                                # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

def dfs(start):                                     # start 1
    visited = [[False] for _ in range(comp+1)]      # vstd [F F F F F F F F]
    visited[start] = True                           # vstd [F T F F F F F F]
    stack = [start]                                 # stck [1]
    total = 0
    while stack:
        cur = stack.pop()                           # cur 1 stck [] / cur 5 stck [2] // cur 6 stck [2] /// cur 2 stck [] //// cur 3 stck [] !!끝!!
        for adj in arr[cur]:                        # arr[1]은 [2, 5] / arr[5]는 [1, 2, 6] // arr[6]은 [5] ; visited[5]는 방문한 적 있으니까 /// arr[2]는 [1, 3, 5] //// arr[3]은 [2] ; visited[2]는 이미 방문한 적 있으니까
            if not visited[adj]:
                visited[adj] = True                 # vstd [F T T F F T F F] / vstd [F T T F F T T F] /// vstd [F T T T F T T F]
                total += 1                          # ttl 2 / ttl 3 /// ttl 4
                stack.append(adj)                   # stck [2, 5] / stck [2, 6] /// stck [3]
    return total

print(dfs(1))

"""4963 섬의 개수 https://www.acmicpc.net/problem/4963"""
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
  dx = [0, 0, 1, 1, 1, -1, -1, -1]
  dy = [1, -1, 1, 0, -1, 1, 0, -1]

  arr[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == h == 0:
    break
  arr = [list(map(int, input().split())) for _ in range(h)]
  cnt = 0

  for i in range(h):
    for j in range(w):
      if arr[i][j] == 1:
        dfs(i, j)
        cnt += 1
  print(cnt)

# RecursionError는 재귀와 관련된 에러! 가장 많이 발생하는 이유는 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 발생
# 해결책1 ; 재귀 함수 사용하지 않기 / DFS 말고 BFS 사용하거나 반복문으로 구현하기
# 해결책2 ; 소스 1의 최대 재귀 깊이를 1,000,000 정도로 크게 설정하면 런타임 에러 없이 실행

""" internetVer

# dfs

from pprint import pprint

def dfs(x, y):                                                      # 델타탐색부터 설정
  dx = [1, 1, -1, -1, 1, -1, 0, 0]                                  # 오 오아래 왼 왼아래 오위 왼위 아래 위
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  field[x][y] = 0                                                   # (x, y) 좌표 자리를 1에서 0으로 터뜨려서 이후에는 이 자리 안 돌게 함
  for i in range(8):                                                # 상하좌우+네모서리 ; 8번 돌아야됨
    nx = x + dx[i]                                                  # x(y)에 dx(dy) 리스트의 인덱스 i에 해당하는 값을 더함
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:          # 더한 값이 0보다 크거나 같고 너비(높이)보다 작으며! & 더한 값에 해당하는 좌표를 가진 자리가 1이면
      dfs(nx, ny)                                                   # 그 자리에서 또 이 함수 반복 ; 인접한 1 다 터뜨려서 더이상 인접한 1 없을 때까지!

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  field = []                                                        # 리스트 비워두기
  count = 0                                                         # 섬 갯수 카운트할 변수 비워두기
  for _ in range(h):
    field.append(list(map(int, input().split())))                   # 리스트 채워서 행렬 만들기
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        dfs(i, j)
        count += 1
  
  print(count)


# bfs

from collections import deque
import sys
read = sys.stdin.readline

def bfs(x, y):
  dx = [1, -1, 0, 0, 1, -1, 1, -1]
  dy = [0, 0, -1, 1, -1, 1, 1, -1]
  field[x][y] = 0
  q = deque()
  q.append([x, y])
  while q:
    a, b = q.popleft()
    for i in range(8):
      nx = a + dx[i]
      ny = b + dy[i]
      if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
        field[nx][ny] = 0
        q.append([nx, ny])

while True:
  w, h = map(int, read().split())
  if w == 0 and h == 0:
    break
  field = []
  count = 0
  for _ in range(h):
    field.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        bfs(i, j)
        count += 1
  print(count)
"""