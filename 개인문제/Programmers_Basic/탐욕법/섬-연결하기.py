# https://programmers.co.kr/learn/courses/30/lessons/42861
# 14:41-16:37 : 해결 못함

# My Solution 4 : Kruskal
# 정석 풀이
# 최소 신장 트리, 간선 비용의 총합
def solution(n, costs):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    parent = list(range(n))
    edges = []
    result = 0

    for line in costs:
        a, b, cost = line
        edges.append((cost, a, b))
    
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    return result

# Solution : Kruskal
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)
    
def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            # union_parents 에 해당하는 부분인데 f의 루트 노드가 t가 되게함
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer

# Solution : 우선순위큐를 이용한 방법
# - 매번 비용이 최소인 간선을 꺼냄
# - 이미 방문한 곳은 다시 방문하지 않는다 <=> cycle이 발생한 노드는 추가시키지 않는다
# - Kruskal의 복잡한 절차 제외하고, cost에만 집중
import heapq as hq

def solution(n, costs):
    answer = 0
    from_to = [ [] for _ in range(n) ]
    visited = [False] * n
    priority = []

    for a, b, cost in costs:
        from_to[a].append((b, cost))
        from_to[b].append((a, cost))
    
    hq.heappush(priority, (0, 0))
    while False in visited:
        cost, start = hq.heappop(priority)
        if visited[start]: continue

        visited[start] = True
        answer += cost
        for end, cost in from_to[start]:
            if visited[end]: continue
            else:
                hq.heappush(priority, (cost, end))
    
    return answer


'''
# My Solution 3
# BFS 이용 모든 시작점에서 각 지점과의 거리를 나타낸 후 
from collections import deque
def solution(n, costs):
    INF = int(1e9)
    graph = [ [] for _ in range(n) ]
    for line in costs:
        a, b, cost = line
        graph[a].append((cost, b))
        # graph[b].append((cost, a))
    
    def bfs(start, graph):
        visited = {}
        q = deque([])
        q.append((0, start))
        while q:
            cost, now = q.popleft()
            # if all(visited):
            #     return cost
            if now not in visited:
                visited[now] = cost
                q.extend(graph[now])
            else:
                visited[now] = min(visited[now], cost)
        return visited.values()

    min_cost = INF
    for i in range(n):
        visited_i = bfs(i, graph)
        if len(visited_i) == n:
            min_cost = min(min_cost, sum(visited_i))
        # min_cost = min(min_cost, cost)
    return min_cost

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	
print(solution(n, costs))
        
exit()


# My Solution 2 
# DFS를 이용한 풀이, 모든 노드를 방문할 때까지 재귀적 탐색 후 cost를 계산해 최솟값 갱신
# 테스트 케이스 통과 못함. 왜?
# 두 섬간 직접적인 연결 없이 반드시 한 번 방문한 곳을 다시 거쳐가야하는 경우?
# 4-0-1
#    \
#     2-3
# 위와 같은 식이면 0은 무조건 한 번 이상 다시 지나가야함
# 그냥 무조건 한 노드로부터 각 노드까지 최소거리 구해서 합하면 되는 거 아닌가?
# -> 다익스트라 -> X

# 그냥 BFS로 다 뻗어나가면서 모든 거리 다 더해?
# 모든 시작점을 BFS로 탐색, cost가 가장 작은 노드부터 먼저 처리 ???

import heapq
def solution(n, costs):
    INF = int(1e9)
    graph = [ [] for _ in range(n) ]
    distance = [INF] * n
    for line in costs:
        a, b, cost = line
        graph[a].append((cost, b))
        graph[b].append((cost, a))
    def dijstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                next_cost = dist + i[0]
                if next_cost < distance[i[1]]:
                    distance[i[1]] = next_cost
                    heapq.heappush(q, (next_cost, i[1]))
    
    dijstra(3)
    print(distance)

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	
print(solution(n, costs))
        
exit()



min_cost = int(1e9)
def solution(n, costs):
    # DFS
    def dfs(graph, v, visited, cost_pre):
        global min_cost
        # 현재 노드 방문 처리
        visited[v] = True
        if all(visited):
            min_cost = min(min_cost, cost_pre)
            return
        # 현재 노드와 연결된 다른 노드 재귀적 방문
        for cost, node in graph[v]:
            if not visited[node]:
                dfs(graph, node, visited, cost_pre + cost)

    graph = [ [] for _ in range(n) ]
    for line in costs:
        a, b, cost = line
        graph[a].append((cost, b))
        graph[b].append((cost, a))
    
    for k in range(n):
        visited = [False] * n
        dfs(graph, k, visited, 0)
    return min_cost

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	
print(solution(n, costs))
        
exit()


# My Solution 1 : 플로이드 워셜 시도 - 경로를 알 수 없음
from pprint import pprint
INF = int(1e9)
def solution(n, costs):
    answer = 0
    graph = [[INF] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
    for line in costs:
        a, b, cost = line
        graph[a][b] = cost
        graph[b][a] = cost
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    pprint(graph)

    return graph
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	
pprint(solution(n, costs))
'''