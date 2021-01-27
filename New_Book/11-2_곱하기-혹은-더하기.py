# 0을 만나면 무조건 다음 연산자는 +, 이외에는 *
S = list(map(str, input()))

result = int(S[0])
S = S[1:]
for n in S:
    cur_n = int(n)
    # 피연산자 모두 0을 포함하지 않은 경우 : 합
    if (cur_n not in [0, 1])&(result not in [0, 1]):
        result *= cur_n
    # 피연산자 중에 0이 존재하는 경우 : 곱
    else:
        result += cur_n

print(result)