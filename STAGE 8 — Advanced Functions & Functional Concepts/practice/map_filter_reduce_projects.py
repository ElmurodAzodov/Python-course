# =========================================
# FUNCTIONAL PROGRAMMING PRACTICE
# map() + filter() + reduce()
# 30 TA PROJECT STYLE TOPSHIRIQ
# =========================================

from functools import reduce


# ==================================================
# 1 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni kvadratga oshiring (map)
# va faqat 50 dan katta bo‘lganlarini chiqaring (filter)

# numbers = [2, 5, 8, 10, 12, 15]
# kvadrat = list(map(lambda x: x**2, numbers))
# natija = list(filter(lambda x: x > 50, kvadrat))
# print(natija)

# ==================================================
# 2 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni 3 ga ko‘paytiring (map)
# va faqat juft sonlarni qoldiring (filter)

# numbers = [1, 4, 7, 10, 13, 16]
# kopaygan = list(map(lambda x: x * 3, numbers))
# natija = list(filter(lambda x: x % 2 == 0, kopaygan))
# print(natija)

# ==================================================
# 3 - TOPSHIRIQ
# ==================================================
# words listidagi barcha so‘zlarni katta harfga o‘tkazing (map)
# va uzunligi 5 dan katta bo‘lganlarini filter qiling.

# words = ["python", "ai", "data", "science", "ml"]
# katta = list(map(lambda x: x.upper(), words))
# natija = list(filter(lambda x: len(x) > 5, katta))
# print(natija)

# ==================================================
# 4 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni kvadratga oshiring (map)
# va ularning yig‘indisini toping (reduce)

# numbers = [1, 2, 3, 4, 5]
# kvadrat = list(map(lambda x: x**2, numbers))
# yigindi = reduce(lambda a, b: a + b, kvadrat)
# print(yigindi)

# ==================================================
# 5 - TOPSHIRIQ
# ==================================================
# numbers listidan faqat musbat sonlarni filter qiling
# va ularni 2 ga ko‘paytiring (map)

# numbers = [-5, 3, 10, -2, 7]
# musbat = list(filter(lambda x: x > 0, numbers))
# natija = list(map(lambda x: x * 2, musbat))
# print(natija)

# ==================================================
# 6 - TOPSHIRIQ
# ==================================================
# words listidan faqat 'a' harfi bor so‘zlarni filter qiling
# va ularning uzunligini chiqaring (map)

# words = ["apple", "kiwi", "banana", "pear", "grape"]
# filtered = list(filter(lambda w: 'a' in w, words))
# lengths = list(map(lambda w: len(w), filtered))
# print(filtered, lengths)

# ==================================================
# 7 - TOPSHIRIQ
# ==================================================
# numbers listidan juft sonlarni filter qiling
# va ularning ko‘paytmasini toping (reduce)

# numbers = [2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# product = reduce(lambda x, y: x * y, evens)
# print(evens, product)

# ==================================================
# 8 - TOPSHIRIQ
# ==================================================
# words listidagi barcha so‘zlarni uzunligiga aylantiring (map)
# va eng katta uzunlikni toping (reduce)

# words = ["python", "developer", "AI", "code"]
# lengths = list(map(lambda w: len(w), words))
# max_length = reduce(lambda x, y: x if x > y else y, lengths)
# print(lengths, max_length)

# ==================================================
# 9 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni kvadratga oshiring
# keyin 100 dan kichiklarini filter qiling

# numbers = [5, 7, 9, 12]
# squares = list(map(lambda x: x**2, numbers))
# filtered = list(filter(lambda x: x < 100, squares))
# print(squares, filtered)

# ==================================================
# 10 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni 10 ga ko‘paytiring
# keyin ularning yig‘indisini hisoblang

# numbers = [1, 2, 3, 4]
# multiplied = list(map(lambda x: x * 10, numbers))
# total = reduce(lambda x, y: x + y, multiplied)
# print(multiplied, total)

# ==================================================
# 11 - TOPSHIRIQ
# ==================================================
# students listidan score > 80 bo‘lgan studentlarni filter qiling
# va ularning ismlarini chiqaring (map)

# students = [
#     {"name": "Ali", "score": 75},
#     {"name": "Vali", "score": 90},
#     {"name": "Aziza", "score": 85},
# ]
# filtered_students = filter(lambda student: student["score"] > 80, students)
# names = list(map(lambda student: student["name"], filtered_students))

# print(names)


# ==================================================
# 12 - TOPSHIRIQ
# ==================================================
# students listidagi barcha score larni oling (map)
# va o‘rtacha ballni hisoblang (reduce)

# students = [
#     {"name": "Ali", "score": 80},
#     {"name": "Vali", "score": 95},
#     {"name": "Aziza", "score": 85},
# ]
# scores = list(map(lambda student: student["score"], students))
# total_score = reduce(lambda a, b: a + b, scores)
# average_score = total_score / len(scores)

# print(average_score)

# ==================================================
# 13 - TOPSHIRIQ
# ==================================================
# products listidan price > 100 bo‘lgan mahsulotlarni filter qiling
# va ularning narxlarini oling (map)

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 20},
#     {"name": "Keyboard", "price": 80},
# ]
# expensive_products = filter(lambda product: product["price"] > 100, products)
# prices = list(map(lambda product: product["price"], expensive_products))

