# 함수 실습문제 6.1.1
# 두 수의 곱
def multiply(x, y):
    """
    두 수의 곱셈 결과를 반환하는 함수
    """
    result = x * y
    return result

print(multiply(4, 6))

# 함수 실습문제 6.1.2
# 세 개의 정수를 인자로 합계와 평균을 출력해주는 함수
def printSumAvg(x, y, z):
    """
    세 수의 합계와 평균을 출력해주는 함수
    """
    total = x + y + z
    avg = total / 3
    print(f"세 수의 합계는 {total}, 평균은 {int(avg)}")

printSumAvg(10, 20, 30)