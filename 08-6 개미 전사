# 8-6 개미 전사
import time
start_time = time.time()

n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]

d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])

end_time = time.time()
print("time : ", end_time - start_time)
