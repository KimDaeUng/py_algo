# https://programmers.co.kr/learn/courses/30/lessons/72413
# 17:37-20:41 : 못 품 

# My Solution 3 : Dijstra
# N 번의 다익스트라를 수행하는 방법
import heapq as hq
def solution(n, s, a, b, fares):
    INF = int(1e9)
    s -= 1
    a -= 1
    b -= 1
    
    graph = [[] for i in range(n)]
    
    for edge in fares:
        c, d, f = edge
        graph[c - 1].append((f, d - 1))
        graph[d - 1].append((f, c - 1))
    
    def dijstra(start, graph):
        distance = [INF] * n # minimum dist table
        q = []
        hq.heappush(q, (0, start)) # (cost, node)
        distance[start] = 0
        
        while q:
            dist, now = hq.heappop(q)
            if distance[now] < dist:
                continue
            for adj_dist, adj_node in graph[now]:
                cost = dist + adj_dist
                if cost < distance[adj_node]:
                    distance[adj_node] = cost
                    hq.heappush(q, (cost, adj_node))
                    
        return distance
    
    all_dist = [dijstra(k, graph) for k in range(n)]

    answer = INF
    for k in range(n):
        answer = min(answer, all_dist[s][k] + all_dist[k][a] + all_dist[k][b])
        
    return answer

# My Solution 2 : Retry
# Floyd-Warshall을 이용한 풀이
# 모든 경로간의 최단 거리를 담은 인접 행렬 costs를 구하고
# 출발점 s, 도착점 a, b, 경유지 k 라할 때
# costs[s][k] + costs[k][a] + costs[k][b]가 최소가 되는 k를 찾으면 된다.
def solution(n, s, a, b, fares):
    s -= 1
    a -= 1
    b -= 1
    INF = int(1e10)
    costs = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                costs[i][j] = 0
    for edge in fares:
        c, d, f = edge
        costs[c-1][d-1] = f
        costs[d-1][c-1] = f
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
    
    answer = INF
    for k in range(n):
        answer = min(answer, costs[s][k] + costs[k][a] + costs[k][b])

    return answer

# Solution 1 : 위의 내 풀이와 동일, 생략

# Solution 2 : Dijstra를 이용한 다른 풀이
# 두 번째 for 문이 모든 경유지에 대한 다익스트라 수행
# 위의 내 풀이보다 매우 느림.
from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    for st, ed, co in fares:
        dic[st].append((co, ed))
        dic[ed].append((co, st))
    ans = []
    for i in range(1, n+1):
        Q = [(0, i)]
        visited = [True] * (n+1)
        dp = [float('inf')] * (n+1)
        dp[i] = 0
        while Q:
            co, des = heapq.heappop(Q)
            if visited[des]:
                visited[des] = False
                for cost, destination in dic[des]:
                    dp[destination] = min(cost + dp[des], dp[destination])
                    heapq.heappush(Q, (dp[destination], destination))
        ans.append(dp[a] + dp[b] + dp[s])

    return min(ans)

# My Solution : Fail
'''
1. Kruskal 이용
- 비용이 최소인 간선 먼저 연결되므로, 그러나 굳이 경유하지 않을 간선까지 포함할 수 있음
-> a와 b가 포함된 모든 간선이 연결된 그래프 찾기?
2. Floyd-Warshall
- n = 200 -> n^3 = 8,000,000 -> 충분히 해볼만
-> 모두 실패
-> 경로 찾기 코드는 비슷하게 구현함
'''

# 	[[inf, inf, inf, inf, inf, inf, inf], 
#     [inf, 0, 63, 41, 10, 24, 25], 
#     [inf, 63, 0, 22, 66, 46, 48], 
#     [inf, 41, 22, 0, 51, 24, 26], 
#     [inf, 10, 66, 51, 0, 34, 35], 
#     [inf, 24, 46, 24, 34, 0, 2], 
#     [inf, 25, 48, 26, 35, 2, 0]]

# 4 -> 6 : 35
# 4 -> 2 : 66
# -> 101

# 중복되는 경로?

# 2: 63,  0, 22, 66, 46, 48
# 6: 25, 48, 26, 35,  2,  0

# A, B 모두 아래와 같은 상황
# S에서 바로 가는 경로 != S에서 다른 곳을 경유하는 최단 경로 != 합승하는 경로

