# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter
def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    
    for p_key, p_value in part.items():
        
        c_value = comp.get(p_key, 0)
        if p_value != c_value:
            return p_key