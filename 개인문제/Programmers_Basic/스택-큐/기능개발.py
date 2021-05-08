# https://programmers.co.kr/learn/courses/30/lessons/42586
# 09:38-10:13
# My Solution
# 작업량을 한번에 계산한 뒤, 하나씩 꺼내면서
# 처음 카운트를 시작하는 작업량보다 작은 작업량이 나오면 누적해 카운트하고
# 큰 작업량이 나오면 이전까지 누적한 카운트를 결과에 저장한 뒤,
# 그 지점부터 그 값을 기준으로 새로 카운트함

import math
def solution(progresses, speeds):
    if len(progresses) == 0:
        return [0]
    
    if len(progresses) == 1:
        return [1]
        
    answer = []
    def prog(progresses, speeds):
        duration = []
        for i, u in zip(progresses, speeds):
            duration.append(math.ceil((100 - i)/u))
        return duration
    dura = prog(progresses, speeds)
    print(dura)
    prev = dura.pop(0)
    count = 1

    while dura:
        curr = dura.pop(0)
        if prev >= curr:
            count += 1
        else:
            answer.append(count)
            count = 1
            prev = curr
    answer.append(count)
            
    return answer

# Solution 1 : 단순 구현
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        # math.ceil 쓰지 않고 ceil
        # int(- 3.5) = -4,  int(3.5) = 3
        progress_day = - (p - 100) // s
        if len(Q) == 0 or Q[-1][0] < progress_day:
            Q.append([progress_day, 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]

# Solution 2 : 큐 이용
from collections import deque
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

