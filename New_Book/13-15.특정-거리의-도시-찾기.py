# https://www.acmicpc.net/problem/18352
# 21:25-21:55 23:10-01:10(테스트케이스 통과 but 메모리 초과)

# 1. 시작도시부터 각 도시까지 최단 거리를 저장한 후
# 2. 특정 최단 거리를 가지는 도시만을 출력
# 메모리 초과 난 이유:
#  - graph에 각 거리를 저장
#  - 시작 노드 기준 거리 계산 저장하는 리스트를 별도로 구함
# BFS 사용

# from collections import deque
# from collections import defaultdict
# import sys

# N, M, K, X = list(map(int, input().split()))
# X = X - 1
# graph = [[] for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     a, b = a - 1, b - 1
#     graph[a].append((b, 0))

# def bfs(graph, start):
#     queue = deque([(start, 0)])
#     while queue:
#         v, dist = queue.popleft()
#         for idx, (v_adj, dist_adj) in enumerate(graph[v]):
#             # if not visited[v_adj]:
#             if dist_adj == 0:
#                 dist_adj = dist + 1
#             else:
#                 dist_adj = min(dist_adj, dist + 1)
#             queue.append((v_adj, dist_adj))
#             graph[v][idx] = (v_adj, dist_adj)                
#             # if dist_adj == K:
#             #     nodes[v_adj] = min(nodes[v_adj], dist_adj)
#                 # nodes.append(v_adj)

# bfs(graph, X)

# # N개의 모든 노드에 대해서 시작지점부터의 거리 구하기

# nodes = [ sys.maxsize for _ in range(N) ]
# for vertex in graph:
#     for vertex_adj, dist in vertex:
#         nodes[vertex_adj] = min(nodes[vertex_adj], dist)

# if K in nodes:
#     for v, dist in enumerate(nodes):
#         if dist == K:
#             print(v + 1)
# else:
#     print(-1)


# # Solution
# from collections import deque

# # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]

# # 모든 도로 정보 입력 받기
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
    
# # 모든 도시에 대한 최단 거리 초기화
# distance = [-1] * (n + 1)
# distance = 0 # 출발 도시까지 거리는 0

# # 너비 우선 탐색(BFS)
# q = deque([x])

# while q:
#     now = q.popleft()
#     # 현재 도시에서 이동할 수 있는 모든 도시를 확인
#     for next_node in graph[now]:
#         # 아직 방문하지 않은 도시라면
#         if distance[next_node] == -1:
#             # 최단 거리 갱신
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)
            
# # 최단 거리가 K인 모든 도시의 번호를 오름치순으로 출력
# check = False
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         check = True

# # 만약 최단 거리가 K인 도시가 없다면 -1 출력
# if check == False:
#     print(-1)

# Retry
from collections import deque
# input
n, m, k, x = map(int, input().split())

graph = [ [] for _ in range(n + 1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs

queue = deque([x])
dists = [-1] * (n + 1)
dists[x] = 0 

while queue:
    cur_node = queue.popleft()
    for adj_node in graph[cur_node]:        
        # 최초 방문시의 거리를 추가한다
        if dists[adj_node] == -1:
            dists[adj_node] = dists[cur_node] + 1
            queue.append(adj_node)

# 거리가 k인 도시만 리턴

is_exist = False
for node in range(1, n + 1):
    if dists[node] == k:
        print(node)
        is_exist = True
if not is_exist:
    print(-1)