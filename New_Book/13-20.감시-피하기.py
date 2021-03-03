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
                # board[nr][nc] = 'V'
                # watch(nr, nc, board)
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