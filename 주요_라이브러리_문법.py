### 주요 라이브러리의 문법 ###

# 내장합수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 라이브러리
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. 순열과 조합 라이브러리를 제공한다.
# heapq : 힙 기능을 제공하는 라이르러리로 우선순위 큐 기능을 구형하기 위해 사용
# biscet : 이진 탐색 기능을 제공하는 라이브러리
# collections : 덱, 카운터등의 유용한 자료구조를 포함하고 있는 라이브러리
# math : 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리 ( 팩토리얼, 제곱근, 최대공약수 등 )

##########
# > 내장함수
# print(), input() 생략

# sum() : 객체의 모든 합을 반환

result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max() : 2개 이상의 파라미터가 들어올 경우 가장 작은, 가장 큰 값을 반환한다.
result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

# eval() : 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
result = eval("( 3 + 5 ) * 7")
print(result)

# sorted() : iterable 객체가 들어왔을 때, 정렬된 결과를 반환 key 속성으로 정렬 기준을 명시 가능.
# 리스트나 튜플
result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

# key를 사용한 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse=True)
print(result)

# 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하여 sorted() 함수를 사용하지 않아도 정렬이 가능하다.
data = [9, 1, 8, 5, 4]
data.sort()

print(data)

#############
# > itertools
# permutations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산해준다.
# 클래스 이므로 객체 초기화 이후애는 리스트 자료형으로 변환하여 사용한다.

from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# combinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산해준다.
# 클래스 이므로 객체 초기화 이후애는 리스트 자료형으로 변환하여 사용한다.
# 순서 고려의 경우 (A, B) 와 (B, A)는 동일한 내용을 포함한 것으로 이를 제외한다.

from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합
print(result)

result = list(combinations(data, 3)) # 3개를 뽑는 모든 조합 : 1가지의 경우밖에 존재하지 않음
print(result)

# product : permutation과 같은 속성으로 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산해준다.
# 원소를 중복하여 뽑는 차이가 존재한다.
# repeat 속성을 사용

from itertools import product

result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 조합
print(result)


# combinations_with_replacement : combinations 와 같은 속성으로 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산해준다.
# 원소를 중복하여 뽑는 차이가 존재한다.

from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합
print(result)

result = list(combinations_with_replacement(data, 3)) # 3개를 뽑는 모든 조합 : 중복을 허용하므로 가능한 모든 조합이 출력됨
print(result)


###########
# > heapq
# 파이썬의 힙은 최소 힙으로 구성되어 있어 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# heapq.heappush() : 힙에 원소를 삽입
# heapq.heappop() : 힙에 원소를 꺼냄

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 차례대로 삽입
    for value in iterable:
        heapq.heappush(h, value)
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    
    return(result)

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# heapq를 사용한 최대 힙 구현
# 원소의 부호를 임의로 변경하는 방식을 사용

# import heapq
def heapsort_max(iterable):
    h = []
    result = []
    
    # 모든 원소를 차례대로 힙에 차례대로 삽입
    for value in iterable:
        heapq.heappush(h, -value)
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    
    return(result)

result = heapsort_max([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


###########
# > bisect
# 2진 탐색 구현을 위해 사용한다.
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 효과적으로 사용된다.

# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 효과적으로 사용 가능하다

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))    # 4가 가장 먼저 나오는 리스트 2번 위치를 반환된다
print(bisect_right(a, x))   # 4가 가장 마지막에 나오는 리스트 4번 위치를 반환된다

# count_by_range(a, left_value, right_value) : 정렬된 리스트에서 [left_value, right_value]에 속하는 데이터의 개수를 반환한다.

# from bisect import bisect_left, bisect_right
# [left_value, right_value]의 개수를 반환 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터를 출력
print(count_by_range(a, -1, 3))


################
# > collections
# deque : 큐 구현에 사용되며 항상 O(1)의 시간복잡도를 가진다.
# 인덱싱, 슬라이싱등의 기능 사용 불가.

# popleft() : 첫 번째 원소를 제거
# pop() : 마지막 원소를 제거
# appendleft() : 첫 번째 인덱스에 원소를 삽입
# append() : 마지막 인덱스에 원소를 삽입

# 큐 구조로 이용시 원소 삽입에는 append(), 삭제에는 popleft()를 사용하면 된다.

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


# Counter : 등장 횟수를 세능 기능 제공. 해당 객체 내부의 원소가 몇 번씩 등장 했는지를 알려준다.

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(counter['red'])
print(dict(counter))    # 사전 자료형 변환


#########
# > math

import math

# 팩토리얼
print(math.factorial(5))

# 제곱근
print(math.sqrt(7))

# 최대공약수
print(math.gcd(21, 14))

# 파이 𝜋, 자연상수 e
print(math.pi)
print(math.e)
