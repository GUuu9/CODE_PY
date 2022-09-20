# 5-3 재귀함수
import time
start_time = time.time()

def recursive_funtion(i):
    if i == 100:
        return

    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_funtion(i+1)
    print(i, '번째 재귀 함수를 종료 합니다.')

recursive_funtion(1)

end_time = time.time()
print("time : ", end_time - start_time)