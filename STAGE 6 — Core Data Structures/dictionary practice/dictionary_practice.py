# ====================================================
#* PYTHON DICTIONARIES — 60 TA TOPSHIRIQ
# ====================================================

# 🟢 1–20: O‘RTA DARAJADAGI TOPSHIRIQLAR
# ----------------------------------------------------

# 1 Dictionarydagi barcha value’lar yig‘indisini toping.

# dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# l = list(dict1.values())
# yigindi = 0
# for i in l:
#     yigindi += i
# print(yigindi)

# 2 Dictionarydagi barcha keylarni alohida listga o‘tkazing.

# dict2 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# keylar_royxati = list(dict2.keys())
# print(keylar_royxati)

# 3 Dictionarydagi barcha value’larni alohida listga o‘tkazing.

# dict3 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# value_royxati = list(dict3.values())
# print(value_royxati)

# 4 Value’si eng katta bo‘lgan keyni toping.

# dict4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# l = list(dict4.items())
# max = 0
# key = []
# for i in l:
#     if i[1] > max:
#         max = i[1]
# for i in l:
#     if i[1] == max:
#         key.append(i[0])
# print(max)
# print(key)
# ------------------------------------
# max_val = 0
# keys = []

# for k, v in dict4.items():
#     if v > max_val:
#         max_val = v
#         keys = [k]
#     elif v == max_val:
#         keys.append(k)

# print(max_val)
# print(keys)

# 5 Value’si eng kichik bo‘lgan keyni toping.

# dict4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# min_val = float('inf')   # Eng katta boshlang'ich qiymat
# keys = []

# for k, v in dict4.items():
#     if v < min_val:
#         min_val = v
#         keys = [k]
#     elif v == min_val:
#         keys.append(k)

# print("Eng kichik qiymat:", min_val)
# print("Shu qiymatga ega key:", keys)

# 6 Dictionarydan faqat juft value’larni saqlab qoling.

# my_dict = {'a': 10, 'b': 15, 'c': 20, 'd': 25, 'e': 30, 'f': 35, 'g': 40}
# juft_dict = {key: value for key, value in my_dict.items() if value % 2 == 0}

# print(f"Asl dictionary: {my_dict}")
# print(f"Faqat juft value'li dictionary: {juft_dict}")

# 7 Dictionarydagi barcha value’larni 2 ga ko‘paytirib yangi dictionary yarating.

# dict1 = {'a': 5, 'b': 10, 'c': 15}

# new_dict = {k: v * 2 for k, v in dict1.items()}

# print(new_dict)

# 8 Ikkita dictionaryni bitta dictionaryga birlashtiring (update() ishlatmasdan).

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# merged = {**dict1, **dict2}
# print(merged)
# # ---------------------------------
# merged = {}

# for d in (dict1, dict2):
#     for k, v in d.items():
#         merged[k] = v

# print(merged)

# 9 Dictionaryda foydalanuvchi kiritgan key bor yoki yo‘qligini tekshiring.

# dict1 = {'name': 'Ali', 'age': 20, 'city': 'Tashkent'}

# key = input("Key kiriting: ")

# if key in dict1:
#     print("Bor")
# else:
#     print("Yo'q")

# 10 Dictionarydan eng uzun keyni aniqlang.

# dict1 = {'apple': 10, 'banana': 20, 'kiwi': 5}

# longest_key = max(dict1, key=len)

# print("Eng uzun key:", longest_key)

# 11 Dictionarydagi value’lar ichidan string bo‘lganlarini toping.

# dict1 = {'a': 10, 'b': "hello", 'c': 25, 'd': "world"}

# for k, v in dict1.items():
#     if isinstance(v, str):
#         print(k, v)

# 12 Dictionarydagi value’lar ichidan int bo‘lganlarini toping.

# dict1 = {'a': 10, 'b': "hello", 'c': 25, 'd': "world"}

# for k, v in dict1.items():
#     if isinstance(v, int):
#         print(k, v)

# 13 Dictionarydagi barcha elementlarni for loop orqali chiqarib bering.

# dict1 = {'a': 10, 'b': "hello", 'c': 25, 'd': "world"}

# for k, v in dict1.items():
#     print("Key:", k, "| Value:", v)

# 14 Dictionarydagi elementlar sonini len() ishlatmasdan toping.

# dict1 = {'a': 10, 'b': "hello", 'c': 25, 'd': "world"}

# count = 0
# for _ in dict1:
#     count += 1

# print("Elementlar soni:", count)

# 15 Dictionarydan value’si 10 dan katta bo‘lgan elementlarni ajrating.

# dict1 = {'a': 5, 'b': 12, 'c': 7, 'd': 20}

# result = {k: v for k, v in dict1.items() if v > 10}
# print(result)

# 16 Dictionarydagi barcha keylarni katta harflarga o‘tkazing.

