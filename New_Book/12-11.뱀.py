# https://www.acmicpc.net/problem/3190


# 14:50-15:54
# Retry 2
n = int(input())
k = int(input())

board = [ [0] * (n + 1) for _ in range(n + 1) ]
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1


l = int(input())
moves = []
for _ in range(l):
    sec, d_idx = input().split()
    if d_idx.strip() == "L":
        d_idx = -1
    else:
        d_idx = 1 
    moves.append((int(sec), d_idx))

# 동, 남, 서, 북 (시계방향)
dr = [0, 1, 0, -1]
dc = [1, 0,  -1, 0]

# 방향 인덱스가 순환하도록 함
def rotate(origin, direc):
    return (origin + direc) % 4

def simul():
    r, c = 1, 1 # 뱀의 초기 좌표
    d = 0 # 초기 방향
    board[r][c] = 2 # 뱀 위치 기록
    snake = [(r, c)] # 뱀 정보: 가장 오른쪽이 머리
    time = 0 # 소요 시간
    moves_idx = 0 # 방향 파악을 위한 인덱스

    while True:
        # 다음 방향 이동
        nr = r + dr[d]
        nc = c + dc[d]
        
        # 맵을 벗어나거나
        # 자기 몸통에 닿은 경우 게임 종료

        if 1 <= nr and nr <= n and 1 <= nc and\
             nc <= n and board[nr][nc] != 2:
            # 사과가 없다면
            if board[nr][nc] == 0:
                # 머리를 새로운 칸에 이동하고
                board[nr][nc] = 2
                snake.append((nr, nc))
                # 꼬리를 삭제
                r_, c_ = snake.pop(0)
                board[r_][c_] = 0
            
            # 사과가 있다면
            if board[nr][nc] == 1:
                # 머리를 새로운 칸에 이동하고 꼬리는 그대로 둔다
                board[nr][nc] = 2
                snake.append((nr, nc))
        
        else:
            time += 1
            break
        
        time += 1 # 시간 없데이트
        r, c = nr, nc # 머리 위치 업데이트
        
        # 방향 업데이트: 현재 time값과 다음 방향 전환이 시작되는 시간이 일치할 때
        if moves_idx < l and moves[moves_idx][0] == time:
            d = rotate(d, moves[moves_idx][1])
            moves_idx += 1

    return time
    
print(simul())


# Solution
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # map
info = [] # Direction Info

# Map info (Position of apples are denoted by 1)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# Direction Info
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 방향 초기값: 동쪽
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치면
        if 1 <= nx and nx <= n and\
            1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())

# # Retry (Failed)
# '''
# 12:00-13:39 : 못 품
# - 예제 입력2에서 틀림
# - 사과를 먹은 후 모든 body의 좌표를 갱신할 떄, 단순 현재 방향으로 갱신하게해서
#   제대로 갱신되지 않음
# '''

# N = int(input())
# K = int(input())

# board = [ [0] * (N + 1) for _ in range(N + 1) ]
# apples = []
# for _ in range(K):
#     r, c = map(int, input().split())
#     board[r][c] = 1
#     apples.append((r, c))

# L = int(input())
# moves = []
# for _ in range(L):
#     sec, direc = input().split()
#     if direc == "U":
#         direc = 0
#     if direc == "D":
#         direc = 1
#     if direc == "L":
#         direc = 2
#     if direc == "R":
#         direc = 3

#     moves.append((int(sec), direc))


# def simul():
#     # "U", "D", "L", "R"(상하좌우)
#     dr = [-1, 1, 0, 0]
#     dc = [ 0, 0, -1, 1]

#     snake = [[1, 1]]
#     prev_direc = 3
#     cur_direc = 3
#     count = 0

#     while moves:
#         # moves를 체크하여 방향 확인
#         sec, new_direc = moves.pop(0)
#         print(f"-----Start New Direction")

#         while sec:
#             print("\t count : {count} / sec : {sec}")
#             print(f"\t snake : {snake}")
#             # 소요된 시간 추가
#             count += 1
#             # 현재 방향으로 sec 만큼 이동
#             nr = snake[0][0] + dr[cur_direc]
#             nc = snake[0][1] + dc[cur_direc]
#             print("\t nr : {nr} / nc : {nc}")

#             # 판 범위를 벗어난 경우 종료
#             if (nr < 1 or nr > N) or\
#                 (nc < 1 or nc > N):
#                 print('\t \t off the wall')
#                 return count
            
#             # 자기 몸에 닿은 경우 종료
#             if [nr, nc] in snake:
#                 print('\t \t touch body')
#                 return count

#             # 이동한 칸에 사과가 있다면
#             # 몸길이를 늘임(head 부분에 사과칸을 추가)
#             if (nr, nc) in apples:
#                 print('\t Yes apple')
#                 apples.remove((nr, nc))
#                 snake.insert(0, [nr, nc])
#             # 이동한 칸에 사과가 없다면
#             # 모든 몸통을 이동시킨다.
#             else:
#                 print('\t No apple')
#                 for body in snake:
#                     body[0] = body[0] + dr[cur_direc]
#                     body[1] = body[1] + dc[cur_direc]
#             sec -= 1
        
#         prev_direc = cur_direc
#         cur_direc = new_direc
#     return count
# print(simul())



# # My Soultion(Failed)
# N = int(input())
# K = int(input())

# apples = []
# board = [[ 0 for _ in range(N)] for _ in range(N)]

# for _ in range(K):
#     row, col = map(int, input().split())
#     board[row][col] = 1
#     apples.append([row, col])

# # R, D, L, U (시계방향 움직임)
# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# L = int(input())
# moves = []
# for _ in range(L):
#     X, C = input().split()
#     moves.append([int(X), C])

# idx = 0


# sh_row, sh_col = 0, 0
# board[sh_row][sh_col] = 1
# while True:
#     d = directions[idx]
#     nsh_row, nsh_col = sh_row + d[0], sh_col + d[1]
#     board[nsh_row][nsh_col] = 1