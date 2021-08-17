kor = int(input("국어 >>> "))
mat = int(input("수학 >>> "))
eng = int(input("영어 >>> "))

ave = (kor + mat + eng) / 3

if ((kor <= 0 or kor > 100) or (mat <= 0 or mat > 100) or (eng <= 0 or eng > 100)):
    print("잘못 입력하였습니다.")
else:
    if (ave >= 80):
        print("불합격")
    else:
        print("합격")