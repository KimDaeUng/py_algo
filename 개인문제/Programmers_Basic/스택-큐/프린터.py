# https://programmers.co.kr/learn/courses/30/lessons/42587
# 11:57-12:04

# My Solution
from collections import deque
def solution(priorities, location):
    priorities = deque([(i, v) for i, v in enumerate(priorities)])
    result = []
    while priorities:
        doc, pr = priorities.popleft()
        is_delayed = False
        for doc_i, pr_i in priorities:
            if pr_i > pr:
                is_delayed = True
                priorities.append((doc, pr))
                break
        if not is_delayed:
            result.append(doc)
    
    return result.index(location) + 1

# Solution : 위와 동일한 접근, 더 간결한 표기
def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[i] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer