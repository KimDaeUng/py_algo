# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/start/
# 20m

# My Solution : Retry
# ref: https://yceffort.kr/2020/06/codility-07-04-stone-wall
def solution(H):
    st = []
    cnt = 0
    for i in range(len(H)):
        while len(st) > 0 and st[-1] > H[i]:
            st.pop()
        while len(st) == 0 or st[-1] < H[i]:
            st.append(H[i])
            cnt += 1
    return cnt