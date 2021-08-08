# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/start/
# 15m

# My Solution
# https://app.codility.com/demo/results/trainingDHKUK6-YXZ/
def solution(S):
    st = []
    for i in S:
        if i == ')' and len(st) > 0 and st[-1] == '(':
            st.pop()
            continue

        st.append(i)

    if len(st) == 0:
        return 1
    else:
        return 0