# 00:00-01:18

# My Solution
# Ref : https://velog.io/@changjunpyo/%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89Binary-Search-upperbound-underbound%EC%9D%98-%EA%B5%AC%ED%98%84
import sys

n, x = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

def solution():
    # upper_bound
    start = 0
    end = n - 1

    while start < end:
        mid = (start + end) // 2
        if data[mid] <= x:
            start = mid + 1
        else:
            end = mid
    upper_bound = start

    # lower_bound
    start = 0
    end = n - 1

    while start < end:
        mid = (start + end) // 2
        if data[mid] < x:
            start = mid + 1
        else:
            end = mid
    lower_bound = start
    return upper_bound - lower_bound

count = solution()
if count == 0:
    print(-1)
else:
    print(count)
exit()
# Solution
# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array, target, mid + 1, end)

n, x = map(int, input().split()) # 데이터 개수 N, 찾고자 하는 값 x를 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 x인 데이터 개수 계산
count = count_by_value(array, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)


# Solution 2: bisect 라이브러리 이용
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터 개수 N, 찾고자 하는 값 x를 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 x인 데이터 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)