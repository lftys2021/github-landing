# 기본형
def printHello():
    print("Hello")

printHello()

# 매개변수가 있는 함수
def sum(a, b):
        print(a + b)

sum(3, 4)

# 반환값이 있는 함수
import random
def getRandomNumber():
    number = random.randint(1, 18)
    return number

print(getRandomNumber())

# 매개변수와 반환값이 있는 함수
def add(a, b):
    result = a + b
    return result

print(add(5, 6))