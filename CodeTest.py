### 자료형 ###

## 리스트 자료형 ##
# > 리스트 생성 #
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 원소 접근
print(a[4])

# 빈 리스트 선언방법 1
a = list()
print(a)

# 빈 리스트 선언방법 2
a = []
print(a)

# 크기가 N 이고, 모든 값이 0 인 1차원 리스트 초기화
N = 10
a = [0] * N
print(a)

# > 리스트의 인덱싱과 슬라이싱 #
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫번째 원소 출력
print(a[-1])

# 뒤에서 세번째 원소 출력
print(a[-3])

# 네번째 원소값 변경
a[3] = 7
print(a)

# 두번째 원소부터 네번째 원소까지 출력
print(a[1:4])

# > 리스트 컴프리헨션 #
# 0 부터 19까지 홀수만 포함하는 리스트 
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지 수의 제곲값을 저장하는 리스트
array = [i * i for i in range(1,10)]
print(array)

# n * m 크기의 2차원 리스트 초기화
n, m = 3, 4
array = [[0] * m for _ in range(n)]
print("2차원 리스트 초기화", array)

# 리스트 컴프리헨션을 사용해야 하는 이유
# 의도이 않은 잘못된 결과값이 나올 수 있다.
n, m = 3, 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print("잘못된 결과값" , array)

# > 리스트 관련 기타 매서드
# append()  / 리스트에 원소를 하나 삽입할 때 사용한다. / O(1)
# sort()    / 기본 정렬 기능으로 오름차순으로 정렬한다. / O(NlogN)
# sort(reverse = True) / 내림차순으로 정렬
# reverse() / 리스트의 원소 순서를 역순으로 정렬한다.   / O(N)
# insert()  / 특정한 인덱스 위치에 원소를 삽일할때 사용. / O(N)
# count()   / 리스트에서 특정한 값을 가지는 데이터의 개수를 센다.   / O(N)
# remove()  / 특정한 값을 갖는 원소를 제거하는데 값을 가진 원소가 여러개면 하나만 제거한다 / O(N)

a = [1, 4, 3]
print("rl기본 리스트 :", a)

# 리스트에 원소를 삽입
a.append(2)
print("삽입 :", a)

# 오름차순 내림차순 정렬
a.sort()
print("오름차순 청렬 :", a)

a.sort(reverse=True)
print("내림차순 청렬 :", a)

# 리스트 뒤집기
a.reverse()
print("원소 뒤집기 :", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3추가 :", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 :", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제 :", a)


# 시간복잡도에 따른 리스트 삭제법
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)