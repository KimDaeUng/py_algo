# https://app.codility.com/programmers/lessons/6-sorting/triangle/

# My Solution
# 배열 내에 삼각형의 각 변의 부등식 조건을 만족하는 세 수가 있는지 확인하는 문제
# 오름차순 정렬하면 부등식 중 하나의 조건만 고려하여 비교가 가능해지므로
# 정렬 O(N*log(N)) 후 단순 선형 탐색 O(N)의 시간 복잡도가 소요됨
def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(2, len(A)):
        if A[i-2] + A[i-1] > A[i]:
            return 1
    else:
        return 0