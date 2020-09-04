import os, sys

# 시간 초과
def solution_1(N, L, cost):
    print(min(
	  [sum(cost[s:s+e])/len(cost[s:s+e])
	   for e in range(L, N+1)
	   for s in range(N)
	   if s+e <= N]))
    return None

# 시간 초과
def solution_2(N, L, cost):
    min_cost = sys.maxsize
    # 또다른 방법
    # 시작인덱스와 끝 인덱스 각각을 두고, 1개씩 붙여나온 평균이
    # 붙이기 전 평균보다 낮아지면 계속 추가
    # 낮아지지 않으면 값 저장 후 시작 인덱스 1 추가해 다시 하나씩 늘려가면서 탐색
    
    # 이걸 모든 가능한 시작점 [0, i + l - 1 ?)에 대해서 수행함
    s_idx = 0
    e_idx = L
    
    p = 1
    while s_idx < (N-L+1):
        print("s_idx : ", s_idx)
        if s_idx + e_idx + p > N : break
    
        cur_cost = sum(cost[s_idx:s_idx+e_idx]) / L
        proced_cost = sum(cost[s_idx:s_idx+e_idx+p]) / (L+p)
        
        # 하루 추가시 비용이, 현재까지의 비용보다 낮다면
        # 최저가를 갱신후, 다음 탐색으로 진행 (시작 인덱스 고정하고 하루를 더 붙임)
        print("s_idx : {} / s+e+p : {} ".format(s_idx, s_idx + e_idx + p))
        print("cur_cost {} / proced_cost {} \n".format(cost[s_idx:s_idx+e_idx], cost[s_idx:s_idx+e_idx+p]))
        
        if cur_cost > proced_cost: 
            print("cur_cost > proced_cost")
            if min_cost > proced_cost:
                min_cost = proced_cost
            p += 1

            # 다음 탐색
            if s_idx + e_idx + p == N:
                s_idx += 1
                p = 1

        # 하루 추가시 비용이, 현재까지 비용보다 크거나 같다면
        # 시작 인덱스를 이동하고 p를 초기화
        else:
            if min_cost > cur_cost:
                min_cost = cur_cost 
            s_idx += 1
            p = 1

    # print(cost[s_idx:e_idx])
    print(min_cost)
    return None

def solution(N, L, cost):
    min_cost = sys.maxsize
    for s in range(N-L+1):
        length = 1
        cur_cost = 0
        for e in range(s, N):
            # print("-"*50)
            # print("StartIdx : {} / L : {} day :".format(s, e))
            # print(cost[s:e])
            cur_cost += cost[e]
            if length >= L:
                if min_cost > cur_cost / length:
                    min_cost = cur_cost / length
            
            length += 1
    print(min_cost)

C = int(sys.stdin.readline())

for i in range(C):
    N, L = map(int, sys.stdin.readline().split())
    cost = list(map(int, sys.stdin.readline().split()))                           
    
    solution(N, L, cost) 
    # solution_1(N, L, cost)  # 시간초과
    # solution_2(N, L, cost)  # 시간초과