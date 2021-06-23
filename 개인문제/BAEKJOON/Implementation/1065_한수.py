# https://www.acmicpc.net/problem/1065
# 13:45-13:52
# My Solution
n = int(input())

def han_num(x):
    if x <= 9:
        return True
    
    x = tuple(map(int, str(x)))
    diff = x[1] - x[0]

    for i in range(2, len(x)):
        if x[i] - x[i - 1] != diff:
            return False
    
    return True

cnt = 0
for i in range(1, n + 1):
    if han_num(i):
        cnt += 1

print(cnt)