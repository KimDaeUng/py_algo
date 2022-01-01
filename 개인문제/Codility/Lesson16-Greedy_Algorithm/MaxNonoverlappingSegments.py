
# My Solution
# https://app.codility.com/demo/results/training9DJZB5-SBU/
def solution(A, B):
    n = len(A)
    if n < 1:
        return 0
    
    answer = 1
    last_end = B[0]

    for i in range(1, n):
        if A[i] > last_end:
            answer += 1
            last_end = B[i]
    return answer