# https://www.acmicpc.net/problem/1976
# 12:17-
# My Solution
'''
확인해야할 도시들이 하나의 그래프 안에 포함이 되어 있는지 파악한다.
Union-Find 자료구조 이용해 parent 테이블을 갱신, 이때 경로압축을 사용하고
parent 테이블에서 여행계획에 해당하는 노드들이 동일한 루트노드인지 확인
'''
string = '''3
3
0 1 0
1 0 1
0 1 0
1 2 3'''
string = '''5
4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

def fp(parent, x):
    if parent[x] != x:
        parent[x] = fp(parent, parent[x])
    return parent[x]
def up(parent, a, b):
    a = fp(parent, a)
    b = fp(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = list(range(n + 1))
for i in range(1, n + 1):
    tmp_list = list(map(int, input().split()))
    for j in range(i, n + 1):
        if tmp_list[j - 1]: # fixed index number 
            up(parent, i, j)

for i in range(1, n + 1):
    fp(parent, i)
# print(parent)
plan = list(map(int, input().split()))

for i in range(1, m):
    if fp(parent, plan[i - 1]) != fp(parent, plan[i]):
        print("NO")
        exit()
print('YES')

# Solution
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 여행지 개수와 여행 계획에 속한 여행지의 개수 입력 받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: #연결된 경우 unioin 연산 수행
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력 받기
plan = list(map(int, input().split()))

result = True
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지) 확인
if result:
    print("YES")
else:
    print("NO")