### 입출력 ###

# > 입력을 위한 일반적인 소스 코드
# 입력받을 데이터 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))
data.sort(reverse = True)

print(data)


# > 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 입력 개수가 많은 경우 input 대신 sys 라이브러리의 sys.stdin.readline()을 사용한다
# import sys
# sys.stdin.readline().rstrip()  /  rstrip()은 공백문자제거

import sys
data = sys.stdin.readline().rstrip()
print(data)

# 변수 출력
a = 1
b = 2

print(a, b)

# 줄바꿈

print(a)
print(b)

# 변수를 문자열로 변환하여 출력
answer = 7

# print("입력 값은 " + answer) 오류발생.
print("입력 값은 " + str(answer))

# ,로 변수를 구분하여 출력 (콤마 사이마다 띄어쓰기 발생)
print("입력 값은", answer)

# f-string (python3.6 이상)
# 문자열 앞에 접두사 f를 붙히고 {}를 통해 변수 삽입가능
print(f"입력 값은 {answer}")
