# 상속
# : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해 사용
import random

class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] 지상에서 달려서 이동하기")

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): #메서드 오버라이딩
        print(f"[{self.name}] 바다에서 헤엄쳐서 이동하기.")

class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")
    def move(self): #메서드 오버라이딩
        print(f"[{self.name}] 하늘에서 날아다니며 이동하기.")
    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[int(random.randint(0,2))]}")


wolf = Wolf("늑대", 1500, 200)
shark = Shark("상어", 2000, 300)
dragon = Dragon("드래곤", 5000, 600)

wolf.move()
print(wolf.max_num)

shark.move()
print(shark.max_num)

dragon.move()
dragon.skill()
print(dragon.max_num)


