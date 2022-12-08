### 자료형 ###

## 집합 자료형 ##
# 중복을 허용하지 않음
# 순서가 존재하지 않음


# 집합 자료형의 초기화
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# > 잡헙 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print("합집합", a | b) # 합집합
print("교집합", a & b) # 교집합
print("차집합", a - b) # 차집합

# > 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 다중 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제 
data.remove(3)
print(data)
