# 생성자
# : 인스턴스를 만들 때 호출되는 메서드

class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        print(f"{name}의 체력 : {health}, 공격력 : {attack}, 스피드 : {speed}")
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health

goblin = Monster("고블린", 800, 120, 300)
goblin.decrease_health(200)
print(goblin.name, "의 남은 체력 : ", goblin.get_health())

wolf = Monster("늑대", 1500, 200, 350)
wolf.decrease_health(120)
print(wolf.name, "의 남은 체력 : ", wolf.get_health())