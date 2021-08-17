result=[33,40,12,63,52]

# 1. 6번의 팔굽혀펴기 개수는 9개
# 리스트의 마지막에 추가하자.
print("1. 리스트 마지막에 추가하기")
result.append(9)
print(result)
print("\n")

# 2. 2번은 재측정하여 50개를 하였다.
# 2번의 데이터를 변경해 보자
print("2. 리스트 데이터 변경")
result[1] = 50
print(result[1])
print("\n")

# 3. 3번부터 6번까지의 데이터를 슬라이싱하기.
print("3. 데이터 슬라이싱")
print(result[2:6])
print("\n")

# 4. 모든 데이터를 오름차순으로 정렬하자.
print("4. 데이터 정렬")
result.sort()
print(result)
print("\n")

