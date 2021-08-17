money = input("현재 가진 금액을 입력 >>> ")

result = int(money)

if (result >= 20000):
    print("오늘 저녁은... 치킨!")
elif (result >= 10000):
    print("오늘 저녁은... 떡볶이!")
elif (result >= 2000):
    print("오늘 저녁은... 편의점 김밥")
else:
    print("오늘 저녁은... 그냥 굶자...")