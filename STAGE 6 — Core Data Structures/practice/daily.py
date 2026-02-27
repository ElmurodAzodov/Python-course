# Quyida sizga **list, tuple, set** mavzulariga oid **10 ta topshiriq savollari** berilgan.
# Ular **oddiydan → juda murakkabgacha** tartiblangan.
# (Funksiyasiz bajarish uchun mo‘ljallangan.)

# ---

# ### 1️⃣ Eng oddiy daraja — List bilan ishlash

# Foydalanuvchidan 5 ta son qabul qiling va:

# * ularni listga joylang
# * eng kattasini va eng kichigini chiqaring

# nums = []
# for i in range(5):
#     nums.append(int(input("Son kiriting: ")))
    
# print(f"Kattasi: {max(nums)}")
# print(f"Kichigi: {min(nums)}")



# ---

# ### 2️⃣ List o‘rtacha daraja

# Foydalanuvchi istalgancha ism kiritadi (`stop` bilan tugaydi).
# Dastur:

# * jami ismlar sonini
# * eng uzun ismni
# * alifbo bo‘yicha saralangan ro‘yxatni chiqarsin

# names = []
# while True:
#     n = input("Ismingizni kiriting: ")
#     if n.lower() == "stop":
#         break
#     names.append(n)
# print(names)
# print(f"Ismlar uzunligi: {len(names)}")

# eng_uzun = ""
# for i in names:
#     if len(i) > len(eng_uzun):
#         eng_uzun = i
# print(f"Eng uzun ism {eng_uzun}, uning uzunligi {len(eng_uzun)}ga teng")

# ---

# ### 3️⃣ List + sikl fikrlash topshirig‘i

# 10 ta son kiriting.
# Dastur:

# * faqat musbat sonlarni yangi listga
# * faqat manfiy sonlarni boshqa listga ajratsin
# * qaysi list uzunligini aniqlasin

# ---

# ### 4️⃣ Set asoslari

# Matn kiriting.
# Dastur:

# * nechta unikal so‘z borligini
# * barcha unikal so‘zlar ro‘yxatini chiqarsin

# ---

# ### 5️⃣ Set amallari

# 2 ta guruh talabalar ismini kiriting (vergul bilan).
# Dastur aniqlasin:

# * ikkala guruhda ham bor talabalar
# * faqat 1-guruhga xoslar
# * faqat 2-guruhga xoslar

# ---

# ### 6️⃣ Tuple boshlang‘ich daraja

# Har talaba uchun `(ism, yosh)` tuple yarating.
# Kamida 5 ta talaba kiriting.
# Dastur:

# * eng katta yoshli talabani
# * o‘rtacha yoshni chiqarsin

# ---

# ### 7️⃣ Tuple + list birga ishlatish

# Talabalar ma’lumoti `(ism, kurs, ball)` ko‘rinishida saqlansin.
# Dastur:

# * eng yuqori ballni
# * eng past ballni
# * 70 dan yuqori olgan talabalar ro‘yxatini chiqarsin

students = []

n = int(input("Nechta talaba kiritilsin: "))

for i in range(n):
    print(f"\n{i+1}-talaba ma'lumoti:")
    name = input("Ism: ")
    course = int(input("Kurs: "))
    score = int(input("Ball: "))
    
    students.append((name, course, score))
    
print(students)

max_student = max(students, key=lambda x: x[2])
min_student = min(students, key=lambda x: x[2])
high_scores = [s for s in students if s[2] > 70]

print(f"Eng yuqori ball: {max_student[2]} ({max_student[0]})")
print(f"Eng past ball: {min_student[2]} ({min_student[0]})")

print("\n70 dan yuqori olgan talabalar:")
for s in high_scores:
    print(s)
# ---

# ### 8️⃣ Murakkabroq mantiqiy topshiriq (List + Set)

# Do‘kon savatiga mahsulotlar kiritiladi (`stop` bilan tugaydi).
# Dastur:

# * jami mahsulotlar sonini
# * unikal mahsulotlar sonini
# * eng ko‘p olingan mahsulotni aniqlasin

# products = []

# print("Mahsulot kiriting (to'xtatish uchun 'stop' yozing):")

# while True:
#     item = input("Mahsulot nomi: ").lower()
    
#     if item == "stop":
#         break
    
#     products.append(item)
# print(products)

# total_count = len(products)

# unique_products = set(products)
# unique_count = len(unique_products)

# most_common = None
# max_count = 0

