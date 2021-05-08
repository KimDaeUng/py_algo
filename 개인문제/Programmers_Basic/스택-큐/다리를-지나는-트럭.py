# https://programmers.co.kr/learn/courses/30/lessons/42583
# 20:55-21:20

# My Solution
# 20:55-21:30
'''
요구사항 그대로 시뮬레이션
bridge 큐를 만들고, 매번 남는 다리 하중을 계산.
하중 여유 있으면 새로운 트럭을 올림
매 iteration 마다 모든 트럭의 시간 + 1, 전체 시간 + 1
제일 첫 번쨰 트럭의 시간이 다리 길이에 도달하면 bridge에서 제거
최초 time = 2 -> 첫번째 윈소의 첫번째 itraion에서 나오는 소요시간과 일치 시켜주기 위함
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([])
    truck_weights = deque([[i, 0] for i in truck_weights])
    count = len(truck_weights)
    truck = truck_weights.popleft()
    truck[1] += 1
    bridge.append(truck)
    time = 2
    while count:
        
        if len(truck_weights):
            left_weight = weight - sum([i[0] for i in bridge])
            if truck_weights[0][0] <= left_weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
        
        # time update
        bridge = deque([ (i[0], i[1] + 1) for i in bridge])
        # print(time, bridge)
        if bridge[0][1] == bridge_length:
            bridge.popleft()
            count -= 1
        time += 1
    
    return time

# Solution : Class 사용
from collections import deque

DUMMY_TRUCK = 0
class Bridge(object):
    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = deque()
        self._current_weight = 0
    
    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item
    
    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return f'Bridge({self._current_weight}/{self._max_weight} : [{list(self._queue)}]'

def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = deque(w for w in truck_weights)
    
    # bridge에 weight = 0인 트럭으로 모두 채움
    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)
    
    # bridge에서 dummy truck을 하나 뺀 후
    # 다리 하중이 허용할 경우 trucks의 첫 번째 원소를 뺴서 추가
    # 아닐 경우 무게 0인 dummy truck 추가
    # count += 1
    count = 0
    while trucks:
        bridge.pop()
        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)
        count += 1
    
    # bridge에 남은 truck들이 지나갈 때까지 카운트
    while bridge:
        bridge.pop()
        count += 1
    
    return count

# Solution 
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    # pop(0)을 쓰는 것을 피하기 위해 reverse
    truck_weights.reverse()

    while truck_weights:
        # bridge에서 첫 번째 원소 뺌
        total_weight -= bridge.popleft()
        # 남은 하중 + 현재 트럭 하중 > 교량 최대 하중: -> 더미 트럭 0 추가
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        # 새 트럭을 올릴 수 있는 경우
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1
    
    # truck_weights에 대기중인 truck을 모두 올리면
    # 가장 마지막으로 올린 트럭은 bridge의 제일 마지막에 위치하므로
    # bridge의 길이만큼 더해줘야 bridge를 건너게됨
    step += bridge_length

    return step