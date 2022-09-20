# 4-2 시각
# 00시부터 n시 59분 59초까지 3이 들어가는 갯수 확인
import time
start_time = time.time()

n = int(input())

count = 0
for i in range(n + 1):      # 시
    for j in range(60):     # 분 
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

end_time = time.time()
print("time : ", end_time - start_time)