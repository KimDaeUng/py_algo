# https://app.codility.com/programmers/lessons/8-leader/dominator/

# 30m
# My Solution2
# https://app.codility.com/demo/results/training65VXWY-5A7/
def solution(A):
    n = len(A)
    cnt = {}
    half = n // 2
    for i, d in enumerate(A):
        if cnt.get(d) is not None:
            cnt[d].append(i)
        else:
            cnt[d] = [i]
    for k, v in cnt.items():
        if len(v) > half:
            return v[0]
    else:
        return -1

# My Solution: Fail(75%)
# https://app.codility.com/demo/results/trainingVNGHS4-JCJ/
'''
The following issues have been detected: wrong answers.

For example, for the input [0, 0, 1, 1, 1] the solution returned a wrong answer (got 1, but element is not a dominator, value 0 has only 2 occurences (n=5)).
array with exactly N/2 values 1, N even + [0,0,1,1,1]
extreme_half2
array with exactly floor(N/2) values 1, N odd + [0,0,1,1,1]

got 1, but element is not a dominator, value 0 has only 2 occurences (n=5)
ot 1, but element is not a dominator, value 0 has only 2 occurences (n=5)
'''
from collections import Counter
def solution(A):
    n = len(A)
    cnt = Counter(A)
    half = n // 2
    for i, (d, v) in enumerate(cnt.items()):
        if v > half:
            return i
    else:
        return -1