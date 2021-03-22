# 대략 1시간?
# # My Solution
# import sys

# n, k = map(int, input().split())
# data = list(map(int, sys.stdin.readline().rstrip().split()))
# data.sort()
# print(data)
# # 탐색 범위를 한정 지어야함
# # (1-하한) (떡 최대 높이 - 손님이 가져갈 길이) 부터 (2-상한) (떡 최대 높이) 까지
# # 하한에서부터 탐색, 매 회차마다 절단된 길이의 합 == 손님이 가져갈 길이 k 이면
# # h의 값을 매번 갱신

# # 그런데 하한점 또한 바로 구할 수 없고, 탐색을 통해 찾아야함
# start = 0
# target_start = data[-1] - k
# # 상한점은 고정
# end = len(data) - 1

# # 하한점 시작점을 찾고, 그 다음부터 하한점의 값을 증가시켜가며 각 값을 저장 후 최댓값 구함

# # 1. 하한점 시작점을 찾음(target_start 이하 중 최댓값)
# while start <= end:
#     mid = (start + end) // 2
#     if data[mid] == target_start:
#         start = mid
#     elif data[mid] < target_start:
#         start = mid + 1
#     else:
#         end = mid - 1

# # 2. 하한 시작점부터 h를 증가시켜가면서
# # 절단된 길이가 일치할 때마다 h를 더 큰 값으로 갱신
# print(start)
# max_value = 0
# for i in range(start, len(data)):
#     h = data[i]
#     cut_data = data[i:]
#     cut_data = [ j - h for j in cut_data ]
#     result = sum(cut_data)
#     print(result)
#     if result == k:
#         max_value = h

# print(max_value)


# Solution
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력 받기
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보 입력 받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    # 잘랐을 때의 떡의 양 계산
    for x in array:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 떄가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)