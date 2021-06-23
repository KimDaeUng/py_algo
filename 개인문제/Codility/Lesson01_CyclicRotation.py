# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/start/

# My Solution
def solution(A, K):
    if len(A) <= 1:
        return A

    cnt = 0
    while cnt != K:
        A = [A[-1]] + A[:-1]
        cnt += 1

    return A

# Solution
# 위 코드는 K가 커질경우 시간초과
# 한 바퀴 완전 순회하는 경우는 스킵하여 빠르게 처리

def solution(A, K):
    N = len(A)
    
    if N < 2:
        return A
    
    if K >= N:
        K = K % N
    
    return A[N - K:] + A[:N - K]