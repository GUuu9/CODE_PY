### 알아두면 유용한 함수 ###

#############
# > 투 포인터
# 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 기법

# 특정 합을 가지는 부분 연속 수열 찾기
# 1. start 와 end가 첫번째 원소의 인덱스(0)를 가리키도록 한다.
# 2. 현재 부분합이 M과 같다면 카운트한다.
# 3. 현재 부분이 M보다 작으면 end를 1 증가시킨다.
# 4. 현재 부분이 M보다 크거나 같으면 start를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2 ~ 4 과정을 반복한다.

# 사전에 정렬된 리스트 A 와 B 선언
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A 와 B 의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * ( n + m )
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
    # 리스트 B 의 모든 원소가 처리되었거나, 리스트 A 의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 A 의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    # 리스트 A 의 모든 원소가 처리되었거나, 리스트 B 의 원소가 더 작을 때
    else:
        # 리스트 B 의 원소를 결과 리스트로 옮기기
        result[k] = b[j]
        j += 1
    k += 1
    
# 결과 리스트 출력
for i in result:
    print(i, end=' ')
    

#############
# > 구간 합 계산
# 연속적으로 나열된 N 개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구한다.

# 1. N개의 수에 대하여 접두사 합(Prefix Sum)을 계산하여 배열 P에 저장한다.
# 2. 매 M갸의 쿼리 정보[L, R]을 확인할 때 구간 합은 P[R] - P[L - 1]이다.

# 접두사 합을 활용한 구간 합 계산
# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산 
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
# 구간 합 계산( 예시 : 3번째 부터 네번째 수까지)
left = 3    # 시작 구간
right = 4   # 종료 구간
print(prefix_sum[right] - prefix_sum[left - 1])

#############
# > 순열과 조합

# permutation : 순열 - 서로다른 N 개에서 r개를 선택하여 일렬로 나열하는 것
# permutations()는 리스트 형태가 아니기 때문에 list()함수로 변환한다.

import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))
    
# combination : 조합 - 서로다른 N 개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
# 마찬가지로 list()로 변환하여 사용

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')