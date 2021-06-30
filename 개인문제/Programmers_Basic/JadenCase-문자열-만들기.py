# https://programmers.co.kr/learn/courses/30/lessons/

# My Solution
def solution(s):
    return ' '.join(list(map(lambda x : x[0].upper() + x[1:].lower()
                              if len(x) > 1 else x.upper(), s.split(" "))))

# Solution: Built-In function: .capitalize()
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])