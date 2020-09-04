import os, sys

def solution_1(N, L, cost):
    min_cost = sys.maxsize
    for s in range(N):
        for e in range(L, N+1): # L일 이상의 모든 경우 탐색
            if s+e > N : continue
            # print("-"*50)
            # print("StartIdx : {} / L : {} day :".format(s, e))
            # print(cost[s:s+e])

            cur_cost = sum(cost[s:s+e]) / len(cost[s:s+e])
            
            if cur_cost < min_cost:
                min_cost = cur_cost
    print(min_cost)
    return None

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
    while s_idx != (N-1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        (cost)):
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

def solution_3(N, L, cost):
    min_cost = sys.maxsize
    # 또다른 방법
    # 시작인덱스와 끝 인덱스 각각을 두고, 1개씩 붙여나온 평균이
    # 붙이기 전 평균보다 낮아지면 계속 추가
    # 낮아지지 않으면 값 저장 후 시작 인덱스 1 추가해 다시 하나씩 늘려가면서 탐색
    
    # 이걸 모든 가능한 시작점 [0, i + l - 1 ?)에 대해서 수행함
    s_idx = 0
    e_idx = L
    
    p = 1
    while s_idx != (N-1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              (cost)):
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

C = int(sys.stdin.readline())

for i in range(C):
    N, L = map(int, sys.stdin.readline().split())
    cost = list(map(int, sys.stdin.readline().split()))                           
    solution_1(N, L, cost) 
    solution_2(N, L, cost)  # 시간초과
    # solution_3(N, L, cost)


exit()


count = 0
while True:
    rl = lambda: sys.stdin.readline()
    line = rl().strip()
    if not line:break
    # if count == 0:
    #     print("count == 0")
        # n_test_case = int(line)
    if (count % 2 == 1)&(count != 0):
        # print("count == 1")
        line = line.split(" ")
        n, l = int(line[0]), int(line[1])
    if (count % 2 == 0)&(count != 0):
        # print("count == 2")
        cost = line.split(" ")
        cost = [int(c) for c in cost]
        # if count == 2:
        #     print("1st Test Case--------------------")
        # if count == 4:
        #     print("2nd Test Case--------------------")
        
        min_cost = sys.maxsize


        # 다른 방법
        # CNN 처럼 stride 하면서 다음 탐색지 목록에 넣고
        # 1개씩 추가로 append한 결과가 큰 것만 추가로 탐색
        # BFS 방식
        
        # 또다른 방법
        # 시작인덱스와 끝 인덱스 각각을 두고, 1개씩 붙여나온 평균이
        # 붙이기 전 평균보다 낮아지면 계속 추가
        # 낮아지지 않으면 값 저장 후 시작 인덱스 1 추가해 다시 하나씩 늘려가면서 탐색

        # 이걸 모든 가능한 시작점 [0, i + l - 1 ?)에 대해서 수행함
        
        
        s_idx = 0
        e_idx = s_idx + l
        
        for i in range(n):
            if e_idx > n : continue
            cur_cost = sum(cost[s_idx:e_idx]) / l
            proced_cost = sum(cost[s_idx:e_idx+1]) / (l+1)
            if cur_cost > proced_cost:
                min_cost = proced_cost
                if e_idx+1 <= n:
                    l += 1
                    e_idx = s_idx + l
            else:
                s_idx += 1
        
        print(cost[s_idx:e_idx])
        print(cur_cost)

            
            


            
        # 무식하게 풀기
        # for e in range(l, n+1): # L일 이상의 모든 경우 탐색
        #     for s in range(n):
        #         if s+e > n : continue
        #         print("-"*50)
        #         print("StartIdx : {} / L : {} day :".format(s, e))
        #         print(cost[s:s+e])
        #         cur_cost = sum(cost[s:s+e]) / e
                

        #         if sum_cost < min_cost:
        #             min_cost = sum_cost
        # print(min_cost)

        # for s in range(n):
        #     for e in range(l, n+1): # L일 이상의 모든 경우 탐색
        #         if s+e > n : continue
        #         print("-"*50)
        #         print("StartIdx : {} / L : {} day :".format(s, e))
        #         print(cost[s:s+e])

        #         sum_cost = sum(cost[s:s+e])
                
        #         if sum_cost < min_cost:
        #             min_cost = sum_cost
        # print(min_cost)
    
    count +=1

