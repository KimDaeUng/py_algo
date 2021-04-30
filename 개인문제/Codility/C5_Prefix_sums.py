# How to calculate the prefix sums in O(n) time complexity.
# p_k = p_{k-1} + a_{k-1}

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

# Mushroom picker O(N + M)
def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    
    # 탐색 범위
    # [k-m, k], [k-m-1, k+1], ..., [k, k + m]
    # 그런데 k-m에서 m > k 인 경우가 생기면 범위를 벗어남
    # 따라서 범위 이탈 방지 위해
    #   - m < k이면 m까지만 좌측 탐색
    #   - m > k이면 k까지만 좌측 탐색
    # 왼쪽 이동 거리 p는 left_pos = p [0, min(m, k)]
    # 오른쪽 이동 거리는
    #   - m < k 일 때 
    #   - m > k 일 때 k + m - 2 * p

    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return result


A = [2, 3, 7, 5, 1, 3, 9]
k = 4
m = 2
print(mushrooms(A, k, m))
A = [2, 3, 7, 5, 1, 3, 9]
k = 4
m = 6
print(mushrooms(A, k, m))
