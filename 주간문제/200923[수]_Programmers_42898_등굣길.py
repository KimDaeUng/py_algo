# https://programmers.co.kr/learn/courses/30/lessons/42898


def solution(m, n, puddles):
    answer = 0
    grid = [[0]*(m+1) for _ in range(n+1)]
    
    grid[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                grid[i][j] = 0
            else:
                grid[i][j] += grid[i-1][j] + grid[i][j-1]
    
    answer = grid[i][j] % 1000000007
    
    return answer