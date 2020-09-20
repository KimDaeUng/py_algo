# https://programmers.co.kr/learn/courses/30/lessons/42895
# DP

# https://www.hamadevelop.me/algorithm-n-expression/

# BFS 완전탐색???

def solution(N, number):
    answer = -1
    def dfs(N:int, number:int, cnt:int, prev:int, answer:int):
        # N의 카운트를 늘려가며 dfs로 수행한다.
        # 값을 저장하고 그 값이 number와 동일한지 확인한다.
        temp_N = N 
        if (cnt > 8):
            answer = -1
            return
        # 이전의 결과값이 목표로하는 number와 일치할 때
        # answer는 현재의 cnt 개수가 되며 탐색을 종료
        if number == prev:
            if answer==-1 | answer > cnt:
                answer = cnt 
            return
        
        # 최대 7이하인 경우에 대해서 탐색 
        for i in range(0, 8-cnt):
            dfs(N, number, cnt+i+1, prev-temp_N, answer)
            dfs(N, number, cnt+i+1, prev+temp_N, answer)
            dfs(N, number, cnt+i+1, prev*temp_N, answer)
            dfs(N, number, cnt+i+1, prev/temp_N, answer)

            temp_N = temp_N * 10 + N
    
    dfs(N, number, 0, 0, answer)
    
    return answer

print(solution(5, 12))

def solution(N, number):
    possible_set = [0,[N]] # 조합으로 나올수 있는 가능한 숫자들, 여기에 계속 append하며 이후에 사용함
    if N == number: #주어진 숫자와 사용해야 하는 숫자가 같은 경우는 1개면 족하므로 1으로 놓는다. 
        return 1
    for i in range(2, 9): # 2부터 8까지로 횟수를 늘려 간다. 
        case_set = [] # 임시로 사용할 케이스 셋, 각 I 별로 셋을 만들어 possible set에 붙인다.

        basic_num = int(str(N)*i) # 같은 숫자 반복되는 거 하나를 추가한다.
        case_set.append(basic_num)
        for i_half in range(1, i//2+1): # 사용되는 숫자의 횟수를 구해야 하는데, 절반 이상으로 넘어가면 같은 결과만 나올 뿐이므로 절반까지만을 사용한다. 
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]: # x와 y를 더하면 i 가 되도록 만든 수다. 
                    # print(possible_set)
                    case_set.append(x+y)# 각 사칙연산 결과를 더한다.
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y !=0:
                        case_set.append(x/y)
                    if x !=0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set) # 최종 결과물 set에 사칙 연산 결과를 더한다.
    return -1 