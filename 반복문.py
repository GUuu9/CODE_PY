### 반복문 ###

# > while 문
i = 1
result = 0

# i가 9보다 작거나 같을때 아래 코드를 반복 실행
# 1
while i <= 9:
    result += i
    i += 1

print(result)

# 2
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

# > for 문
# 1
result = 0

# i는 1부터 9까지 모든 값을 순회
for i in range(1, 10):
    result += i
    
print(result)

# 2
score = [90, 85, 77, 65, 97]

for i in range(5):
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격 입니다.")
        
# 3
score = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list: # 만약 리스트에 있는 학생이 부정행위라면 반복문의 처음으로 돌아간다.
        continue
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격 입니다.")
    
# 4 반복문은 중첩하여 사용가능하다.
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()
