# 6-2 삽입 정렬
import time
start_time = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # i 부터 1까지 반복
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

end_time = time.time()
print("time : ", end_time - start_time)
