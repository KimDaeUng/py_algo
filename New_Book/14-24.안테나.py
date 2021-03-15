# https://www.acmicpc.net/problem/18310
# 20:10-21:20 : 못 품

# My Solution 중앙값
'''
평균으로 찾으면 평균값과 실제 집의 위치와 다를 수 있다.
따라서 데이터 포인트를 기준으로 하는 중앙값으로 찾는다.
'''
N = int(input())
data = sorted(map(int, input().split()))
print(data[(N - 1)//2])

# 


# Failed Solution
# 1. 시간 초과
# import sys

# N = int(input())
# data = list(map(int, input().split()))

# min_value = sys.maxsize
# min_house = sys.maxsize

# for i in range(N):
#     center_house = data[i]
#     left_house = data[:i]
#     right_house = data[i+1:]

#     left_deviate = sum([ abs(i - center_house) for i in left_house])
#     right_deviate = sum([ abs(i - center_house) for i in right_house])
#     # print(center_house, left_deviate + right_deviate)
#     # print(left_house, right_house)
#     tmp_min_value = left_deviate + right_deviate
#     if min_value > tmp_min_value:
#         min_value = tmp_min_value
#         min_house = min(min_house, center_house)
#     elif min_value < tmp_min_value:
#         break
# print(min_house)

# 2. 시간초과
# import sys

# N = int(input())
# data = list(map(int, input().split()))

# min_house = sys.maxsize
# min_deviate = sys.maxsize

# for center in data:
#     cur_deviate = 0
#     for i in range(N):
#         cur_deviate += abs(center - data[i])
#     if cur_deviate < min_deviate:
#         min_deviate = cur_deviate
#         min_house = center
    
# print(min_house)