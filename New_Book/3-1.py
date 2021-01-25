n = 1260
count = 0 

# 큰 단위 화폐부터 차례로 
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n //coin # 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
    n %= coin # 거슬러 준 나머지 금액 갱신

print(count)
