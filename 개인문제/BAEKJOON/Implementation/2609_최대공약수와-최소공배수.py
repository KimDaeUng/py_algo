# https://www.acmicpc.net/problem/2609
# 01:47-02:18
from math import sqrt
a, b = map(int,input().split())

def div_find(x):
    if x <= 3:
        return [x]
    arr = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            arr.append(i)
            arr.append(x // i)
    return arr

div_a = set(div_find(a))
div_b = set(div_find(b))

GCD_set = sorted(list(div_a & div_b))
if len(GCD_set) == 0:
    GCD = 1
    LCM = a * b
else:
    GCD = GCD_set[-1]
    LCM = a * b // GCD

print(GCD)
print(LCM)
