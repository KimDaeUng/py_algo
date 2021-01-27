# 11:20-11:33
# 입력
data = list(map(str, input()))

# 0과 1을 각각 카운트 하되,
# 직전과 달라질 경우에 카운트 추가

zero = 0
one = 0
pre = ""
for i in data:
    # 직전과 다를 경우(최초 포함)
    if pre != i:
        pre = i # 새로운 pre 갱신
        if i == "0":
            zero +=1
        else:
            one += 1
    # 직전과 같을 경우는 셀 필요 없음

print(min(zero, one))