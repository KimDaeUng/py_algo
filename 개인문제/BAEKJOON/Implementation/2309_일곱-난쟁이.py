# https://www.acmicpc.net/problem/2309
# 01:20-01:45
string = '''20
7
23
19
10
15
25
8
13'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

from itertools import combinations
sum_ = 0
arr = []
for i in range(9):
    arr.append(int(input()))

comb = list(combinations(arr, 7))

for case in comb:
    if sum(case) == 100:
        break

case = list(case)
case.sort()

for i in case:
    print(i)