# https://programmers.co.kr/learn/courses/30/lessons/42862

# 19:18-
def solution(n, lost, reserve):
    answer = 0
    # 여벌의 체육복을 가져온 학생이 도난당한경우 제거
    lost = set(lost)
    reserve = set(reserve)
    inter = lost.intersection(reserve)
    lost = list(lost - inter)
    reserve = list(reserve - inter)
    
    n_lost = len(lost)
    n_safe = n - n_lost
    
    if n == n_lost:
        return 0
    
    for s in lost:
        # 인접 번호 학생 중 여벌의 체육복을 가져온 학생이 있으면
        for d in [-1, 1]:
            near_s = s + d
            if 0 < near_s <= n and \
            near_s in reserve:
                reserve.remove(near_s)
                n_safe += 1
                break
            
    return n_safe

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)