# dict1 = {'a': 5, 'b': 12, 'c': 7, 'd': 20}
# result = {k.upper(): v for k, v in dict1.items()}
# print(result)


# 17 Dictionarydagi barcha value’larni string ko‘rinishga o‘tkazing.

# dict1 = {'a': 5, 'b': 12, 'c': 7, 'd': 20}
# result = {k: str(v) for k, v in dict1.items()}
# print(result)


# 18 Dictionarydan faqat value’lari unikal bo‘lgan elementlarni toping.

# dict1 = {'a': 5, 'b': 12, 'c': 7, 'd': 20}
# result = {k: v for k, v in dict1.items() if list(dict1.values()).count(v) == 1}
# print(result)

# 19 Dictionarydan tasodifiy bitta elementni o‘chiring.
# import random

# import random

# dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# key = random.choice(list(dict1.keys()))
# del dict1[key]

# print(dict1)

# 20 Dictionarydan nusxa (copy) olib, original o‘zgarmasligini tekshiring.

# dict1 = {'a': 1, 'b': 2, 'c': 3}

# copy_dict = dict1.copy()

# copy_dict['d'] = 4

# print("Original:", dict1)
# print("Copy:", copy_dict)

# ----------------------------------------------------
# 🔴 21–40: QIYIN TOPSHIRIQLAR
# ----------------------------------------------------

# 21 Dictionarydagi value’larning chastotasini hisoblang.

# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# freq = {}

# for v in d.values():
#     if v in freq:
#         freq[v] += 1
#     else:
#         freq[v] = 1

# print(freq)

# 22 Dictionaryni value’lar bo‘yicha o‘sish tartibida saralang.

# d = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

# sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))

# print(sorted_dict)

# 23 Dictionaryni value’lar bo‘yicha kamayish tartibida saralang.

d = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)

# 24 Ikkita dictionarydagi bir xil keylarning value’larini qo‘shing.

# 25 Dictionary ichida dictionary bo‘lsa, barcha sonlarning yig‘indisini toping.

# 26 Nested dictionaryni tekis (flat) dictionaryga aylantiring.

# 27 Dictionarydan faqat hashable value’li elementlarni ajrating.

# 28 Dictionarydagi value’lari palindrom bo‘lgan keylarni toping.

# 29 Dictionary ichidagi tuple value’lardan eng katta sonni toping.

# 30 Dictionaryni key uzunligi bo‘yicha saralang.

# 31 Dictionarydagi barcha key-value juftliklarini teskari qilib yangi dictionary yarating.

# 32 Dictionarydan value’lari list bo‘lgan elementlarni ajrating.

# 33 Dictionaryda nechta unique value borligini aniqlang.

# 34 Dictionarydagi eng ko‘p takrorlangan value’ni toping.

# 35 Dictionarydagi barcha sonli value’larning o‘rtacha qiymatini hisoblang.

# 36 Dictionarydagi value’lar orasida faqat musbat sonlarni qoldiring.

# 37 Dictionaryni deep copy qilib, nested elementlar mustaqilligini tekshiring.

# 38 Dictionary ichidagi barcha tuple’larni listga aylantiring.

# 39 Dictionarydagi value’lari bir xil bo‘lgan keylarni guruhlang.

# 40 Dictionary ichida dictionary bo‘lsa, maksimal chuqurlikni aniqlang.

# ----------------------------------------------------
# 🟣 41–60: KATTA PROYEKT TOPSHIRIQLAR
# ----------------------------------------------------

# 41 TALABALAR BAHOLASH TIZIMI
# Vazifa:
# - Dictionary yarating, u quyidagi ko‘rinishda bo‘lsin:
#   {
#     "Ali": {"Math": 90, "Physics": 85},
#     "Vali": {"Math": 78, "Physics": 88}
#   }
# - Har bir talabaning o‘rtacha bahosini hisoblang
# - Barcha talabalar ichidan:
#   • eng yuqori bahoni
#   • eng past bahoni toping


# 42 ONLINE DO‘KON BOSHQARUV TIZIMI
# Vazifa:
# - Mahsulotlar quyidagi ko‘rinishda saqlansin:
#   {
#     "Olma": {"price": 5000, "count": 10},
#     "Banan": {"price": 8000, "count": 5}
#   }
# - Barcha mahsulotlarning umumiy narxini hisoblang
# - Eng qimmat mahsulotni aniqlang


# 43 BANK HISOB-KITOB TIZIMI
# Vazifa:
# - Foydalanuvchi balanslari dictionaryda saqlansin:
#   {"Ali": 1_000_000, "Vali": 500_000}
# - Quyidagi amallarni bajaring:
#   • balansni ko‘rish
#   • pul qo‘shish
#   • pul yechish
# - Balans manfiy bo‘lib ketmasligini tekshiring


