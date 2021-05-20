# https://www.acmicpc.net/problem/13555
# https://www.acmicpc.net/problem/17409 # New ver.
# 13:12-14:28
string = '''4 3
1 2 2 10'''

# string = '''5 3
# 1 2 3 5 4'''
# string = '''2 1
# 1 2'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 2 : Fenwick Tree 이용
'''
# Solution 참고함
https://www.geeksforgeeks.org/count-number-increasing-subsequences-size-k/
https://lastknight00.tistory.com/11

@ 접근법
- Dynamic Programming, 2D array dp를 만들어 
  array의 j번째 값 arr[j]로 끝나는 길이가 i인 배열의 개수를
  dp[i][j]에 저장한다.
- 점화식
  dp[i][j] = 1, where i = 1 and 1 <= j <= n
  dp[i][j] = sum(dp[i-1][j]),
  where 1 < i <= k, i <= j <= n and 
        arr[m] < arr[j] for (i - 1) <= m < j
'''
# Solution 2 : BIT를 이용한 방법
import sys
# input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (100000 + 2) for _ in range(50 + 1)]

def q(p, k):
    s = 0
    while p:
        s = (s + dp[k][p]) % 5000000
        p -= (p & -p)
    return s

def u(p, k, v):
    while p <= n + 1:
        dp[k][p] = (dp[k][p] + v) % 5000000
        p += (p & -p)

u(1, 0, 1)
for i in arr:
    for j in range(1, m + 1):
        u(i + 1, j, q(i, j - 1))

print(int(q(n + 1, m)))
exit()
# Solution 1 : only for-loop : 
# https://www.geeksforgeeks.org/count-number-increasing-subsequences-size-k/
def n_of_incsuqseq_sizek(arr, n, k):
    arr = [0] + arr
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 길이가 1이고 arr[j]로 끝나는 증가하는 부분 수열의 개수
    for j in range(n + 1):
        dp[1][j] = 1

    # matrix dp[][]를 만든다.
    # 여기서 'l'은 증가하는 부분 수열의 길이를 의미
    for l in range(2, k + 1): # 위에서 길이 1인 경우를 처리 했으므로 2부터 시작
        # 길이 'l'이고 arr[j]로 끝나는 증가하는 부분 수열 각각에 대해
        for j in range(l, n + 1):
            # 증가하는 부분 수열의 개수를 센다
            dp[l][j] = 0
            # 길이가 1인 경우까지 포함해 세기 때문에 l - 1 부터 시작
            # arr[j] 이전의 모든 값 arr[i] (where 1 <= i <= j)에 대해서
            # arr[i] < arr[j] (증가하는 경우에 해당하면)
            # 길이가 l - 1이고 arr[i]로 끝나는 수열의 개수를
            # 길이가 l이고 arr[j]로 끝나는 수열의 개수에 더함
            # 길이가 l인 arr[j]로 끝나는 부분 수열의 개수
            # = 길이가 l-1인 arr[m] ((l - 1) <= m <= j)로 끝나는 부분 수열의 개수의 총합
            for i in range(l - 1, j + 1):
                if arr[i] < arr[j]:
                    dp[l][j] += dp[l - 1][i]
    
    # size k인 증가하는 부분 수열의 개수를 모두 더함
    sum_ = 0
    for i in range(k, n + 1):
        sum_ += dp[k][i]
    
    return sum_

# Driver Code
# arr = [12, 8, 11, 13, 10,
#           15, 14, 16, 20 ]
# n = len(arr)
# k = 4
 
print("Number of Increasing Subsequences of size",
         m, "=", n_of_incsuqseq_sizek(arr, n, m))
 


exit()
    


# # My Solution 1 : Failed
# count = 1
# if k == 1 and n == 1:
#     print(1)
#     exit()
# if k == 1:
#     for i in range(1, n):
#         if arr[i - 1] <= arr[i]:
#             count += 1
#     print(count)
#     exit()
# if n == k:
#     for i in range(1, n):
#         if arr[i - 1] > arr[i]:
#             count = 0
#             print(count)
#             exit()
#     print(count)
#     exit()

# is_gain = True
# len_cum = 1
# count = 0
# for i in range(1, n - 1):
#     if arr[i-1] > arr[i]:
#         is_gain = False
#         len_cum = 1
#         continue
#     len_cum += 1

#     # if is_gain:
#     #     count += 1
#     #     continue

#     if len_cum % k == 0:
#         if is_gain:
#             count += 1
#             continue
#         count += 1
#         is_gain = True
#         len_cum -= 1
#         continue
#     else:
#         len_cum %= k
#         continue
    
# print(count)




# My Solution 1 : Failed
# count = 1

# if k == 1 and n == 1:
#     print(1)
#     exit()
# if k == 1:
#     # for i in range(1, n):
#     #     if arr[i - 1] <= arr[i]:
#     #         count += 1
#     print(0)
#     exit()
# if n == k:
#     for i in range(1, n):
#         if arr[i - 1] > arr[i]:
#             count = 0
#             print(count)
#             exit()
#     print(count)
#     exit()

# for i in range(1, k):
#     if arr[i - 1] > arr[i]:
#         count = 0

# tmp = arr[:k]
# if count:
#     for i in range(k, n):
#         if tmp[-1] <= arr[i]:
#             count += 1
#             tmp = tmp[1:] + [arr[i]]

# else:
#     k = 3
#     0 5 4 3 2 1 2 3
#     init_idx = k
#     while init_idx < n and arr[init_idx - 1] > arr[init_idx]:
#         init_idx += 1
#     if init_idx < n:
#         # 증가하는 부분 수열이 되는 인덱스 범위 찾기
#         init_idx_end = init_idx + 1
#         while init_idx_end + k < n and \
#               init_idx_end < init_idx_end + k and\
#               arr[init_idx_end - 1] <= arr[init_idx_end]:
#             init_idx_end += 1
#     else:


#     for i in range(k, n):
#         if tmp[-1] <= arr[i]:
#             count += 1
#             tmp = tmp[1:] + [arr[i]]

#     print(count % 5000000)
