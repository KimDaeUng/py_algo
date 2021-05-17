# 14:14-

string = '''7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)
    
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    else:
        return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

print(parent)
edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    # union_parent(parent, a, b)


edges.sort()

def check(edges):
    result = 0
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    for a in range(2, n + 1):
        find_parent(parent, a)
    return result

answer = int(1e9)
aaa = []
for idx in range(m):
    edge = edges.pop(idx)
    result = check(edges)
    aaa.append(result)
    answer = min(answer, result)
    edges.insert(idx, edge)

print(aaa)

# for edge in edges:
#     cost, a, b = edge
#     if a == 2 or b == 2 or a == 4 or b == 4:
#         print(edge)