# A, B, S가 반드시 존재하는 MST를 구하고 간선의 모든 비용을 더한 값과
# 플로이드 워셜로 구한 두 최단 경로의 단순합을 비교해 더 작은 값 출력?

    # Floyd-Warshall


    # print(graph)



from collections import deque

def solution(n, s, a, b, fares):
    def direct_floyed(n, fares):
        INF = int(1e9)
        graph_f = [[INF] * (n + 1) for _ in range( n + 1 )]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph_f[i][j] = 0
        
        
        for line in fares:
            c, d, f = line
            graph_f[c][d] = f
            graph_f[d][c] = f
        
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    graph_f[i][j] = min(graph_f[i][j], graph_f[i][k] + graph_f[k][j])

        return graph_f
    
    graph_f = direct_floyed(n, fares)

    # Kruskal
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
    
    parent = list(range(n + 1))
    # parent_pathcomp = list(range(n + 1))

    # 간선 정보 
    edges = []
    for line in fares:
        c, d, f = line
        edges.append((f, c, d))
        edges.append((f, d, c))
    
    edges.sort()

    def check(edge_list, start, a, b):
        # start에서 시작해 A, B까지 연결되어 있다면 경로를 리턴
        # grpah 생성
        graph = {}
        for edge in edge_list:
            f, c, d = edge
            if c not in graph:
                graph[c] = [(f, d)]
            else:
                graph[c].append((f, d))
            if d not in graph:
                graph[d] = [(f, c)]
            else:
                graph[d].append((f, c))
        # s, a, b가 포함되어 있지 않으면 BFS를 수행하지 않음
        if start not in graph or a not in graph or b not in graph:
            return False
        

        # BFS를 S에서 시작해서 A, B에 도달하는지 확인
        visited = [False] * (n + 1)
        q = deque([])
        q.append((0, start, str(start)))
        

        result_path = []
        # print(graph)
        while q:
            now_cost, now_node, path = q.popleft()
            # print(now_node)
            visited[now_node] = True
            # a, b에 도달한 경우 path에 추가
            # if path.endswith(str_a) or \
            #    path.endswith(str_b):
            result_path.append((now_cost, path))
            
            for next_cost, next_node in graph[now_node]:
                if not visited[next_node]:
                    q.append((now_cost + next_cost, next_node, path + " " + str(next_node)))
                
        if visited[s] + visited[a] + visited[b] == 3:
            return result_path
        else:
            return False
        
    cost_total = 0
    edge_list = []
    for edge in edges:
        f, c, d = edge
        # 사이클이 발생하지 않는 edge만 집합에 포함
        if find_parent(parent, c) != find_parent(parent, d):
            # edge_list에 최소 엣지만 포함?
            edge_list.append((f, c, d))
            edge_list.append((f, d, c))
            union_parent(parent, c, d)
            cost_total += f
            # 현재까지 그래프가 a, b, s를 포함하는 MST인지 확인
            p = check(edge_list, s, a, b)
            if p:
                break
            else:
                continue
    print('p : ', p)
    print('edge_list : ', edge_list)
    str_a = str(a)
    str_b = str(b)
    result = []
    for p_cost, cum_p in p:
        if cum_p.endswith(str_a):
            result.append((p_cost, cum_p))
        if cum_p.endswith(str_b):
            result.append((p_cost, cum_p))
    result = list(set(result))
    print('result : ', result)
    # a, b 어느 한쪽을 갔다가 상대쪽으로 가는 경우
    if len(result) == 1:
        answer = result[0][0]
    # a, b가 따로 가는 경우
    else:
        path_a = result[0][1].split()
        path_b = result[1][1].split()
        path_com = []
        for pa, pb in zip(path_a, path_b):
            if pa == pb:
                path_com.append(pa)
            else:
                break
        path_com = ' '.join(path_com)
        # print(path_com)
        com_cost = [ i[0] for i in p if i[1] == path_com][0]
        # print(com_cost)
        a_cost = result[0][0]
        b_cost = result[1][0]

        diverge_cost = a_cost + b_cost - com_cost
        direct_cost = graph_f[s][a] + graph_f[s][b]
        answer = min(diverge_cost, direct_cost)
    
    return answer

        
    if p:
        answer = min(p[0][0], cost_total)
    else:
        answer = cost_total
    return answer

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n, s, a, b = 7, 3, 4, 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

n, s, a, b = 6, 4, 5, 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

print(solution(n, s, a, b, fares))