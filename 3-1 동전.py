# 3-1 거스름돈
import time

n = int(input("거스름돈을 입력 : "))
start_time = time.time()
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)

end_time = time.time()
print("time : ", end_time - start_time)
