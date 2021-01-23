# https://programmers.co.kr/learn/courses/30/lessons/42840

# 13:35 -> 

# https://programmers.co.kr/learn/courses/30/lessons/42840

# 13:35 -> 14:07

# My Solution
def supo1_gen():
    while True:
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5

def supo2_gen():
    while True:
        yield 2
        yield 1
        yield 2
        yield 3
        yield 2
        yield 4
        yield 2
        yield 5
    
def supo3_gen():
    while True:
        yield 3
        yield 3
        yield 1
        yield 1
        yield 2
        yield 2
        yield 4
        yield 4
        yield 5
        yield 5

supo1 = supo1_gen()
supo2 = supo2_gen()
supo3 = supo3_gen()

def solution(answers):
    c1, c2, c3 = 0, 0, 0

    for a, s1, s2, s3 in zip(answers, supo1, supo2, supo3):
        if a == s1:
            c1 += 1
        if a == s2:
            c2 += 1
        if a == s3:
            c3 += 1
    
    answer_list = [c1, c2, c3]
    max_answer = max(answer_list)

    answer = [i+1 for i, j in enumerate(answer_list) if j == max_answer ]
    answer.sort()
    return answer


# Good Solution

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result