# 7-7 부품 찾기(집합 자료형)
import time
start_time = time.time()

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')


end_time = time.time()
print("time : ", end_time - start_time)
