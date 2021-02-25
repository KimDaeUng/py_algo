# https://www.acmicpc.net/problem/14502
# 21:30-23:32 : 못 품
# 23:32-23:53 : 힌트 본 후 품
# 11:15-1

# 1. 벽을 칠 모든 경우를 찾고
# -> 모든 경우를 다 시험해? -> 2023 가지수, 해볼만 함
# 2. 각 경우에서 바이러스를 퍼뜨린 뒤, 0의 개수를 세야함

# 처음에 틀렸던 이유
# - 전파 시뮬레이션을 하면서 동시에 카운트를 하려함

import copy
from itertools import combinations

# 테스트 케이스 입력
n, m = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

# n, m = 4, 6
# world = [[0, 0, 0, 0, 0, 0],
#  [1, 0, 0, 0, 0, 2],
#  [1, 1, 1, 0, 0, 2],
#  [0, 0, 0, 0, 0, 2]]

# n, m = 8, 8
# world = [[2,0,0,0,0,0,0,2],
# [2,0,0,0,0,0,0,2],
# [2,0,0,0,0,0,0,2],
# [2,0,0,0,0,0,0,2],
# [2,0,0,0,0,0,0,2],
# [0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0]]

# 전체 case 계산

whole_cases = []
viruses = []
for y in range(n):
    for x in range(m):
        if world[y][x] == 0:
            whole_cases.append((y, x))
        if world[y][x] == 2:
            viruses.append((y, x))
new_whole_cases = list(combinations(whole_cases, 3))


# 전파 시뮬레이션

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def simulation(y, x, board):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        else:
            if board[ny][nx] == 0:
                board[ny][nx] = 2
                simulation(ny, nx, board)

def count(board):
    cnt = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                cnt += 1
    return cnt

# 모든 경우에 대해서 시뮬레이션 및 최대 0의 값 count
max_count = 0
for walls in new_whole_cases:
    board = copy.deepcopy(world)
    for wall in walls:
        y, x = wall[0], wall[1]
        board[y][x] = 1
    for y, x in viruses:
        simulation(y, x, board)
    max_count = max(max_count, count(board))
    del board

print(max_count)


# def simulation(y, x, board):
#     # 현재 위치가 0이면 일단 2로 바꿨다 가정하고 count +=1 and 방문처리
#     count = 0
#     if (board[y][x] == 2):  
#         board[y][x] = -1
#         count += 1
#     # 벽(1)이거나 이미 방문한 곳(-1)이면 0 리턴하고 종료
#     elif (board[y][x] == 1) or (board[y][x] == -1):
#         board[y][x] = -1
#         return 0
#     # 0인 경우 2로 바꾼 후 재귀처리
#     elif board[y][x] == 0:
#         board[y][x] = 2
#         return simulation(y, x, board)

#     # (현재 위치가 0인 상태에서)
#     # 상하좌우 탐색해 칸이 0이면 재귀하여 카운트
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if ny < 0 or ny >= n or nx < 0 or nx >= m:
#             continue        
#         count += simulation(ny, nx, board)
#     return count

# import sys
# import copy
# max_counts = 0
# for walls in new_whole_cases:
#     board = copy.deepcopy(world)
#     for wall in walls:
#         y, x = wall[0], wall[1]
#         board[y][x] = 1
#     for y in range(n):
#         for x in range(m):
#             if board[y][x] == 2:
#                 max_counts = max(max_counts, num_zeros - simulation(y, x, board))
#                 break
#     del board

# print(max_counts)

# # Solution

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치 한 뒤 맵 리스트
for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0

# DFS 이용해 각 바이러스가 사방으로 퍼지게 하기
def simul(x, y):
    for _ in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바리어스 배치 후, 재귀수행
                temp[nx][ny] = 2
                simul(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산 하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        # temp에 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    simul(i, j)
        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                # 재귀로 들어가 울타리 3개 설치할 때까지 반복,
                # 3개 설치되면 전파 시뮬레이션 후 result 갱신 한 뒤,
                # data를 복구하고, 다음 케이스로 넘어감
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

