# https://programmers.co.kr/learn/courses/30/lessons/12915
# My Solution
# 15:11-15:12
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))