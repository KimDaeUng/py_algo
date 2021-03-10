# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

# import re
# begin = 'hit'
# target = 'cog'
# words = ["hot", "dot", "dog", "lot", "log", "cog"]

# # x를 제외한 나머지 문자열의 개수를 찾는 코드, n이면 True 아니면 Fasle
# except_matches = lambda x, y, n : True if len(re.findall(r'(?:(?!{}).)'.format(x), y))==n else False

# # begin의 각 글자를 순회하면서 words의 각 단어에서 하나만 바뀐 것을 선택해야함
# N = len(begin)-1
# answer = []
# for c in begin:
#     queue = []
#     for w in words:
#         # x를 제외한 문자열의 개수가 2이면(하나만 일치하면) queue에 등록
#         if except_matches(c, w, N):
#             queue.append(w)
#         N -= 1
#         # 모든 다음 후보들들을 검사
#         while queue:
#             # 첫번째 후보 단어 선택
#             q_word = queue.pop(0)
#             for q in q_word:
#                 # e를 제외한 문자열의 개수가 1이면(두 개가 일치하면) queue에 등록
#                 if except_matches(q, w, N):
#                     if N > 0:
#                         queue.append(w)
#                         N -= 1
#                     elif N == 0:
#                         answer.append()

#                     continue

# Retry - (Pass)
# 17:18-18:22
# 단어를 w라 하자, w0과 w1은 한글자만 차이가 나야함
# 모든 경우를 탐색하는 BFS
# 한글자만 차이나면 q에 넣기, 깊이도 함께 넣어서 나중에 출력하도록 함

from collections import deque
def solution(begin, target, words):
    len_word = len(begin)

    q = deque([])
    q.append((0, begin))

    words
    visited = [ 0 for _ in range(len(words) + 1) ]
    route = []
    while q:
        dist, cur_w = q.popleft()
        
        if cur_w == target:
            return dist 

        # 하나의 알파벳만 차이나면 큐에 추가
        for idx, w in enumerate(words):
            count = 0

            if visited[idx] == 1:
                continue

            for i in range(len_word):
                if cur_w[i] == w[i]:
                    count += 1

            if count == len_word - 1:
                q.append((dist + 1, w))
                visited[idx] = 1
                route.append((dist + 1, w))
                print(route)
    return 0
        

# print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
exit()

# Solustion
#########################

# from collections import deque

# def solution(begin, target, words):
#     def bfs(s):
#         de = deque()
#         de.append(s)

#         while de:
#             x = de.popleft()
#             if x == target:
#                 break
            
#             for i in words:
#                 c = 0
#                 # 자리수 동일, 현재 선택된 각 단어를 한 글자씩 비교
#                 for be, wo in zip(x, i):
#                     # 각 단어가 일치하면 count
#                     if be == wo:
#                         c += 1
#                 # 한 개의 알파벳만 바꿀 수 있으며, 방문한 적이 업는 경우
#                 if c == len(x)-1 and di[i] == 0:
#                     di[i]= di[x]+1
#                     de.append(i)

# di = dict()
# di[bigin] = 0
# for i in words:
#     di[i] = 0
# bfs(begin)

# # di에 0이 아닌 
# try:
#     if di[target] != 0:
#         return di[target]
# except:
#     return 0

