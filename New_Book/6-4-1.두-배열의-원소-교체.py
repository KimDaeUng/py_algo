N, K = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

# 첫번쨰 인덱스부터 확인하며 두 배열의 원소를 최대 K번 비교
for i in range(K):
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    
    # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
    else:
        break

print(sum(A))