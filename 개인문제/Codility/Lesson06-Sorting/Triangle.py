# https://app.codility.com/programmers/lessons/6-sorting/triangle/
# https://app.codility.com/demo/results/training4VRZAR-KVE/
# My Solution
# 배열 내에 삼각형의 각 변의 부등식 조건을 만족하는 세 수가 있는지 확인하는 문제
# 오름차순 정렬하면 부등식 중 하나의 조건만 고려하여 비교가 가능해지므로
# 정렬 O(N*log(N)) 후 단순 선형 탐색 O(N)의 시간 복잡도가 소요됨
# 질문)
# 연속된 세 수만 고려하는 이유
# 만약 A[i]의 i 인덱스 증가 -> A[i] 증가하는데,
# 부등식에서는 A[i]가 더 커지는 경우를 고려할 필요 X
# 따라서 좌변의 두 수 또한 함께 증가해야함
def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(2, len(A)):
        if A[i-2] + A[i-1] > A[i]:
            return 1
    else:
        return 0