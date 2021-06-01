# https://www.acmicpc.net/problem/14888
# 12:30-13:09
# My Solution 1 : Permutations를 이용한 풀이
'''
모든 경우를 탐색해야
연산자의 개수로 나열가능한 모든 순열을 구하고
모든 경우를 계산한다
시간 초과에 아슬아슬하게 걸림
'''

# string = '''2
# 5 6
# 0 0 1 0'''

string = '''3
3 4 5
1 0 1 0'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)


from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
ops_arr = list(map(int, input().split()))

comb = ''

for i, nop in enumerate(ops_arr):
    if i == 0: comb += '+' * nop
    if i == 1: comb += '-' * nop
    if i == 2: comb += '*' * nop
    if i == 3: comb += '/' * nop

comb = permutations(list(comb))
ops = {'+' : lambda x, y : x + y,
       '-' : lambda x, y : x - y,
       '*' : lambda x, y : x * y,
       '/' : lambda x, y : x // y \
           if x >= 0 else -(-x // y)}

def cal(ops_comb, arr):
    result = arr[0]
    for op, d in zip(ops_comb, arr[1:]):
        result = ops[op](result, d)
    return result

min_value = int(1e9)
max_value = int(-1e9)

for ops_comb in comb:
    result = cal(ops_comb, arr)
    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)

# My Solution 2 : DFS
# 재귀탐색 뼈대 코드로 기억해둘 것
n = int(input())
data = list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())

min_v = int(1e9)
max_v = -int(1e9)

def dfs(i, now):
    global add, sub, mul, div, min_v, max_v
    if i == n:
        min_v = min(min_v, now)
        max_v = max(max_v, now)
    else:
        if add > 0: add -= 1; dfs(i + 1, now + data[i]);add += 1
        if sub > 0: sub -= 1; dfs(i + 1, now - data[i]);sub += 1
        if mul > 0: mul -= 1; dfs(i + 1, now * data[i]);mul += 1
        if div > 0: div -= 1; dfs(i + 1, now // data[i] if now >=0 else -(-now // data[i]));div += 1
dfs(1, data[0])
print(max_v)
print(min_v)

# My Soultion 3 : BFS
from collections import deque
n = int(input())
data = list(map(int,input().split()))
ops_counter = list(map(int, input().split()))

min_v = int(1e9)
max_v = -int(1e9)

q = deque([])
q.append((data[0], ops_counter, 0))
while q:
    now, ops_cnt, i = q.popleft()
    if i == n - 1:
        min_v = min(min_v, now)
        max_v = max(max_v, now)
        continue
    i += 1
    if ops_cnt[0] > 0:
        ops_cnt_c = ops_cnt[:]
        ops_cnt_c[0] -= 1
        q.append((now + data[i], ops_cnt_c, i))
    if ops_cnt[1] > 0:
        ops_cnt_c = ops_cnt[:]
        ops_cnt_c[1] -= 1
        q.append((now - data[i], ops_cnt_c, i ))
    if ops_cnt[2] > 0:
        ops_cnt_c = ops_cnt[:]
        ops_cnt_c[2] -= 1
        q.append((now * data[i], ops_cnt_c, i))
    if ops_cnt[3] > 0:
        ops_cnt_c = ops_cnt[:]
        ops_cnt_c[3] -= 1
        q.append((int(now / data[i]), ops_cnt_c, i))

print(max_v)
print(min_v)


# Solution : DFS
n = int(input())
data = list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 어데이트
    if i == n - 1:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i + 1])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i + 1])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i + 1])
            mul += 1
        if div > 0:
            div -= 1
            if now >= 0:
                dfs(i + 1, now // data[i + 1])
            else:
                dfs(i + 1, - (- now // data[i + 1]))
            div += 1

dfs(0, data[0])
print(max_value)
print(min_value)