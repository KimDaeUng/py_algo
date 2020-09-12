# https://leetcode.com/problems/course-schedule/
class Solution:

    def dfs(self, node, graph,, visited):
        # 더 이상 node를 선수로 한 방문 노드가 없을 떄
        if node not in graph:
            return True 

        for n in graph[node]:
            # 이미 방문 중인 노드라면
            # 해당 노드의 완료 여부를 리턴
            if n in visited:
                return visited[n] == 2
            # 노드를 방문 중인 상태로 변경
            visited[n] = 1
            if not self.dfs(n, graph, visited):
                return False
            # 노드를 완료로 변경
            visited[n] = 2
        
        return True
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for p in prerequisites:
            graph[p[1]].append(p[0])

        visited = defaultdict(int)

        for node in graph:
            visited[node] = 1
            if not self.dfs(node, graph, visited):
                return False # 이미 방문한 노드를 재방문 한 경우(Cycle이 존재하는 경우)
            visited[node] = 2
        
        return True