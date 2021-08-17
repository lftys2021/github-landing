# 리스트 실습문제 5.2.2
a = []

# 1~7일 턱걸이 개수
x = int(input("1일차 턱걸이 횟수 >>> "))
a.append(x)
x = int(input("2일차 턱걸이 횟수 >>> "))
a.append(x)
x = int(input("3일차 턱걸이 횟수 >>> "))
a.append(x)
x = int(input("4일차 턱걸이 횟수 >>> "))
a.append(x)
x = int(input("5일차 턱걸이 횟수 >>> "))
a.append(x)
x = int(input("6일차 턱걸이 횟수 >>> "))
a.append(x)
x = int(input("7일차 턱걸이 횟수 >>> "))
a.append(x)

total = a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6]
avg = total / 7

print(int(avg))

