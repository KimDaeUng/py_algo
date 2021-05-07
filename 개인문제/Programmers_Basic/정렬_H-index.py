# 16:07-16:20, 16:40-17:28
def solution(citations):
    citations.sort(reverse=True)
    len_c = len(citations)
    max_h = citations[0]
    answer = 0
    # citations에서 가장 큰 값에서부터 내림차순으로 h 탐색
    for h in range(max_h, -1, -1):
        # h번 이상 인용되지 않은 논문의 최초 인덱스 번호 탐색
        idx = 0
        while idx < len_c and citations[idx] >= h:
            idx += 1
        
        upper = idx           # h번 이상 인용된 논문의 수
        lower = len_c - upper # 나머지 논문의 수
        
        # h번 이상 인용된 논문의 수가 h편 이상이고 나머지 논문이 h편 이하 인용
        if upper >= h and lower <= h:
            answer = max(answer, h)
        
    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))


# Solution
# 오름차순 정렬 후, l - i = h로 취급해 하나씩 검사
# l - i : 인용횟수가 citaionts[i] 이상인 논문의 편 수가 몇 편이 남았는가?
# citaions[i] >= l - i : 그 중 가장 작은 인용횟수가 citaionts[i]개 이상인 논문의 편 수 이상인가?
# -> 다시 정리 : 인용 수 h번 이상인 것들 가운데 가장 작은 것의 인용 수는 h이상 이어야 한다. & h번 이상인 것들의 개수는 l-i개이다.
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    # print(citations, l)

    for i in range(l):
        # print(i, citations[i], l-i)
        if citations[i] >= l-i:
            return l-i
    return 0


citations = [3, 0, 6, 1, 5]
print(solution(citations))