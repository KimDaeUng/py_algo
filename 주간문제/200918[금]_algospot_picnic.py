# # https://algospot.com/judge/problem/read/PICNIC
# from collections import defaultdict
import sys
# def solution(N, M, M_list):
#     # 짝에 대한 해시테이블 X 안돼겠네
#     # mate_dict = defaultdict(set)
#     # length = len(M_list)
#     # for i in range(0, length, 2):
#     #     mate_dict[M_list[i]].add(M_list[i+1])
#     #     mate_dict[M_list[i+1]].add(M_list[i])
#     # print(mate_dict)
    
#     # 1. 전체 짝 조합의 수 : n C 2 = K, 
#     # 2. 한 방법 내 짝의 수 : N / 2 = N'
#     # 3. 짝 조합으로 만들 수 있는 "방법"의 수 : N'    
    
#     # 친구쌍을 set으로 변환 
#     m_list = []
#     for i in range(0, length, 2):
#         m_list.append(set(M_list[i], M_list[i+1])) 
    
#     # 1. m_list에서 순차적으로 쌍 탐색
#     stack = []
#     l = 0

#     while 
#         while l == N/2:
#             mate = m_list.pop()
#             stack.append(mate)
#             left_list = [i for i in m_list if (mate[0] not in i)&(mate[1] not in i)]
#             if len(left_list) < N/2:
#                 m_list.append(mate)
#                 continue
#             else:
#                 m_list = left_list
#                 l += 1

#     # 모든 경우에 대해서 탐색?
#     for i 

def matching(finished):
    # 재귀함수의 종료조건
    if all(finished):
        return 1
    
    first_people = finished.index(False)
    count = 0

    for i in range(first_people+1, len(finished)):
        # first_people로 선택된 사람을 기준으로, 탐색이 끝나지 않은 
        # 나머지 모든 사람과 관계를 모두 비교하여 둘이 친구이면
        if not finished[i] and areFriend[first_people][i]:
            finished[i] = True     # 탐색했음 두 명 모두에 체크
            finished[first_people] = True
            # 재귀호출을 통해 first_people에 대한 나머지 인원들에 대하여도 탐색을 진행
            count += matching(finished)
            # 다음 iteration을 돌기위해 초기화
            finished[i] = False
            finished[first_people] = False
    # 탐색이 진행되는 중에 친구로 가능한 짝이 남아있지 않는경우 또는 모든 탐색의 최종 출력으로
    return count


C = int(sys.stdin.readline())

for i in range(C):
    N, M = map(int, sys.stdin.readline().split())
    M_list = list(map(int, sys.stdin.readline().split()))    
    
    m_list = []
    for i in range(0, M*2, 2):
        m_list.append(M_list[i:i+2])
    # print(M_list)
    # print(m_list)
    areFriend = [ [ False for _ in range(N)] for _ in range(N)]
    
    for mate in m_list:
        areFriend[mate[0]][mate[1]] = True 
        areFriend[mate[1]][mate[0]] = True 
    
    finished = [False for _ in range(N)]
    print(matching(finished))


# N = int(input())


# def pairing( finished ) :

#     if all(finished) :
#         return 1

#     first_people = finished.index(False)
#     count = 0

#     for i in range(first_people+1, len(finished)) :

#         if not finished[i] and areFriend[first_people][i] :

#             finished[i] = True
#             finished[first_people] = True
#             count += pairing(finished)
#             finished[i] = False
#             finished[first_people] = False

#     return count


# for _ in range(N) :

#     n,m = map(int, input().split())
#     pairs = []
#     line = list(map(int,input().split()))

#     for i in range(0,m*2,2) :
#         pairs.append(line[i:i+2])
#     print(line)
#     print(pairs)

#     areFriend = [ [ False for _ in range(n)] for _ in range(n) ]

#     for pair in pairs :
#         areFriend[pair[0]][pair[1]] = True
#         areFriend[pair[1]][pair[0]] = True

#     finished = [False for _ in range(n)]

#     print(pairing(finished))