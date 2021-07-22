# https://app.codility.com/programmers/lessons/6-sorting/distinct/
# 10m
# My Solution
# len(set(A))도 있지만 이를 안쓰고 하는 방법
def solution(A):
    if len(A) == 0:
        return 0
    A.sort()
    st = [A[0]]
    for i in range(1, len(A)):
        if st[-1] != A[i]:
            st.append(A[i])
    return len(st)