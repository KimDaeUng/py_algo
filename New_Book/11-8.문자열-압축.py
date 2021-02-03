# https://programmers.co.kr/learn/courses/30/lessons/60057
# 22:40-01:00 (2h20m)
from collections import defaultdict
import sys
def solution(s):
    length = len(s)
    if length == 1:
        return 1
    
    # cf. length = 1 인 경우, memory 변수에 None이 할당되어 에러남
    minimum = sys.maxsize
    for span in range(1, (length//2)+1):
        # memory 조각만큼을 기억한 뒤 뒷부분을 조사 
        # 최초 실행시 [0:span] 이나, 반복되지 않는 경우 다음 span으로 update
        memory = s[:span]
        cur_span = s[span:2*span]

        iter_end = (length // span)+1
        
        i = 1
        tmp_results = []
        tmp = [1, memory]
        while (i <= iter_end+1):
            # 현재 메모리의 조각과 다음 조각이 일치하면 카운트
            i += 1
            if memory == cur_span:
                tmp[0] += 1
            # 불일치할 경우, 불일치한 cur_span을 memory로 대체하고 다음 iter로 넘어감
            else:
                tmp_results.append(tmp)
                memory = cur_span
                tmp = [1, memory]
            cur_span = s[i*span:(i+1)*span]
        
        result = len(''.join([ str(v) + k if v != 1 else k for v, k in tmp_results ]))
        
        minimum = min(minimum, result)

    return minimum