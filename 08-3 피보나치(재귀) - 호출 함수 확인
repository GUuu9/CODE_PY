# 8-3 피보나치(재귀) - 호출 함수 확인
import time
start_time = time.time()

d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')

    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = pibo(x - 1) + pibo(x - 2)
    
    return d[x]

pibo(6)

end_time = time.time()
print("time : ", end_time - start_time)
