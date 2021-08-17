import random

lotto = []

while True:
    print("로또 번호 만들기")
    select = int(input("1. 중복 허용 2. 중복 불허 3. 종료 >>> "))
    
    def get_Random_Number():
        number = random.randint(1, 45)
        return number

    if select == 1:
        # 중복 허용
        for i in range(6):
            ran_Num = int(get_Random_Number())
            lotto.append(ran_Num)

        lotto.sort()

        for j in lotto:
            print(j, end = " ")
        print("\n")
    elif select == 2:
        # 중복 불허
        count = 0

        while True:
            if count == 6:
                break

            ran_Num = int(get_Random_Number())
            
            if ran_Num not in lotto:
                lotto.append(ran_Num)
                count += 1

        lotto.sort()

        for j in lotto:
            print(j, end = " ")
        print("\n")
    elif select == 3:
        print("종료합니다.")
        break
    else:
        print("다시 선택하십시오.")
    
    lotto.clear()
