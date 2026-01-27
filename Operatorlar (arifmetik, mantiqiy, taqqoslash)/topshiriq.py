
## 1-topshiriq


son = int(input("Son kiriting: "))

shart1 = (son % 2 == 0) and (son > 0)
shart2 = (son % 3 == 0) or (son % 5 == 0)

print("Juft va musbatmi:", shart1)
print("3 yoki 5 ga bo‘linadimi:", shart2)
print("Ikkala shart ham rostmi:", shart1 and shart2)


## 2-topshiriq

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

print("a > b va ikkalasi musbatmi:", (a > b) and (a > 0 and b > 0))
print("a va b teng emasmi:", a != b)
print("a + b >= 100 mi:", a + b >= 100)


## 3-topshiriq

son = int(input("Son kiriting: "))

print("Toq va manfiy emasmi:", (son % 2 != 0) and (son >= 0))
print("4 ga bo‘linmaydimi:", son % 4 != 0)
print("0 emasmi:", son != 0)

## 4-topshiriq

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))

print("a < b < c:", a < b and b < c)
print("Uchala musbatmi:", a > 0 and b > 0 and c > 0)
print("Kamida bittasi juftmi:", a % 2 == 0 or b % 2 == 0 or c % 2 == 0)


## 5-topshiriq


son = int(input("Son kiriting: "))

print("10 va 50 oralig‘idami:", son >= 10 and son <= 50)
print("Juft yoki 3 ga bo‘linadimi:", son % 2 == 0 or son % 3 == 0)
print("Manfiy emasmi:", son >= 0)