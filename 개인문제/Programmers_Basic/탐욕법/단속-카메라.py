# https://programmers.co.kr/learn/courses/30/lessons/42884
# Coment : 작동 방식이 아직 명확히 이해되지 않음, 다시 봐야함
# 05:00-05:40 : 못 품
# 15:00-16:52
# My Solution : Retry
# 진입 지점 기준 오름차순 정렬
# 카메라를 최댓값으로 초기화 camera = 30001
# 가장 마지막 원소(진입지점이 가장 큰 차량 경로)부터 작은 순으로 탐색, 현재 탐색 중인 경로를 route라 할 때
# 1. 카메라 위치가 진출 지점 route[1] 보다 크면, 카메라 위치를 진입지점 route[0]로 갱신하고 answer += 1
# 2. 카메라 위치가 진입 지점 route[1] 보다 작거나 같으면 스킵하고 넘어간다.
# @ route[0] > camera가 되는 일은 없다(맨 처음에 진입 시점 기준으로 오름차순 정렬 했고, camera는 이전 경로에서의 진입 시점 값이므로 항상 route[0] < camera가 보장됨.
# @ 현재 경로의 진출 시점 route[1] 보다 카메라 위치가 더 오른쪽에 있는 경우
#   카메라 위치를 현재 경로의 진입 시점 route[0]으로 당긴다. 이때 카메라를 새로 설치하기 때문에 answer +=1 

def solution(routes):
    routes.sort()
    camera = 30001
    answer = 0
    
    for route in reversed(routes):
        if route[1] < camera:
            camera = route[0]
            answer += 1
    return answer

# Solution :
'''
https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/
- 차량들이 카메라에 최대한 많이 잡히는 구간에 카메라를 설치하는 방법 구현
# 해결 방법 2가지
1. 카메라를 만났는지에 대한 check 배열을 만들고 각 구간을 모두 검사하는 방법
2. 진출 지점 기준으로 정렬 후 카메라에 걸리는지 확인하는 방법
'''

# 1. 카메라 만났는지에 대한 check 배열을 만들고 각 구간을 모두 검사
# O(N^2)
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    leng = len(routes)
    checked = [0] * leng
    
    for i in range(leng):
        if checked[i] == 0:
            camera = routes[i][1] # 진출 지점에 카메라를 갱신
            answer += 1
        for j in range(i + 1, leng):
            # i 이상의 나머지 차량들에 대해서 진입 진출시점 사이에 카메라가 있으면?
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    
    print(checked)

    return answer

# 2. 진출 지점 기준으로 정렬 후 카메라에 걸리는지 확인
# 풀이 과정
# 1. 진출 지점 기준으로 오름차순 정렬(routes[x][1] 기준)
# 2. 최대 -30000이니 초기 카메라 위치를 -30001로 초기화 해준다.
# 3. routes 배열을 반복하면서 카메라가 진입 지점(route[0])보다 작은지 확인
# 4. 작다면, 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미이니
#  4-1. 카메라를 추가로 세우고
#  4-2. 가장 최근 카메라의 위치(route[1])를 갱신한다.
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        print('route', route)
        if camera < route[0]:
            print(' camera < route[0] == True: answer : {} camera : {}'.format(answer, camera))
            answer += 1
            camera = route[1]
    return answer