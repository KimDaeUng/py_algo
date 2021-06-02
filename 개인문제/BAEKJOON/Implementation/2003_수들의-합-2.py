# https://www.acmicpc.net/problem/2003
# 12:12-12:30
'''
투 포인터
- 합이 M보다 작으면 오른쪽 인덱스 +
- 합이 M보다 크면 왼쪽 인덱스 + 
- 합이 M이면 카운트 후 왼쪽 인덱스 +
'''

string = '''10 5
1 2 3 4 2 5 3 1 1 2'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 1 : 단순 while문과 sum 내장함수 이용
# 시간복잡도 O(N^2)이 됨
n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 0
cnt = 0

while e <= n:
    sum_ = sum(arr[s:e])
    if sum_ == m:
        cnt += 1
        s += 1
    elif sum_ < m:
        e += 1
    elif sum_ > m:
        s += 1

print(cnt)

# My Solution 2:
# 구간합을 유지하면서 시작과 끝 업데이트만 반영
# 시간 복잡도 O(N)
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
interval_sum = 0
cnt = 0

while start < n:
    if interval_sum >= m:
        if interval_sum == m:cnt += 1
        interval_sum -= arr[start]
        start += 1
    elif interval_sum < m:
        if end < n:
            interval_sum += arr[end]
            end += 1
        else:
            start += 1

print(cnt)

# Solution
n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
interval_sum = 0 
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += arr[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        cnt += 1
    interval_sum -= arr[start]

print(cnt)