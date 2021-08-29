


# My Solution:Retry
# https://app.codility.com/demo/results/trainingM8B9U4-7TN/
def solution(A):
    cnt_left = {}
    cnt_right = {}
    for i in range(len(A)):
        if cnt_right.get(A[i]) is not None:
            cnt_right[A[i]] += 1
        else:
            cnt_right[A[i]] = 1

    cur_leader = 0
    cur_leader_cnt = 0
    len_left = 0
    len_right = len(A)
    n_leader = 0

    for i in range(len(A)):
        cnt_right[A[i]] -= 1
        len_right -= 1

        if cnt_left.get(A[i]) is not None:
            cnt_left[A[i]] += 1
        else:
            cnt_left[A[i]] = 1
        len_left += 1
        
        if cnt_left[A[i]] > cur_leader_cnt:
            cur_leader = A[i]
            cur_leader_cnt = cnt_left[A[i]]
        
        if cur_leader_cnt > len_left / 2 and \
           cnt_right[cur_leader] > len_right / 2:
            n_leader += 1

    return n_leader

# My Solution1: Fail
'''
For example, for the input [4, 4, 2, 5, 3, 4, 4, 4] the solution returned a wrong answer (got 2 expected 3).
'''
def solution(A):
    cnt_left = {}
    cnt_right = {}
    n = len(A)
    for i in range(n):
        if cnt_right.get(A[i]) is not None:
            cnt_right[A[i]] += 1
        else:
            cnt_right[A[i]] = 1

    cnt_leader = 0
    len_left = 0
    len_right = len(A)
    n_leader = 0

    for i in range(n):
        cnt_right[A[i]] -= 1
        len_right -= 1

        if cnt_left.get(A[i]) is not None:
            cnt_left[A[i]] += 1
        else:
            cnt_left[A[i]] = 1
        len_left += 1
        
        if cnt_left[A[i]] > cnt_leader:
            cnt_leader = A[i]
        
        if cnt_left[A[i]] > len_left // 2 and \
           cnt_right[cnt_leader] > len_right // 2:
            n_leader += 1

    return n_leader