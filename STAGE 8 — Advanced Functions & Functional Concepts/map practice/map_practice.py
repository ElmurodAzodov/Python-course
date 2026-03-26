"""
PYTHON MAP() FUNKSIYASI BO'YICHA TOPSHIRIQLAR
Oddiy → O‘rta → Qiyin darajalar aralash berilgan
Har bir masalada map() ishlatish shart
"""


# ==============================
# 1
# List ichidagi barcha sonlarni 2 ga ko‘paytiring
# nums = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * 2, nums))
# print(result)

# ==============================
# 2
# List ichidagi sonlarni string ko‘rinishiga o‘tkazing
# nums = [10, 20, 30, 40]
# result = list(map(str, nums))
# print(result)

# ==============================
# 3
# List ichidagi barcha stringlarni katta harfga (UPPER) o‘tkazing
# words = ["python", "html", "css", "javascript"]
# katta_harf = list(map(lambda a: a.upper(), words))
# print(katta_harf)

# ==============================
# 4
# List ichidagi sonlarning kvadratini chiqaring
# nums = [2, 4, 6, 8]
# kv = list(map(lambda x: x ** 2, nums))
# print(kv)

# ==============================
# 5
# List ichidagi sonlarning kubini chiqaring
# nums = [1, 2, 3, 4, 5]
# kub = list(map(lambda x: x ** 3, nums))
# print(kub)

# ==============================
# 6
# String list ichidagi har bir element uzunligini aniqlang
# words = ["apple", "banana", "cherry", "kiwi"]
# uzunligi = list(map(lambda x: len(x), words))
# print(uzunligi)

# ==============================
# 7
# String list ichidagi barcha elementlarni int ga aylantiring
# numbers = ["10", "20", "30", "40"]
# numbers_int = list(map(int, numbers))
# print(numbers_int)

# ==============================
# 8
# List ichidagi barcha sonlarga 5 qo‘shing
# nums = [3, 6, 9, 12]
# nums_plus_5 = list(map(lambda x: x + 5, nums))
# print(nums_plus_5)

# ==============================
# 9
# List ichidagi barcha sonlarni float ga aylantiring
# nums = [1, 2, 3, 4, 5]
# nums_float = list(map(float, nums))
# print(nums_float)

# ==============================
# 10
# Ikki list elementlarini qo‘shing
# a = [1, 2, 3]
# b = [4, 5, 6]


# ==============================
# 11
# List ichidagi barcha stringlarni teskari qilib chiqaring
# words = ["python", "developer", "code"]
# teskari = list(map(lambda x: x[::-1], words))
# print(teskari)

# ==============================
# 12
# List ichidagi sonlarning absolute qiymatini chiqaring
# nums = [-5, -2, 3, -1, 7]


# ==============================
# 13
# List ichidagi sonlarni string qilib "Number: x" formatga o‘tkazing
# nums = [1, 2, 3, 4]


# ==============================
# 14
# Ikki listni ko‘paytiring
# a = [1, 2, 3]
# b = [10, 20, 30]


# ==============================
# 15
# List ichidagi stringlarni capitalize qiling
# words = ["python", "java", "golang", "rust"]


# =========================================
#              MINI PROJECTLAR
# =========================================


# ==============================
# PROJECT 1
# Foydalanuvchi kiritgan sonlar listini
# kvadratga oshirib yangi list qaytaring

# numbers = input("Sonlarni kiriting (bo'sh joy bilan): ").split()


# ==============================
# PROJECT 2
# Foydalanuvchi kiritgan ismlarni
# katta harf bilan chiqaring

# names = input("Ismlarni kiriting: ").split()


# ==============================
# PROJECT 3
# List ichidagi narxlarni soliq bilan hisoblang
# soliq = 12%

# prices = [100, 250, 400, 150]

# ==============================
# PROJECT 4
# Email listidan faqat username qismini ajratib oling

# emails = [
#     "ali@gmail.com",
#     "vali@yahoo.com",
#     "john@mail.com"
# ]


# ==============================
# PROJECT 5
# List ichidagi matnlarni slug formatga o'tkazing
# Masalan: "Hello World" → "hello-world"

# titles = [
#     "Python Dasturlash",
#     "Web Development Course",
#     "Full Stack Developer"
# ]