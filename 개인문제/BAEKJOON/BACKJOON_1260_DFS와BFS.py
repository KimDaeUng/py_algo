from sys import stdin

# # https://pilyeooong.tistory.com/196
# N, M, V = map(int, stdin.readline().split())
# print(N, M, V)
# graph = [[0] * (N + 1) for _ in range(N + 1)]
# visited = [False] * (N+1)

# for _ in range(M):
#     a, b = list(map(int, stdin.readline().split()))
#     graph[a][b] = 1
#     graph[b][a] = 1
# print(graph)

# def dfs(v):
#     visited[v] = True
#     print(v, end='')
#     # 1부터 나머지 모든 정점을 순회
#     for i in range(1, N + 1):
#         if not visited[i] and graph[v][i] == 1:
#             # 재귀를 통해 현재 정점의 첫번째 간선에 연결된 정점부터 탐색
#             dfs(i)

# def bfs(v):
#     queue = [v]
#     visited[v] = True
#     while queue:
#         # 시작하는 정점을 queue를 이용해 선택(FIFO)
#         v = queue.pop(0)
#         print(v, end='')

#         for i in range(1, N+1):
#             # 방문한 적이 없고 간선이 존재하면
#             if not visited[i] and graph[v][i] == 1:
#                 # queue에 해당 정점을 추가하고
#                 queue.append(i)
#                 # 방문 체크
#                 visited[i] = True
# dfs(V)
# print()
# visited = [False] * (N+1)
# bfs(V)


##################################
#  Jinhyuck's solution
# graph = {}
# n = input().split(' ')
# node, edge, start = [int(i) for i in n]

# for i in range(edge):
#     edge_info = input().split(' ')
#     n1, n2 = [int(j) for j in edge_info]
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)

#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)
# print(graph)


##################################
# Save the graph
from sys import stdin
from collections import defaultdict
from collections import deque

# graph = defaultdict(list)
# node, edge, start = map(int, stdin.readline().split())

# for i in range(edge):
#     n1, n2 = list(map(int, stdin.readline().split()))
#     graph[n1].append(n2)
#     graph[n2].append(n1)
graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]

for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n in visited:
            pass
        elif n in graph:
            visited.append(n)
            temp = list(set(graph[n]) - set(visited))
            temp.sort(reverse=True)
            stack += temp
    
    return visited

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n in visited:
            pass
        elif n in graph:
            visited.append(n)
            temp = list(set(graph[n]) - set(visited))
            temp.sort()
            queue += temp
    return visited

print(*DFS(graph, start))
print(*BFS(graph, start))


##########################################
# 위에건 되고 아래건 왜 안 되는 거지?
from sys import stdin
from collections import deque

graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]

for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        
        if n not in visited:
            visited.append(n)
            
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                
                temp.sort(reverse=True)
                stack += temp
                
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

print(DFS(graph, start))
print(BFS(graph, start))