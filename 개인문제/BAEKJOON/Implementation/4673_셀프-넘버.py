# https://www.acmicpc.net/problem/4673
# 13:00-13:33
# My Solution
'''
셀프넘버 : 생성자가 없어서 d(n)으로 만들어지지 않는 수
10000까지의 카운터를 만들고, d(n)으로 만들어지는 수를 지워나감
남은 번호들이 셀프넘버
'''

def d(n):
    n = str(n)
    return int(n) + sum(map(int, n))

counter = [False] * 10001

for idx in range(1, 10001):
    if counter[idx] == True:
        continue
    while True:
        idx = d(idx)
        if idx >= 10001:
            break
        if counter[idx] == False:
            counter[idx] = True

for i in range(1, 10001):
    if counter[i] == False:
        print(i)

# Solution 1
# https://velog.io/@sch804/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-4673%EB%B2%88-%EC%85%80%ED%94%84%EB%84%98%EB%B2%84
# 원래 솔루션은 리스트의 각 위치에 값을 저장하는 방식이었으나
# 실행 시간 때문에 set으로 변경
def d(n):
    return n + sum(map(int, str(n)))

self_num_set = set()
# self_num_set에 i의 d(i)를 추가
for i in range(1, 10001):
    self_num_set.add(d(i))

for i in range(1, 10001):
    if i not in self_num_set:
        print(i)