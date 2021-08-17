# 클래스 실습문제 8.1.1
class items:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.weight = weight
        self.price = price
        self.isdropable = isdropable
    def sale(self):
        print(f"{self.name}을(를) {self.price}에 판매 가능합니다.")
    def discard(self):
        if self.isdropable:
            print(f"{self.name}을(를) 버렸습니다.")
        else:
            print(f"{self.name}을(를) 버릴 수 없습니다.")

class WearableItem(items):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"{self.name}을(를) 착용했습니다. {self.effect}")
class UsableItem(items):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"{self.name}을(를) 사용했습니다. {self.effect}")

sword = WearableItem("이가닌자의 검", 30000, 3.5, True, "체력 5000증가, 마력 5000증가")
sword.wear()
sword.sale()
sword.discard()

potion = UsableItem("신비한투명물약", 150000, 0.1, False, "투명효과 300초 지속")
potion.discard()
potion.sale()
potion.use()
