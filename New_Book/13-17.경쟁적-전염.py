# https://www.acmicpc.net/problem/18405
# 15:56-17:55
# 바이러스의 각 위치에서부터 깊이 s번 만큼의 bfs
# 메모리 초과로 실패
# 메모리 초과 원인: 현재 노드에서 각 위치를 확인할 때 방문한 위치도 다 집어넣었기 때문

from collections import deque

n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
s, x_r, y_r = map(int, input().split())

len_col = len(board[0])

# 우, 좌, 하, 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = []
for x in range(n):
    for y in range(len_col):
        if board[x][y] != 0:
            q.append((x, y, board[x][y], 0))
q = sorted(q, key=lambda x : x[2])

# BFS로 풀어야함

q = deque(q)
depth = 0
while q:
    x, y, v, depth = q.popleft()
    if depth == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= len_col:
            continue
        else:
            if board[nx][ny] == 0:
                board[nx][ny] = v
                q.append((nx, ny, v, depth + 1))

print(board[x_r-1][y_r-1])

# Solution
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 위치 x, 위치 y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, targer_y = map(int, input().split())

# BFS 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][targer_y - 1])