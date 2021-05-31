# https://www.acmicpc.net/problem/1978
# 02:23-02:30
from math import sqrt
n = int(input())
arr = list(map(int, input().split()))

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

result = 0
for i in arr:
    if is_prime(i):
        result += 1
print(result)