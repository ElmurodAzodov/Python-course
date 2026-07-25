"""
📋 PYTHON LIST VA UNING METODLARI — MASHQLAR TO'PLAMI
=======================================================
Jami: 50 ta topshiriq
🟡 O'rtacha daraja: 30 ta (1-30)
🔴 Qiyin daraja: 20 ta (31-50)

Har bir topshiriq ostiga o'z yechimingizni yozing.
Test qilish uchun print() dan foydalaning.
"""


# ============================================================
# 🟡 O'RTACHA DARAJA (1-30)
# ============================================================

# 1. Berilgan list: [12, 45, 3, 67, 23, 1, 89]
# Listni o'sish tartibida saralang (sort() metodi bilan)


# 2. Yuqoridagi listni kamayish tartibida saralang


# 3. ["olma", "banan", "uzum", "nok"] listiga "shaftoli" ni oxiriga qo'shing (append)


# 4. Xuddi shu listning boshiga "gilos" ni qo'shing (insert)


# 5. list dan "banan" so'zini o'chiring (remove)


# 6. [10, 20, 30, 40, 50] listining oxirgi elementini pop() bilan chiqarib oling
# va uni alohida o'zgaruvchida saqlang


# 7. Xuddi shu listning 0-indeksidagi elementini pop(0) bilan olib tashlang


# 8. [5, 3, 8, 3, 9, 3, 2] listida 3 soni nechta marta uchrashini count() bilan toping


# 9. ["a", "b", "c", "d", "e"] listida "c" elementining indeksini index() bilan toping


# 10. [1, 2, 3] va [4, 5, 6] listlarini extend() yordamida birlashtiring


# 11. [1, 2, 3, 4, 5] listini reverse() bilan teskari tartibga o'tkazing


# 12. Berilgan listni clear() bilan tozalang: [1, 2, 3]


# 13. [10, 20, 30] listining nusxasini copy() bilan yarating va nusxaga 40 qo'shing
# (asl list o'zgarmasligiga ishonch hosil qiling)


# 14. 1 dan 10 gacha bo'lgan sonlar listini range() va list() yordamida yarating


# 15. ["mushuk", "it", "quyon"] listidan slicing yordamida faqat birinchi ikkitasini oling


# 16. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] listidan slicing bilan faqat juft indeksdagi
# elementlarni oling (masalan [::2])


# 17. [1, 2, 3, 4, 5] listini slicing yordamida teskari tartibda chiqaring ([::-1])


# 18. Ikkita list: ["ism1", "ism2"] va [25, 30] — bularni zip() yordamida
# lug'atga (dict) aylantiring


# 19. [3, 1, 4, 1, 5, 9, 2, 6] listidagi eng katta va eng kichik sonlarni
# max() va min() bilan toping


# 20. Yuqoridagi listdagi barcha sonlar yig'indisini sum() bilan hisoblang


# 21. ["olma", "banan", "gilos"] listining uzunligini len() bilan toping


# 22. [1, 2, 3] listi ichida 5 soni bor yoki yo'qligini "in" operatori bilan tekshiring


# 23. List comprehension yordamida 1 dan 20 gacha bo'lgan juft sonlar listini tuzing


# 24. List comprehension yordamida 1 dan 10 gacha sonlarning kvadratlari listini tuzing


# 25. ["Ali", "vali", "HASAN", "guli"] listidagi barcha so'zlarni katta harfga
# aylantiruvchi yangi list yarating (list comprehension bilan)


# 26. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] listidan faqat 5 dan katta sonlarni
# list comprehension bilan ajratib oling


# 27. Bo'sh list yarating va foydalanuvchidan (yoki o'zingiz belgilagan)
# 5 ta son kiritib, ularni append() bilan listga qo'shing


# 28. [1, [2, 3], [4, [5, 6]]] — ichma-ich (nested) list yarating va
# indekslash orqali 6 raqamiga yeting


# 29. ["non", "sut", "tuxum"] va ["yog'", "guruch"] listlarini "+" operatori
# yordamida birlashtiring (extend() ishlatmasdan)


# 30. [5, 2, 8, 1, 9] listini sort() metodi bilan, lekin reverse=True parametri
# bilan kamayish tartibida saralang


# ============================================================
# 🔴 QIYIN DARAJA (31-50)
# ============================================================

