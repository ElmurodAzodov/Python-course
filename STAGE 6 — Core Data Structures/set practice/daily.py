
#* Set
sonlar = {1, 2, 3, 4, 5, 6, 7, 8}
sonlar1 = [1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, "10", "10"]
ismlar = ["Abrorbek", "Hurmatbek", "Shoxruzbek", "Abrorbek"]
setga_ogirish = set(sonlar1)
setga_ogirish1 = set(ismlar)

sonlar.add(2)
sonlar.update([11, 22, 33])
# sonlar.pop()
sonlar.clear()
# sonlar.remove(33)
# sonlar.discard(34) # bu ham ochiradi lekin mos qiymat bolmasa xatolik bermaydi
print(sonlar)
# print(sonlar)
# print(setga_ogirish)
# print(setga_ogirish1)
# print(type(sonlar))