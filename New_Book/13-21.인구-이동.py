# https://www.acmicpc.net/problem/16234
# 17:40-18:37 : 못 품. 지난 번 구역 개수 찾기 응용해야 할 것 같음
# 18:50-19:55 : 못 품.
N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# 1. 모든 칸을 탐색해서 국경선을 공유하는 곳의 좌표를 찾는다.(DFS)
# 2. 인구이동을 시켜 값을 갱신한다.
# 3. 1-2를 인구이동이 불가할때까지 반복한다.

# 1. 국경선 공유하는 곳의 좌표 찾기
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# DFS
union = []
visited = [ [ 0 for _ in range(N) ] for _ in range(N) ]

from collections import deque
q = deque([])
visited[0][0] = 0
cnt = 0
idx = 1
for r in range(N):
    for c in range(N):
        # 4방향 탐색
        if visited[r][c] == 0:
            q.append((r, c))
            visited[r][c] = idx
            while q:
                # 현재 위치
                cr, cc = q.popleft()
                for i in range(4):
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    # 범위 안에 있고
                    if 0 <= nr < N and 0 <= nc < N:
                        # 현재 위치와의 차이가 조건을 충족하고, 방문한 적이 없으면
                        # 큐에 넣어주고, 값을 현재 인덱스로 넣어준다.
                        diff = abs(A[cr][cc] - A[nr][nc])
                        if (visited[nr][nc] == 0) and (L <= diff <= R):
                            q.append((nc, nr))
                            visited[nr][nc] = idx
        # 이어져 있는 곳을 다 지나면 co
        else:
            idx += 1
print(visited)


# def dfs(r, c, i):
#     global visited
#     if visited[r][c] != 0:
#         return
#     visited[r][c] = i

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr and nr < N and 0 <= nc and nc < N:
#             diff = abs(A[r][c] - A[nr][nc])
#             if L <= diff and diff <= R:
#                 union.append((nr, nc))
#                 # visited[]
#                 dfs(nr, nc, i)
#     return
# i = 0
# for r in range(N):
#     for c in range(N):
#         if visited[r][c] != 0:
#             continue
#         else:
#             dfs(r, c, i)
#             i += 1
# print(visited)

### 

# 못풀겠다
# Solution
from collections import deque

# 땅의 크기(N), L, R 값 입력
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색(BFS)을 위한 큐 자료 구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구수
    count = 1 # 현재 연합의 국가수
    
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny <= n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            # 해당 나라가 처리되지 않았다면
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    # (process가 하나도 진행되지 않아서
    # 매 셀마다 index가 증가한 경우
    # -> 더 이상 인구이동이 발생하지 않는 경우)
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)