try:
    num = int(input("음슈룰 압룍허요 주세요 >>>"))
    if num >= 0:
        raise Exception("양수 입력 불가")
except Exception as e:
    print("에러 발생! 양수 입력!")
