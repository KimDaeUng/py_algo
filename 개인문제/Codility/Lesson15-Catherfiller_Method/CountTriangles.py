# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/start/

# My Solution : fail O(N^3)
# https://app.codility.com/demo/results/trainingVX7YAB-GRN/

def solution(A):
    n = len(A)
    if n < 3:
        return 0
    
    A.sort()
    answer = 0 

    front = 2

    for i in range(2, len(A)):
        front = i
        if A[i-2] == A[front]:
            continue
        while (front < n):
            for j in range(i-1, front):
                if A[i-2] + A[j] > A[front]:
                    answer += 1
                    # print(A[i-2], A[i-1], A[front])
            front += 1

    return answer


# Soluttion : O(N^2)
# ref : https://parkssiss.tistory.com/344
def solution(A):
    n = len(A)
    if n < 3:
        return 0
    
    A.sort()
    answer = 0 

    front = 2

    for i in range(2, len(A)):
        front = i
        for j in range(i-1, n):
            while (front < n and A[i-2] + A[j] > A[front]):
                front += 1
            if front > j:
                answer += front - j - 1

    return answer
