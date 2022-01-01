
# https://app.codility.com/demo/results/trainingX6PPCZ-6MH/
def solution(K, A):
    n = len(A)    
    answer = 0
    cum_len = 0
    for i in range(n):
        cum_len += A[i]

        if cum_len >= K:
            answer += 1
            cum_len = 0
    
    return answer