# 6-8 성적이 낮은 순서로 학생 출력
import time
start_time = time.time()

n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')

end_time = time.time()
print("time : ", end_time - start_time)
