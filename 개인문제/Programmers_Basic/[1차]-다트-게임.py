# https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3
# 15:14-15:57 

# MySolution
'''
- 3번의 기회
- 기회마다 점수는 0~10
- 점수와 함꼐 S D T 영역 존재, 각 영역 당첨시 점수의 1, 2, 3제곱, 점수마다 하나씩 존재
- 옵션: 점수마다 둘 중 하나만 존재하거나 않을 수도 있다.
    - 스타상* : (해당 점수 + 바로 전에 얻은 점수) * 2
        - 최초 기회시엔 해당점수만
        - 다른 스타상과 중첩 가능(4배)
        - 아차상과 중첩 가능: -2배

    - 아차상# : - 해당 점수

입력형식
"점수|보너스|[옵션]"으로 이뤄진 문자열 3세트
- 점수 : 0~10 
- 보너스 : S, D, T 중 하나
- 옵션 : *, #, None
'''
# My Solution
import re
def solution(dartResult):
    comp = re.compile(r'([\d]{1,2}){1,2}([SDT])([*#]){0,1}')
    dartResult = comp.findall(dartResult)
    result = []
    bonus2square = { k:v for v, k in enumerate('SDT', start=1)}
    for score, bonus, option in dartResult:
        cur_val = int(score) ** bonus2square[bonus]
        
        if option == '#':
            cur_val = -cur_val
        elif option == '*':
            cur_val *= 2
            if len(result) != 0:
                result[-1] *= 2
        result.append(cur_val)
            
    return sum(result)

# Solution 1: Regualr Expression
# 내풀이와 동일하지만 좀 더 깔끔
import re
def solution(dartResult):
    bouns = {'S' : 1, 'D' : 2, 'T': 3}
    option = {'' : 1, '*', '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?')
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        
        dart[i] = int(dart[i][0]) ** bouns[dart[i][1]] * option[dart[i][2]]
    return sum(dart)

# Solution 2:
# 숫자 10의 길이가 달라 처리가 어려움 -> replace이용 길이 맞춘 뒤
# 각 요소들을 원소로 하는 리스트로 변환
# 각 기회의 구성요소 길이가 옵션으로 인해 3, 4로 불규칙적임
# 따라서 point를 저장하는 stack을 두어
# 현재 score는 여기에 담아 직전 값으로 불러와서 사용,
# 나머지 보너스나 옵션은 매번 판정하여 stack에 저장된 점수에 처리
def solution(dartResult):
    answer =[]
    dartResult = dartResult.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dartResult]

    i = -1
    sdt = list('SDT')
    for j in point:
        # Bonus
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j) + 1)
        # Option
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        # Score
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)