# 31. Berilgan list: [4, 2, 7, 2, 9, 4, 1, 7, 9, 3]
# Listdan takrorlanmagan (unique) elementlardan iborat yangi list tuzing,
# lekin dastlabki tartibni saqlab qoling (set() ishlatmasdan, faqat list bilan)


# 32. [[1, 2, 3], [4, 5], [6, 7, 8, 9]] — nested listni bitta tekis (flat)
# listga aylantiring: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# (list comprehension yoki nested loop bilan)


# 33. [10, 20, 30, 40, 50] va [1, 2, 3, 4, 5] listlarini elementma-element
# qo'shib, yangi list hosil qiling: [11, 22, 33, 44, 55]
# (zip() yordamida, "+" operatorisiz)


# 34. ["Alisher", "Bobur", "Cho'lpon", "Dilshod"] listini har bir ismning
# uzunligiga qarab saralang (sort() ning key parametri bilan, len funksiyasidan foydalaning)


# 35. [{"ism": "Ali", "yosh": 25}, {"ism": "Vali", "yosh": 20}, {"ism": "Guli", "yosh": 30}]
# listini "yosh" kaliti bo'yicha o'sish tartibida saralang (key=lambda ishlatib)


# 36. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] listini 3 tadan bo'laklarga (chunk) bo'ling:
# natija: [[1,2,3], [4,5,6], [7,8,9], [10]]


# 37. [3, 6, 9, 12, 15] va [2, 4, 6, 8] listlarining kesishmasini
# (ikkalasida ham bo'lgan elementlarni) toping, faqat list va loop bilan (set ishlatmasdan)


# 38. Matritsa (2 o'lchamli list) berilgan: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Uni transponirlang (qatorlarni ustunga aylantiring):
# natija: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# 39. [5, 1, 4, 2, 8, 3] listini o'zingiz yozgan bubble sort algoritmi bilan
# saralang (Python ning sort() metodidan foydalanmasdan)


# 40. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] listida eng katta ikkinchi sonni
# (max() ni ikki marta chaqirmasdan, bitta o'tishda) toping


# 41. Berilgan gap: "Bu yerda ba'zi so'zlar takrorlanmoqda va ba'zi so'zlar takrorlanmoqda"
# Gapni so'zlarga bo'ling (split) va har bir so'z nechta marta takrorlanganini
# lug'at (dict) shaklida chiqaring — faqat list va dict bilan (Counter ishlatmasdan)


# 42. [1, 2, 3] listining barcha mumkin bo'lgan qism to'plamlarini (subsets)
# hosil qiling: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]


# 43. [1, 2, 3] va ["a", "b", "c"] listlaridan barcha mumkin bo'lgan
# juftliklarni (Cartesian product) hosil qiling: [(1,"a"), (1,"b"), ... ]
# (itertools ishlatmasdan, faqat nested loop bilan)


# 44. [10, 22, 9, 33, 21, 50, 41, 60] listidan eng uzun o'sib boruvchi
# ketma-ketlik (longest increasing subsequence) uzunligini toping


# 45. Berilgan list: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# Har bir elementning nechta marta takrorlanganini ko'rsatuvchi
# [(element, soni), ...] ko'rinishidagi list tuzing, lekin elementlar
# birinchi marta uchragan tartibda bo'lsin


# 46. [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] listidan medianasini (o'rtacha qiymatini)
# sort() dan foydalanib, lekin statistics moduli ishlatmasdan hisoblang


# 47. Ikkita saralangan list: [1, 3, 5, 7] va [2, 4, 6, 8] — bularni
# bitta saralangan listga birlashtiring, lekin sort() ishlatmasdan,
# "merge" algoritmi (ikkita pointer) yordamida


# 48. [1, 2, 3, 4, 5] listining barcha elementlarini o'zaro almashtirib
# (permutations) chiqing — itertools ishlatmasdan, rekursiya yordamida
# (kichik list, masalan uzunligi 3 bo'lgan list bilan sinab ko'ring)


# 49. Katta list: list(range(1, 1000001)) — bu listdan faqat 7 ga qoldiqsiz
# bo'linadigan va 3 ga bo'linganda qoldiq 1 chiqadigan sonlarni
# list comprehension bilan samarali tarzda ajratib oling (birinchi 20 tasini chiqaring)


# 50. O'zingiz "Stack" (steK) tuzilmasini oddiy Python list yordamida amalga oshiring:
# push(list, element), pop(list), peek(list), is_empty(list) funksiyalarini yozing
# va ularni sinab ko'ring