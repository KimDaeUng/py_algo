# https://programmers.co.kr/learn/courses/30/lessons/12926

# My Solution
# 14:43-
def solution(s, n):
    u_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_alpha = u_alpha.lower()
    
    # 문자 -> 숫자 -> 쉬프트(범위 넘어가지 않도록 처리) -> 문자
    
    u_alpha2idx = { k: v for v, k in enumerate(u_alpha)}
    l_alpha2idx = { k: v for v, k in enumerate(l_alpha)}
    
    result = ''
    for s_ in s:
        if s_ in u_alpha2idx:
            idx = u_alpha2idx[s_]
            idx = (idx + n) % 26
            new_s_ = u_alpha[idx]
            
        elif s_ in l_alpha2idx:
            idx = l_alpha2idx[s_]
            idx = (idx + n) % 26
            new_s_ = l_alpha[idx]
            
        elif s_ == ' ':
            new_s_ = s_
        
        result += new_s_
    
    return result

# Solution
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)