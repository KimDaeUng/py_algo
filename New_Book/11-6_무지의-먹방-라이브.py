# https://programmers.co.kr/learn/courses/30/lessons/42891

# 시도
# def solution(food_times, k):
#     answer = 0
#     # 목적 : k초가 되었을 때 무엇을 가리키는지를 출력
#     # 방식 :
#     # 하나씩 순회하면서, 0이면 패스하고 다음 음식을 -1
#     idx = 0
#     sec = 0
#     len_food_times = len(food_times)
#     while sec != k:
#         # 1) 0이 아닐 경우 1씩 섭취
#         #    소요 시간(sec) += 1
#         print(sec, food_times)
#         if food_times[idx%len_food_times] != 0:
#             food_times[idx%len_food_times] -= 1
#             idx += 1
#             sec += 1
#         # 2) 0일 경우 idx만 1 추가하여 다음 iter로 넘어감
#         #    sec는 카운트 하지 않음
#         else:
#             idx += 1
#             continue
#     return (idx%len_food_times)+1

# food_times = [3, 1]
# K = 3
# print(solution(food_times, K))


# Solution (이분 탐색)
def solution(food_times, k):
    # 전체 가능한 입력값의 범위에서 이분탐색으로
    # k보다 작거나 같은 마지막 인덱스의 최댓값을 구한다
    low, high = 0, 10**8
    n, cutting, idx = len(food_times), 0, 0
    while low <= high:
        mid = (low + high) // 2
        # 마지막 값의 인덱스는 n의 배수,
        # mid번 만큼 전체를 순회했을 때 마지막 인덱스 번호
        v = n * mid
        # mid번 만큼 전체를 순회했다 -> 각 원소들에서 mid만큼을 뺐다.
        # 마지막 인덱스 = n개의 원소를 mid 번만큼 순회한 횟수 + 음수의 총합
        for f in food_times:
            tmp = f - mid
            if tmp < 0:
                v += tmp
        # 만일 v가 k보다 작거나 같다면, 
        # 한 번에 빼야되는 수(순회 횟수) cutting을 구한 것이므로 저장.
        # 마지막 인덱스를 가리키는 시간 v를 idx에 복사
        if v <= k:
            cutting, idx = mid, v
            low = mid + 1
        else:
            high = mid - 1
    
    # k보다 작거나 같은 가장 마지막 인덱스까지 먹방 진행
    food_times = [f-cutting for f in food_times]

    # 나머지에 대해 
    for i in range(n):
        # 양수인 경우 중에 소요시간이 k와 일치되는 순간
        # 현재 인덱스를 리턴하고 종료
        if food_times[i]>0 and idx == k:
            return i + 1
        # 양수인 경우에만 전체 소요시간을 카운트
        else: # food_times[i] <= 0 | idx != k
            if food_times[i]>0:
                idx += 1
    return -1


# Dongbin book solution

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면
    # 시간안에 다 먹게되므로 -1 리턴
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선 순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        print("sum_value : ", sum_value)
        print("q[0][0] : ", q[0][0])
        print("previous : ", previous)
        print("length : ", length)
        print("((q[0][0] - previous) * length) : ", ((q[0][0] - previous) * length))
        print("sum_value + ((q[0][0] - previous) * length) : ",sum_value + ((q[0][0] - previous) * length))
        now = heapq.heappop(q)[0]
        print('now : ', now)
        sum_value += (now - previous) * length
        print('sum_value : ', sum_value)
        length -= 1 # 다 먹은 음식 제외
        preivous = now # 이전 음식 시간 재설정
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]


food_times = [8, 6, 4]
K = 15
print(solution(food_times, K))