# 5-2 queue
import time
start_time = time.time()

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

end_time = time.time()
print("time : ", end_time - start_time)