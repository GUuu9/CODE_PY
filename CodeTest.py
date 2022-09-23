# 7-4 한줄 입력
import time
start_time = time.time()

import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

end_time = time.time()
print("time : ", end_time - start_time)
