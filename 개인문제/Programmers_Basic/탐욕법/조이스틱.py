# https://programmers.co.kr/learn/courses/30/lessons/42860
# My Solution
def solution(name):
    answer = 0
    n = len(name)
    '''
    N은 A부터 뒤로 26-14+1 = 13, 앞으로도 13
    O부터는 뒤에서 세는 것이 빠름
    1 2 3 4 5 6 7 8 9 10111213
     A B C D E F G H I J K L M
    14151617181920212223242526
     N O P Q R S T U V W X Y Z
    '''
    def w2n(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')] # ord('A')를 뺴기 때문에 위로는 13, 아래로는 12까지
    
    for ch in name:
        answer += w2n(ch)
        
    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        l_dist = idx
        r_dist = n - next_idx
        if l_dist < r_dist:
            move = min(move, l_dist * 2 + r_dist)
        else:
            move = min(move, l_dist + r_dist * 2)
    answer += move
    return answer

# Solution : 완벽한 Solution 아님
def solution(name):
    answer = 0
    name = list(name)
    base = ["A"] * len(name)
    idx = 0
    # 방금 문자를 이동시킨 인덱스에서 오른쪽 문자와 왼쪽 문자 중 A가 아닌 것을 더 빨리 만나는 쪽으로 이동
    while True:
        r_idx = 1
        l_idx = 1

        # A가 아니면 
        if name[idx] != "A":
            # 반대로 바꾸는 경우가 더 빠르면 
            diff = ord(name[idx]) - ord("A")
            if diff > 13:
                answer += 26 - (ord(name[idx]) - ord("A"))
            else:
                answer += ord(name[idx]) - ord("A")
            # 확인이 끝난 지점은 'A'로 바꿈
            name[idx] = "A"
        
        # 모든 수정이 끝나면 stop
        if name == base:
            break
        
        # 방금 이동한 인덱스에서 오른쪽과 왼쪽 둘 중 하나라도 A인 것을 만날때까지 거리 count
        for i in range(1, len(name)):
            if name[idx + i] == "A":
                r_idx += 1
            else:
                break
            if name[idx - i] == "A":
                l_idx += 1
            else:
                break
        # "A"가 아닌 것을 만나는 거리가 보다 짧은 쪽으로 이동
        # 1. 왼쪽으로 이동하고 이동한 거리만큼 이동
        if r_idx > l_idx:
            answer += l_idx
            idx -= l_idx
        # 2. 오른쪽으로 이동 
        else:
            answer += r_idx
            idx += r_idx
    
    return answer

print(solution('JEROEN'))

'''
최적화해야할 요소 2가지
1. 상하 최소 거리로 알파벳 바꾸기
2. 좌우 최소거리 구해 방향 정한 후 이동

- chane 배열에는 각 알파벳마다 상하 조정 중 min값으로 최소 횟수 담아두기
- idx 0번부터 시작해서 좌우 이동 횟수 answer에 더해주기
- 좌우 방향 전환시에는 바꿔야하는 알파벳이 나오기까지 좌우 거리를 구하고, 그 중 최솟값이 되는 방향으로 전환
- 모든 알파벳이 조정된 경우 (chane sum이 0)

'''
# Solution : 완벽한 Solution 아님
def solution(name):
    # 상하 조정 알파벳 최소 횟수
    change = []
    n = len(name)
    for i in name:
        # 위로 이동하는 거리, 아래로 이동하는 거리
        change.append(min(ord(i)-ord('A'), ord('Z') - ord(i) + 1))
    idx = 0
    answer = 0

    while True:
        # 상하 이동 횟수 추가
        answer += change[idx]
        # 이미 확인한 문자 삭제
        change[idx] = 0

        # 모든 문자를 확인한 경우 종료
        if sum(change) == 0:
            return answer
        
        # 좌우 이동 방향 정하기, 이미 확인한 문자 or A인 문자가 아닌 쪽
        l, r = 1, 1
        while change[idx - l] == 0:
            l += 1
        while change[idx + r] == 0:
            r += 1
        # 위치(인덱스) 조정
        answer += l if l < r else r
        idx += - l if l < r else r

# Solution : 상하 이동 한 번에 계산 후 좌우이동 최소 계산
def solution(name):
    answer = 0
    n = len(name)
    
    def alphabet2num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]
    
    for ch in name:
        answer += alphabet2num(ch)

    move = n - 1
    for idx in range(n):
        # 오른쪽방향 'A'라면 계속 이동 (next_idx += 1)
        next_idx = idx + 1
        # print(f"idx = {idx} / char : {name[idx]} ----------------")
        # print(f'    next_idx : {next_idx}')
        while (next_idx < n) and (name[next_idx] == 'A'):
            # print(f'        while ({next_idx}) < ({n}) and ({name[next_idx]}) == "A"')
            next_idx += 1
            # print(f'        next_idx += 1 : {next_idx}')
        distance = min(idx, n - next_idx)
        # print(f'    distance : min({idx}, {n}-{next_idx}) = {distance}')
        move = min(move, idx + n - next_idx + distance)
        # print(f'    move : min({move}, {idx} + {n} - {next_idx} + {distance}) = {move}')

    answer += move
    return answer

