

# My Solution: Fail
def solution(A):
    if len(A) <= 2:
        return 0

    p_cand = []
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            p_cand.append(i)

    if len(p_cand) <= 1:
        return len(p_cand)

    p_arr = [0] * len(A)
    p_arr[0] = p_arr[-1] = 0

    for p in p_cand:
        p_arr[p] = 1
    
    # print(p_arr)

    n = len(A) 
    # n_sqrt = int(n ** 0.5)

    block_slice = []
    for i in range(1, n + 1):
        q, r = divmod(n, i)
        if r == 0:
            block_slice.append((q, i))
    # print(block_slice)
    max_n_block = 0
    for span, n_block in block_slice:
        # print(span, n_block)
        for i in range(n_block):
            # print('\t',i * span, (i + 1) * span)
            # print('\t',sum(p_arr[i * span:(i + 1) * span]))
            if sum(p_arr[i * span:(i + 1) * span]) == 0:
                return max_n_block
        max_n_block = max(n_block, max_n_block)
        
    return max_n_block