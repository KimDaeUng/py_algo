# https://www.acmicpc.net/problem/1197
# 16:35-16:39
string = '''3 3
1 2 1
2 3 2
1 3 3'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

import sys
input = sys.stdin.readline
v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

def fp(p, x):
    if p[x] != x:
        p[x] = fp(p, p[x])
    return p[x]

def up(p, a, b):
    a = fp(p, a)
    b = fp(p, b)
    if a > b:
        p[a] = b
    else:
        p[b] = a

edges = []
for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    edges.append((c, b, a))

edges.sort()
ans = 0
for edge in edges:
    c, a, b = edge
    if fp(parent, a) != fp(parent, b):
        up(parent, a, b)
        ans += c
print(ans)