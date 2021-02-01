https://programmers.co.kr/learn/courses/30/lessons/12978
from collections import deque
def solution(N, road, K):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    # 1번 마을에서 배달에 4시간 이하가 걸리는 마을은 [1, 2, 3, 4,]

    graph = {}
    for info in road:
        node1, node2, time_cost = info
        if node1 not in graph:
            graph[node1] = [(node2, time_cost)]
        elif (node2, time_cost) not in graph[node1]:
            graph[node1].append((node2, time_cost))
        
        if node2 not in graph:
            graph[node2] = [(node1, time_cost)]
        elif (node1, time_cost) not in graph[node2]:
            graph[node2].append((node1, time_cost))

    
    # BFS
    def bfs(graph, root):
        visited = []
        queue = deque([root]) # root : tuple (number, cost=0)
        total_cost = 0

        while queue:
            node, cost = queue.popleft()
            total_cost += cost
            if node not in visited:
                visited.append((node, cost))
                if node in graph:
                    temp = list(set(graph[node]) - set(visited))
                    temp.sort(key=lambda x : x[0])
                    queue += temp
        
        return visited
    
    visited = bfs(graph, (1, 0))
    answer = []
    for node, cost in visited:
        if cost <= K:
            if node not in answer:
                answer.append(node)

    return answer