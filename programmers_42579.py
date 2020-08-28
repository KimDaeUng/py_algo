# https://programmers.co.kr/learn/courses/30/lessons/42579
import time
def solution(genres, plays):
    answer = []
    # Make unique index
    from collections import defaultdict, OrderedDict
    from operator import itemgetter
    from heapq import nlargest
    genre_dic = defaultdict(OrderedDict)
    # genre_dic = defaultdict(list)
    genre_count = defaultdict(int)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        # genre_dic[g].append((i, p))
        genre_count[g] += p
        if (len(genre_dic[g]) >= 1):
            pre_max_value = list(genre_dic[g].items())[0]
            if pre_max_value is not None:
                if p > pre_max_value[1]:
                    del genre_dic[g][pre_max_value[0]]
                    genre_dic[g][i] = p
                    genre_dic[g][pre_max_value[0]] = pre_max_value[1]
                    pre_max_value = p
        else:
            continue

    genre_sorted = sorted(genre_count.items(), key=itemgetter(1))[::-1]
    for g, _ in genre_sorted:
        song_sorted = nlargest(2, genre_dic[g].items(), key=itemgetter(1,0))
        answer.extend([ s for s, _ in song_sorted])
        # answer.extend([ s[0] for s in song_sorted ])

    return answer

if __name__ == '__main__':
    genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'hiphop', 'rock', 'disco']
    plays = [500, 600, 150, 800, 2500, 210, 200, 3000]

    # 샘플이 하나라면
    # genres = ['classic']
    # plays = [500]

    # 장르가 하나밖에 없다면?
    # genres = ['classic', 'classic', 'classic']
    # plays = [500, 600, 150]


    # 장르에 속한 곡이 하나라면
    # genres = ['classic', 'pop', 'classic', 'classic']
    # plays = [500, 600, 150, 800]

    run_time = []
    for _ in range(1000):
        s = time.time()
        solution(genres, plays)
        run_time.append(time.time() -s)
    print(solution(genres, plays))
    print(sum(run_time)/1000)