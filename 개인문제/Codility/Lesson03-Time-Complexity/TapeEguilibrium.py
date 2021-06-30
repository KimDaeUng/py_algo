# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

# Timeout : O(N^2)
def solution(A):
    N = len(A)
    P = 1
    answer = int(1e9*2)
    while P < N:
        diff = abs(sum(A[:P]) - sum(A[P:]))
        P += 1
        answer = min(answer, diff)
    return answer

# Solution : O(N)
def solution(A):
    N = len(A)
    answer = int(1e9*2)

    L = A[0]
    R = sum(A[1:])
    
    P = 0
    while P < N - 1:
        diff = abs(L - R)
        answer = min(answer, diff)
        P += 1
        L += A[P]
        R -= A[P]
    return answer