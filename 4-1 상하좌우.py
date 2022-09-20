# 4-1 상하좌우
import time
start_time = time.time()

n = int(input())
x, y = 1, 1
tours = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for tour in tours:
    for i in range(len(move_types)):
        if tour == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > y:
        continue
        
    x, y = nx, ny

print(x, y)

end_time = time.time()
print("time : ", end_time - start_time)
