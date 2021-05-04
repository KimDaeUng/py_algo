# Programmers의 가장 먼 노드 문제와 거의 동일
# https://programmers.co.kr/learn/courses/30/lessons/49189

'''
# 20:06-20:46
한 노드에서 가장 먼 노드 구하기
거리는 모두 1로 동일
dijkstra
heapq 이용
'''
import heapq
INF = int(1e9)

string = '''6 7
3 6
4 3
3 2
1 3
1 2 
2 4
5 2'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

n, m = map(int, input().split())
edge = []
for i in range(m):
    edge.append(list(map(int, input().split())))


def solution(n, edge):
    # Note that this is undirected graph
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
    
    # Find answer
    max_dist = 0
    min_idx_max_dist = INF
    dup_count = 0

    for i in distance:
        if i < INF:
            max_dist = max(max_dist, i)
    for i, d in enumerate(distance):
        if max_dist == d and i != 0:
            min_idx_max_dist = min(i, min_idx_max_dist)
            dup_count += 1

    return ' '.join(list(map(str, [min_idx_max_dist, max_dist, dup_count])))

print(solution(n, edge))

# Solution
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 최단 거리가 가장 먼 노드 번호
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))