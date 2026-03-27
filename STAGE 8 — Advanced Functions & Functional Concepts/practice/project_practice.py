# ==============================
# PYTHON PRACTICE PROJECTS (15 TA)
# Mavzular: string, list, tuple, dict, set, functions, map, filter, reduce
# ==============================
from functools import reduce

# 1. PROJECT: USERNAME ANALYZER
# Foydalanuvchidan username qabul qiling.
# - string methodlar bilan: katta/kichik harf, uzunlik, faqat harf/raqamligini tekshiring
# - unique belgilarni set yordamida aniqlang
# - dictionaryga quyidagi info ni saqlang:
#   {length, has_digit, has_upper, unique_count}
# - function yozib, natijani chiroyli chiqarib bering

# def analyze_username(username):
#     info = {
#         "length": len(username),
#         "has_digit": any(map(str.isdigit, username)),
#         "has_upper": any(map(str.isupper, username)),
#         "unique_count": len(set(username)),
#     }
#     return info
# print(analyze_username("Username123!"))



# 2. PROJECT: EMAIL LIST CLEANER
# Email ro'yxati berilgan (list).
# - string method bilan '@' borligini tekshiring
# - filter orqali faqat valid email qoldiring
# - map orqali hammasini kichik harfga o'tkazing
# - set orqali duplicate email'larni olib tashlang
# - natijani list sifatida qaytaring


# 3. PROJECT: PRODUCT INVENTORY SYSTEM
# Mahsulotlar dictionaryda:
# {product_name: (price, quantity)}
# - function yozing:
#   - eng qimmat mahsulot
#   - umumiy qiymat (reduce ishlatib)
#   - quantity 0 bo'lganlarni filter qiling
# - natijalarni chiqarish

products = {
    "apple": (2, 5),
    "banana": (1, 0),
    "laptop": (1000, 2)
}
# [("apple", (2, 5)), ("banana", (1, 0), ("laptop", (1000, 2))]
def product_func(products):
    qimmat_mahsulot = max(products.items(), key=lambda x: x[1][0])
    umumiy_qiymat = reduce(lambda acc, x: acc + x[1][0], products.items(), 0)
    nol = dict(filter(lambda x: x[1][1] > 0, products.items()))

    return qimmat_mahsulot, umumiy_qiymat, nol
print(product_func(products))

# 4. PROJECT: WORD FREQUENCY COUNTER
# Matn berilgan (string).
# - so'zlarga ajrating (split)
# - list orqali hisoblang
# - dictionaryda saqlang: {word: count}
# - eng ko'p ishlatilgan 5ta so'zni chiqaring


# 5. PROJECT: PASSWORD STRENGTH CHECKER
# Password qabul qiling:
# - string methodlar bilan tekshiring:
#   - uzunlik >= 8
#   - katta harf bor
#   - raqam bor
# - set orqali unique belgilar soni
# - function orqali "Weak", "Medium", "Strong" deb baholang


# 6. PROJECT: STUDENT GRADE ANALYZER
# Students dict:
# {name: [grades]}
# - map bilan o'rtacha bahoni hisoblang
# - filter bilan faqat >= 70 bo'lganlar
# - reduce bilan umumiy o'rtacha
# - natijani tuple ko'rinishida qaytaring


# 7. PROJECT: UNIQUE WORD FINDER
# 2 ta matn berilgan:
# - set orqali faqat 1-matnda bor so'zlar
# - faqat 2-matnda bor so'zlar
# - ikkala matnda ham borlari
# - natijani dictionaryda saqlang


# 8. PROJECT: PHONE BOOK SEARCH SYSTEM
# dict: {name: phone}
# - function:
#   - ism bo'yicha qidirish (string lower)
#   - qisman mos keladiganlarni list qaytarsin
# - map orqali barcha ismlarni katta harf qiling


# 9. PROJECT: NUMBER PROCESSING TOOL
# list ichida sonlar:
# - filter bilan faqat juft sonlar
# - map bilan kvadratga oshiring
# - reduce bilan yig'indisini toping
# - tuplega aylantiring


# 10. PROJECT: TEXT FORMATTER
# Matn berilgan:
# - har bir gapni katta harf bilan boshlang
# - ortiqcha probellarni olib tashlang
# - map bilan har bir so'zni capitalize qiling
# - natijani qaytaring


# 11. PROJECT: SHOPPING CART
# list of dict:
# [{"name": "apple", "price": 2, "qty": 3}, ...]
# - reduce bilan umumiy summa
# - filter bilan qty > 0
# - map bilan faqat nomlarni oling
# - natijani chiqarish


# 12. PROJECT: DATA CLEANING TOOL
# list ichida string va numberlar aralash:
# - filter bilan faqat stringlar
# - map bilan strip() qiling
# - set orqali unique qiymatlar
# - list qilib qaytaring


# 13. PROJECT: LOGIN SYSTEM SIMULATION
# dict: {username: password}
# - function:
#   - login tekshiradi
#   - string method bilan trim va lower
# - muvaffaqiyatli loginlarni listga qo'shing


# 14. PROJECT: TAG SYSTEM (HASHTAGS)
# string: "#python #code #python #learn"
# - split qilib listga oling
# - set orqali unique taglar
# - dictionaryda count qiling
# - eng mashhur tagni toping


# 15. PROJECT: FILE NAME ORGANIZER
# list: ["file1.txt", "image.png", "doc.pdf"]
# - string method bilan extension ajrating
# - dictga joylang:
#   {"txt": [...], "png": [...]}
# - map/filter ishlatib fayllarni tartiblang
# - natijani chiqaring


# ==============================
# MAQSAD:
# Har bir projectda:
# - kamida 1 ta function ishlating
# - map, filter, reduce ishlating
# - string/list/dict/set bilan ishlang
# ==============================