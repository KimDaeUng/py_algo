# https://programmers.co.kr/learn/courses/30/lessons/60063
# 18:38-21:14 : 못 품. 21:50-22:30 : 재시도, 실패.
'''
시뮬레이션 문제?
각 위치에서 가능한 행동
1. 이동 (4)
2. 회전 (2)
BFS로 각 위치에서 가능한 행동 수행하기?
틀린 이유:
- visited를 격자처럼 처리, 방문 여부 판단이 모호했음
- 코드 가족성 저하로 오류 발생 위치 파악이 어려움
- 방문 위치 좌표를 set으로 저장하지 않아 중복 파악이 어려움
코드 가독성 저해 요소:
- board가 범위를 벗어났는지 파악하는 조건문
- 로봇의 가로, 세로 방향 판단 및 회전 가능 여부 파악하는 조건문을 지나치게 세부적으로 짬
- 이동 가능한 다음 위치를 찾을 때, 이동과 회전을 따로 처리
'''

# My Solution(Try 2 - Pass)
from collections import deque

# (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [ 0, 0, -1, 1]


def get_possible_case(cord, n, board):

    possible_cases = []
    
    # 현재 좌표를 받아옴
    cord = list(cord)
    cord0_r, cord0_c = cord[0][0], cord[0][1]
    cord1_r, cord1_c = cord[1][0], cord[1][1]

    # 4방향 이동
    for i in range(4):
        next_cord0_r, next_cord0_c = cord0_r + dr[i], cord0_c + dc[i]
        next_cord1_r, next_cord1_c = cord1_r + dr[i], cord1_c + dc[i]
        # 판 범위 안에 있는지
        if 1 <= next_cord0_r <= n and 1 <= next_cord0_c <= n and \
            1 <= next_cord1_r <= n and 1 <= next_cord1_c <= n:
            # 이동한 위치의 값이 0이어야 함
            if board[next_cord0_r][next_cord0_c] == 0 \
                and board[next_cord1_r][next_cord1_c] == 0:
                possible_cases.append({(next_cord0_r, next_cord0_c),
                    (next_cord1_r, next_cord1_c)})

    # 회전
    # 1. 가로 방향인 경우(높이 r이 동일)
    if cord0_r == cord1_r:
        # 날개가 위/아래 방향으로 움직임
        for i in [-1, 1]:
            # 장애물 체크
            if 1 <= cord0_r + i <= n and 1 <= cord1_r+ i <= n:
                if board[cord0_r + i][cord0_c] == 0 \
                    and board[cord1_r + i][cord1_c] == 0:
                    # cord0이 축인 경우 / cord1이 축인 경우
                    possible_cases.append({(cord0_r, cord0_c), (cord0_r + i, cord0_c)})
                    possible_cases.append({(cord1_r, cord1_c), (cord1_r + i, cord1_c)})

    # 2. 세로 방향인 경우
    elif cord0_c == cord1_c:
        # 날개가 좌/우 방향으로 움직임
        for i in [-1, 1]:
            # 장애물 체크
            if 1 <= cord0_c + i <= n and 1 <= cord1_c + i <= n:
                if board[cord0_r][cord0_c + i] == 0 \
                    and board[cord1_r][cord1_c + i] == 0:
                    # cord0이 축인 경우 / cord1이 축인 경우
                    possible_cases.append({(cord0_r, cord0_c), (cord0_r, cord0_c + i)})
                    possible_cases.append({(cord1_r, cord1_c), (cord1_r, cord1_c + i)})
        
    return possible_cases


def solution(board):
    n = len(board)
    # 인덱스 번호 및 범위 판정 용이성을 위한 새 보드 
    new_board = [ [ 1 for _ in range(n + 1) ] for _ in range(n + 1) ]
    for r in range(n):
        for c in range(n):
            new_board[r + 1][c + 1] = board[r][c]

    visited = []

    # Search
    q = deque([])
    q.append(
        (
            {(1, 1), (1, 2)}, 0
        )
        )
    
    while q:
        cord, time = q.popleft()

        if (n, n) in cord:
            return time
        
        print(cord)
        possible_cases = get_possible_case(cord, n, new_board)

        for case in possible_cases:
            if case not in visited:
                q.append((case, time + 1))
                visited.append(case)

    return None


board = [[0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]]

