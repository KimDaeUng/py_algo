# https://programmers.co.kr/learn/courses/30/lessons/12913
# 3h?

# My Solution: Retry
# ref: https://ssungkang.tistory.com/entry/%EB%95%85%EB%94%B0%EB%A8%B9%EA%B8%B0%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4level2
# 솔루션 보고 다시 품
def solution(land):
    N = len(land)
    for i in range(1, N):
        for j in range(4):
            land[i][j] += max([land[i - 1][k] for k in range(4) if k != j])
    return max(land[N-1])

# Solution
def solution(land):
    N = len(land)
    for i in range(1, N):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1: ])
    return max(land[-1])