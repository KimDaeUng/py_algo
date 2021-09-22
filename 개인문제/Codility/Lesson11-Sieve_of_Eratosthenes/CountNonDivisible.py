

# My Solution: Fail
# https://app.codility.com/demo/results/training7H2ZQ7-5P3/

def solution(A):
    result = [0] * len(A)
    for i in range(len(A)):
        target = A[i]
        ct = 0
        for j in range(len(A)):
            if target % A[j] != 0 and A[j] != A[i] and A[j] != 1:
                ct += 1
        result[i] = ct
    return result