# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
# 1H 10M
# My Solution
# https://app.codility.com/demo/results/trainingSCP98U-V37/
def solution(S):
    if len(S) == 0:
        return 1
    if len(S) == 1:
        return 0

    st = [S[0]]
    S = S[1:]

    n1 = 1 if st[-1] == '(' else 0
    n2 = 1 if st[-1] == '{' else 0
    n3 = 1 if st[-1] == '[' else 0

    for i in S:
        if i == '(':
            n1 += 1
        elif i == '{':
            n2 += 1
        elif i == '[':
            n3 += 1
        st.append(i)

        if len(st) >= 2:
            if st[-2] == '(':
                if st[-1] == ')':
                    n1 -= 1
                    del st[-2:]
                    
            elif st[-2] == '{':
                if i == '}':
                    n2 -= 1
                    del st[-2:]
                    
            elif st[-2] == '[':
                if i == ']':
                    n3 -= 1
                    del st[-2:]
                
    if n1 == 0 and n2 == 0 \
        and n3 == 0 and len(st) == 0:
        return 1
    else:
        return 0