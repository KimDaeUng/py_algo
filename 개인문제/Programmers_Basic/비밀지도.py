# https://programmers.co.kr/learn/courses/30/lessons/17681

# My Solution
# 16:45-17:00
def solution(n, arr1, arr2):
    return list(map(lambda x, y: bin(x|y)[2:].zfill(n)\
                    .replace('1', '#')\
                    .replace('0', ' '), arr1, arr2))