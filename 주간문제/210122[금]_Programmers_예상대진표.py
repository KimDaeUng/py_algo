# https://programmers.co.kr/learn/courses/30/lessons/12985

# 10:27 ->11:49
def solution(n,a,b):
    # answer = 3
    round_count = 0
    while a != b:
        round_count += 1
        a = (a+1)//2
        b = (b+1)//2
    return round_count

'''
N명이 참가하고 토너먼트 형식으로 진행

2 명끼리 대전 후 이긴 사람이 진출

이긴 사람은 다음 라운드에서 새 번호를 부여

처음 라운드에서 A 번을 가진 참가자가 B번 참가자와 몇 번쨰 라운드에서 만나는지
(A, B가 만날 때 까지 연속적으로 이긴다고 가정할 때)

'''

