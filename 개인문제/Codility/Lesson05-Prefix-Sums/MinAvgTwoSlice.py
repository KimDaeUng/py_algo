

# My Solution 2:
# https://app.codility.com/demo/results/trainingCEFZZ4-7YW/
def solution(A):
    min_avg = (A[0] + A[1])/2
    answer = 0
    if len(A) == 2:
        return answer
    for s in range(len(A) - 2):
        cur_avg = min((A[s] + A[s + 1]) / 2,
                      (A[s] + A[s + 1] + A[s + 2]) / 3)
        if cur_avg < min_avg:
            min_avg = cur_avg
            answer = s
    else:
        s += 1
        cur_avg = (A[s] + A[s + 1]) / 2
        if cur_avg < min_avg:
            min_avg = cur_avg
            answer = s
    return answer

# My Solution 1 : Fail
def solution(A):
    prefix_sum = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        prefix_sum[i] = prefix_sum[i-1] + A[i - 1]
    min_mean = 10 ** 9
    min_sidx = 0
    for e in range(2, len(A) + 1):
        for s in range(1, e):
            tmp_mean = prefix_sum[e] - prefix_sum[s - 1]
            if min_mean > tmp_mean:
                min_mean = tmp_mean
                min_sidx = s - 1
    
    return min_sidx