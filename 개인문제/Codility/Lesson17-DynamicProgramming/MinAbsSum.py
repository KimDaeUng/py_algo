
# My Solution 2 : Fail
# https://app.codility.com/demo/results/trainingAY5R53-8NN/
def solution(A):
    N = len(A)
    if N == 0:
        return 0
    elif N == 1:
        return A[0]

    dp = [0] * N
    dp[0] = abs(A[0])
    dp[0] = min(A[0] + A[1], A[0] - A[1], key=lambda x:abs(x))

    for i in range(1, N):
        for j in range(i, N):
            if j <= i:
                cands = [(0, dp[i]), (1, dp[i] - A[j]), (2, dp[i] + A[j])]
                idx, min_abs = min(cands, key=lambda x: abs(x[1]))
                dp[i] = cands[idx][1]

    return abs(dp[-1])


# My Solution : Fail
# https://app.codility.com/demo/results/trainingFDED73-V28/def solution(A):
def solution(A):
    N = len(A)
    if N == 0:
        return 0
    elif N == 1:
        return A[0]

    # Desecending with index
    sort_A = sorted([(i, a) for i, a in enumerate(A)], key=lambda x : -abs(x[1]))

    # Simulation?
    cur_sum = sort_A[0][1]


    for i in range(1, N):
        sub = cur_sum - sort_A[i][1]
        add = cur_sum + sort_A[i][1]
        if abs(sub) > abs(add):
            cur_sum = add
        elif abs(sub) <= abs(add):
            cur_sum = sub

    # answer = [i[1] for i in sorted(answer, key=lambda x : x[0])]

    return abs(cur_sum)