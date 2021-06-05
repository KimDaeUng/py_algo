# https://www.acmicpc.net/problem/16234
# 00:02-
# My Solution
'''
DFS 사용해 각 지점부터 인접한 국가에 대해
인구차이를 확인하며 연합 구성
연합의 좌표와 전체값, 국가 개수 저장후
더이상 연합을 찾을 수 없으면 인구수를 업데이트, 인구이동 카운트
방문하지 않았던 좌표로 넘어간 뒤 동일한 과정을 수행
주의 : 연합마다 카운트가 아니라 전체 맵에 대해서 인구이동이 발생하면 카운트
'''

string = '''2 20 50
50 30
20 40'''
string = '''2 40 50
50 30
20 40'''
string = '''2 20 50
50 30
30 40'''
string = '''3 5 10
10 15 20
20 30 25
40 22 10'''
string = '''4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, L, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
M = len(arr[0])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    global tmp_sum, tmp_cnt, tmp_visited
    # 현재 노드를 아직 방문하지 않았다면
    if tmp_visited[x][y] == 0:
        # 방문처리
        tmp_visited[x][y] = 1
        tmp_cnt += 1
        tmp_sum += arr[x][y]
        tmp_union.append((x, y))
        
        # 상, 하, 좌, 우 재귀호출로 방문
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= N \
                or ny < 0 or ny >= M:
                continue

            diff = abs(arr[nx][ny] - arr[x][y])
            if L <= diff and diff <= R:
                dfs(nx, ny)

        return True

    # 방문 했다면
    return False

cnt = 0
prev_cnt = 0
while True:
    tmp_visited = [ [0] * M for _ in range(N) ]
    is_img = False
    for i in range(N):
        for j in range(M):
            tmp_sum = 0
            tmp_cnt = 0
            tmp_union = []
            if dfs(i, j):
                if len(tmp_union) > 1:
                    tmp_avg = tmp_sum // tmp_cnt
                    for x, y in tmp_union:
                        arr[x][y] = tmp_avg
                    is_img = True
    if is_img:
        cnt += 1

    if prev_cnt == cnt:
        break
    prev_cnt = cnt

print(cnt)

# Solution : BFS
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
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
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하여
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    
    # 연합 국가끼리 인구를 분해
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
            # 해당 나라가 아직 처리되지 않았다면
            if union[i][j] == -1:
                process(i, j, index)
            index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)