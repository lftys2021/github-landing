# 반복문 실습문제 5.3.2
# 메뉴 보기

while True:
    print("[메뉴를 입력하세요]")
    x = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >>> "))

    if x == 1:
        print("-> 게임을 시작합니다.")
    elif x == 2:
        print("-> 실시간 랭킹")
    elif x == 3:
        print("-> 게임을 종료합니다.")
        break
    else:
        print("-> 다시 입력해 주세요.")
