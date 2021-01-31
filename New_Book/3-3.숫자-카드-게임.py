# 19:50-20:20
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    tmp_line = list(map(int, input().split()))
    matrix.append(tmp_line)

def solution(matrix):
    answer = max([ min(i) for i in matrix ])
    return answer

print(solution(matrix))