print(solution(board))


# Solution
from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과(이동 가능 위치)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [ 0, 0,-1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y = pos1_x + dx[i], pos2_y + dy[i]
        pos2_next_x, pos2_next_y = pos2_x + dx[i], pos2_y + dy[i]

        # 이동하고자 하는 두 칸이 모두 비어있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 회전: 위쪽 or 아래쪽
            # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
            if board[pos1_x + 1][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 회전: 왼쪽 or 오른쪽
            # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
            if board[pos1_x][pos1_y + 1] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달 => 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0

# My Solution(Try 1 - Failed)
# from collections import deque
# # from queue import PriorityQueue

# def solution(board):
#     answer = 0
    
#     N = len(board)
    
#     visited = [ [ 0 for _ in range(N)] for _ in range(N) ]
    
#     # 상, 하, 좌, 우
#     dr = [-1, 1, 0, 0]
#     dc = [ 0, 0, -1, 1]

#     def is_inboard(l, r):
#         if (0 <= l < N and 0 <= r < N) and board[l][r] == 0:
#             return True
#         else:
#             return False

#     def get_rotate_cases(axis_r, axis_c, wing_r, wing_c, visited):
#         # 회전 가능한 모든 경우의 좌표를 리턴
#         rotate_cases = []

#         # 가로인지 세로인지 파악
#         row_diff = axis_r - wing_r
#         col_diff = axis_c - wing_c

#         # 가로 형태, 축이 오른쪽
#         if row_diff > 0:
#             # 시계/반시계 방향 : 축의 '상'/'하' 방향으로 날개가 이동
#             for i in range(2):
#                 nwing_r = axis_r + dr[i]
#                 nwing_c = axis_c + dr[i]
#                 # 보드 안에 이동한 위치가 없다면 다른 경우로 넘어감
#                 if not is_inboard(nwing_r, nwing_c):
#                     continue
#                 # 방문여부 체크
#                 if visited[nwing_r][nwing_c] >= 2:
#                     continue
#                 # 회전 각에 장애물이 없는지 확인
#                 if i == 0: # 시계방향인 경우, 축기준 좌상단
#                     if board[axis_r - 1][axis_c - 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))
#                 elif i == 1: # 반시계방향인 경우, 축기준 좌하단
#                     if board[axis_r + 1][axis_c - 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))

#         # 가로 형태, 축이 왼쪽 
#         elif row_diff < 0:
#             # 시계/반시계 방향 : 축의 '상'/'하' 방향으로 날개가 이동
#             for i in range(2):
#                 nwing_r = axis_r + dr[i]
#                 nwing_c = axis_c + dr[i]
#                 # 보드 안에 이동한 위치가 없다면 다른 경우로 넘어감
#                 if not is_inboard(nwing_r, nwing_c):
#                     continue
#                 # 방문여부 체크
#                 if visited[nwing_r][nwing_c] >= 2:
#                     continue
#                 # 회전 각에 장애물이 없는지 확인
#                 if i == 0: # 반시계방향인 경우, 축기준 우상단
#                     if board[axis_r - 1][axis_c + 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))
#                 elif i == 1: # 시계방향인 경우, 축기준 우하단
#                     if board[axis_r + 1][axis_c + 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))
        
#         # 세로 형태, 축이 위쪽
#         if col_diff < 0:     
#             # 시계/반시계 방향 : 축의 '좌'/'우' 방향으로 날개가 이동
#             for i in range(2,4):
#                 nwing_r = axis_r + dr[i]
#                 nwing_c = axis_c + dr[i]
#                 # 보드 안에 이동한 위치가 없다면 다른 경우로 넘어감
#                 if not is_inboard(nwing_r, nwing_c):
#                     continue
#                 # 방문여부 체크
#                 if visited[nwing_r][nwing_c] >= 2:
#                     continue
#                 # 회전 각에 장애물이 없는지 확인
#                 if i == 2: # 시계방향인 경우, 축기준 좌하단
#                     if board[axis_r + 1][axis_c - 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))
#                 elif i == 3: # 반시계방향인 경우, 축기준 우하단
#                     if board[axis_r + 1][axis_c + 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))

#         # 세로 형태, 축이 아래쪽
#         elif col_diff > 0:
#             # 반시계/시계 방향 : 축의 '좌'/'우' 방향으로 날개가 이동
#             for i in range(2, 4):
#                 nwing_r = axis_r + dr[i]
#                 nwing_c = axis_c + dr[i]
#                 # 보드 안에 이동한 위치가 없다면 다른 경우로 넘어감
#                 if not is_inboard(nwing_r, nwing_c):
#                     continue
#                 # 방문여부 체크
#                 if visited[nwing_r][nwing_c] >= 2:
#                     continue
#                 # 회전 각에 장애물이 없는지 확인
#                 if i == 2: # 반시계방향인 경우, 축기준 좌상단
#                     if board[axis_r - 1][axis_c - 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))
#                 elif i == 3: # 시계방향인 경우, 축기준 우상단
#                     if board[axis_r - 1][axis_c + 1] == 0:
#                         rotate_cases.append((nwing_r, nwing_c))
#         return rotate_cases

#     def connection_check(r_L, c_L, r_R, c_R):
#         r_diff = abs(r_L - r_R)
#         c_diff = abs(c_L - c_R)
#         if abs(r_diff - c_diff) == 1:
#             return True
#         else:
#             return False
        
#     q = deque([])
#     q.append(((0, 0), (0, 1), 0))

#     # q = PriorityQueue()
#     # q.put((0, (0, 0), (0, 1)))
#     ends = []
#     import sys
#     min_value = sys.maxsize

#     while q:        
#         # 현재 로봇의 좌표
#         robot_L, robot_R, depth = q.popleft()
#         # depth, robot_L, robot_R = q.get()
#         r_L, c_L = robot_L
#         r_R, c_R = robot_R

#         if min_value < depth:
#             break
        
#         # print(depth, robot_L, robot_R)
        
#         # 방문처리
#         visited[r_L][c_L] += 1
#         visited[r_R][c_R] += 1

#         # 1. 4방향 이동 확인
#         for i in range(4):
#             nr_L, nc_L = r_L + dr[i], c_L + dc[i]
#             nr_R, nc_R = r_R + dr[i], c_R + dc[i]
#             if is_inboard(nr_L, nc_L) and is_inboard(nr_R, nc_R)\
#              and visited[nr_L][nc_L] <= 2 and visited[nr_R][nc_R] <= 2\
#                  and connection_check(nr_L, nc_L, nr_R, nc_R):
#                 n_robot_L, n_robot_R = (nr_L, nc_L), (nr_R, nc_R)
#                 q.append((n_robot_L, n_robot_R, depth + 1))
#                 # q.put((depth + 1, n_robot_L, n_robot_R))
#                 visited[nr_L][nc_L] += 1
#                 visited[nr_R][nc_R] += 1

#                 if (nr_L == N - 1 and nc_L == N - 1) \
#                     or (nr_R == N - 1 and nc_R == N - 1):
#                     # ends.append(depth + 1)
#                     if min_value > depth + 1:
#                         min_value = depth + 1

#         # 2. 회전 확인
#         rotate_cases_0 = get_rotate_cases(r_L, c_L, r_R, c_R, visited)
#         rotate_cases_1 = get_rotate_cases(r_R, c_R, r_L, c_L, visited)
        
#         for case in rotate_cases_0:
#             case_r, case_c = case
#             if connection_check(r_L, c_L, case_r, case_c) \
#                 and visited[case_r][case_c] < 2:
#                 q.append(((r_L, c_L), case, depth + 1))
#                 # q.put((depth + 1, (r_L, c_L), case))
#                 visited[case_r][case_c] += 1

#                 if case_r == N - 1 and case_c == N - 1:
#                     # ends.append(depth + 1)
#                     if min_value > depth + 1:
#                         min_value = depth + 1

#         for case in rotate_cases_1:
#             case_r, case_c = case
#             if connection_check(r_L, c_L, case_r, case_c) \
#                 and visited[case_r][case_c] < 2:
#                 q.append(((r_R, c_R), case, depth + 1))
#                 # q.put((depth + 1, (r_R, c_R), case))
#                 visited[case_r][case_c] += 1
#                 if case_r == N - 1 and case_c == N - 1:
#                     # ends.append(depth + 1)
#                     if min_value > depth + 1:
#                         min_value = depth + 1
#     # answer = min(ends)
#     print(visited)
#     return min_value
# print(solution(board))