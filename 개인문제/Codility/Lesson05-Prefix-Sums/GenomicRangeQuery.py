# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
# 1h?
# My Solution
# https://app.codility.com/demo/results/training8RCVQ4-UNB/
def solution(S, P, Q):
    n = len(S)
    mA = [0] * (n + 1)
    mC = [0] * (n + 1)
    mG = [0] * (n + 1)

    for i in range(len(S)):
        if S[i] == 'A':
            mA[i + 1] += 1
        elif S[i] == 'C':
            mC[i + 1] += 1
        elif S[i] == 'G':
            mG[i + 1] += 1
        mA[i + 1] += mA[i]
        mC[i + 1] += mC[i]
        mG[i + 1] += mG[i]

    result = []
    for (s, e) in zip(P, Q):
        num_A = mA[e+1] - mA[s]
        num_C = mC[e+1] - mC[s]
        num_G = mG[e+1] - mG[s]

        if num_A > 0:
            result.append(1)
            continue
        elif num_C > 0:
            result.append(2)
            continue
        elif num_G > 0:
            result.append(3)
            continue
        else:
            result.append(4)
            continue

    return result