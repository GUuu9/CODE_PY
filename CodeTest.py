### 알아두면 유용한 함수 ###

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