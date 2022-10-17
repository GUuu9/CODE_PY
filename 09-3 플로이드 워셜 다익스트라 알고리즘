# 9-3 플로이드 워셜 다익스트라 알고리즘
from multiprocessing import heap
import time
start_time = time.time()

INF = int(1e9) # 무한을 의미하는 값을 설정(10억)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        
        else:
            print(graph[a][b], end=" ")
    print()

end_time = time.time()
print("time : ", end_time - start_time)
