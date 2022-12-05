### 자료형 ###

## 문자열 자료형 ##
# > 문자열 초기화 #
data = 'Hello Wolrd'
print(data)

data = "Don't you Know \"Python\"?"
print(data)

# > 문자열 연산 #
a = "Hello"
b = "World"

print(a + " " + b)

## 튜플 자료형 ##
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 []를 사요하지만 튜플은 ()을 사용
a = (1, 2, 3, 4)
print(a)

#a[2] = 7
# 위 코드에서는 튜플 전체가 출력이 되며 튜플 내의 값을 변경에는 오류가 발생된다.

## 사전 자료형 ##
## : 딕셔너리
# 키값 - 데이터 구조
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print('사과를 키값으로 가지는 데이터가 존재')

# 해당 기능은 튜플이나 리스트에서도 사용이 가능하다.

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