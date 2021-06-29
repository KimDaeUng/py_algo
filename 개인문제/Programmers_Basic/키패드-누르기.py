# https://programmers.co.kr/learn/courses/30/lessons/67256
# 00:46-00:25

# My Solution:
# 양측 손의 마지막 번호 위치
# manhatton dist
# m
def solution(numbers, hand):
    answer = ''
    L, R = '*', '#'
    lridx = { k : "R" if k % 3 == 0 else 'L' for k in [1, 4, 7, 3, 6, 9] }
    keypad = [[1, 2, 3],[4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    
    num = 1
    num2cor = {}
    for r in range(3):
        for c in range(3):
            num2cor[num] = (r, c)
            num += 1
    for c, i in enumerate(keypad[-1]):
        num2cor[i] = (3, c)
    
    def dist(finger, target):
        return sum(map(lambda x, y : abs(x - y),
                       num2cor[finger], num2cor[target]))
    
    for d in numbers:
        if d in lridx:
            if lridx[d] == 'L':
                answer += 'L'
                L = d
            elif lridx[d] == 'R':
                answer += 'R'
                R = d
        else:
            ldist = dist(L, d)
            rdist = dist(R, d)
            if ldist < rdist:
                answer += 'L'
                L = d
            elif ldist > rdist:
                answer += 'R'
                R = d
            else:
                if hand == 'right':
                    answer += 'R'
                    R = d
                elif hand == 'left':
                    answer += 'L'
                    L = d

    return answer

numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"
print(solution(numbers, hand))