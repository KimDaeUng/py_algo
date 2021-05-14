# https://programmers.co.kr/learn/courses/30/lessons/43164
# 23:35-05:00

# My Solution 3 : DFS - Recursive
from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for k in graph.keys():
        graph[k].sort()
    
    target_len = len(tickets) + 1
    def dfs(start, footprint):
        # start : str, footprint : list
        
        if len(footprint) == target_len:
            return footprint
        
        idx = 0
        limit = len(graph[start])
        while idx < limit:
            node = graph[start].pop(idx)
            
            fp = footprint[:] + [node]
            
            path = dfs(node, fp)
            if path: return path
            graph[start].insert(idx, node)
            idx += 1
        # While문 대신
#         for idx, node in enumerate(graph[start]):
#             graph[start].pop(idx)
            
#             fp = footprint[:] + [node]
            
#             path = dfs(node, fp)
#             if path: return path
            
#             graph[start].insert(idx, node)
            
    answer = dfs('ICN', ['ICN'])
    return answer

    
# My Solution 2: DFS - iterative : Retry 
from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    for (a, b) in tickets:
        graph[a].append(b)
    for k in graph:
        graph[k].sort(reverse=True)
    
    st = ['ICN']
    answer = []
    while st:
        node = st[-1]
        
        # 1. 현재 노드에서 시작하는 티켓이 없는 경우
        # - 입력 데이터 자체에서 없거나, 티켓을 모두 쓴 경우
        if node not in graph or not graph[node]:
            answer.append(st.pop())
        
        # 2. 경로 탐색이 가능한 경우
        # - 현재 노드를 시작점으로 하는 티켓이 존재
        else:
            st.append(graph[node].pop())
    
    answer.reverse()
    return answer    

# Solution 2 : DFS Recursive
from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for k, v in tickets:
            routes[k].append(v)

    def dfs(key, footprint):
        if len(footprint) == N + 1:
            return footprint
        
        for idx, country in enumerate(routes[key]):
            routes[key].pop(idx)

            fp = footprint[:] # copy
            fp.append(country)

            ret = dfs(country, fp)
            if ret: return ret # 모든 티켓을 사용해 통화한 경우

            routes[key].insert(idx, country) # 통과 못했으면 티켓 반환
    
    routes = init_graph()
    for r in routes:
        routes[r].sort()
    N = len(tickets)
    answer = dfs('ICN', ['ICN'])



    

# Solution 1 : DFS iterative
from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for k, v in tickets:
            routes[k].append(v)
    
    # 스택을 사용한 DFS
    def dfs():
        stack = ['ICN']
        path = [] # 가려고 하는 경로를 저장하는 변수
        while stack:
            top = stack[-1]
            # 특정 공항에서 출발하는 표가 없다면
            # 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or not routes[top]:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop())
        
        return path[::-1]
    
    routes = init_graph()
    for r in routes:
        routes[r].sort(reverse=True)
    answer = dfs()
    return answer


# My Solution 1 : Stack, DFS : Fail
import heapq as hq
def solution(tickets):
    answer = []
    st = []
    st.append(("ICN", ["ICN"]))
    visited = []
    paths = []
    len_tickets = len(tickets)
    tickets_backup = tickets[:]
    # tickets_removed = []
    while st:
        node, path = st.pop()
        if len(path) == len_tickets + 1:
            paths.append(path)
            
        # elif len(tickets) == 0:
        #     ticket = tickets_backup
            
            # tickets = tickets_backup
            # node, path = st.pop()
        # tickets.extend(visited)
            
        tmp = []
        # tickets_copy = []
        # while tickets:
        #     ticket = tickets.pop()
        #     if node == ticket[0]:
        #         tmp.append((ticket[-1], path + [ticket[-1]]))
        #         # visited.append((ticket[-1], path + [ticket[-1]]))
        #         visited.append(ticket)
        #     else:
        #         tickets_copy.append(ticket)
        # tickets = tickets_copy
            
        for ticket in tickets:
            if node == ticket[0]:
                tmp.append((ticket[-1], path + [ticket[-1]]))
                visited.append(ticket)
                # tickets.remove(ticket)
                
        # print(tmp)
        # print('tickets : ', tickets)
        tmp = sorted(tmp,reverse=True, key=lambda x : x[0])
        # print('tmp : ', tmp)
        st.extend(tmp)
        # print('stack', st)
        
    print('path', paths)
                
        
                
                
                
    return paths[0]