# 44 LOGIN VA RO‘YXATDAN O‘TISH TIZIMI
# Vazifa:
# - Foydalanuvchi ma’lumotlari quyidagicha bo‘lsin:
#   {"admin": {"password": "1234", "tries": 0}}
# - Login va parolni tekshiring
# - Noto‘g‘ri parol kiritilsa urinishlar sonini oshiring
# - 3 marta xato bo‘lsa, foydalanuvchini bloklang


# 45 TELEFON KONTAKTLAR MENEDJERI
# Vazifa:
# - Kontaktlar quyidagicha saqlansin:
#   {"Ali": "+998901234567"}
# - Quyidagi imkoniyatlar bo‘lsin:
#   • kontakt qo‘shish
#   • kontakt o‘chirish
#   • raqamni o‘zgartirish
#   • ism bo‘yicha qidirish


# 46 MATN TAHLIL DASTURI
# Vazifa:
# - Foydalanuvchi matn kiritadi
# - Har bir so‘z nechta marta ishlatilganini hisoblang
# - Eng ko‘p va eng kam ishlatilgan so‘zni toping


# 47 SHOPPING CART (SAVATCHA)
# Vazifa:
# - Savatcha dictionary ko‘rinishida bo‘lsin:
#   {"Olma": {"price": 5000, "count": 2}}
# - Mahsulot qo‘shish
# - Mahsulotni o‘chirish
# - Miqdorni o‘zgartirish
# - Umumiy to‘lov summasini hisoblash


# 48 IMTIHON NATIJALARI ANALIZI
# Vazifa:
# - Talabalar baholari saqlansin:
#   {"Ali": 85, "Vali": 72}
# - Baho asosida avtomatik grade chiqaring:
#   90–100 → A
#   80–89  → B
#   70–79  → C
#   60–69  → D
#   <60    → F


# 49 MINI TARJIMON DASTURI
# Vazifa:
# - Lug‘at yarating:
#   {"hello": "salom", "book": "kitob"}
# - Ingliz → O‘zbek tarjima qiling
# - Agar so‘z topilmasa, "Tarjima topilmadi" chiqaring


# 50 LOG TIZIMI
# Vazifa:
# - Loglar quyidagicha saqlansin:
#   {"INFO": [], "ERROR": [], "WARNING": []}
# - Xabar va turini kiriting
# - Har bir tur bo‘yicha nechta xabar borligini chiqaring


# 51 ONLINE VOTING TIZIMI
# Vazifa:
# - Nomzodlar va ovozlar saqlansin:
#   {"Ali": 0, "Vali": 0}
# - Ovoz berilganda hisobni oshiring
# - Eng ko‘p ovoz olgan nomzodni aniqlang


# 52 O‘YIN STATISTIKASI TIZIMI
# Vazifa:
# - O‘yinchi natijalari saqlansin:
#   {"Ali": [100, 150, 200]}
# - Eng yuqori ochko
# - O‘rtacha ochko
# - Rekordni aniqlang


# 53 KUTUBXONA BOSHQARUV TIZIMI
# Vazifa:
# - Kitoblar quyidagicha saqlansin:
#   {"Python": {"author": "Guido", "available": True}}
# - Kitob bor-yo‘qligini tekshiring
# - Olingan kitobni mavjud emas deb belgilang


# 54 RESTAURANT BUYURTMA TIZIMI
# Vazifa:
# - Buyurtmalar saqlansin:
#   {"Osh": 2, "Shashlik": 3}
# - Har bir taom narxini hisobga olib
# - Umumiy tushumni hisoblang


# 55 TALABALAR DAVOMATI TIZIMI
# Vazifa:
# - Davomat quyidagicha saqlansin:
#   {"Ali": [True, False, True]}
# - Qatnashgan va qatnashmagan kunlarni hisoblang


# 56 FILE METADATA TIZIMI
# Vazifa:
# - Fayllar quyidagicha saqlansin:
#   {"test.txt": {"size": 1200, "type": "text"}}
# - Eng katta hajmli faylni toping


# 57 CHAT XABARLAR ANALIZI
# Vazifa:
# - Xabarlar quyidagicha bo‘lsin:
#   {"Ali": 15, "Vali": 8}
# - Kim eng ko‘p xabar yuborganini aniqlang


# 58 ONLINE TEST PLATFORMASI
# Vazifa:
# - Savollar va to‘g‘ri javoblar saqlansin
# - Foydalanuvchi javoblarini tekshiring
# - Yakuniy ballni hisoblang


# 59 INVENTARIZATSIYA TIZIMI
# Vazifa:
# - Ombor mahsulotlari saqlansin:
#   {"Laptop": 5, "Mouse": 20}
# - Mahsulot qo‘shish va kamaytirish
# - Qaysi mahsulot tugayotganini aniqlang


# 60 FINANCE TRACKER
# Vazifa:
# - Daromad va xarajatlar saqlansin:
#   {"income": [500000], "expense": [200000]}
# - Umumiy daromad
# - Umumiy xarajat
# - Yakuniy balansni hisoblang