# Basic O(NM)
# where N is the number of nodes, M is the number of queries
import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기
n = int(input())
parent = [0] * (n + 1) # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))


# Faster Version : O(MlogN)
import sys
input = sys.stdin.readline # 시간 초과 피하기 위한 빠른 입력 함수
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기 위한 재귀 깊이 제한 설정
LOG = 21 # 2^20 = 1,000,000 

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        # 한 칸 위의 부모 정보만 구함
        parent[y][0] = x
        dfs(y, depth + 1)
    

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0) # 루트 노드는 1번 노드
    # 2의 제곱꼴로 건너 뛰었을 때의 부모 값을 기록
    for i in range(1, LOG):
        for j in range(1, n + 1):
            # j의 2^1 번째 위의 부모 노드는
            # j의 부모 노드의 부모노드(1칸 위 부모 노드의 1칸 위 부모노드)
            # j의 2^2 번째 위의 부모 노드는
            # j의 2칸 위 부모노드의 2칸 위 부모 노드
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 항상 b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        # 깊이 차이가 충분히 클 경우 2의 제곱꼴만큼 감소하도록 만듦
        # 1 << i : 이진수 1의 비트를 왼쪽으로 i번 이동
        # 2의 제곱수보다 깊이의 차이가 큰 경우
        # 2의 제곱꼴씩 감소하도록 이동
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
        # 예를 들어 깊이 차이가 15면
        # 8, 4, 2, 1 이런식으로 줄어들게 만든다.
    
    # 부모가 같다면 바로 리턴
    if a == b:
        return a
    # 부모가 같지 않다면 같을 때까지
    # 2의 제곱 형태로 큰 값부터 작은 값까지 거슬러 올라간다.
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))