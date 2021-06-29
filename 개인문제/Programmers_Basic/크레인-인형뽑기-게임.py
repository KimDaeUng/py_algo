# https://programmers.co.kr/learn/courses/30/lessons/64061
# 00:18-00:32
# My Solution
def solution(board, moves):
    answer = 0
    rotated_board = list(map(lambda x:
                        [i for i in x if i != 0][::-1],
                        zip(*board)))
    stack = []
    for i in moves:
        if len(rotated_board[i - 1]) != 0:
            stack.append(rotated_board[i - 1].pop())
        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                del stack[-2], stack[-1]
                answer += 2
    
    return answer

# Solution: Stack
def solution(board, moves):
    stack = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] =0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        del stack[-2], stack[-1]
                        answer += 2
                break
    return answer