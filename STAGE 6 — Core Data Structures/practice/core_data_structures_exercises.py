"""
10 ta Intervyu Darajasidagi Topshiriqlar
Mavzu: Core Data Structures (List, Tuple, Set, Dictionary)
"""

# =========================================================
# Topshiriq 1 — O‘rta daraja
# "Talabalar ma'lumotlar bazasi"
# =========================================================

students = [
    {"name": "Ali", "age": 20, "grade": 85},
    {"name": "Vali", "age": 22, "grade": 90},
    {"name": "Sami", "age": 20, "grade": 78},
    {"name": "Ali", "age": 21, "grade": 92}
]

# Vazifalar:
# 1. Barcha talabalarni grade bo‘yicha kamayish tartibida chiqaring.
# 2. name bo‘yicha takrorlanuvchi talabalarni toping va alohida ro‘yxatga chiqaring.
# 3. Eng yosh va eng keksa talabani toping.
# 4. Har bir age bo‘yicha nechta talaba borligini hisoblang.


# =========================================================
# Topshiriq 2 — O‘rta+ daraja
# "Matn tahlil qilish"
# =========================================================

text = "python java python c++ java python javascript c++ python"

# Vazifalar:
# 1. So‘zlarning chastotasini hisoblang.
# 2. Eng ko‘p qatnashgan 3 ta so‘zni chiqaring.
# 3. Faqat bir marta qatnashgan so‘zlarni toping.
# 4. So‘zlarni alifbo tartibida chiqaring.


# =========================================================
# Topshiriq 3 — Murakkab
# "Contact Manager"
# =========================================================

contacts = [
    ("Ali", "998901234567"),
    ("Vali", "998901234568"),
    ("Ali", "998901234569"),
    ("Zafar", "998901234570")
]

# Vazifalar:
# 1. Kontaktlarni name bo‘yicha guruhlang.
# 2. Yangi kontakt qo‘shish imkoniyati yarating.
# 3. Telefon raqam orqali kontaktni qidirish funksiyasi.
# 4. Barcha kontaktlarni name bo‘yicha tartiblab chiqaring.


# =========================================================
# Topshiriq 4 — Murakkab
# "Baholarni guruhlash"
# =========================================================

grades = [85, 92, 78, 90, 85, 92, 88, 75, 78, 90, 100, 85]

# Vazifalar:
# 1. Baholarni takrorlanmaydigan qilib chiqaring.
# 2. Baholarni toifalarga ajrating:
#    0–59 -> "Fail"
#    60–74 -> "Good"
#    75–89 -> "Very Good"
#    90–100 -> "Excellent"
# 3. Har bir toifaga nechta talaba tushganini hisoblang.
# 4. Eng ko‘p uchragan bahoni toping.


# =========================================================
# Topshiriq 5 — Murakkab
# "Mahsulot inventarizatsiyasi"
# =========================================================

inventory = [
    {"name": "Olma", "price": 5000, "quantity": 10},
    {"name": "Banan", "price": 7000, "quantity": 5},
    {"name": "Olma", "price": 5500, "quantity": 3},
    {"name": "Shaftoli", "price": 8000, "quantity": 7}
]

# Vazifalar:
# 1. Mahsulotlarni name bo‘yicha guruhlang va umumiy miqdorini hisoblang.
# 2. Eng qimmat va eng arzon mahsulotni toping.
# 3. Umumiy inventar qiymatini hisoblang (price * quantity).
# 4. name bo‘yicha qidirish funksiyasi yarating.


# =========================================================
# Topshiriq 6 — Murakkab
# "Yo‘lovchi tashish tizimi"
# =========================================================

stops = [
    {"stop": "A", "in": 5, "out": 0},
    {"stop": "B", "in": 3, "out": 2},
    {"stop": "C", "in": 4, "out": 1},
    {"stop": "D", "in": 2, "out": 5}
]

# Vazifalar:
# 1. Har bir bekatdagi yo‘lovchilar sonini hisoblang.
# 2. Eng ko‘p yo‘lovchi chiqqan bekatni toping.
# 3. Har bir bekatda necha kishi qolganini (in - out) hisoblang.
# 4. Bekatlar bo‘yicha harakatni ko‘rinishida chiqaring (masalan: A: +5).


# =========================================================
# Topshiriq 7 — Murakkab+
# "Guruhlar va a'zolar"
# =========================================================

groups = {
    "Python": ["Ali", "Vali", "Sami"],
    "Java": ["Vali", "Zafar", "Ali"],
    "C++": ["Sami", "Zafar", "Bobur"]
}

# Vazifalar:
# 1. Barcha a'zolarni takrorlanmasdan chiqaring.
# 2. Har bir a'zo nechta guruhda qatnashganini hisoblang.
# 3. Faqat bitta guruhda qatnashgan a'zolarni toping.
# 4. Eng ko‘p a'zosi bo‘lgan guruhni toping.


# =========================================================
# Topshiriq 8 — Murakkab+
# "Ish vaqti hisoboti"
# =========================================================

work_log = [
    ("Ali", "2025-04-01", 8),
    ("Vali", "2025-04-01", 7),
    ("Ali", "2025-04-02", 6),
    ("Zafar", "2025-04-01", 9),
    ("Vali", "2025-04-02", 8),
    ("Ali", "2025-04-03", 5)
]

# Vazifalar:
# 1. Har bir xodimning umumiy ish soatini hisoblang.
# 2. Eng ko‘p va eng kam ishlagan xodimni toping.
# 3. Har bir kunning umumiy ish soatini hisoblang.
# 4. Xodimlarni ish soati bo‘yicha kamayish tartibida chiqaring.


# =========================================================
# Topshiriq 9 — Murakkab++
# "Yo‘nalishlar tarmog‘i"
# =========================================================

routes = [
    ("Toshkent", "Samarqand"),
    ("Samarqand", "Buxoro"),
    ("Toshkent", "Nukus"),
    ("Buxoro", "Xiva"),
    ("Samarqand", "Toshkent")
]

# Vazifalar:
# 1. Barcha shaharlar ro‘yxatini takrorlanmasdan chiqaring.
# 2. Har bir shahardan nechta yo‘nalish borligini hisoblang.
# 3. "Toshkent"dan to‘g‘ridan-to‘g‘ri borish mumkin bo‘lgan shaharlarni toping.
# 4. Ikki shahar o‘rtasida to‘g‘ridan-to‘g‘ri yo‘nalish bor-yo‘qligini tekshiruvchi funksiya yarating.


# =========================================================
# Topshiriq 10 — Intervyu darajasi
# "Murojaatlar tahlili"
# =========================================================

appeals = [
    {"id": 1, "user": "Ali", "type": "texnik", "status": "yopiq"},
    {"id": 2, "user": "Vali", "type": "moliyaviy", "status": "ochiq"},
    {"id": 3, "user": "Sami", "type": "texnik", "status": "ochiq"},
    {"id": 4, "user": "Ali", "type": "texnik", "status": "ochiq"},
    {"id": 5, "user": "Zafar", "type": "moliyaviy", "status": "yopiq"}
]

# Vazifalar:
# 1. Har bir foydalanuvchi nechta murojaat qilganini hisoblang.
# 2. Har bir type bo‘yicha nechta ochiq va yopiq murojaat borligini hisoblang.
# 3. Eng ko‘p murojaat qilgan foydalanuvchini toping.
# 4. Ochiq murojaatlar soni 1 dan ko‘p bo‘lgan foydalanuvchilarni chiqaring.
# 5. Murojaatlarni status bo‘yicha guruhlab, har bir guruhni type bo‘yicha tartiblang.