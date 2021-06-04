# https://www.acmicpc.net/problemBaseException0
# 18:55-22:22

string = '''2 7
2 3 2 3 1 2 7'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 2 : Retry
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

mtap = []
cnt = 0
for i in range(len(arr)):
    if arr[i] in mtap:
        continue
    if len(mtap) < n:
        mtap.append(arr[i])
        continue
    # 멀티탭이 다 차있는 경우
    elif len(mtap) == n:
        # 멀티탭 내부에 있는 것 중 우선적으로 제거할 것은
        # 이후에 더이상 등장하지 않거나 이후에 가장 늦게 사용하는 것을 뺀다.
        item_max_idx = 0
        mtap_max_idx = 0
        is_exist = True
        for idx, e in enumerate(mtap):
            if e in arr[i:]:
                tmp_idx = arr[i:].index(e)
            else:
                tmp_idx = 101
                is_exist = False
            
            if item_max_idx < tmp_idx:
                item_max_idx = tmp_idx
                mtap_max_idx = idx
            
            if not is_exist:
                break

        del mtap[mtap_max_idx]
        mtap.append(arr[i])
        cnt += 1

print(cnt)

# My Solution 1 : fail
# 등장횟수와 마지막 인덱스를 모두 고려하려함
# 마지막 인덱스만 쓰는 방법도 시도 했으나,
# 더이상 등장하지 않는 경우를 고려 못함
# import sys
# # input = sys.stdin.readline
# from collections import Counter

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# count = [0] * (n + 1)
# uq = tuple(set(arr))

# # [ 0, 1, 2, 3, 4 ] 
# # [ 4, 3, 2, 1, 0 ]  5 - IDX - 1

# last_idx = {}
# for i in uq:
#     idx = arr[::-1].index(i)
#     if idx != -1:
#         idx = len(arr) - idx - 1
#         last_idx[i] = idx


# # 등장 횟수, 마지막 인덱스
# arr_cnt = Counter(arr)
# arr_cnt = {k : (v, last_idx[k]) for k, v in arr_cnt.items()}
# arr_cnt = sorted(arr_cnt.items(), key=lambda x: (-x[1][0]))
# mtap = [ i[0] for i in arr_cnt ][:n]

# print(mtap)
# cnt = 0
# for i in range(len(arr)):
#     print(i, '---------')
#     if arr[i] in mtap:
#         continue
#     else:
#         mtap.pop()
#         cnt += 1
#         mtap.append(arr[i])
#         print(mtap)

# print(cnt)

# Solution
# https://jokerldg.github.io/algorithm/2021/03/21/multitap.html
n, k = map(int, input().split())
multitap = list(map(int, input().split()))

plugs = [] 
count = 0

for i in range(k):
    if multitap[i] in plugs:
        continue
    # 플러그가 1개라도 비어있으면 집어넣는다.
    if len(plugs) < n:
        plugs.append(multitap[i])
        continue
    
    multitap_idxs = [] # 다음 멀티탭의 값을 저장
    hsaplug = True
    
    for j in range(n):
        # 멀티탭 안에 플러그값이 있다면
        if plugs[j] in multitap[i:]:
            # 멀티탭 인덱스 위치값 가져오기
            multitap_idx = multitap[i:].index(plugs[j])
        else:
            multitap_idx = 101
            hasplug = False
        
        # 인덱스에 값을 넣어준다.
        multitap_idxs.append(multitap_idx)
        
        # 없다면 종료
        if not hasplug:
            break