# print(prices)

# ==================================================
# 14 - TOPSHIRIQ
# ==================================================
# products listidagi barcha price larni oling (map)
# va umumiy narxni hisoblang (reduce)

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 20},
#     {"name": "Keyboard", "price": 80},
# ]
# prices = list(map(lambda product: product["price"], products))
# total_price = reduce(lambda a, b: a + b, prices)

# print(total_price)

# ==================================================
# 15 - TOPSHIRIQ
# ==================================================
# emails listidan faqat gmail email larni filter qiling
# va domen qismini olib tashlang (map)

# emails = [
#     "ali@gmail.com",
#     "user@yahoo.com",
#     "dev@gmail.com",
# ]
# gmail_emails = filter(lambda email: "@gmail.com" in email, emails)
# usernames = list(map(lambda email: email.replace("@gmail.com", ""), gmail_emails))

# print(usernames)

# ==================================================
# 16 - TOPSHIRIQ
# ==================================================
# numbers listidan faqat 3 ga bo‘linadigan sonlarni filter qiling
# va ularni kvadratga oshiring (map)

# numbers = [3, 6, 7, 9, 10, 12]
# result = list(map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numbers)))
# print(result)

# ==================================================
# 17 - TOPSHIRIQ
# ==================================================
# words listidan uzunligi 4 dan katta so‘zlarni filter qiling
# va ularning uzunliklari yig‘indisini hisoblang

words = ["AI", "python", "data", "science"]
filtered_words = list(filter(lambda word: len(word) > 4, words))
length_sum = sum(map(len, filtered_words))

print(filtered_words)
print(length_sum)

# ==================================================
# 18 - TOPSHIRIQ
# ==================================================
# numbers listidan toq sonlarni filter qiling
# va ularni 5 ga ko‘paytiring

# numbers = [1, 2, 3, 4, 5, 6]


# ==================================================
# 19 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni string ga aylantiring
# va ularni bitta stringga birlashtiring

# numbers = [1, 2, 3, 4, 5]


# ==================================================
# 20 - TOPSHIRIQ
# ==================================================
# numbers listidan musbat sonlarni filter qiling
# va eng katta sonni toping

# numbers = [-10, 5, 20, -3, 7]


# ==================================================
# 21 - TOPSHIRIQ
# ==================================================
# users listidan age > 18 bo‘lganlarni filter qiling
# va ularning ismlarini katta harfga o‘tkazing

# users = [
#     {"name": "Ali", "age": 17},
#     {"name": "Vali", "age": 25},
#     {"name": "Aziza", "age": 22},
# ]


# ==================================================
# 22 - TOPSHIRIQ
# ==================================================
# transactions listidan faqat musbat qiymatlarni filter qiling
# va umumiy daromadni hisoblang

# transactions = [100, -20, 50, -10, 200]


# ==================================================
# 23 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni kvadrat ildizini hisoblang
# va 5 dan katta bo‘lganlarini filter qiling

import math

# numbers = [4, 9, 16, 25, 36]


# ==================================================
# 24 - TOPSHIRIQ
# ==================================================
# words listidan palindrom so‘zlarni filter qiling

# words = ["level", "python", "madam", "code"]


# ==================================================
# 25 - TOPSHIRIQ
# ==================================================
# students listidan score > 70 bo‘lganlarni filter qiling
# va eng yuqori ballni toping

# students = [
#     {"name": "Ali", "score": 60},
#     {"name": "Vali", "score": 85},
#     {"name": "Aziza", "score": 90},
# ]


# ==================================================
# 26 - TOPSHIRIQ
# ==================================================
# numbers listidagi barcha sonlarni 2 ga ko‘paytiring
# keyin ularning ko‘paytmasini hisoblang

# numbers = [2, 3, 4]


# ==================================================
# 27 - TOPSHIRIQ
# ==================================================
# products listidan price < 500 bo‘lganlarni filter qiling
# va narxlarini 10% ga oshiring

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Phone", "price": 400},
#     {"name": "Monitor", "price": 300},
# ]


# ==================================================
# 28 - TOPSHIRIQ
# ==================================================
# numbers listidan tub sonlarni filter qiling
# va ularning yig‘indisini toping

# numbers = [2, 3, 4, 5, 6, 7, 11]


# ==================================================
# 29 - TOPSHIRIQ
# ==================================================
# employees listidan salary > 1500 bo‘lganlarni filter qiling
# va ularning salary larini yig‘ing

# employees = [
#     {"name": "Ali", "salary": 1200},
#     {"name": "Vali", "salary": 2000},
#     {"name": "Aziza", "salary": 1800},
# ]


# ==================================================
# 30 - TOPSHIRIQ (JUDA KATTA PROJECT)
# ==================================================
# E-COMMERCE ORDER ANALYSIS
#
# orders listidan quyidagilarni bajaring:
#
# 1. price > 100 bo‘lgan orderlarni filter qiling
# 2. har bir price ga 12% tax qo‘shing
# 3. barcha orderlarning umumiy summasini hisoblang

# orders = [
#     {"id": 1, "price": 80},
#     {"id": 2, "price": 150},
#     {"id": 3, "price": 300},
#     {"id": 4, "price": 50},
# ]
