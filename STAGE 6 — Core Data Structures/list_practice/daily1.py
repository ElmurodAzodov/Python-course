
# mevalar = ["olma", ["nashvati", "limon"], "anor", "uzum", "banan", "mandarin"]
# aralash = [1, 2, 3.4, 8/2, True, False, None, "birnarsa"]
# bosh_list = []
# ism = "Hurmatbek"
# ism_list = list(ism)
# mevalar[0] = [i for i in range(10)]
# print(mevalar)
# print(mevalar[0])
# print(mevalar[4])
# print(mevalar[-5])
# print(mevalar[1][0])

# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sonlar1 = [i for i in range(1, 11) if i % 2 == 0]
# l = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         l.append(i)

# print(sonlar1)
# print(l)

# print(mevalar)
# print(aralash)
# print(ism_list)




#* List comprehension usulida bajaring:

#& 0dan 100gacha sonlarni chiqaring

#& 0dan 100gacha bo'lgan sonlar orasidan juft sonlarni chiqaring

#& 0dan 100gacha bo'lgan sonlar orasidan toq sonlarni chiqaring

#& 0dan 100gacha bo'lgan sonlar orasidan 3 va 5 ga bo'linadigan sonlarni chiqaring

#& 0dan 100gacha bo'lgan sonlar orasidan 7 va 3 ga bo'linadigan 
#& sonlarning yig'indisini chiqaring


# ==============================================================================================================
# ==============================================================================================================
# ==============================================================================================================

#* Methods

oquvchilar = ["Dastonbek", "Jahongir", "Hurmatbek", "Abrorbek", "Shoxruzbek", "Boburjon", "Sherzodbek"]

#^ .append() - oxiriga faqat bitta element qo'shadi
oquvchilar.append("Behruz")

#^ .extend() - oxiriga bir nechta element qo'shadi, [] lar ichida yoziladi
oquvchilar.extend(["Marjona", "Mohira", "Dilobar"])

#^ .insert()
oquvchilar.insert(0, "Nuraddin")
oquvchilar[0] = "Nurbek"
print(oquvchilar)