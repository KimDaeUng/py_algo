# https://www.acmicpc.net/problem/11657

'''
음의 간선이 존재하는 그래프에서 최단 경로 탐색?
1번 도시에서 출발해서 나머지 도시 모두로 가는 가장 빠른 시간

'''
# My Solution
import sys
input = sys.stdin.readline
INF = int(1e9)

def bmf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur, next_node, cost = edges[j]
            # 시작 노드로부터 현재 노드 cur를 거쳐서 next_node로 가는 비용이
            # 시작 노드에서 바로 가는 비용보다 더 크다면
            if dist[cur] != INF and dist[cur] + cost < dist[next_node]:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환
                if i == n - 1:
                    return True
    return False

n, m = map(int,input().split())
dist = [INF] * (n + 1)

edges = []
for i in range(m):
    a, b, c = map(int,input().split())
    edges.append((a, b, c))

neg_cycle = bmf(1)

if neg_cycle:
    print('-1')
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])


## Solution
import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전제 n번의 round 반복
    for i in range(n):
        # 매 반복마다 '모든 간선'을 확인하여
        for j in range(m):
            cur = edges[j][1]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False

# 노드 개수, 간선 개수
n, m = map(int,input().split())
# 모든 간선 정보 담는 리스트
edges = []
# 최단 거리 테이블 모두 무한으로 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int,input().split())
    edges.append((a, b, c))

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우, -1 출력
        if dist[i] == INF:
            print('-1')
        # 도달할 수 있는 경우 거리 출력
        else:
            print(dist[i])