# https://leetcode.com/problems/different-ways-to-add-parentheses/

from typing import List

# 제출용 코드
class Solution:
    '''
    연산자를 찾아 좌우로 분할, 연산자 양쪽에 하나의 원소가 남을때까지 재귀하여 연산 결과를 List로 반환,
    반환된 리스트는 상위 단계의 재귀에서 분할된 양쪽 리스트 중 하나에 할당되어 이중 for 문으로 분할된 쪽에서의 가능한 모든 연산 결과에 대해
    해당 단계의 연산으로 모두 계산함
    
    최소 작업 : 입력 스트링의 모든 연산자에 대해서 좌우로 분할, 분할된 좌우리스트 원소들의 조합으로 연산자로 계산할 수 있는 모든 결과를 리스트로 반환
    기저 사례 : 연산자가 없으면 재귀 종료
    '''
    def diffWaysToCompute(self, input: str) -> List[int]:
        
        ops = {'+' : lambda x, y : x+y,
               '-' : lambda x, y : x-y,
               '*' : lambda x, y : x*y}
        t = 0
        
        def recursive_op(input_str, ops, tab=t):
            # 기저 사례
            # 들어온 스트링에 연산자가 더이상 남아있지 않으면 숫자 리턴
            if not (("+" in input_str)|("-" in input_str)|("*" in input_str)):
                return [int(input_str)]
            
            # 최소 작업
            # 들어온 스트링에 연산자가 있는 경우
            # 스트링의 모든 원소를 순회하면서 
            ret = []
            for i in range(len(input_str)):
                s = input_str[i]

                # 현재 문자열이 연산자이면 이를 기준으로 좌우로 분할한다.
                # 좌우로 분할된 부분 각각에 대해 재귀함수를 적용해
                # L_list = [숫자, ..., ], R_list = [숫자, ..., ]가 되면(트리의 끝에 도달)
                # 아래 이중 for문으로 연산 결과를 리턴한다.
                # 리턴된 결과는 L_list, 또는 R_list의 한 쪽에 리스트 형태로 저장되고
                # 보다 상위 단계에서의 L_list의 모든 원소와 R_list의 모든 원소에 대해 현재 단계의 연산자로 가능한 모든 연산을
                # ret 리스트에 저장해 반환한다.
                # 들어온 스트링에 대해 모든 연산자를 하나씩 거치면서 좌우로 나누고
                # 좌우에 대한 연산을 수행하는데, 좌우 각각의 가능한 연산 결과가 여러개의 값이 될 수 있기 때문에 리스트로 리턴하게 함
                # 좌우에서 리스트로 반환된 모든 값에 대한 모든 조합을 계산해서 반환
                # 최초 연산결과(ret)은 트리의 끝까지, 즉 양쪽이 숫자가 될 때까지 재귀가 되어야 발생하고, 이 결과를 
                # 상위 단계의 좌우리스트 중 하나에 할당하여 모든 가능한 결과가 나오게 됨.

                # 각 리스트에 다시 recursive_op를 적용한다.

                L_list, R_list = [], []
                if s in ['+', '-', '*']:
                    
                    L_list = recursive_op(input_str[:i], ops, tab=tab+1)
                    R_list = recursive_op(input_str[i+1:], ops, tab=tab+1)

                    for L_s in L_list:
                        for R_s in R_list:
                            ret.append(ops[s](L_s, R_s))
            return ret
        
        return recursive_op(input, ops)




# 연산 과정 찍어보기 위한 코드
'''
최소 작업 : 연산자를 찾아 좌우로 분할, 좌우에 대해 연산
기저 사례 : 연산자가 없으면 재귀 종료
'''
def diffWaysToCompute(input: str) -> List[int]:
    
    ops = {'+' : lambda x, y : x+y,
            '-' : lambda x, y : x-y,
            '*' : lambda x, y : x*y}
    t = 0
    
    def recursive_op(input_str, ops, tab=t):
        # Base case
        # 들어온 스트링에 연산자가 더이상 남아있지 않으면 숫자 리턴
        
        if not (("+" in input_str)|("-" in input_str)|("*" in input_str)):
            print("\t"*tab," No left ops, return {}".format(int(input_str)))
            return [int(input_str)]
        
        # Recursive case
        # 들어온 스트링에 연산자가 남아있을 경우
        # 각 문자열을 순회하면서
        ret = []
        for i in range(len(input_str)):
            s = input_str[i]

            # 현재 문자열이 연산자에 해당하면
            # 좌우 리스트로 분할한다.
            # 재귀함수는 피연산자가 나올때까지 좌우로 탐색을 계속하고 
            # 각 리스트에 다시 recursive_op를 적용한다.

            L_list, R_list = [], []

            if s in ['+', '-', '*']:
                print("\t"*tab,"===========================")
                print("\t"*tab,"index number : {} / Operator : {}".format(i, s))
                print("\t"*tab, " Parentheses : {} | {}".format(input_str[:i], input_str[i+1:]))
                print("\t"*tab," L_list recursive input : {} ---------------".format(input_str[:i]))
                L_list = recursive_op(input_str[:i], ops, tab=tab+1)
                print("\t"*tab," L_list : ", L_list)

                print("\t"*tab," R_list recursive input : {} ---------------".format(input_str[i+1:]))
                R_list = recursive_op(input_str[i+1:], ops, tab=tab+1)
                print("\t"*tab," R_list : ", R_list)

                for L_s in L_list:
                    for R_s in R_list:
                        ret.append(ops[s](L_s, R_s))
                print("\t"*tab," ret : ", ret)
                        
        return ret
    
    return recursive_op(input, ops)

