# https://www.acmicpc.net/problem/2110
# 15:20-18:39
'''
N : 집의 개수
C : 공유기의 개수
C간의 거리가 최대가 되도록 각각의 집에 설치

3번이면 이분탐색 1단계 수행해서 중간값으로
4번이면 이분탐색 2단계 수행해서 양쪽의 중간값으로
5번이면 이분탐색 3단계 수행해서 네 개 조각들의 각각의 중간값으로
여튼 이분 탐색으로 쪼갠 중간값과 시작값과 끝값의 차이를 누적해서, 그 중 최소인 것을 출력?

'''
# Retry 
'''
- 탐색 대상 : 가장 인접한 두 공유기 사이의 거리
- 매 후보를 mid로 하여 체크,
  해당 거리만큼 떨어트렸을 때 설치 대수를 카운트하여,
  가능한 설치 대수가 작을 경우 두 공유기 사이의 거리를 줄여(후보 리스트의 왼쪽 분할) 탐색,
  가능한 설치 대수가 크거나 같으면, 두 공유기 사이 거리를 늘려(후보 리스트의 오른쪽 분할) 탐색
  (같을 때 늘려야 가능한 거리 후보의 상한값을 구할 수 있음)
'''
n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
start = 0
end = data[-1] - data[0]
max_dist = 0

while start <= end:
    mid = (start + end) // 2
    prev_value = data[0]
    count = 1
    
    # 이전값 + gap(mid) 이상인 최초의 값을 만날 때,
    # 그 값으로부터 다시 gap(mid)를 더한 값으로 갱신하고
    # 설치한 공유기 대수를 더함
    for i in range(n):
        if data[i] >= prev_value + mid:
            prev_value = data[i]
            count += 1
    # 설치한 대수(count)가 설치해야하는 공유기 수(C)보다 작으면
    # mid(gap)을 줄여 더 많이 설치하도록 해야함
    # 더 작은 값의 후보 (후보 리스트 왼편)을 탐색
    if count < c:
        end = mid - 1
    # 설치한 대수(count)가 설치해야하는 공유기 수(C)보다 크거나 같으면
    # C를 설치할 수 있는 최대 gap을 구하기 위해
    # 더 큰 값의 후보 (후보 리스트 오른편)을 탐색
    else:
        max_dist = mid
        start = mid + 1

print(max_dist)



# Solution
# 집의 개수(N)과 공유기의 개수(C)를 입력받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보 입력 받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = array[1] - array[0] # 집의 좌표 중에 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중에 가장 큰 값
result = 0

while (start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value = array[0]
    count = 1
    # 현재 mid값을 이용해 공유기를 설치
    for i in range(1, n): # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)

# My Solution (Failed)
# import sys

# n, c = map(int, input().split())

# data = []
# for _ in range(n):
#     data.append(int(input()))

# start = 0
# end = n - 1 

# # 예외 처리
# if n == 2:
#     if c == 1:
#         min_value = 0
#     elif c == 2:
#         min_value = abs(data[0] - data[1])
#     # print(min_value)
#     exit()

# min_value = 200000
# data.sort()


# def bin_search(array, start, end, depth, max_depth):
#     global min_value
#     # 종료 조건
#     if start > end:
#         return None
#     if max_depth == depth:
#         return None
    
#     mid = (start + end) // 2
#     # print(array[mid] - array[start])
#     # print(array[end] - array[mid])
    
#     # 가장 인접한 두 공유기 사이의 거리가 기존 값보다 더 작아지면 갱신
#     if (array[mid] - array[start]) <= min_value:
#         if array[mid] - array[start] == 0:
#             return None
#         min_value = array[mid] - array[start]
#     # 크거나 같으면 탐색
#     elif (array[end] - array[mid]) <= min_value:
#         if array[end] - array[mid] == 0:
#             return None
#         min_value = array[end] - array[mid]
#     # 양쪽을 모두 탐색함
#     bin_search(array, start, mid, depth + 1, max_depth)
#     bin_search(array, mid + 1, end, depth + 1, max_depth)


# # 공유기 개수가 짝수, 홀수인지에 따라 분기
# max_depth = c // 2
# if c % 2 == 0:
#     mid = (start + end) // 2
#     if c == 2:
#         max_depth = 2
#     # print(data, start, mid, max_depth - 1)
#     bin_search(data, start, mid, 0, max_depth - 1)
#     bin_search(data, mid + 1, end, 0, max_depth - 1)
# else:
#     bin_search(data, start, end, 0, max_depth)

# print(min_value)


# Retry
# import sys

# n, c = map(int, input().split())

# data = []
# for _ in range(n):
#     data.append(int(input()))

# data.sort()

# # 탐색하는 값은 가장 인접한 두 공유기 사이의 거리
# start = 1
# end = data[-1] - data[0]

# max_gap = 0
# while start < end:
#     print(start, end)
#     mid = (start + end) // 2
#     for i in range(c, 0, -1):
#         tmp = data[0] + i * mid
#         if tmp < data[-1]:
#             print('tmp < data[-1]')
#             break

#     # Gap을 더 줄일 필요
#     if i < c:
#         end = mid
#     elif i == c:
#         max_gap = max(mid, max_gap)
#         start = mid
#         if start == end:
#             print(max_gap)
#             break

# print(max_gap)