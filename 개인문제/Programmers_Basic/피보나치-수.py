# https://programmers.co.kr/learn/courses/30/lessons/12945

# My Solution 3: Iterative
def solution(n):
    f1, f2 = 0, 1
    # f(n) = f(n - 1) + f(n - 2)
    for _ in range(2, n + 1):
        # new_f1 <- f2
        # new_f2 <- f1 + new_f1
        f1, f2 = f2, f2 + f1
    return f2 % 1234567

# My Solution 2: Recursive
import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    def rec(n):
        if n <= 1:
            return n

        if dp[n] != 0:
            return dp[n]
        else:
            dp[n] = (rec(n - 1) + rec(n - 2)) % 1234567
            return dp[n]

    return rec(n)


# My Solution 1: Timeout
# Recursive way
import sys
sys.setrecursionlimit(10 ** 6)
def solution(n):
    if n <= 1:
        return n
    return (solution(n - 1) + solution(n - 2)) % 1234567