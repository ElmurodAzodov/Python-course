# =========================================
# PYTHON FILTER() PRACTICE
# 15 TA TOPSHIRIQ + 5 TA PROJECT
# =========================================


# ===============================
# 1 - TOPSHIRIQ (O'RTACHA)
# ===============================
# numbers listidan faqat JUFT sonlarni filter() yordamida ajrating.

# numbers = [3, 8, 15, 22, 7, 10, 33, 40]

# juft_sonlar = list(filter(lambda x: x % 2 == 0, numbers))
# print("Juft sonlar:", juft_sonlar)

# ===============================
# 2 - TOPSHIRIQ
# ===============================
# numbers listidan faqat TOQ sonlarni filter() yordamida ajrating.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# toq_sonlar = list(filter(lambda x: x % 2 != 0, numbers))
# print("Toq sonlar:", toq_sonlar)

# ===============================
# 3 - TOPSHIRIQ
# ===============================
# numbers listidan 10 dan KATTA sonlarni filter qiling.

# numbers = [4, 11, 25, 3, 9, 15, 8]
# katta_sonlar = list(filter(lambda x: x > 10, numbers))
# print("10 dan katta sonlar:", katta_sonlar)

# ===============================
# 4 - TOPSHIRIQ
# ===============================
# words listidan uzunligi 5 dan katta bo‘lgan so‘zlarni ajrating.

# words = ["python", "code", "AI", "programming", "data", "filter"]
# uzun_sozlar = list(filter(lambda x: len(x) > 5, words))
# print(uzun_sozlar)

# ===============================
# 5 - TOPSHIRIQ
# ===============================
# names listidan faqat 'A' harfi bilan boshlanadigan ismlarni filter qiling.

# names = ["Ali", "Vali", "Aziza", "Bekzod", "Anvar", "Dilshod"]
# names_A = list(filter(lambda x: x.startswith('A'), names))
# print(names_A)

# ===============================
# 6 - TOPSHIRIQ
# ===============================
# numbers listidan faqat MUSBAT sonlarni filter qiling.

# numbers = [-5, 10, -3, 7, 0, 25, -1]
# positive_numbers = list(filter(lambda x: x > 0, numbers))
# print(positive_numbers)

# ===============================
# 7 - TOPSHIRIQ
# ===============================
# numbers listidan faqat 3 ga bo‘linadigan sonlarni filter qiling.

# numbers = [3, 7, 9, 12, 14, 18, 20]
# divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
# print(divisible_by_3)

# ===============================
# 8 - TOPSHIRIQ
# ===============================
# words listidan ichida 'a' harfi bor so‘zlarni filter qiling.

# words = ["apple", "pear", "grape", "kiwi", "banana"]
# words_with_a = list(filter(lambda x: 'a' in x, words))
# print(words_with_a)

# ===============================
# 9 - TOPSHIRIQ
# ===============================
# numbers listidan faqat 2 xonali sonlarni filter qiling.

numbers = [5, 12, 99, 7, 120, 45, 3]
two_digit_numbers = list(filter(lambda x: 10 <= x <= 99, numbers))
print(two_digit_numbers)

# ===============================
# 10 - TOPSHIRIQ (QIYINROQ)
# ===============================
# numbers listidan kvadrati 100 dan katta bo‘ladigan sonlarni filter qiling.

# numbers = [5, 8, 11, 3, 12, 4]


# ===============================
# 11 - TOPSHIRIQ
# ===============================
# students listidan yoshi 18 dan katta bo‘lgan studentlarni filter qiling.

# students = [
#     {"name": "Ali", "age": 17},
#     {"name": "Vali", "age": 20},
#     {"name": "Aziza", "age": 19},
#     {"name": "Bekzod", "age": 16},
# ]


# ===============================
# 12 - TOPSHIRIQ
# ===============================
# numbers listidan tub sonlarni filter qiling.

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# ===============================
# 13 - TOPSHIRIQ (ANCHA QIYIN)
# ===============================
# products listidan narxi 100 dan katta bo‘lgan mahsulotlarni filter qiling.

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 25},
#     {"name": "Keyboard", "price": 80},
#     {"name": "Phone", "price": 900},
# ]


# ===============================
# 14 - TOPSHIRIQ
# ===============================
# emails listidan faqat "@gmail.com" bilan tugaydigan email larni filter qiling.

# emails = ["user1@gmail.com", "test@yahoo.com", "dev@gmail.com", "admin@mail.ru"]


# ===============================
# 15 - TOPSHIRIQ (JUDA QIYIN)
# ===============================
# numbers listidan palindrom sonlarni filter qiling.
# Masalan: 121, 343, 999

# numbers = [121, 45, 343, 89, 999, 123]


# ==================================================
# ================= PROJECT TOPSHIRIQLAR =============
# ==================================================


# =========================================
# PROJECT 1: USER FILTRATION SYSTEM
# =========================================
# users listidan quyidagilarni filter qiling:
# - age > 18
# - country == "Uzbekistan"

# users = [
#     {"name": "Ali", "age": 22, "country": "Uzbekistan"},
#     {"name": "John", "age": 17, "country": "USA"},
#     {"name": "Aziza", "age": 25, "country": "Uzbekistan"},
#     {"name": "Tom", "age": 30, "country": "UK"},
# ]


# =========================================
# PROJECT 2: ONLINE SHOP FILTER
# =========================================
# products listidan quyidagilarni filter qiling:
# - price < 500
# - rating >= 4

# products = [
#     {"name": "Laptop", "price": 1200, "rating": 4.8},
#     {"name": "Phone", "price": 400, "rating": 4.2},
#     {"name": "Headphones", "price": 150, "rating": 3.9},
#     {"name": "Monitor", "price": 300, "rating": 4.5},
# ]


# =========================================
# PROJECT 3: PASSWORD SECURITY FILTER
# =========================================
# passwords listidan faqat kuchli passwordlarni filter qiling:
# shartlar:
# - kamida 8 ta belgi
# - kamida bitta raqam bor

# passwords = [
#     "abc123",
#     "password",
#     "Secure123",
#     "hello",
#     "Admin2024",
# ]


# =========================================
# PROJECT 4: FILE FILTER SYSTEM
# =========================================
# files listidan faqat ".py" fayllarni filter qiling.

# files = [
#     "main.py",
#     "app.js",
#     "index.html",
#     "filter.py",
#     "styles.css",
# ]


# =========================================
# PROJECT 5 (KATTA PROJECT)
# STUDENT DATA ANALYSIS
# =========================================
# students listidan quyidagilarni filter qiling:
#
# 1. score > 80
# 2. age >= 18
# 3. city == "Tashkent"
#
# uchala shartni bajargan studentlarni chiqaring.

# students = [
#     {"name": "Ali", "age": 19, "score": 85, "city": "Tashkent"},
#     {"name": "Vali", "age": 17, "score": 90, "city": "Samarkand"},
#     {"name": "Aziza", "age": 20, "score": 88, "city": "Tashkent"},
#     {"name": "Bekzod", "age": 22, "score": 70, "city": "Tashkent"},
# ]
