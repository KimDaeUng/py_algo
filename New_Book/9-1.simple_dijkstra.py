# '최단 거리'만을 구하는 단순화된 코드
# 데이터수가 많다는 가정 하에 input()을 sys.std.readline()으로 치환
# 모든 리스트는 (노드 개수 + 1) 크기로 할당해 노드 번호를 인덱스로 하여 바로 리스트에 접근 가능

import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드 -> b번 노드 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호 변환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])


# def testcase():
#     yield '6 11'
#     yield '1'
#     yield '1 2 2'
#     yield '1 3 5'
#     yield '1 4 1'
#     yield '2 3 3'
#     yield '2 4 2'
#     yield '3 2 3'
#     yield '3 6 5'
#     yield '4 3 3'
#     yield '4 5 1'
#     yield '5 3 1'
#     yield '5 6 2'

# G = testcase()

# def input():
#     return next(G)