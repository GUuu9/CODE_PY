### 조건문 ###

## 비교연산자 
# X == Y    / X와 Y가 서로 같을때 True
# X != Y    / X와 Y가 서로 다를때 True
# X > Y     / X가 Y보다 클 때 True
# X < Y     / X가 Y보다 작을 때 True
# X >= Y    / X가 Y보다 크거나 같을 때 True 
# X <= Y    / X가 Y보다 작거나 같을 때 True

## 논리 연산자
# X and Y   / X와 Y가 모두 True일때 True
# X or Y    / X와 Y중에 하나라도 True이면 True
# not X     / X가 거짓일 때 True

## 기타 연산자
# X in 리스트 / 리스트 안에 X가 들어가 있을 때 True
# X not in 리스트  / 리스트 안에 X가 들어가 있지 않을 때 True

# 1
x = 15

if x >= 10:
    print(x)

# 2    
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('F')
    
# 3
score = 85


if score >= 70: # 해당되는 코드는 모두 실행
    print('70점 이상')
    if score >= 80:
        print('80점 이상')
        if score >= 90:
            print('90점 이상')
            
else:
    print('성적 저조')
    
print('조건문 밖에 있어 무조건 실행되는 코드')

# 4
score = 85

if score >= 80:
   pass # pass를 사용하면 조건문만 생성해 두고 처리 부분은 비워둘 수 있다.
else:
   print('성적 저조')

# 5
score = 85

if score >= 80: result = "Success"
else: result = "Fail"

print(result)
