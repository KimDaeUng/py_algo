# https://www.acmicpc.net/problem/3665
# 약 6시간
# 접근법
# 정해진 우선 순위에 맞게 전체 팀 순서를 나열해야 한다
# -> Topological Sort
# 순위 정보를 그래프 정보로 표현한 뒤, 위상 정렬 알고리즘 이용
# 높은 등수 -> 낮은 등수로 방향 그래프 표현하면
# 높은 등수가 먼저 진입차수가 0이 되어 뽑히기 때문에 순위 표현 가능
# 상대 순위가 뒤집히는 경우는 두 노드 간의 간선 방향이 뒤집히는 것으로 표현
# # 올바른 순위 여부 체크
# - 위상 정렬 수행 과정에서 큐에서 노드 뽑을 때 큐의 원소가 항상 1개로 유지되는 경우에만 고유 순위 존재
# - 사이클이 존재할 경우엔 순위가 결정되지 않음

string = '''3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 4 : 아래 코드를 다시 정리한 코드
from collections import deque
t = int(input())
for _ in range(t):
    # 노드의 개수와 순위 정보 입력받기
    n = int(input())
    nodes = list(map(int, input().split()))
    
    # 위상정렬을 위한 graph, indegree table
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    # 자신 보다 낮은 등수를 가진 팀을 가리키도록 방향 그래프
    for i in range(n):
        for j in range(i + 1, n):
            graph[nodes[i]][nodes[j]] = 1
            indegree[nodes[j]] += 1
    
    # 상대 순위 변경
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        # x -> y 방향이거나, y -> x 방향일 수 있음
        # 두 경우 모두 고려해 방향을 뒤집어 줘야함
        # 1. x -> y
        if graph[x][y] == 1:
            graph[x][y] = 0
            graph[y][x] = 1
            indegree[x] += 1
            indegree[y] -= 1
        # 2. y -> x
        else:
            graph[x][y] = 1
            graph[y][x] = 0
            indegree[x] -= 1
            indegree[y] += 1

    # 위상 정렬 수행
    q = deque()
    # 1. 진입 차수 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 2. 큐가 진행되는 동안
    unique_count = 0
    cycle_count = 0
    result = []
    while q:
        now = q.popleft()
        result.append(now)
        cycle_count += 1
        # 현재 노드와 연결된 모든 간선을 제거
        unique_count = 0
        for i in range(1, n + 1):
            if graph[now][i] == 1:
                indegree[i] -= 1
                # 제거한 간선의 진입 차수가 0이 된 경우 큐에 추가
                if indegree[i] == 0:
                    q.append(i)
                    unique_count += 1

    if cycle_count < n:
        print("IMPOSSIBLE")
    elif unique_count > 1:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()

            

# My Solution 3 :
# 1, 2 시도는 Kruskal로 완전히 잘못 접근함
# 아래는 솔루션으로 아이디어 잡은 뒤 다시 푼 코드
# 문제 조건 체크에 지저분한 부분 있음
def topology_sort(n, nodes, m, changes_x, changes_y):
    indegree = [0] * (n + 1)
    graph = [[0] * (n + 1) for i in range(n + 1)]
    # 자기보다 낮은 등수를 가진 팀을 가리키도록 방향 그래프
    for i in range(n):
        x = nodes[i]
        for j in range(i + 1, n):
            y = nodes[j]
            graph[x][y] = 1
            indegree[y] += 1
    # 상대적인 순위 바꾸기
    for i in range(m):
        x, y = changes_x[i], changes_y[i]
        # print('x, y', x, y)
        if graph[x][y] == 0:
            graph[x][y] = 1
            graph[y][x] = 0
            indegree[x] -= 1
            indegree[y] += 1
        elif graph[x][y] == 1:
            graph[x][y] = 0
            graph[y][x] = 1
            indegree[x] += 1
            indegree[y] -= 1
    
    # pprint(graph)
    # pprint(indegree)
    result = []
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    pop_count = 0
    certrain = True
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        pop_count += 1
        result.append(now)
        # 해당 원소와 연결된 노드의 진입 차수에서 1 빼기
        count = 0 
        for i, v in enumerate(graph[now][1:], start=1):
            # 연결되어 있다면 연결된 노드의 진입 차수에서 1을 뺸다
            if v == 1:
                indegree[i] -= 1
            # 새롭게 진입 차수가 0이 되는 노드 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)
                    count += 1
        # 1. 위상 정렬 결과가 여러 개인 경우 확인
        # (진입 차수가 0인 노드의 개수가 2 이상)
        if count > 1:
            print("?")
            return
    # 2. 사이클이 발생하는 경우 확인
    # (n개의 노드를 뽑기 전에 큐가 비는 경우)
    if pop_count < n:
        print("IMPOSSIBLE")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in result:
            print(i, end=' ')
        print()

t = int(input())
for _ in range(t):
    # 노드의 개수와 순위 정보 입력받기
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    changes_x = []
    changes_y = []
    for i in range(m):
        x, y =map(int,input().split())
        changes_x.append(x)
        changes_y.append(y)
    topology_sort(n, data, m, changes_x, changes_y)



        
# Solution
from collections import deque

# 테스트 케이스만큼 반복
for tc in range(int(input())):
    # 노드 개수 입력 받기
    n = int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n + 1) for i in range(n + 1)]
    # 작년 순위 정보 입력
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    
    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    # 위상 정렬(Topology Sort) 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    # 처음 시작시 진입차수 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    certain = True # 위상 정렬 결과가 오직 하나인지 여부
    cycle = False  # 그래ㅐ프 내 사이클 존재 여부

    # 정확히 노드 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면 사이클 발생의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)
    
    # 사이클이 발생하는 경우(일관성 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif not certain:
        print("?")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in result:
            print(i, end=' ')
        print()