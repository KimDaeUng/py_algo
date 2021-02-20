# 20:41-
'''
N x M 크기의 직사각형 형태의 미로에 갇혀 있다
0 : 괴물
1 : 통로
(1, 1)에서 시작해 (N, M)으로 이동하는 1의 값의 최단 경로
시작칸과 마지막칸 모두 포함

''' 
from collections import deque


N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input())))

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 벽인 경우 무시
            if board[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return board[N - 1][M - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))