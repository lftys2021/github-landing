# 파일 입출력 실습문제 10.1.1
import csv

def show_profit(data):
    name = data[0]
    purchase_price = int(data[1])
    amount = int(data[2])
    target_price = int(data[3])

    profit = (target_price - purchase_price) * amount
    # profit_ratio = round((target_price/purchase_price - 1) * 100, 2)
    profit_ratio = (target_price/purchase_price - 1) * 100

    print(f"{name}의 수익금 : {profit}원, 수익률 : {profit_ratio:.2f}%")

file = open("./myvenv/Chapter10/mystock.csv", "r", encoding="utf8")

reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)

file.close()

