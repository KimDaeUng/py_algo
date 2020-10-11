# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    # 양쪽 끝을 예외처리하는 대신, 0을 패딩해 동일한 작업 적용하도록 함
    triangle = [[0] + line + [0] for line in triangle]
    
    # i 번째 라인 -> i+1 개의 원소
    # 직전라인 왼쪽, 오른쪽의 합 중 최대를 저장
    # answer : 마지막 줄 최대값 
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])