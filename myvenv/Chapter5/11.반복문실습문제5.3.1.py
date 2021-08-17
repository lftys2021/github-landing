# 반복문 실습문제 5.3.1
# 구구단 출력 문제

x = int(input("몇 단을 출력할까요? >>> "))
for i in range(1, 20):
    result = x * i
    print(x, " * ", i, " = ", result)

