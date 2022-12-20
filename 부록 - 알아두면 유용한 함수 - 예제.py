### 알아두면 유용한 함수 ###
# 문제 해결

#############
# > 소수 구하기

# 입력 조건
# - 첫째 줄에 자연수 M과 N이 빈칸을 사이에 두고 주어진다 (1 <= M <= N <= 1,000,000)
# - 단, M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력 조건
# - 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# import math

# m, n = map(int, input().split())
# array = [True for i in range(10000001)] # 모든 수가 소수(True)인 것으로 초기화
# array[1] = 0 # 1은 소수가 아님

# # 에라토스테네스의 체 알고리즘
# for i in range(2, int(math.sqrt(n) + 1)): # 2부터 제곱근까지 모든 수를 확인
#     if array[i] == True:    # i가 소수인경우 i를 제외한 i의 모든 배수를 제거
#         j = 2
#         while i * j <= n:
#             array[i * j] = False
#             j += 1
            
# # M 부터 N 까지의 모든 소수 출력
# for i in range(m, n + 1):
#     if array[i]:
#         print(i)
        

#############
# > 암호 만들기

# 입력 조건
# - 첫째 줄에 두 정수 L, C가 주어진다 (3 <= L <= C <= 15)
# - 다음 줄에는 C개의 문자들이 주어지며 공백으로 구분한다
# - 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다

# 출력 조건
# - 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())
array = list(map(str, input().split()))
array.sort()

for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
            
    #최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))
