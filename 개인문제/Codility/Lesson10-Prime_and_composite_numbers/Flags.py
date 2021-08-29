# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
# 2h
# My Solution: Fail
# https://app.codility.com/demo/results/trainingFSDVK9-8V7/
def solution(A):
    if len(A) <= 2:
        return 0
    
    # peak candidates:
    p_cand = []
    for p in range(1, len(A)-1):
        if A[p - 1] < A[p] and A[p + 1] < A[p]:
            p_cand.append(p)


    if len(p_cand) < 1:
        return len(p_cand)
    
    # peaks
    min_diff = int(1e9)
    for i in range(len(p_cand) - 1):
        # diffs.append(abs(p_cand[i] - p_cand[i + 1]))
        min_diff = min(min_diff, abs(p_cand[i] - p_cand[i + 1]))

    return min_diff + 1

# Solution
# https://app.codility.com/demo/results/trainingU54KPU-Q36/
# ref:https://datacodingschool.tistory.com/71

def solution(A):
    if len(A) <= 2:
        return 0
    
    # peak candidates:
    p_cand = []
    for p in range(1, len(A)-1):
        if A[p - 1] < A[p] and A[p + 1] < A[p]:
            p_cand.append(p)


    if len(p_cand) <= 1:
        return len(p_cand)
    
    p_arr = [0] * len(A)
    p_arr[0] = p_arr[-1] = -1
    
    p_idx = -1
    for p in range(len(A)-2, 0, -1):
        if A[p - 1] < A[p] and A[p + 1] < A[p]:
            p_idx = p
        p_arr[p] = p_idx
    
    max_n_flag = -1

    for i in range(1, len(p_cand) + 1):
        idx = 1
        n_flag = 0

        while n_flag < i:
            if idx < len(p_arr):
                if p_arr[idx] != -1:
                    n_flag += 1
                    idx = p_arr[idx] + i
                else:
                    return max_n_flag
            else:
                return max_n_flag

        max_n_flag = max(max_n_flag, n_flag)
    
    return max_n_flag