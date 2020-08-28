# https://programmers.co.kr/learn/courses/30/lessons/42579
import time
# Error Code
# def solution(genres, plays):
#     answer = []
#     # Make unique index
#     from collections import defaultdict, OrderedDict
#     from operator import itemgetter
#     from heapq import nlargest
#     genre_dic = defaultdict(OrderedDict)
#     # genre_dic = defaultdict(list)
#     genre_count = defaultdict(int)
    
#     for i, (g, p) in enumerate(zip(genres, plays)):
#         # genre_dic[g].append((i, p))
#         genre_count[g] += p
#         if len(genre_dic[g]) == 0:
#             genre_dic[g][i] = p
#             print('-'*50)
#             print('len == 0, add this')
#             print('genere_dic[{}][{}] : {}'.format(g, i, genre_dic[g][i]))
#             continue

#         # 새 값이 들어올 때마다 기존 값과 비교해 큰 쪽이 왼쪽에 오도록 정렬
#         if (len(genre_dic[g]) >= 1):
#             print('-'*50)
#             print('genere_dic[{}]s length >= 1, add this'.format(g))


#             pre_max_value = list(genre_dic[g].items())[0]
#             print('pre_max_value : {} / p : {}'.format(pre_max_value, p))
#             # 현재값 p가 이전의 최대값보다 크면 
#             if p > pre_max_value[1]:
#                 print("  if p({}) > pre_max_value[1]{}".format(p, pre_max_value))
#                 # 해시테이블 내 순서 바꾸기 위해 지웠다가 다시 씀
#                 print('  origin genere_dic[{}] : {}'.format(g, genre_dic[g]))

#                 del genre_dic[g]
#                 genre_dic[g][i] = p
#                 genre_dic[g][pre_max_value[0]] = pre_max_value[1]
#                 print('  reordered genere_dic[{}] : {}'.format(g, genre_dic[g]))
#                 print('  genre_dic[{}] : {}'.format(g, genre_dic[g]) )

#             # 현재값 p가 이전 최대값보다 작거나 같으면그대로 붙임
#             else:
#                 print("  if p({}) <= pre_max_value[1]{}".format(p, pre_max_value))
#                 # 이 때 해당 장르 길이가 2보다 크거나 같으면 추가하지 않고 스킵함
#                 if len(genre_dic[g]) == 2:
#                     print("    if len(genre_dic[{}])({}) >= 2, continue".format(g, len(genre_dic[g]), pre_max_value))
#                     print('    genre_dic[{}] : {}'.format(g,genre_dic[g]) )
#                     continue
#                 else:
#                     genre_dic[g][i] = p
#                     print('    add genre_dic[{}][{}] = {}'.format(g, i, p))
#                     print('    genre_dic[{}] : {}'.format(g,genre_dic[g]) )
#     print(genre_dic)
#     genre_sorted = sorted(genre_count.items(), key=itemgetter(1))[::-1]
#     for g, _ in genre_sorted:
#         answer.extend([ s for s, _ in genre_dic[g].items()])
#         # answer.extend([ s[0] for s in song_sorted ])

#     return answer

def solution(genres, plays):
    answer = []
    
    from collections import defaultdict
    genre_dic = defaultdict(dict)
    genre_count = defaultdict(int)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_count[g] += p
        genre_dic[g][i] = p
       
    genre_sorted = sorted(genre_count.items(), key=lambda x : x[1])[::-1]
    for g, _ in genre_sorted:
        song_sorted = sorted(genre_dic[g].items(), key=lambda x : (-x[1], x[0]))[:2]
        answer.extend([ s for s, _ in song_sorted])
    return answer

if __name__ == '__main__':
    # genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'hiphop', 'rock', 'disco']
    # plays =  [      500,   600,       150,       800,  2500,      210,    200,   3000]

    # 샘플이 하나라면
    # genres = ['classic']
    # plays = [500]

    # 장르가 하나밖에 없다면?
    # genres = ['classic', 'classic', 'classic']
    # plays = [500, 600, 150]


    # Basic Case
    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plays = [500, 600, 150, 800, 2500]

    run_time = []
    for _ in range(1000):
        s = time.time()
        solution(genres, plays)
        run_time.append(time.time() -s)
    print(sum(run_time)/1000)

    print(solution(genres, plays))