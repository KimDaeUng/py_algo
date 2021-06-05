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

# Retry
# 19:27-19:53 20:08-20:44 -> 1h?
'''
# 어떻게 하면 좋을까?
- 각 길이만큼 쪼개서 압축 시도
- 그 중 제일 적은 길이를 출력
'''
from collections import deque

def solution(s):
    length = len(s)
    
    min_value = 1001

    if length == 1:
        return 1
    
    # 2부터 최대 길이의 절반까지 한 덩어리로 묶는 경우를 검사
    for span in range(1, (length//2) + 1):
        count = 1
        compare_str = s[ : span ]
        total_len = 0
        
        for i in range(span, length + 1, span):
            # print(compare_str)
            if compare_str == s[i:i+span]:
                count += 1
            else:
                # 만약 직전과 다르면, 문자열 개수 갱신, 개수가 2 이상인 경우)
                if count >= 2:
                    total_len = total_len + len(str(count)) + span
                # 문자 개수가 1인 경우 그냥 더함
                elif count == 1:
                    total_len = total_len + span
                # 비교 대상이되는 문자열을 갱신, 문자열 개수도 갱신
                compare_str = s[i:i+span]
                count = 1
        
        # 남는 문자열 처리
        if i < length:
            total_len += len(s[i:])
        # print(total_len)
        # print('='*50)
        min_value = min(min_value, total_len)
    
    return min_value


print(solution('abcabcabcabcdededededede'))

# Solution
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려 가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    
    return answer