# https://www.acmicpc.net/problem/1920
# 22:17-00:25
# 어이없는 실수, Sort를 안해서 계속 틀렸다.

string = '''5
4 1 5 2 3
5
1 3 7 9 5'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution
n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

def bs(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = (L + R) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            R = mid - 1
        else:
            L = mid + 1
    return 0

arr_n.sort()
for i in arr_m:
    print(bs(arr_n, i))