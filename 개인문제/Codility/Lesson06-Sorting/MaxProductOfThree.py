# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
# 1H

# My Solution
def solution(A):
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    # 0이 3개 중 반드시 한 번 이상 들어가는 경우
    if A.count(0) >= len(A) - 2:
        return 0
    A = sorted(A, key=lambda x : abs(x), reverse=True)
    pos = []
    neg = []
    for i in A:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    
    cand = []
    # 양수 3개를 곱한 것 vs 음수 2개 * 양수 1개를 곱한 것을 비교
    if len(pos) >= 3:
        cand.append(pos[0] * pos[1] * pos[2])
    
    if len(neg) >= 2 and len(pos) >= 1:
        cand.append(neg[0] * neg[1] * pos[0])
    
    # 위 케이스에 해당되지 않는 나머지 경우
    cand.extend([A[0] * A[1] * A[2], A[-1] * A[-2] * A[-3]])
    
    return max(cand)