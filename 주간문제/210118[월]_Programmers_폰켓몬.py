# https://programmers.co.kr/learn/courses/30/lessons/1845
from collections import Counter
def solution(nums):
    hash_table = Counter(nums)
    half_N = len(nums)/2
    type_N = len((hash_table).keys())
    if type_N > half_N:
        return half_N
    else:
        return type_N