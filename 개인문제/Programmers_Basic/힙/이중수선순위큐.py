# https://programmers.co.kr/learn/courses/30/lessons/42628
# 18:33-19:02
# My Solution
# 최소힙으로 구현, 최대값을 찾을 때 마다 최대힙으로 변환
# 0.05ms
import heapq
def solution(operations):
    answer = [0, 0]
    queue = []
    for line in operations:
        ctrl, digit = line.split(' ')
        if ctrl == 'I':
            digit = int(digit)
            heapq.heappush(queue, digit)
        else:
            if digit == '-1':
                try:
                    heapq.heappop(queue)
                except:
                    continue
            else:
                queue = [ -i for i in queue]
                heapq.heapify(queue)
                try:
                    heapq.heappop(queue)
                except:
                    pass
                queue = [ -i for i in queue]
                heapq.heapify(queue)
    
    if len(queue):
        answer[1] = heapq.heappop(queue)
        queue = [ -i for i in queue]
        heapq.heapify(queue)
        answer[0] = -heapq.heappop(queue)
    
    return answer

# Solution
# nlargest, nsmallest를 이용해 각각 최대, 최소값 구한 뒤
# 해당값 삭제 후 다시 heapify
# 남은 heap의 원소가 1개일 경우, 최댓값과 최솟값 동일
import heapq

def solution(arguments):
    dp_queue = []
    for arg in arguments:
        op, val = arg.split(' ')
        if op == 'I':
            heapq.heappush(dp_queue, int(val))
        else:
            try:
                if val == '1':
                    remove_value = heapq.nlargest(1, dp_queue)[0]
                else:
                    remove_value = heapq.nsmallest(1, dp_queue)[0]
            except IndexError:
                pass
            else:
                dp_queue.remove(remove_value)
                heapq.heapify(dp_queue)

    if len(dp_queue) == 0:
        max_value = 0
        min_value = 0
    elif len(dp_queue) == 1:
        max_value = dp_queue[0]
        min_value = dp_queue[0]
    else:
        max_value = heapq.nlargest(1, dp_queue)[0]
        min_value = heapq.nsmallest(1, dp_queue)[0]

    return [max_value, min_value]