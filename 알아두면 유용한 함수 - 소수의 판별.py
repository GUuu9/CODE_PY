### 알아두면 유용한 함수 ###

#############
# > 소수의 판별

def is_prime_number(x):
    # 2부터 (x-1)까지 모든 수를 확인
    for i in range(2, x):
        # x 가 해당 수로 나누어 떨어지는지 판별
        if x % i == 0:
            return False # 소수가 아님
    return True          # 소수

print(is_prime_number(4))
print(is_prime_number(7))

# 해당 방법의 시간 복잡도는 O(x)이다.

# 자연수의 약수 성질을 활용하여 소수 판별( 제곱근 까지만 확인 하면 소수 판별 가능 )
# 해당 방법 수행시 시간 복잡도는 O(X^1/2)로 처리 할 수 있다.

import math

def is_prime_number_sqrt(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True          # 소수

print(is_prime_number_sqrt(4))
print(is_prime_number_sqrt(7))


# 다중 소수를 찾는 경우 에라토스테네스의 체를 사용한다.
# N 보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

# 1. 2부터 N 까지 모든 자연수를 나열한다.
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다
# 3. 남은 수 중에서 i의 배수를 모드 제거한다(i 는 제거하지 않음)
# 4. 더이상 반복할 수 없을 때 까지 2, 3을 반복한다.

# import math

n = 1000 # 판별 범위
array = [True for i in range(n+1)] # 처음에는 0과 1을 제외하고 모든 수가 소수(True) 인것으로 초기화

for i in range(2, int(math.sqrt(n))):
    if array[i] == True: # i가 소수(True)인 경우( 남은 수인 경우 ) i를 제외한 모든 배수를 지우기
        # i를 제외한 모든배수를 지움 True -> False
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
