# https://www.acmicpc.net/problem/12851

# https://m.blog.naver.com/paula23/221806668833
step_list = [lambda x: x-1, lambda x:x+1, lambda x: x*2]

N, K = map(int, input().split())
queue = [N]
checked = [False]*100001
found = False
time = 0
answer = 0

if N == K:
    found = True
    answer +=1

visited = {N : 1}
while not found : # 맞을 때 까지 반복
    depth = {}
    for node in queue:
        for step in step_list:
            move = step(node)
            if move < 0 or move > 100000:
                continue
            if move == K:
                answer += visited[node]
                found = True
            # depth에 없고 탐색 안 했던 것이면 추가
            if move not in depth and not checked[move]: 
                checked[move]=True
                depth[move] = visited[node]
            # depth에 있고, 탐색 했던 것이면 방문횟수 추가
            elif move in depth and checked[move]:
                depth[move]+=visited[node]
    
    # 현재 깊이에서 가능한 다음에 이동한 인덱스들을 다음 iter의 queue로 갱신
    queue = list(depth.keys())
    # 현재 depth에 누적된 정보를 visited에 갱신
    visited = depth
    time += 1

print(time)
print(answer)
