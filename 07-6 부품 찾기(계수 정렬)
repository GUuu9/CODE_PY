# 7-6 부품 찾기(계수 정렬)
import time
start_time = time.time()

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        

end_time = time.time()
print("time : ", end_time - start_time)
