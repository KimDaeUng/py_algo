# 09:58-11:19
'''
위상 정렬 문제
입력 예시의 그래프는 아래와 같다.
     /--------\
1(10) - 2(10)  \
      \ 3(4) - 4(4)
             \ 5(3)

현재 노드까지 오기 위한 최소 비용 = 현재 노드 비용 + 선행 노드들의 비용
'''

string = '''5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

from collections import deque
# 노드 개수 입력
n = int(input())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = { k : {'cost' : 0, 'pre' : [], 'ind' : 0 } for k in range(n + 1)}

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n + 1):
    line = list(map(int, input().split()))[:-1]
    graph[i]['cost'] = line[0]
    graph[i]['pre'].extend(line[1:])
    graph[i]['ind'] = len(graph[i]['pre'])

# print(graph)
# print(indegree)
def cal_cost(graph, x, cumsum):
    if len(graph[x]['pre']) == 0:
        return cumsum + graph[x]['cost']
    else:
        min_node = min([ (graph[i]['cost'], i) \
            for i in graph[x]['pre']], key=lambda k : k[0])[1]
        # print(min_node, [ (graph[i]['cost'], i) \
        #     for i in graph[x]['pre']])
        # print('cumsum',cumsum, graph[min_node]['cost'])
        return cal_cost(graph, min_node, cumsum + graph[x]['cost'])
# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    result_dic = { i : [] for i in range(1, n + 1)}
    q = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if graph[i]['ind'] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]['pre']:
            result_dic[now].append(i, )
            graph[i]['ind'] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if  graph[i]['ind'] == 0:
                q.append(i)
    return result

result = topology_sort()
for i in range(1, n + 1):
    print(cal_cost(graph, i, 0))

# Solution
'''
위상정렬 응용
각 노드(강의)에 대한 인접 노드 확인시 인접한 노드에 대하여 현재보다 강의시간이 더 긴 경우를 찾는다면
더 오랜 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블을 갱신해 답을 구할 수 있다
따라서 위상 정렬을 수행하면서 매번 간선 정보를 확인해 결과 테이블을 갱신한다.
- result : 최종적으로 각 강의를 수강하기까지의 최소 시간의 리스트(결과 테이블)
처음에 각 강의 시간은 time 리스트 변수에 담겨 있는데, 위상 정렬 함수 초기 부분에서 deepcopy() 함수를 이용해
time 리스트 변수 값을 복사하여 result 리스트 변수의 값으로 설정하는 작업이 수행된다.

'''
from collections import deque
import copy

# 노드 개수 입력
v = int(input())
# 모든 노드에 대한 진입차수는 0
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)
# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드의 진입차수에서 1 빼기
        for i in graph[now]:
            # time[i] : 강의 i의 소요시간(문제에서 주어진 값)
            # result[i] : 강의 i까지 오기위한 총비용의 현재까지의 최댓값
            # result[now] : now까지 오기위한 총비용의 현재까지의 최댓값
            # 위상 정렬을 수행하면서 매번 각 강의의 최대 비용을 갱신

            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()