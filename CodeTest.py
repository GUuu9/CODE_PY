### 함수 ###

# 구조
# def 함수명(매개변수):
#     실행할 소스코드
#     retun 반환 값

# ex add
def add(a, b):
    return(a + b)

print(add(3, 7))

# return 제거
def add_Re(a, b):
    print('함수 결과', a + b)
    
add_Re(3, 7)

add_Re(b = 3, a = 11)

# 함수 밖의 데이터 변경시 global 키워드 사용
c = 0

def func():
    global c
    c += 1
    
for i in range(10):
    func()

print(c)

def add_Re_Re(a, b):
    return a + b

# 람다 표현식
print((lambda a, b: a + b)(3, 7))