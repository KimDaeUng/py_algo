# https://programmers.co.kr/learn/courses/30/lessons/43162 
# 00:14-02:58
'''
# My Solution
1. Union-Find
2. DFS(iterative, adj matrix)
3. BFS
# Solution
1. DFS(iterative, adj matrix)
2. DFS(Recursive, adj list)
'''

# My Solution 3 : BFS
# 각각의 노드를 시작점으로해서 연결된 모든 노드를 방문 완료하면 answer += 1
# visited list로 각 노드별 방문 여부 체크, 모든 노드를 방문할 때까지 수행
from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(start):
        q = deque([start])
        visited[start] = True
        while q:
            i = q.popleft()
            for j in range(n):
                if computers[i][j] and not visited[j]:
                    visited[j] = True
                    q.append(j)
    i = 0
    while not all(visited):
        if not visited[i]:
            bfs(i)
            answer += 1
        i += 1
    return answer

# My Solution 2 : DFS
# basicBFS
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(start, computers):
        st = [start]
        visited[start] = True
        while st:
            i = st.pop()
            for j in range(n):
                if computers[i][j] and not visited[j]:
                    visited[j] = True
                    st.append(j)
        
    i = 0
    while not all(visited):
        if not visited[i]:
            dfs(i, computers)
            answer += 1
        i += 1
                    
    return answer

# My Solution 1 : Union-Find Data Structure
# Union-Find 자료구조로 parent table에 있는 서로 다른 루트 노드의 개수를 리턴
def solution(n, computers):
    
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
    
    parent = list(range(n))
    
    for r in range(n):
        for c in range(n):
            if computers[r][c]:
                union_parent(parent, r, c)
    
    # 위 연산에서 누락된 경로압축 수행
    for x in range(n):
        find_parent(parent, x)

    return len(set(parent))

# Solution 1 : DFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()

            if visited[j]:
                continue

            visited[j] = True
            
            for i in range(n):
                if computers[j][i] and not visited[i]:
                    stack.append(i)
    i = 0
    while False in visited:
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    
    return answer
    
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))

# Solution 2 : Recursive DFS
# 하나의 네트워크를 방문할때마다 root node를 제외한 방문한 적 없는 adj node의 개수를 카운트한 뒤
# 전체 노드 개수 - root 노드를 제외한 노드의 개수를 구함
def solution(n, computers):
    # Adj Mtx -> Adj List
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].append(j)
    
    visited = set()
    count = [0] # 전역변수처럼 함수 내부에서도 접근가능하게 하기 위해

    def dfs_rec(graph, root, visited, count):
        visited.add(root)

        for node in graph[root]:
            if not node in visited:
                count[0] += 1
                dfs_rec(graph, node, visited, count)
    
    for i in range(n):
        dfs_rec(graph, i, visited, count)

    return n - count[0]