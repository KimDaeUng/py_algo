# https://www.acmicpc.net/problem/1715

# 16:23-17:26
# 피보나치수열처럼 더하면 틀림
# 매번 가장 작은 두 값을 뽑아 더해야한다.
# 다음과 같은 케이스에서 피보나치수열은 최적해가 아님
'''
5
10
10
10
10
10
'''
# 피보나치수열 방식(X): 20 + (20 + 10) + (30 + 10) + (40 + 10) = 20 + 30 + 40 + 50 = 140
# 우선순위큐 방식(O): (10 + 10) + | (10 + 10) + | (20 + 10) + |(30 + 20) = 20 + 20 + 30 + 50 = 120

import heapq

N = int(input())
data = []
for i in range(N):
    heapq.heappush(data, int(input()))

def solution(data):
    if N == 1:
        return 0

    if N == 2:
        return sum(data) 
    
    count = 0
    while data:
        # 원소가 하나만 남으면 더이상 비교하지 않으므로 종료
        if len(data) < 2:
            break

        a = heapq.heappop(data)
        b = heapq.heappop(data)
        count += a + b
        heapq.heappush(data, a + b)
    
    return count
        
print(solution(data))

# Solution 코드 생략(정답과 동일)