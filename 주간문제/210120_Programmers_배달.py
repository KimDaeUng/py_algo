# https://programmers.co.kr/learn/courses/30/lessons/12978

# My Solution(Retry)
from collections import deque
from collections import defaultdict
import sys
# 각 위치까지의 최단거리를 저장해 놓는 리스트를 만들고
# 조건을 만족하는 것의 개수 카운트
# 탐색시 BFS 수행하고, 각 지점간의 최단 거리를 저장하여 불러와 사용

def solution(N, board, K):
    # 1부터 각 지점까지의 최단거리 (인덱스 맞추기 위해 길이가 N+1)
    min_dist = [sys.maxsize for i in range(N + 1)]
    min_dist[1] = 0
    
    # 각 지점간의 최소 거리를 저장
    dist_mtx = [ [sys.maxsize for _ in range(N + 1)] for _ in range(N + 1) ]
    # 인접 노드를 쉽게 검색하기 위한 변환
    graph = defaultdict(list)
    for info in board:
        a, b, dist = info
        graph[a].append(b)
        graph[b].append(a)
        # 현재 주어진 연결정보의 거리(dist)가 이전 정보보다 작으면
        tmp_dist = min(dist_mtx[a][b], dist)
        dist_mtx[a][b] = tmp_dist
        dist_mtx[b][a] = tmp_dist
    
    # BFS 탐색
    q = deque([1]) # 시작노드 1
    
    while q:
        cur_node = q.popleft()
        # 현재 노드의 인접 노드들을 모두 탐색
        for sub_node in graph[cur_node]:
            dist = min_dist[cur_node] + dist_mtx[cur_node][sub_node]
            # 계산된 1부터 sub_node까지의 거리가 기존 최단거리보다 작고,
            # K이하의 거리일 경우 min_dist를 갱신 후, 큐에 추가
            if dist < min_dist[sub_node] and dist <= K:
                min_dist[sub_node] = dist
                q.append(sub_node)
    
    return len([ i for i in min_dist if i <= K ])


# Test
N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4

print(solution(N, road, K))

# Solution
# https://jinomadstory.tistory.com/111
from math import inf
from collections import defaultdict
from collections import deque

def solution(N, roads, K):
    # 1에서 해당 마을까지의 최단거리
    answer = [inf, 0] + [inf for i in range(N-1)]
    graph = defaultdict(list) # 각 마을에서 갈 수 있는 경로
    dist_array = [[inf for _ in range(N+1)] for _ in range(N+1)]

    # graph, dist_array의 정보 저장
    for info in roads:
        a, b, dist = info
        graph[a].append(b)
        graph[b].append(a)
        # 각 노드간의 최소 거리만 저장하게함
        if dist_array[a][b] > dist:
            dist_array[a][b], dist_array[b][a] = dist, dist
    
    queue = deque([1])
    while queue:
        cur_node = queue.popleft()
        sub_nodes = graph[cur_node]

        for sub_node in sub_nodes:
            # dist = cur_node 까지의 최단거리 + cur_node->sub-node 사이의 거리
            dist = answer[cur_node] + dist_array[cur_node][sub_node]
            # dist 가 1부터 sub_node 까지의 최단거리 보다 작고, and K이하인 경우
            if dist < answer[sub_node] and dist <= K:
                answer[sub_node] = dist
                queue.append(sub_node)

    return len(answer) - answer.count(inf)


# My Solution(Fail)
# from collections import deque
# def solution(N, road, K):
#     answer = 0

#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')

#     # 1번 마을에서 배달에 4시간 이하가 걸리는 마을은 [1, 2, 3, 4,]

#     graph = {}
#     for info in road:
#         node1, node2, time_cost = info
#         if node1 not in graph:
#             graph[node1] = [(node2, time_cost)]
#         elif (node2, time_cost) not in graph[node1]:
#             graph[node1].append((node2, time_cost))
        
#         if node2 not in graph:
#             graph[node2] = [(node1, time_cost)]
#         elif (node1, time_cost) not in graph[node2]:
#             graph[node2].append((node1, time_cost))

    
#     # BFS
#     def bfs(graph, root):
#         visited = []
#         queue = deque([root]) # root : tuple (number, cost=0)
#         total_cost = 0

#         while queue:
#             node, cost = queue.popleft()
#             total_cost += cost
#             if node not in visited:
#                 visited.append((node, cost))
#                 if node in graph:
#                     temp = list(set(graph[node]) - set(visited))
#                     temp.sort(key=lambda x : x[0])
#                     queue += temp
        
#         return visited
    
#     visited = bfs(graph, (1, 0))
#     answer = []
#     for node, cost in visited:
#         if cost <= K:
#             if node not in answer:
#                 answer.append(node)

#     return answer


# Retry(18:29-)

# BFS로 각 지점의 거리를 추적하고,
# 1번 마을부터 일정거리 이내의 개수를 카운트

# from collections import defaultdict, deque
# from sys import int_info
# def solution(N, road, K):

#     # 처리하기 쉬운 형태로 변환
#     graph = {}

#     for info in road:
#         a, b, cost = info
#         a -= 1
#         b -= 1
        
#         if a not in graph:
#             graph[a] = [(b, cost)]
#         elif (b, cost) not in graph[a]:
#             graph[a].append((b, cost))

#         if b not in graph:
#             graph[b] = [(a, cost)]
#         elif (a, cost) not in graph[b]:
#             graph[b].append((a, cost))

#     q = deque([])
#     root = (0, 0)
#     q.append(root)

#     visited = []
#     costs = [ 0 for _ in range(N) ]
#     costs[0] = 0

#     while q:
#         node = q.popleft()
#         # 현재 지점의 인접 노드 방문 
#         for sub_node, sub_cost in graph[node]:
#             # 현재 비용 계산
#             cur_cost = costs[node] + sub_cost
#             if cur_cost < 


#             if (sub_node, sub_cost) not in visited :
#                 q.append((sub_node, cost + sub_cost))
#                 visited.append((sub_node, sub_cost))
#         # visited.append((node, cost))
    
#     count = len([ i for i in costs if 0 <= i <= K])
#     costs[node] = cost 
#     print(costs)
#     return count

