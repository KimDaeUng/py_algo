# https://programmers.co.kr/learn/courses/30/lessons/60058
# 16:35-18:43: 못품. 정상인 경우가 주어지는 경우를 잡지 못 함

# 처음에 틀렸던 함수 (입력 케이스가 이미 정답인 경우에도 변환 수행)
# def is_correct(s):
#     if len(s) == 0:
#         return True
#     if s[0] == ')':
#         return False
#     else:
#         half_length = len(s) // 2
#         # 반으로 자른 앞부분에 ')'가 없어야함
#         if (')' not in s[:half_length]) and ('(' not in s[half_length:]):
#             return True
#         else:
#             return False

def is_balance(s):
    nl, nr = 0, 0
    for i in s:
        if i == '(':
            nl += 1
        elif i == ')':
            nr += 1
    if nl == nr:
        return True
    else:
        return False

def is_correct(s):
    c = 0
    for i in s:
        if i == '(':
            c += 1
        else:
            if c == 0:
                return False
            c -= 1
    return True

def solution(p):
    # 1. 빈 문자열인 경우
    if p == '':
        return p
    # 2. 문자열 p를 두 '균형작힌 괄호 문자열' u, v로 분리
    length = len(p)
    for i in range(2, length + 1, 2):
        u, v = p[:i], p[i:]
        # u가 더이상 분리할 수 없는 균형잡힌 괄호 문자열이고, v도 균형잡힌 문자열인경우
        if is_balance(u) and is_balance(v):
            # 3. u가 올바른 괄호 문자열이라면
            if is_correct(u):
                tmp_result = solution(v)
                return u + tmp_result
            # 4. u가 올바른 괄호 문자열이 아니라면
            else:
                result = '(' + solution(v) + ')'

                # (최초 풀이시 틀린 부분) : 단순 뒤집기로 하면 안됨
                # u = u[1:-1][::-1]
                # return result + u

                u = list(u[1:-1])
                for j in range(len(u)):
                    if u[j] == '(':
                        u[j] = ')'
                    else:
                        u[j] = '('
                result += ''.join(u)
                    
                return result
# p = "()))((()"
p = "(()())()"
print(solution(p))

# Solution

# # '균형잡힌 괄호 문자열'의 인덱스 반환
# def balanced_idx(p):
#     c = 0 # '('의 개수
#     for i in range(len(p)):
#         if p[i] == '(':
#             c += 1
#         else:
#             c -= 1
#         if c == 0:
#             return i

# # '올바른 괄호 문자열'인지 판단
# def check_sound(p):
#     c = 0 # '('의 개수
#     for i in p:
#         if i == '(':
#             c += 1
#         else:
#             # 쌍이 맞지 않는 경우에 False 반환
#             if c == 0:
#                 return False
#             c -= 1
#     return True # 쌍이 맞는 경우 True 반환

# def solution(p):
#     answer = ''
#     if p == '':
#         return answer
#     idx = balanced_idx(p)
#     u = p[:idx + 1]
#     v = p[idx + 1:]
#     # '올바른 괄호 문자열'이면, v에 대해 함수를 수행한 결과를 붙여 반환
#     if check_sound(u):
#         answer = u + solution(v)
#     # '올바른 괄호 문자열'이 아니라면 아래 과정을 수행
#     else:
#         answer = '(' + solution(v) + ')'
#         u = list(u[1:-1])
#         for i in range(len(u)):
