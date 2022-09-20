# 5-4 재귀함수를 통한 팩토리얼
import time
# start_time = time.time()


# 반복
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    
    return result

# 재귀
def factorial_recursive(n):
    if n <= 1:
        return 1
    
    return n * factorial_recursive(n-1)

# end_time = time.time()
# print("time : ", end_time - start_time)


start_time = time.time()
print('반복', factorial_iterative(5))
end_time = time.time()
print("time : ", end_time - start_time)

start_time = time.time()
print('재귀', factorial_recursive(5))
end_time = time.time()
print("time : ", end_time - start_time)
