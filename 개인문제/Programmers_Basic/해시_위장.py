# https://programmers.co.kr/learn/courses/30/lessons/42578
# 01:20-01:50


def solution(clothes):
    hash_map = {}
    for v, k in clothes:
        if k in hash_map:
            hash_map[k] += 1
        else:
            hash_map[k] = 1
    total = 1
    for k, v in hash_map.items():
        total *= v + 1
    return total - 1