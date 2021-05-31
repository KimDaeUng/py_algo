# https://www.acmicpc.net/problem/2693
# 02:20-02:22
string = '''4
1 2 3 4 5 6 7 8 9 1000
338 304 619 95 343 496 489 116 98 127
931 240 986 894 826 640 965 833 136 138
940 955 364 188 133 254 501 122 768 408'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)


tc = int(input())

for i in range(tc):
    arr = list(map(int, input().split()))
    arr.sort();print(arr[-3])