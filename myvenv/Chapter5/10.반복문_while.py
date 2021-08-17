# 01. while 사용법
# - 반복 횟수가 정해지지 않았을 때 사용
# while 조건식:
#    반복할 명령
#    증감식

i = 0

while i < 10:
    print(i, "번째 다짐, 나는 할 수 있다!")
    i += 2

# 02. 무한루프
# while True:
#   반복할 명령
#   if 조건식:
#       break

while True:
    x = input("please press q for exit.....")
    if x == "q":
        break

