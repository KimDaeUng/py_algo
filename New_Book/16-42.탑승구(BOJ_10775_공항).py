# https://www.acmicpc.net/problem/10775

# 21:05-22:03 : 해결 못함.

string = '''4
3
4
1
1'''

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


# My Solution 2 : Retry
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

# 탑승구의 개수 입력받기
g = int(input())
# 비행기의 개수 입력받기
p = int(input())
parent = [0] * (g + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

count = 0
for _ in range(p):
    f = int(input())
    cur_root = find_parent(parent, f)
    if cur_root == 0:
        break
    union_parent(parent, cur_root, cur_root - 1)
    count += 1

print(count)


# My Solution 1 : Fail (Timeout)
import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
gates = { i : 0 for i in range(g+ 1) }

count = 0
for _ in range(p):
    f = int(input())
    fill = False
    for i in range(f, 0, -1):
        if gates[f] == 0:
            gates[f] = 1
            fill = True
            count += 1
    
    if i == 0 and not fill:
        print(count)
        exit()

print(count)



    

# Solution
'''
Union-find 자료구조를 포인터처럼 활용
1. 각 게이트를 노드로 취급하여 0번 게이트를 포함하는 g + 1 크기의 parent table을 만든다.
2. i번 게이트에 비행기가 도킹함 -> i번 게이트와 i - 1번 게이트를 union 연산
   -> i번 게이트의 루트 노드가 i - 1이 됨
3. 새로운 비행기를 가장 큰 번호의 게이트인 자기 번호부터 넣을때,
   find_parent 연산을 수행하게 되면 이미 도킹된 위치에 도착할 경우 이것의 root 노드는 
   남은 것들 중에서 비어있는 가장 큰 인덱스가 된다.
   이것과 이것의 바로 옆에 있는 것을 다시 union 연산
4. 모든 비행기에 대해 2, 4를 반복하다가 root가 0이 될 때 더이상 넣을 것이 없으므로 종료한다.
'''
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
# 탑승구의 개수 입력받기
g = int(input())
# 비행기의 개수 입력받기
p = int(input())
parent = [0] * (g + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = 1

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구의 루트 확인
    if data == 0: # 현재 루트가 0이라면, 종료
        break
    union_parent(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1
print(result)