# 02:16-02:30

# My Solution
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = n - 1

while start <= end:
    mid = (start + end) // 2
    if data[mid] == mid:
        print(mid)
        exit()
    elif data[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1

print(-1)

# Solution(Recursive)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 변환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

# 이진 탐색 수행
index = binary_search(array, 0, n-1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 고정점이 있는 경우 해당 인덱스 출력
else:
    print(index)