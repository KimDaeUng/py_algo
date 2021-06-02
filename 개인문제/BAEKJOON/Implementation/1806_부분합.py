# https://www.acmicpc.net/problem/1806
# 12:30-13:35
string = '''10 15
5 1 3 5 10 7 4 9 2 8'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 3 : Prefix Sum : retry
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cum = [0] * (n + 1)

for i in range(1, n + 1):
    # arr의 인덱스 i - 1 == cum의 인덱스 i
    cum[i] = cum[i - 1] + arr[i - 1]

start, end = 0, 0
answer = 100001
# 시작점을 조건으로 하지 않으면 end가 n에 도달한 후
# start를 n - 1까지 줄여나가는 경우를 체크할 수 없음
while start < n:
    if cum[end] - cum[start] >= s:
        answer = min(answer, end - start)
        start += 1
    else:
        if end < n:
            end += 1
        else:
            start += 1
if answer == 100001:
    answer = 0
print(answer)

# My solution 2 : Prefix Sum
# 미리 누적합을 구해둔 테이블을 이용해 구간합을 빠르게 구하는 방식

import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))
# 범위가 아닌 원소 하나만으로 합이 가능한 경우
if s in arr:
    print(1)
    exit()

# dp[i] : i번째 원소까지의 누적합
dp = [0] * (n + 1)
i = 1
while i < n + 1:
    dp[i] = arr[i] + dp[i - 1]
    i += 1

def interval(l, r):
    if l > 1:
        return dp[r] - dp[l - 1]
    else:
        return dp[r]
l = 1
r = 1
length = 100001
while r < n + 1:
    sum_ = interval(l, r)
    if sum_ >= s:
        cur_len = r - l + 1
        if length > cur_len:
            length = cur_len
        l += 1
    elif sum_ < s:
        r += 1

if length != 100001:
    print(length)
else:
    print(0)

# # My solution 1 : two pointers
# # 시간초과
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = 0
length = 100001
while r < n:
    sum_ = sum(arr[l:r])
    if sum_ >= s:
        cur_len = r - l + 1
        if length > cur_len:
            length = cur_len
        l += 1
    elif sum_ < s:
        r += 1

if length != 100001:
    print(length)
else:
    print(0)

# Solution 1 : 투 포인터
# 위의 내 풀이는 합 계산시 매번 O(N)의 시간복잡도
# 새롭게 추가되거나 빼는 값에 대해서만 총합에서 처리함
n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end, cur = 0, 0, 0
answer = 100001

while True:
    if cur >= s:
        answer = min(answer, end - start)
        cur -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        cur += arr[end]
        end += 1

if answer == 100001:
    answer = 0

print(answer)

# # Solution 2 : 부분합
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix = [0] * (n + 1)
start, end = 0, 0

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

answer = 100001

while start < n:
    if prefix[end] - prefix[start] >= s:
        answer = min(answer, end - start)
        start += 1
    else:
        if end < n:
            end += 1
        else:
            start += 1

if answer == 100001:
    answer = 0
print(answer)