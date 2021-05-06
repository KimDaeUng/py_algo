# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    def compute(arr, cmd):
        i, j, k = cmd
        return sorted(arr[i-1:j])[k-1]
    answer = [compute(array, cmd) for cmd in commands]
    
    return answer

# Best
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))