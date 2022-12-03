# 6-7 위에서 아래로
import time
start_time = time.time()

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
    print(i, end=' ')


end_time = time.time()
print("time : ", end_time - start_time)
