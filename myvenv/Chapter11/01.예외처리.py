won = input("원화금액을 입력하세요 >>> ")
dollar = input("환율을 입력하세요 >>> ")

try:
    print(int(won) / int(dollar))
except ValueError as e:
    print("문자열 예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("0으로 나누는 건 불가합니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally:
    print("항상 실행되는 코드")