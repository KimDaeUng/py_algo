# https://programmers.co.kr/learn/courses/30/lessons/60058
# 16:35-18:43: 못품. 정상인 경우가 주어지는 경우를 잡지 못 함


# p = input().strip()

# 0. 예외처리

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

def is_correct_init(p, e_idx):
    if e_idx == len(p):
        return False
    if p[e_idx] == ')':
        if e_idx == 0:
            return False
        else:
            return True
    # '('로 시작할 경우 재귀호출해 ')'을 만나면 True, '('일 경우에는 계속 탐색하는데 끝까지 탐색해도 안나오면 False
    elif p[e_idx] == '(':
        if is_correct_init(p, e_idx + 1) and e_idx % 2 == 0:
            return True
        else:
            return False

print(is_correct_init("()))((()", 0))
exit()

def is_correct(s):
    if len(s) == 0:
        return True
    if s[0] == ')':
        return False
    else:
        half_length = len(s) // 2
        # 반으로 자른 앞부분에 ')'가 없어야함
        if (')' not in s[:half_length]) and ('(' not in s[half_length:]):
            return True
        else:
            return False

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
                new_u = u[1:-1][::-1]
                return result + new_u
p = "()))((()"
print(solution(p))