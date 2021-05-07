# 02:50-

t = int(input())
INF = int(1e9)
for _ in range(t):
    n = int(input())
    # graph = [ [INF] * (n + 1) for _ in range(n + 1) ]
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        