
# 19:34-45 : 다익스트라로 착각
# 19:45-19:58
'''
"시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다." 조건에 주의
-> 간선 정보를 저장할 때 매번 min 값으로 갱신해야함
'''
string = '''5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

    
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != INF:
            print(graph[i][j], end=' ')
        else:
            print(0, end=' ')
    print()

# Solution
INF = int(1e9)

n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)을 만ㄷ르고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
    
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+ 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력 
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 0 출력
        if graph[a][b] == INF:
            print(0, end=' ')
        # 도달할 수 있는 경우, 거리를 출력
        else:
            print(graph[a][b], end=' ')
    print()