# https://leetcode.com/problems/number-of-islands/

# My Solution
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        visited = [[0] * N for _ in range(M)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        def bfs(start, visited):
            x, y = start
            visited[x][y] = True
            queue = deque([start])
            
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if nx < 0 or nx >= M or ny < 0 or ny >= N \
                        or visited[nx][ny] == 1 or grid[nx][ny] == "0":
                        continue
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
            
        answer = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    bfs((i, j), visited)
                    answer += 1

        return answer