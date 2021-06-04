# https://www.acmicpc.net/problem/2042
# 12:36- 13:08
string = '''5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] * (n + 1)
tree = [0] * (n + 1)

def prefix_sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s

def update(i, dif):
    while i < n + 1:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    arr[i] = int(input())
    update(i, arr[i])

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    elif a == 2:
        print(interval_sum(b, c))