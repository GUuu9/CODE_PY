### 자료형 ###

## 수 자료형
# > 정수형
a = 1000
print(a)

a = -7
print(a)

a = 0
print(0)


# > 실수형
# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부의 생략
a = 5.
print(a)

a = -.7
print(a)


# 지수 표현 방식
a = 1e9
print(a)

a = 752.5e1
print(a)

a = 3954e-3
print(a)


# 컴퓨터는 실수를 정확하게 표현할 수 없기에 생기는 오류
a = 0.3 + 0.6
# a = 0.8999999999999999
print(a)

if a == 0.9:
    print(True)
else:
    print(False)
    
    
# 따라서 round 함수를 사용하여 반올림 하여 계산한다.
# 코딩 테스트에서는 실수형 비교시 소수점 다섯번째 자리에서 반올림한 결과값으로 정답을 확인함.
a = 0.3 + 0.6
print(round(a,4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)
    
# > 수 자료형의 연산
a = 7
b = 3

#나누기
print(a / b)
#나머지
print(a % b)
#몫
print(a // b)
#제곱연산
print(a ** b)