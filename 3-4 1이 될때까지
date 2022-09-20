# 3-4 1이 될때까지
import time
start_time = time.time()

n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)

print(result)

end_time = time.time()
print("time : ", end_time - start_time)


# 이하 코드는 동작하나 값이 커지면 처리시간이 증하한다.
# n, k = map(int, input().split())

# result = 0

# while n != 1:
#     if (n % k == 0):
#         n = n // k
#     else:
#         n -= 1   
#     result += 1

# print(result)
