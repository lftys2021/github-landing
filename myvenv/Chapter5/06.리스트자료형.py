animals = ["가물치", "벼메뚜기", "비단뱀", "도마뱀"]

empty = []

# 2. 리스트 조작하기

# - 데이터 접근하기
# 인덱스틑 0부터 시작
print(animals[2])
print(animals[-1])

# 데이터 추가
animals.append("고라니")
print(animals[2])
print(animals[-1])

# 데이터 할당하기
animals[1] = "청개구리"
print(animals[1])

# 데이터 삭제하기
del animals[0]
print(animals)

# 리스트 슬라이싱
print(animals[1:3])
print(animals[1,3])
print(animals[:])

# 리스트 길이
print(len(animals))

# 리스트 정렬
animals.sort()
print(animals)