# for product in unique_products:
#     count = products.count(product)
#     if count > max_count:
#         max_count = count
#         most_common = product


# print(f"Jami mahsulotlar soni: {total_count}")
# print(f"Unikal mahsulotlar soni: {unique_count}")

# if most_common:
#     print(f"Eng ko‘p olingan mahsulot: {most_common} ({max_count} marta)")
# else:
#     print("Mahsulot kiritilmadi.")
# ---

# ### 9️⃣ Katta topshiriq (Tuple + List + saralash)

# Talabalar `(ism, yosh, ball)` tuple ko‘rinishida kiritiladi.
# Dastur:

# * talabalarni ball bo‘yicha kamayish tartibida saralasin
# * eng yaxshi 3 talabani chiqarsin
# * o‘rtacha ballni hisoblasin
# Talabalar (ism, yosh, ball) tuple ko‘rinishida kiritiladi

# student = [("Donyor", 21, 78), ("Akmal", 23, 79), ("Bahrom", 25, 80)]
# students = []
# n = int(input("Nechta talaba kiritilsin: "))
# for i in range(n):
#     name = input("Ism: ")
#     age = int(input("Yosh: "))
#     score = int(input("Ball: "))
#     students.append((name, age, score))
# students.sort(key = lambda x: x[2], reverse=True)
# print(students)
# # print(student)
# print(f"Eng yaxshi 3ta talaba: {students[:3]}")

#================================================================

# students = []

# n = int(input("Nechta talaba kiritilsin: "))

# for i in range(n):
#     print(f"\n{i+1}-talaba ma'lumotlari:")
#     name = input("Ism: ")
#     age = int(input("Yosh: "))
#     score = int(input("Ball: "))
    
#     students.append((name, age, score))

# # Ball bo‘yicha kamayish tartibida saralash
# students.sort(key=lambda x: x[2], reverse=True)

# print("\nSaralangan ro'yxat (ball bo‘yicha kamayish):")
# for s in students:
#     print(s)

# # Eng yaxshi 3 talaba
# print("\nEng yaxshi 3 talaba:")
# for s in students[:3]:
#     print(s)

# # O‘rtacha ballni hisoblash
# total_score = 0
# for s in students:
#     total_score += s[2]

# average = total_score / len(students)

# print(f"\nO‘rtacha ball: {average:.2f}")

# ---

# ### 🔟 Juda katta murakkab loyiha (List + Tuple + Set fikrlash)

# Universitet tizimi yarating:

# Har talaba: `(ism, fakultet, kurs, fanlar_ro‘yxati)`

# Dastur:

# barcha unikal(takrorlanmagan) fanlarni aniqlasin
# eng ko‘p fan olgan talabani topsin
# har fakultetda nechta talaba borligini chiqarsin
# 3 tadan kam fan olgan talabalarni alohida ro‘yxatga ajratsin

# talabalar = [
#     ("Ali", "Informatika", 2, ["Matematika", "Fizika", "Dasturlash"]),
#     ("Vali", "Matematika", 1, ["Matematika", "Statistika"]),
#     ("Gulnora", "Informatika", 3, ["Matematika", "Dasturlash", "Fizika", "Algoritmlar"]),
#     ("Sardor", "Biologiya", 2, ["Biologiya", "Kimyo"]),
#     ("Nilufar", "Informatika", 1, ["Matematika", "Dasturlash"]),
#     ("Aziz", "Matematika", 2, ["Matematika", "Fizika", "Statistika"]),
# ]

# all_fanlar = set()
# for talaba in talabalar:
#     all_fanlar.update(talaba[3])

# print("Barcha unikal fanlar:", all_fanlar)

# max_fan_soni = 0
# eng_kop_fan_talaba = []
# for talaba in talabalar:
#     fan_soni = len(talaba[3])
#     if fan_soni > max_fan_soni:
#         max_fan_soni = fan_soni
#         eng_kop_fan_talaba = [talaba[0]]
#     elif fan_soni == max_fan_soni:
#         eng_kop_fan_talaba.append(talaba[0])

# print("Eng ko'p fan olgan talaba(talabalar):", eng_kop_fan_talaba, "(", max_fan_soni, "fan )")


# fakultetlar = {}
# for talaba in talabalar:
#     fakultet = talaba[1]
#     fakultetlar[fakultet] = fakultetlar.get(fakultet, 0) + 1

# print("Fakultetlar bo'yicha talabalar soni:", fakultetlar)