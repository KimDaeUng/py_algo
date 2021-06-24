# https://www.acmicpc.net/problem/5622
# My Solution
'''
문자 -> 다이얼 -> 걸리는 시간
'''
alpha = ("ABC", "EDF", "GHI","JKL", "MNO", "PQRS", "TUV", "WXYZ")
alpha2time = { a : n for n, sub_a in enumerate(alpha, start=3) for a in sub_a}

string = input()
time = 0
for s in string:
    time += alpha2time[s]
print(time)