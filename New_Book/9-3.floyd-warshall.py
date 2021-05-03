INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

def testcase():
    yield '4'
    yield '7'
    yield '1 2 4'
    yield '1 4 6'
    yield '2 1 3'
    yield '2 3 7'
    yield '3 1 5'
    yield '3 4 4'
    yield '4 3 2'
    
G = testcase()

def input():
    return next(G)

# 노드 개수, 간선 개수 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)을 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초가화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()