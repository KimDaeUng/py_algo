# https://programmers.co.kr/learn/courses/30/lessons/42577
# 00:15-00:55

# Solution : No Hash
def solution(phoneBook):
    phoneBook.sort()

    for s1, s2 in zip(phoneBook, phoneBook[1:]):
        if s2.startswith(s1):
            return False
    return True

# Solution 2 : Hash
def solution(phoneBook):
    hash_table = {}
    for p_num in phoneBook:
        hash_table[p_num] = 1
    for p_num in phoneBook:
        tmp = ''
        for num in p_num:
            tmp += num
            if tmp in hash_table and tmp != p_num:
                return False
    return True