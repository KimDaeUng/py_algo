# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    N = len(A)

    if N < 1:
        return 1

    max_a = max(A)
    counter = [0] * (max_a + 1)

    for i in A:
        counter[i - 1] = 1
    
    for n, i in enumerate(counter, start=1):
        if i == 0:
            return n