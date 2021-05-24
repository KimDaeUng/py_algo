# https://www.acmicpc.net/problem/1654
# 01:20-02:30

string = '''4 4
802
743
457
539'''

# string = '''1 1
# 1000'''

# string = '''4 4
# 10000
# 10000
# 10000
# 10000
# '''


def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution
k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input())) 

# if k == n and sum(arr) == (arr[0] * len(arr)):
#     print(min(arr))
#     exit()

L = 1       # 나누는 수의 범위를 찾기 떄문에 1 부터 
R = max(arr)

max_length = 0
while L <= R:
    mid = (L + R) // 2
    count = sum([ x // mid for x in arr])
    # print(L, R, mid, count)
    # 개수가 n보다 작다면
    # 더 잘게 쪼개기 위해 mid를 줄여야함
    if n > count:
        R = mid - 1
    elif n < count:
        L = mid + 1
        max_length = mid
    # 만약 max_length를 위처럼 안하고 아래처럼 별도로 하면
    # 오답 판정
    # n < count 인 경우에 최대길이가 생길 수 있기 때문
    # else:
    #     L = mid + 1
        # max_length = mid 

print(max_length)