# 실습문제 4.3.1
# 사용자로부터 두개의 숫자를 입력 받고,
# 더한 결과를 출력하기

x = input("첫번째 숫자를 입력하세요 >>>")
y = input("두번째 숫자를 입력하세요 >>>")

print(type(x)) 
print(type(y))
result = int(x) + int(y)
print(result)