diffWaysToCompute("2*3-4*5")
'''
 ===========================
 index number : 1 / Operator : *
  Parentheses : 2 | 3-4*5
  L_list recursive input : 2 ---------------
          No left ops, return 2
  L_list :  [2]
  R_list recursive input : 3-4*5 ---------------      
         ===========================
         index number : 1 / Operator : -
          Parentheses : 3 | 4*5
          L_list recursive input : 3 ---------------  
                  No left ops, return 3
          L_list :  [3]
          R_list recursive input : 4*5 ---------------
                 ===========================
                 index number : 1 / Operator : *
                  Parentheses : 4 | 5
                  L_list recursive input : 4 ---------------
                          No left ops, return 4
                  L_list :  [4]
                  R_list recursive input : 5 ---------------
                          No left ops, return 5
                  R_list :  [5]
                  ret :  [20]
          R_list :  [20]
          ret :  [-17]
         ===========================
         index number : 3 / Operator : *
          Parentheses : 3-4 | 5
          L_list recursive input : 3-4 ---------------
                 ===========================
                 index number : 1 / Operator : -
                  Parentheses : 3 | 4
                  L_list recursive input : 3 ---------------
                          No left ops, return 3
                  L_list :  [3]
                  R_list recursive input : 4 ---------------
                          No left ops, return 4
                  R_list :  [4]
                  ret :  [-1]
          L_list :  [-1]
          R_list recursive input : 5 ---------------
                  No left ops, return 5
          R_list :  [5]
          ret :  [-17, -5]
  R_list :  [-17, -5]
  ret :  [-34, -10]
 ===========================
 index number : 3 / Operator : -
  Parentheses : 2*3 | 4*5
  L_list recursive input : 2*3 ---------------
         ===========================
         index number : 1 / Operator : *
          Parentheses : 2 | 3
          L_list recursive input : 2 ---------------
                  No left ops, return 2
          L_list :  [2]
          R_list recursive input : 3 ---------------
                  No left ops, return 3
          R_list :  [3]
          ret :  [6]
  L_list :  [6]
  R_list recursive input : 4*5 ---------------
         ===========================
         index number : 1 / Operator : *
          Parentheses : 4 | 5
          L_list recursive input : 4 ---------------
                  No left ops, return 4
          L_list :  [4]
          R_list recursive input : 5 ---------------
                  No left ops, return 5
          R_list :  [5]
          ret :  [20]
  R_list :  [20]
  ret :  [-34, -10, -14]
 ===========================
 index number : 5 / Operator : *
  Parentheses : 2*3-4 | 5
  L_list recursive input : 2*3-4 ---------------
         ===========================
         index number : 1 / Operator : *
          Parentheses : 2 | 3-4
          L_list recursive input : 2 ---------------
                  No left ops, return 2
          L_list :  [2]
          R_list recursive input : 3-4 ---------------
                 ===========================
                 index number : 1 / Operator : -
                  Parentheses : 3 | 4
                  L_list recursive input : 3 ---------------
                          No left ops, return 3
                  L_list :  [3]
                  R_list recursive input : 4 ---------------
                          No left ops, return 4
                  R_list :  [4]
                  ret :  [-1]
          R_list :  [-1]
          ret :  [-2]
         ===========================
         index number : 3 / Operator : -
          Parentheses : 2*3 | 4
          L_list recursive input : 2*3 ---------------
                 ===========================
                 index number : 1 / Operator : *
                  Parentheses : 2 | 3
                  L_list recursive input : 2 ---------------
                          No left ops, return 2
                  L_list :  [2]
                  R_list recursive input : 3 ---------------
                          No left ops, return 3
                  R_list :  [3]
                  ret :  [6]
          L_list :  [6]
          R_list recursive input : 4 ---------------
                  No left ops, return 4
          R_list :  [4]
          ret :  [-2, 2]
  L_list :  [-2, 2]
  R_list recursive input : 5 ---------------
          No left ops, return 5
  R_list :  [5]
  ret :  [-34, -10, -14, -10, 10]
'''