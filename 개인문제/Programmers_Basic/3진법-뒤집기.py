# https://programmers.co.kr/learn/courses/30/lessons/68935
# 17:15-18:40

# My Solution 2: Built-in func int(number, base)
# ref: https://btfnswt.tistory.com/81
# 3)45 - 0
# 3)15 - 0
# 3) 5 - 2
#    1 - 

def solution(n):
    n_3_rev = ''
    while True:
        n, r = divmod(n, 3)
        n_3_rev += str(r)
        if n == 0:
            break

    return int(n_3_rev, 3)

print(solution(45))

# My Solution 1:
def solution(n):
    n_3_rev = []
    while True:
        n, r = divmod(n, 3)
        n_3_rev.append(r)

        if n == 0:
            break
    
    answer = 0
    cube_n = len(n_3_rev) - 1

    for i in n_3_rev:
        answer += i * (3 ** cube_n)
        cube_n -= 1
    return answer

print(solution(45))

    # 아래 부분으로 쓰면 timepout
    # for k, i in zip(range(len(n_3_rev) - 1, -1, -1), n_3_rev):
    #     answer += i * 3 ** k
    # return answer