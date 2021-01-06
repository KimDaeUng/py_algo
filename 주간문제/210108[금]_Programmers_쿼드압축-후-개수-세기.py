# https://programmers.co.kr/learn/courses/30/lessons/68936

# Recursive
# 1. 4등분하는 과정
# 2. 각 조각의 원소가 모두 동일한가? 
#   -> 동일하면 하나로 압축 후 리턴
#   -> 아니면 하나로 다시 1로 반족

# 고민한 답

from itertools import chain

def solution(arr):
    
    def rec(arr):
        n = len(arr)
        half_n = n//2
        flatten = [ pixel for sublist in arr for pixel in sublist]

        # 1. Base case
        if n == 1:
            # print("base case : ", [arr[0][0]])
            return [arr[0][0]]
        # 2. 현재 arr가 모두 동일한 수인 경우 압축
        if n**2 == sum(flatten):
            # print("Compress to 1")
            # print("----"*10)
            return [1]
        elif sum(flatten) == 0:
            # print("Compress to 0")
            # print("----"*10)
            return [0]

        # 3. 아닌 경우 4분할 후 재귀 적용 
        UL = [row[:half_n] for row in arr[:half_n]]
        UR = [row[half_n:] for row in arr[:half_n]]
        DL = [row[:half_n] for row in arr[half_n:]]
        DR = [row[half_n:] for row in arr[half_n:]]
        
        # print("UL : ", UL)
        # print("UR : ", UR)
        # print("DL : ", DL)
        # print("DR : ", DR)
        # 관심사는 0과 1의 개수이기 때문에 nested list일 필요가 없음
        results = rec(UL) + rec(UR) + rec(DL) + rec(DR)
        # print(results)
        # print("----"*10)
        return results

    comp = rec(arr)
    answer = [comp.count(0), comp.count(1)]
    return answer


def solution(arr):

    def rec(arr):
        n = len(arr)
        half_n = n//2
        flatten = [ pixel for sublist in arr for pixel in sublist]

        # 1. Base case
        if n == 1:
            print("base case : ", [arr[0][0]])
            return [arr[0][0]]
        # 2. 현재 arr가 모두 동일한 수인 경우 압축
        if n**2 == sum(flatten):
            print("Compress to 1")
            print("----"*10)
            return [1]
        elif sum(flatten) == 0:
            print("Compress to 0")
            print("----"*10)
            return [0]

        # 3. 아닌 경우 4분할 후 재귀 적용 
        UL = [row[:half_n] for row in arr[:half_n]]
        UR = [row[half_n:] for row in arr[:half_n]]
        DL = [row[:half_n] for row in arr[half_n:]]
        DR = [row[half_n:] for row in arr[half_n:]]
        
        print("UL : ", UL)
        print("UR : ", UR)
        print("DL : ", DL)
        print("DR : ", DR)
        # 관심사는 0과 1의 개수이기 때문에 nested list일 필요가 없음
        results = rec(UL) + rec(UR) + rec(DL) + rec(DR)
        print(results)
        print("----"*10)
        return results

    comp = rec(arr)
    answer = [comp.count(0), comp.count(1)]
    return answer

