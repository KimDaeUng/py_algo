# https://algospot.com/judge/problem/read/PICNIC
from collections import defaultdict
import sys
def solution(N, M, M_list):
    # 짝에 대한 해시테이블 X 안돼겠네
    # mate_dict = defaultdict(set)
    # length = len(M_list)
    # for i in range(0, length, 2):
    #     mate_dict[M_list[i]].add(M_list[i+1])
    #     mate_dict[M_list[i+1]].add(M_list[i])
    # print(mate_dict)
    
    # 1. 전체 짝 조합의 수 : n C 2 = K, 
    # 2. 한 방법 내 짝의 수 : N / 2 = N'
    # 3. 짝 조합으로 만들 수 있는 "방법"의 수 : N'    
    
    # 친구쌍을 set으로 변환 
    m_list = []
    for i in range(0, length, 2):
        m_list.append(set(M_list[i], M_list[i+1])) 
    
    # 1. m_list에서 순차적으로 쌍 탐색
    stack = []
    l = 0

    while 
        while l == N/2:
            mate = m_list.pop()
            stack.append(mate)
            left_list = [i for i in m_list if (mate[0] not in i)&(mate[1] not in i)]
            if len(left_list) < N/2:
                m_list.append(mate)
                continue
            else:
                m_list = left_list
                l += 1




    # 모든 경우에 대해서 탐색?
    for i 



C = int(sys.stdin.readline())

for i in range(C):
    N, M = map(int, sys.stdin.readline().split())
    M_list = tuple(map(int, sys.stdin.readline().split()))                           
    
    solution(N, M, M_list) 
    # solution_1(N, L, cost)  # 시간초과
    # solution_2(N, L, cost)  # 시간초과