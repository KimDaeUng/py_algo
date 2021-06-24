# https://www.acmicpc.net/problem/1157
from collections import Counter
s = input().upper()
if len(s) < 2:
    print(s)
    exit()

s_cnt = Counter(s)
s_cnt = sorted(s_cnt.items(), key = lambda x : -x[1])
is_duplicated = False

if s_cnt[0][1] == s_cnt[1][1]:
    print('?')
else:
    print(s_cnt[0][0])