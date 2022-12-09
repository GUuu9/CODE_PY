### 알아두면 유용한 함수 ###

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
