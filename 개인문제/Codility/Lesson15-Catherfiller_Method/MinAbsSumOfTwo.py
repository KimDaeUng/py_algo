# https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/start/

# My Solution
# https://app.codility.com/demo/results/training54DEF3-EXY/
def solution(A):
    A.sort(key=abs)
    min_sum = int(1e9)
    for i in range(1, len(A)):
        min_sum = min(min_sum, abs(A[i - 1] + A[i]))
    return min_sum