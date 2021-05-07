# 02:50-
string = '''3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4'''

# string = '''5 5
# 4 3
# 4 2
# 3 2
# 1 2
# 2 5'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution
# 각 위치에 도달하는 비용 2차원 배열 distance에 기록, 갱신
# 시작 점부터 상하좌우 이동, 맵을 벗어나지 않는 범위 내에서 현재까지 최소 비용과 비교
from collections import deque

def solution(n, costs):
    distance = [[INF] * n for _ in range(n)]
    q = deque([])
    q.append((costs[0][0], (0, 0)))

    # L, D, R, U
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        cost, (x, y) = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                n_cost = cost + costs[nx][ny]
                if n_cost < distance[nx][ny]:
                    distance[nx][ny] = n_cost
                    q.append((distance[nx][ny], (nx, ny)))
    # print(distance)
    return distance[-1][-1]


t = int(input())
INF = int(1e9)
for _ in range(t):
    n = int(input())
    costs = []
    for i in range(n):
        costs.append(list(map(int, input().split())))
    print(solution(n, costs))

# Solution
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 테스트 케이스 만큼 반복
for tc in range(int(input())):
    # 노드 개수 입력 받기
    n = int(input())
    
    # 전체 맵 정보 입력 받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0 # 시작 위치는 (0, 0)
    # 시작 노드로 가기 위한 비용은 (0, 0) 위치의 값으로 설정해 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    
    print(distance[n - 1][n - 1])