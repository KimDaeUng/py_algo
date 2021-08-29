# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/start/
# 30m

# My Solution : Retry
# https://app.codility.com/demo/results/trainingZTMQMM-2Z6/
# ref : https://jobjava00.github.io/algorithm/codility/lesson7/Fish/
def solution(A, B):
    st = []
    cnt = 0
    for fish, d in zip(A, B):
        if d == 1:
            st.append(fish)
        else:
            while len(st) > 0 and st[-1] < fish:
                st.pop()
            if len(st) == 0:
                cnt += 1

    return cnt + len(st)