'''
# 20:06-20:46
한 노드에서 가장 먼 노드 구하기
거리는 모두 1로 동일
dijkstra
heapq 이용
'''
import heapq
INF = int(1e9)

def solution(n, edge):
    # Note that It's undirected graph
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for v in edge:
        v1, v2 = v
        graph[v1].append((v2, 1))
        graph[v2].append((v1, 1))
    
    # Dijkstra
    start = 1
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if cost > distance[now]:
            continue
        for i in graph[now]:
            adj_node, adj_cost = i
            cur_cost = adj_cost + cost
            if cur_cost < distance[adj_node]:
                distance[adj_node] = cur_cost
                heapq.heappush(q, (cur_cost, adj_node))
    
    # Find max distance without INF
    max_dist = 0
    answer = 0
    for i in distance:
        if i < INF:
            max_dist = max(max_dist, i)
    for i in distance:
        if max_dist == i:
            answer += 1
    return answer