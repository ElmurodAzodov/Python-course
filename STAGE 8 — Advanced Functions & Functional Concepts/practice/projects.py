"""
========================================
🐍 PYTHON MEGA PROJECT TASKS (10 TA)
STAGE 3 → STAGE 8 (FULL PRACTICE)
========================================
Har bir project alohida funksiya yoki modul sifatida yozilsin.
Har bir projectda:
- string
- condition
- loop
- data structures
- function
- advanced concepts
ishlatilishi SHART.
========================================
"""

# ======================================
# 1 - PROJECT (O'RTACHA)
# TEXT ANALYZER
# ======================================
# Foydalanuvchidan matn oling va:
# - nechta so'z borligini aniqlang
# - eng ko'p uchragan so'zni toping
# - barcha so'zlarni kichik harfga o'tkazing
# - faqat harflardan iborat so'zlarni filter qiling
# - natijani dictionary qilib qaytaring


# ======================================
# 2 - PROJECT
# PASSWORD VALIDATOR
# ======================================
# Parolni tekshiruvchi dastur yozing:
# Shartlar:
# - kamida 8 ta belgidan iborat
# - kamida 1 ta katta harf
# - kamida 1 ta kichik harf
# - kamida 1 ta raqam
# - kamida 1 ta maxsus belgi (!@#$%)
# Natija True yoki False qaytarsin


# ======================================
# 3 - PROJECT
# EMAIL PARSER
# ======================================
# Email list berilgan:
# ["ali@gmail.com", "test@yahoo.com", ...]
#
# Har bir emailni:
# - username
# - domain
# ga ajrating
#
# Natija:
# {
#   "gmail.com": ["ali"],
#   "yahoo.com": ["test"]
# }


# ======================================
# 4 - PROJECT
# WORD GAME (INTERMEDIATE+)
# ======================================
# Foydalanuvchidan so'z oling
# - so'zni teskarisiga o'giring
# - palindrome ekanligini tekshiring
# - harflarni tartiblab yangi string yarating
# - nechta unli va undosh borligini aniqlang


# ======================================
# 5 - PROJECT
# LOG FILE ANALYZER
# ======================================
# Berilgan log matn:
# "ERROR: file not found\nINFO: started\nERROR: crash"
#
# - ERROR lar sonini toping
# - INFO lar sonini toping
# - har bir qatordan levelni ajrating
# - dictionary ko'rinishida qaytaring


# ======================================
# 6 - PROJECT
# CUSTOM FILTER & MAP ENGINE
# ======================================
# O'zingiz map() va filter() ni yozing:
#
# def my_map(func, iterable):
# def my_filter(func, iterable):
#
# Va ularni ishlatib:
# - sonlarni kvadratga oshiring
# - faqat juft sonlarni ajrating


# ======================================
# 7 - PROJECT
# STUDENT MANAGEMENT SYSTEM
# ======================================
# Talabalar ro'yxati:
# [
#   {"name": "Ali", "score": 85},
#   {"name": "Vali", "score": 60},
# ]
#
# Qiling:
# - eng yuqori ballni toping
# - o'rtacha ballni hisoblang
# - 70 dan yuqorilarni filter qiling
# - ismlarini katta harfga o'tkazing


# ======================================
# 8 - PROJECT
# REGEX VALIDATOR SYSTEM
# ======================================
# re modulidan foydalanib:
# - email validatsiya
# - telefon raqam validatsiya
# - faqat harflardan iborat stringni tekshirish
#
# Barchasini bitta funksiya ichida yozing


# ======================================
# 9 - PROJECT
# MINI TEMPLATE ENGINE
# ======================================
# Matn:
# "Hello {name}, you are {age} years old"
#
# Function yozing:
# render(template, data)
#
# Natija:
# render("Hello {name}", {"name": "Ali"})
# → "Hello Ali"
#
# replace(), regex ishlatish mumkin


# ======================================
# 10 - PROJECT
# FUNCTIONAL CALCULATOR ENGINE
# ======================================
# Calculator yozing:
#
# Qo'llab-quvvatlaydi:
# - +, -, *, /
# - string input: "2 + 3 * 4"
#
# Talablar:
# - parsing (split, regex)
# - precedence (operator ustunligi)
# - recursion yoki stack ishlatish
# - error handling
#
# BONUS:
# - decorator bilan logging qo'shing
# - cache (lru_cache) ishlating


# ======================================
# TEXT SEARCH ENGINE
# ======================================
# Matnlar listi berilgan:
# ["python is great", "I love coding", ...]
#
# Qiling:
# - search(query) funksiyasi yozing
# - qidiruv natijasini relevance bo'yicha tartiblang
# - har bir so'z nechta marta uchraganini hisoblang
# - inverted index yarating:
#   {"python": [0, 2], "coding": [1]}
#
# Juda real project!
# ======================================