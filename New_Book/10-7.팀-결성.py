# https://www.acmicpc.net/problem/1717
string = '''7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution : Union-Find Data Structure
import sys
input = sys.stdin.readlines
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def weighted_union_parent(parent, size_list, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    # 더 작은 트리가 더 큰 트리의 아래로 가야 트리가 세로로 길어지는 것이 방지됨
    if size_list[x] > size_list[y]:
        parent[y] = x
        size_list[x] += size_list[y]
    else:
        parent[x] = y
        size_list[y] += size_list[x]
    
n, m = map(int, input().split())
parent = list(range(n + 1))
size_list = [1] * (n + 1)
for _ in range(m):
    ctl, a, b = map(int, input().split())
    if ctl == 0:
        weighted_union_parent(parent, size_list, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')