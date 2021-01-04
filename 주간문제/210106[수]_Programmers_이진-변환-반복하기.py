# https://programmers.co.kr/learn/courses/30/lessons/70129

# 같은 변환을 반복한다 -> 재귀?
# return : 이진변환의 횟수 & 변환과정에서 제거된 0의 개수
# -> 재귀함수에서 계속 받아야하는 부분


def solution(s):
    n_trans = 0
    n_del = 0
    
    def rec(string, n_trans, n_del):
        # Base case
        if string == "1":
            return [n_trans, n_del]
        
        # Recursive case
        len_string = len(string)
        n_one = string.count("1")
        
        n_del_cur = len_string - n_one
        n_trans += 1
        n_del += n_del_cur
        
        # transfrom decimal to binary
        string = bin(n_one)[2:]
        return rec(string, n_trans, n_del)

    return rec(s, n_trans, n_del)