print(solution("BBAABAAAB"))
'''

012345678
BBAABAAAB

다음 인덱스가 'A'인지 확인하고, A이면 next_idx += 1
-> 연속된 'A'의 덩어리가 끝난 첫번째 index를 구하게됌

distance = min(idx, n - next_idx)
n - next_idx : A덩어리가 끝난 오른쪽 문자열 덩어리
idx : 현재 위치

i = 1일때
	next_idx = 4
	distance = min(1, 9 - 4) = 1
	move = 9 - 1 = 8
	1번 인덱스로 가면 시작점에서 오른쪽으로 움직이는 경우인 i = 1번 움직이는 것과
	왼쪽으로 움직여 끝으로 가는 경우인 n - next_idx = 5번 움직이는 것 중 작은 값을 택해야함
	두 방법 중 짧은 쪽을 택해 갔다가 반대로 되돌아 오기 떄문에 새로운 move 수를 계산하는 식은 아래처럼 구성됌
	연속된 A 덩어리가 여러개라 할지라도 모든 덩어리 경우를 세서 가장 적은 move 수를 정하기 때문에 상관 없음
	move = min(move, (idx) + (n - next_idx) + distance)

idx = 0 / char : B ----------------
    next_idx : 1
    distance : min(0, 9-1) = 0
    move : min(8, 0 + 9 - 1 + 0) = 8
idx = 1 / char : B ----------------
    next_idx : 2
        while (2) < (9) and (A) == "A"
        next_idx += 1 : 3
        while (3) < (9) and (A) == "A"
        next_idx += 1 : 4
    distance : min(1, 9-4) = 1
    move : min(7, 1 + 9 - 4 + 1) = 7
idx = 2 / char : A ----------------
    next_idx : 3
        while (3) < (9) and (A) == "A"
        next_idx += 1 : 4
    distance : min(2, 9-4) = 2
    move : min(7, 2 + 9 - 4 + 2) = 7
idx = 3 / char : A ----------------
    next_idx : 4
    distance : min(3, 9-4) = 3
    move : min(7, 3 + 9 - 4 + 3) = 7
idx = 4 / char : B ----------------
    next_idx : 5
        while (5) < (9) and (A) == "A"
        next_idx += 1 : 6
        while (6) < (9) and (A) == "A"
        next_idx += 1 : 7
        while (7) < (9) and (A) == "A"
        next_idx += 1 : 8
    distance : min(4, 9-8) = 1
    move : min(6, 4 + 9 - 8 + 1) = 6
idx = 5 / char : A ----------------
    next_idx : 6
        while (6) < (9) and (A) == "A"
        next_idx += 1 : 7
        while (7) < (9) and (A) == "A"
        next_idx += 1 : 8
    distance : min(5, 9-8) = 1
    move : min(6, 5 + 9 - 8 + 1) = 6
idx = 6 / char : A ----------------
    next_idx : 7
        while (7) < (9) and (A) == "A"
        next_idx += 1 : 8
    distance : min(6, 9-8) = 1
    move : min(6, 6 + 9 - 8 + 1) = 6
idx = 7 / char : A ----------------
    next_idx : 8
    distance : min(7, 9-8) = 1
    move : min(6, 7 + 9 - 8 + 1) = 6
idx = 8 / char : B ----------------
    next_idx : 9
    distance : min(8, 9-9) = 0
    move : min(6, 8 + 9 - 9 + 0) = 6
10
'''