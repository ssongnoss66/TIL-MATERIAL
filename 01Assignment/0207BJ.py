"""1063 킹 https://www.acmicpc.net/problem/1063"""












































"""internet Ver
king, stone, N = input().split()                        # 킹위치 A1 돌위치 A2 움직이는횟수 2
k = list(map(int, [ord(king[0]) - 64, king[1]]))        # k = [1, 1]
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))      # s = [1, 2]
move = {
    'R': [1, 0], 
    'L': [-1, 0], 
    'B': [0, -1], 
    'T': [0, 1], 
    'RT': [1, 1], 
    'LT': [-1, 1], 
    'RB': [1, -1], 
    'LB': [-1, -1]
    }

for _ in range(int(N)):                                 # 1️⃣이동횟수만큼 돌기 > 킹 [1, 1] 돌 [1, 2] 2️⃣킹 [1, 2] 돌 [1, 3]
    m = input()                                         # 1️⃣킹 이동 T [0, 1] 2️⃣킹 이동 R [1, 0]
    nx = k[0] + move[m][0]                              # 1️⃣킹 좌우 nx = 1 + 0 = 1 2️⃣킹 좌우 nx = 1 + 1 = 2
    ny = k[1] + move[m][1]                              # 1️⃣킹 상하 ny = 1 + 1 = 2 2️⃣킹 상하 ny = 2 + 0 = 2
    if 0 < nx <= 8 and 0 < ny <= 8:                     # 1️⃣킹 체스판 안에 있으면 2️⃣킹 체스판 안에 있으면
        if nx == s[0] and ny == s[1]:                   # 1️⃣킹과 돌의 위치가 같으면
            sx = s[0] + move[m][0]                      # 1️⃣돌 좌우 sx = 1 + 0 = 1
            sy = s[1] + move[m][1]                      # 1️⃣돌 상하 sy = 2 + 1 = 3
            if 0 < sx <= 8 and 0 < sy <= 8:             # 1️⃣돌 체스판 안에 있으면
                k = [nx, ny]                            # 1️⃣킹 [1, 2]
                s = [sx, sy]                            # 1️⃣돌 [1, 3]
        else:                                           # 2️⃣킹과 돌의 위치가 다르면
            k = [nx, ny]                                # 2️⃣킹 [2, 2]
print(f'{chr(k[0] + 64)}{k[1]}')                        # 킹 B2
print(f'{chr(s[0] + 64)}{s[1]}')                        # 돌 A3

# 아스키코드 A 65 B 66 C 67 ...
"""

"""teacher Ver
# 8방향 델타값 ; 방향이 알파벳으로 입력되므로 딕셔너리 사용
directions = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1),
}

# 아스키코드 이용해 체스판 위치를 좌표로 변환
# ord() ; 특정 문자를 아스키코드로 변환하는 파이썬 내장 함수
# 65는 아스키코드에서 "A"를 나타내므로 이를 빼서 열의 좌표값 구함
k, s, n = input().split()

kx, ky = 8 - int(k[1]), ord(k[0]) - 65          # king x, y
sx, sy = 8 - int(s[1]), ord(s[0]) - 65          # stone x, y
"""