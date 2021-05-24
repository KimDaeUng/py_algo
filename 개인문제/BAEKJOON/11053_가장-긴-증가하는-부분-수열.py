# https://www.acmicpc.net/problem/11053
# https://www.acmicpc.net/problem/12015 # 2
# https://www.acmicpc.net/problem/12738 # 3
# 18:30-18:40

string = '''6
10 20 10 30 20 50'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 1 : DP : O(N^2)
# dp[i] : arr[i]로 끝나는 가장 긴 증가 부분 수열의 개수
# dp[i] = max(dp[i], dp[j] + 1) where 0 <= j < i
# 
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# Solution 1 : Binary Search
# https://sihyungyou.github.io/baekjoon-12015/

# 1.1 Using bisect_left
import bisect
n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
result = 1
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        result += 1
    else:
        # 정렬 순서를 유지하면서 dp에 arr[i]를 삽입할 가장 왼쪽 인덱스
        # 최종적으로 DP에는 각 위치에 있을 최소값이 저장됨
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(result)

# 1.2 No module
n = int(input())
arr = list(map(int, input().split()))

# LIS를 만들어 둔 뒤, Binary Search로 삽입 위치를 지정
# 삽입될 index에 기존 값이 있다면 n은 그 값보다 작거나 같기 때문에 갱신하고,
# 삽입될 index가 LIS 길이와 같다면, 즉 LIS 최대값(마지막 원소)보다 n이 크다면 
lis = arr[:1]
for n in arr[1:]:
    # 현재 위치 n에 대하여
    low, high = 0, len(lis)
    while low < high:
        mid = (low + high) // 2
        if lis[mid] < n:
            low = mid + 1
        else:
            high = mid
    if low == len(lis):
        lis.append(n)
    else:
        lis[low] = n

len(lis)

# Solution 2 : Binary Indexed Tree(BIT)