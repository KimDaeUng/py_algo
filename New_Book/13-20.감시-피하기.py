# https://www.acmicpc.net/problem/18428
# 18:45-20:05

# DFS / BFS 도 아닌 구현 및 완전탐색 문제
# 연구소 문제와 비슷
# 격벽의 모든 경우의 수 찾고,
# 각 경우마다 선생 위치에서 상하좌우로 직진하여 학생을 만나지 않는 경우가 존재하면 'YES' 출력

n = int(input().strip())
hall = []
case_list = []
teacher_list = []
for r in range(n):    
    hall.append(list(input().split()))
    tmp_line = hall[-1]
    for c in range(n):
        if tmp_line[c] == 'X':
            case_list.append((r, c))
        if tmp_line[c] == 'T':
            teacher_list.append((r, c))

from itertools import combinations
from copy import deepcopy
case_list = list(combinations(case_list, 3))


# 좌, 우, 상, 하
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

catch = False
def watch(r, c, board, catch):
    # 4방향으로 벽을 만날때까지 
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        while 0 <= nr and nr < n and 0 <= nc and nc < n:
            if board[nr][nc] == 'X':
                nr = nr + dr[i]
                nc = nc + dc[i]
                continue
            # 벽 또는 다른 선생을 만날 경우 다른 방향으로 넘어감
            elif board[nr][nc] == 'O' or board[nr][nc] == 'T':
                break
            # 잡히면 해당 회차는 끝
            elif board[nr][nc] == 'S':
                catch = True
                return catch
    return catch

for case in case_list:
    hall_tmp = deepcopy(hall)
    for r, c in case:
        hall_tmp[r][c] = 'O'
    catch = False
    for teacher in teacher_list:
        r, c = teacher
        catch = watch(r, c, hall_tmp, catch)
        # print(catch)
        if catch:
            break
    if not catch:
        print('YES')
        exit()
print("NO")


# Solution
from itertools import combinations
n = int(input())
board = []
teachers = []
spaces =[]

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teacher.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장매울 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')