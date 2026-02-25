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

names = []
while True:
    n = input("Ismingizni kiriting: ")
    if n == "stop":
        break
    names.append(n)
print(names)
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

# ---

# ### 8️⃣ Murakkabroq mantiqiy topshiriq (List + Set)

# Do‘kon savatiga mahsulotlar kiritiladi (`stop` bilan tugaydi).
# Dastur:

# * jami mahsulotlar sonini
# * unikal mahsulotlar sonini
# * eng ko‘p olingan mahsulotni aniqlasin

# ---

# ### 9️⃣ Katta topshiriq (Tuple + List + saralash)

# Talabalar `(ism, yosh, ball)` tuple ko‘rinishida kiritiladi.
# Dastur:

# * talabalarni ball bo‘yicha kamayish tartibida saralasin
# * eng yaxshi 3 talabani chiqarsin
# * o‘rtacha ballni hisoblasin

# ---

# ### 🔟 Juda katta murakkab loyiha (List + Tuple + Set fikrlash)

# Universitet tizimi yarating:

# Har talaba: `(ism, fakultet, kurs, fanlar_ro‘yxati)`

# Dastur:

# * barcha unikal fanlarni aniqlasin
# * eng ko‘p fan olgan talabani topsin
# * har fakultetda nechta talaba borligini chiqarsin
# * 3 tadan kam fan olgan talabalarni alohida ro‘yxatga ajratsin

# ---

# Agar xohlasangiz, keyingi qadam sifatida men sizga:

# * 🟢 shu topshiriqlarning **yechimlarini bosqichma-bosqich**
# * 🟢 yoki **imtihon varianti ko‘rinishida PDF darajada**
# * 🟢 yoki **real mini-loyiha shakliga keltirib**

# ham tayyorlab berishim mumkin.
