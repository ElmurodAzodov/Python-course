# =========================================================
# PYTHON FUNCTIONS EXERCISES
# =========================================================


# 1
# Ikki son qabul qiladigan funksiya yozing.
# Funksiya bu ikki sonning yig‘indisini hisoblab return qilsin.


# 2
# Uchta son qabul qiladigan funksiya yozing.
# Funksiya berilgan sonlar ichidan eng kattasini return qilsin.


# 3
# Bitta son qabul qiladigan funksiya yozing.
# Agar son juft bo‘lsa True, agar toq bo‘lsa False return qilsin.


# 4
# String (matn) qabul qiladigan funksiya yozing.
# Funksiya matndagi barcha harflarni katta harfga aylantirib return qilsin.


# 5
# List qabul qiladigan funksiya yozing.
# Funksiya list ichidagi barcha sonlarning yig‘indisini return qilsin.


# 6
# Funksiya yozing.
# Funksiya bitta son qabul qilsin.
# Agar argument berilmasa default qiymat 10 bo‘lsin.
# Funksiya shu sonning kvadratini return qilsin.


# 7
# Ikki son qabul qiladigan funksiya yozing.
# Funksiyani chaqirishda argumentlarni keyword argument sifatida ishlating.


# 8
# Cheksiz miqdorda son qabul qiladigan funksiya yozing (*args).
# Funksiya berilgan sonlar ichidan eng kattasini return qilsin.


# 9
# *args yordamida bir nechta son qabul qiladigan funksiya yozing.
# Funksiya barcha sonlarning o‘rtacha qiymatini return qilsin.

def average_numbers(*args):
    total = sum(args)
    count = len(args)

    if count == 0:
        return 0

    return total / count

print(average_numbers(10, 20, 30))
print(average_numbers(5, 15, 25, 35))

# 10
# **kwargs qabul qiladigan funksiya yozing.
# Funksiya kelgan barcha ma’lumotlarni dictionary ko‘rinishida return qilsin.

def get_data(**kwargs):
    return kwargs

print(get_data(name="Ali", age=20, city="Tashkent"))

# 11
# Ikki son qabul qiladigan funksiya yozing.
# Funksiya quyidagi 4 ta natijani return qilsin:
# - yig‘indi
# - ayirma
# - ko‘paytma
# - bo‘linma


# 12
# String qabul qiladigan funksiya yozing.
# Funksiya matn ichidagi unli harflar sonini hisoblab return qilsin.


# 13
# Default argument sifatida list ishlatadigan funksiya yozing.
# Funksiya listga yangi element qo‘shib return qilsin.


# 14
# Keyword-only argument ishlatiladigan funksiya yozing.
# Masalan: func(a, b, *, operation)
# operation qiymatiga qarab amal bajarilsin.


# 15
# Bitta son qabul qiladigan funksiya yozing.
# Funksiya shu sonning faktorialini hisoblab return qilsin.


# 16
# List qabul qiladigan funksiya yozing.
# Funksiya list ichidan faqat musbat sonlarni ajratib yangi list return qilsin.


# 17
# String qabul qiladigan funksiya yozing.
# Funksiya matn palindrom (teskari o‘qilganda ham bir xil) ekanligini tekshirsin.


# 18
# Ikki list qabul qiladigan funksiya yozing.
# Funksiya ikki listni birlashtirib yangi list return qilsin.


# 19
# Global o‘zgaruvchi yarating.
# Funksiya ichida global kalit so‘zidan foydalanib shu o‘zgaruvchini o‘zgartiring.


# 20
# LEGB qoidasini ko‘rsatadigan kichik dastur yozing.
# Local, Global va Built-in o‘zgaruvchilardan foydalaning.


# 21
# List qabul qiladigan funksiya yozing.
# Funksiya listdagi eng kichik va eng katta sonni return qilsin.


# 22
# String qabul qiladigan funksiya yozing.
# Funksiya matnda nechta so‘z borligini hisoblab return qilsin.


# 23
# String qabul qiladigan funksiya yozing.
# Funksiya matnni snake_case formatiga o‘tkazib return qilsin.


# 24
# *args orqali bir nechta son qabul qiladigan funksiya yozing.
# Funksiya barcha sonlarni ko‘paytirib return qilsin.


# 25
# **kwargs orqali student ma’lumotlarini qabul qiladigan funksiya yozing.
# Funksiya ma’lumotlarni chiroyli formatda return qilsin.


# 26
# List qabul qiladigan funksiya yozing.
# Funksiya list ichidan faqat unique elementlarni return qilsin.


# 27
# Bitta son qabul qiladigan funksiya yozing.
# Funksiya son tub (prime) yoki yo‘qligini aniqlasin.


# 28
# List qabul qiladigan funksiya yozing.
# Funksiya list ichida eng ko‘p takrorlangan elementni return qilsin.


# 29
# String qabul qiladigan funksiya yozing.
# Funksiya har bir harf nechta marta qatnashganini dictionary qilib return qilsin.


# 30
# List qabul qiladigan funksiya yozing.
# Funksiya listni teskari tartibda return qilsin.



# =========================================================
# PROJECT TOPSHIRIQLAR
# =========================================================


# PROJECT 1
# Calculator funksiyasi yozing.
#
# calculate(a, b, operation)
#
# operation quyidagi qiymatlardan biri bo‘lishi mumkin:
# "add"      → qo‘shish
# "subtract" → ayirish
# "multiply" → ko‘paytirish
# "divide"   → bo‘lish
#
# Funksiya natijani return qilsin.


# PROJECT 2
# Student baholarini tahlil qiladigan funksiya yozing.
#
# analyze_grades(*grades)
#
# Funksiya quyidagilarni return qilsin:
# - o‘rtacha baho
# - eng katta baho
# - eng kichik baho
# - 60 dan yuqori baholar soni


# PROJECT 3
# Foydalanuvchi ma’lumotlarini formatlaydigan funksiya yozing.
#
# format_user(**kwargs)
#
# Masalan:
# format_user(name="Ali", age=21, country="Uzbekistan")
#
# Natija quyidagicha bo‘lishi kerak:
#
# Name: Ali
# Age: 21
# Country: Uzbekistan