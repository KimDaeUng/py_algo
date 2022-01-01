# https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/
# 10m
# My Solution
# https://app.codility.com/demo/results/training9HAFMM-64X/
def solution(A):
    return len(set(map(abs, A)))