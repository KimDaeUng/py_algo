
# https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    return sum(map(lambda x, y: x * y, sorted(A), sorted(B, reverse=True)))