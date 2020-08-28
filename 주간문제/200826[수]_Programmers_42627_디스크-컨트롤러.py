# https://programmers.co.kr/learn/courses/30/lessons/42627


'''
스케치 

1. 요청 시점 순으로 정렬

2. 요청 시점이 가장 빠른 작업 바로 실행 -> 최초 시작 작업이라 하자

3. 최초 시작 작업이 종료되기 전까지 요청되는 작업의 개수 >= 2 일 때 우선순위 부여
   * 만약 모든 작업 종료후 요청되는 경우에는 가장 빠른 요청 우선

4. 우선순위
  - 요청부터 종료까지 걸리는 시간이 짧은 순으로 정렬
  - 요청부터 종료까지 걸리는 시간 : |작업요청시각 - (최초시작작업종료시각+작업소요시간)|

'''


def solution(jobs):
    import heapq
    n = len(jobs)
    time, end, queue = 0, -1, []
    # time : 진행중인 작업이 종료되는 시각, 우선순위큐에 진행 중인 작업 없을 경우 +1
    # end : 직전 작업의 종료시각

    # 처리한 프로세스 수
    count = 0
    
    answer = 0

    while count < n:
        # Step 1 : 우선순위큐에 요청 작업 추가
        for i in jobs:
            # i[0] = 프로세스 입력 시간, i[1] = 프로세스 끝날 때까지 걸리는 시간
            # 직전 작업의 종료시각(end)과 현재 작업의 종료 시각(또는 현재 시각 time) 사이에 들어온 요청에 대하여
            if end < i[0] <= time: 
                answer += (time - i[0])     # 각 요청 작업의 대기 시간을 모두 answer에 더해둡니다.
                heapq.heappush(queue, i[1]) # 작업시간 큐에 넣음
        
        # Step 2 : heap 내 작업 처리
        if len(queue) > 0:
            # 가장 빨리 끝나는 프로세스가 끝날 때까지는 우선순위큐에 있는 프로세스 전부 대기시간이므로 값을 추가
            answer += len(queue) * queue[0]
            # 직전 작업이 끝난 시각 갱신 
            end = time
            # 가장 빨리 끝나는 프로세스가 걸린 시간을 더해줌,
            # 이 작업이 진행되는 동안 요청된 작업을 다시 Step 1에서 추가
            time += heapq.heappop(queue)
            # 프로세스가 끝났으므로 count + 1 해준다.
            count += 1
        
        else:
            # 힙에 요청받은 작업이 없을 경우, time +1, Step 1 의 탐색범위 증가
            time += 1

    return int(answer/n)
        
        
                




def solution(jobs):
    answer = 0
    import heapq

    haep = []
    sorted_jobs = sorted(jobs, key=lambda x : x[1])
    for j in sorted_jobs:
        heapq.heappush(heap, j)
    print(heap)
    def cal(startq, queries):
        tmp = 0
        for q in queries:
            tmp += 1 if startq == q


    # Pointing?
    for i, (s, e) in enumerate(sorted_jobs):
        # Scan to check whether there're jobs
        print("Finding {}th job's queries".format(i))
        queries = []
        
        for p in range(s, e):
            queries.append([ j for j in sorted_jobs[i:] if j[0] == p ])
        
        q2e = [abs(j[0] - (sorted_jobs[0]+j[1])) for j in sorted_jobs]



    # 작업 요청 시간 순 & 소요시간 순으로 정렬
    # 동일 요청 시간에 복수의 작업요청이 있을 경우 종료시간 작은 순

    sorted_jobs
    query2end = [abs(j[0] - (sorted_jobs[0]+j[1])) for j in sorted_jobs]
    print(query2end)
    return answer

if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6], [3, 7], ]
    solution(jobs)
    