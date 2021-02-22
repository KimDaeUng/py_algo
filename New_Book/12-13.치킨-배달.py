# https://www.acmicpc.net/problem/15686
from collections import deque

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]

def chicken_dist(x, y, board):
    queue = deque()
    queue.append((x, y))
    visited = [ [ 0 for _ in range(N) ] for _ in range(N) ]
    init = (x, y)
    is_init = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 처음 지점을 다시 방문하지 않도록 처리
            if ((nx == init[0]) and (ny == init[1])) and (not is_init):
                continue
            # 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 방문한 적이 있을 경우 무시
            if visited[ny][nx] > 0:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((nx, ny))
            
            is_init = False

            # 치킨집을 발견한 경우 치킨거리 반환 후 종료
            if board[ny][nx] == 2:
                return visited[ny][nx]

# 최소 치킨거리

sum_dist = 0
for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            sum_dist += chicken_dist(x, y, board)

print(sum_dist)