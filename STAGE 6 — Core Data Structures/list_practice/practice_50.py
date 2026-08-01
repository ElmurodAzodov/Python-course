"""
DAILY.PY — SLICING MAVZUSI BO'YICHA MASHQLAR
==============================================
Jami: 50 ta masala
  - 25 ta O'RTACHA daraja
  - 25 ta MURAKKAB daraja

Qoidalar:
  - Faqat SLICING (ro'yxat kesish, list[boshlanish:tugash:qadam])
  - if/else shartlari
  - for/while looplar
  - list (ro'yxat) bilan ishlash
  - Har bir masaladan keyin yechim yozish uchun joy qoldirilgan.
  - O'zingiz yechib ko'ring, keyin javobni tekshiring.
"""


# ==================================================================
# 1-QISM: O'RTACHA DARAJA (25 ta masala)
# ==================================================================

# --- Masala 1 ---
# Berilgan ro'yxatning birinchi 5 ta elementini slicing orqali oling.
raqamlar = [3, 7, 1, 9, 4, 6, 2, 8, 5, 0]
# Yechim:


# --- Masala 2 ---
# Ro'yxatning oxirgi 4 ta elementini slicing yordamida chiqaring.
mevalar = ["olma", "nok", "uzum", "shaftoli", "gilos", "banan", "anor"]
# Yechim:


# --- Masala 3 ---
# Ro'yxatni [2:7] oralig'ida kesib oling va natijani chop eting.
sonlar = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Yechim:


# --- Masala 4 ---
# Ro'yxatni teskari tartibda chiqaring (slicing bilan, [::-1] dan foydalaning).
ismlar = ["Ali", "Vali", "Guli", "Doni", "Karim"]
# Yechim:


# --- Masala 5 ---
# Ro'yxatdan har ikkinchi elementni ([::2]) slicing orqali ajratib oling.
sonlar2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Yechim:


# --- Masala 6 ---
# Ro'yxatning o'rtasidagi 3 ta elementini slicing orqali toping (uzunlik toq son deb hisoblang).
royxat = [5, 10, 15, 20, 25, 30, 35]
# Yechim:


# --- Masala 7 ---
# Slicing yordamida ro'yxatni ikkiga bo'ling (chap va o'ng yarim) va ikkalasini alohida chop eting.
sonlar3 = [1, 2, 3, 4, 5, 6, 7, 8]
# Yechim:


# --- Masala 8 ---
# Berilgan ro'yxatdan faqat 3-elementdan (indeks 2) 6-elementgacha (indeks 6 kirmaydi) bo'lgan
# qismini oling, so'ng if yordamida uning uzunligi 4 ga tengligini tekshiring.
malumot = [11, 22, 33, 44, 55, 66, 77, 88]
# Yechim:


# --- Masala 9 ---
# for loop yordamida 1 dan 20 gacha bo'lgan ro'yxat yarating, so'ng slicing orqali
# faqat o'rtadagi 10 ta sonni ajratib oling.
# Yechim:


# --- Masala 10 ---
# Ro'yxatdagi manfiy qadam bilan (masalan [::-2]) slicing qilib, teskari tartibda
# har ikkinchi elementni chiqaring.
sonlar4 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Yechim:


# --- Masala 11 ---
# Foydalanuvchidan (yoki tayyor ro'yxatdan) 3 ta bo'lakka slicing orqali bo'lib,
# har bir bo'lakni alohida qatorda chop eting (for loop bilan).
harflar = list("abcdefghij")
# Yechim:


# --- Masala 12 ---
# Ro'yxatning birinchi yarmi va ikkinchi yarmini solishtiring: agar ular teng
# uzunlikda bo'lsa "Teng", aks holda "Teng emas" deb chiqaring (if/else).
royxat2 = [1, 2, 3, 4, 5, 6, 7]
# Yechim:


# --- Masala 13 ---
# Ro'yxatdan slicing yordamida faqat toq indeksdagi elementlarni oling,
# so'ng ularning yig'indisini for loop bilan hisoblang.
sonlar5 = [3, 6, 9, 12, 15, 18, 21, 24]
# Yechim:


# --- Masala 14 ---
# Matnni (string) slicing orqali 5 harfdan iborat bo'laklarga bo'lib,
# har bir bo'lakni alohida chop eting.
matn = "PythonDasturlashTiliJudaQiziq"
# Yechim:


# --- Masala 15 ---
# Ro'yxatdan boshidagi va oxiridagi bittadan elementni olib tashlab (slicing bilan),
# qolgan qismini yangi ro'yxatga saqlang.
royxat3 = [100, 200, 300, 400, 500, 600]
# Yechim:


# --- Masala 16 ---
# while loop yordamida ro'yxat bo'ylab yurib, har safar slicing bilan
# 2 tadan element olib, ularni chop eting.
sonlar6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Yechim:


# --- Masala 17 ---
# Ro'yxatning uzunligi juft yoki toqligini aniqlang (if/else), so'ng agar juft bo'lsa
# uni teng ikkiga, toq bo'lsa deyarli tengga slicing orqali bo'ling.
royxat4 = [4, 8, 15, 16, 23, 42]
# Yechim:


# --- Masala 18 ---
# Ro'yxatdagi eng katta 3 ta qiymatni sort qilib, so'ng slicing yordamida
# ulardan faqat oxirgi 3 tasini ajratib chiqaring.
sonlar7 = [45, 12, 78, 34, 90, 23, 56, 8]
# Yechim:


# --- Masala 19 ---
# Berilgan matnni slicing bilan teskari o'giring va u palindrom ekanligini
# if/else yordamida tekshiring.
soz = "dod"
# Yechim:


# --- Masala 20 ---
# Ro'yxatdan har 3-elementni ([::3]) slicing orqali oling va for loop bilan
# ularning o'rtacha qiymatini hisoblang.
sonlar8 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
# Yechim:


# --- Masala 21 ---
# Ro'yxatning birinchi n ta elementini (n — foydalanuvchi kiritadi yoki o'zgaruvchi
# sifatida berilgan) slicing orqali oling, agar n ro'yxat uzunligidan katta bo'lsa
# xabar chiqaring (if/else).
royxat5 = [7, 14, 21, 28, 35]
n = 8
# Yechim:


# --- Masala 22 ---
# Ro'yxatni 2 tadan bo'lib chiqadigan bo'laklarga (chunk) slicing va while loop
# yordamida ajrating.
sonlar9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Yechim:


# --- Masala 23 ---
# Matndan faqat unlilarni emas, balki slicing orqali har 2-harfni oling,
# so'ng natijada nechta harf borligini chop eting.
matn2 = "dasturlashqiziqarli"
# Yechim:


# --- Masala 24 ---
# Ro'yxatdagi manfiy indekslardan foydalanib ([-5:-1] kabi) oxiridan
# bo'lak oling va uni for loop bilan ekranga chiqaring.
sonlar10 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Yechim:


# --- Masala 25 ---
# Ro'yxatni slicing bilan uchga bo'ling (boshi, o'rtasi, oxiri) va har bir
# qismning yig'indisini solishtirib, eng katta yig'indili qismni if/else bilan aniqlang.
sonlar11 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Yechim:


# ==================================================================
# 2-QISM: MURAKKAB DARAJA (25 ta masala)
# ==================================================================

# --- Masala 26 ---
# Ro'yxatni slicing orqali teskari tartibga o'girib, so'ng for loop bilan
# har bir elementni asl holati bilan solishtirib, o'zgarmagan elementlar sonini toping.
royxat6 = [1, 2, 3, 2, 1]
# Yechim:


# --- Masala 27 ---
# Berilgan ro'yxatni k qadam bilan aylantiring (rotate): oxirgi k ta elementni
# boshiga olib o'ting, faqat slicing (konkatensatsiya bilan) yordamida bajaring.
royxat7 = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
# Yechim:


# --- Masala 28 ---
# Ro'yxatni ikkita teng bo'lakka slicing bilan bo'lib, ularni birma-bir (zip qilmasdan,
# for va indekslash bilan) qo'shib, yangi ro'yxat hosil qiling.
royxat8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Yechim:


# --- Masala 29 ---
# Matnda berilgan so'zni slicing yordamida boshqa so'z bilan (indekslarni topib)
# almashtiring, agar so'z topilmasa if/else orqali xabar bering.
matn3 = "Python dasturlash tili juda foydali"
qidiruv = "foydali"
almashtirish = "kuchli"
# Yechim:


# --- Masala 30 ---
# Ro'yxatni slicing orqali oynacha (sliding window, uzunligi 3) usulida
# ko'rib chiqing va har bir oynachaning yig'indisi 15 dan katta bo'lsa chop eting.
sonlar12 = [4, 5, 6, 7, 2, 8, 9, 1, 3]
# Yechim:


# --- Masala 31 ---
# Ro'yxatdagi elementlarni ikki guruhga (juft indeksli va toq indeksli) slicing
# orqali ajrating, so'ng ikkala guruhning yig'indisi orasidagi farqni toping.
sonlar13 = [12, 7, 4, 9, 15, 3, 8, 21, 6, 2]
# Yechim:


# --- Masala 32 ---
# Berilgan matnni slicing bilan uch qismga bo'ling va har bir qismning bosh
# harfini katta qilib, natijalarni birlashtiring (if/else yordamida qism bo'sh emasligini tekshiring).
matn4 = "salom dunyo qandaysiz"
# Yechim:


# --- Masala 33 ---
# Ro'yxat ichidan slicing yordamida faqat markazdagi elementlarni (chekka 2 tadan
# tashlab) oling va while loop bilan ularning ko'paytmasini hisoblang.
sonlar14 = [2, 3, 4, 5, 6, 7, 8]
# Yechim:


# --- Masala 34 ---
# Ikkita ro'yxatni slicing orqali navbatma-navbat (interleave) birlashtiring,
# agar uzunliklari teng bo'lmasa if/else bilan xabar bering.
royxatA = [1, 3, 5, 7]
royxatB = [2, 4, 6, 8]
# Yechim:


# --- Masala 35 ---
# Ro'yxatni slicing bilan teskari yo'nalishda 2 tadan guruhlab (masalan [::-1]
# dan keyin chunklab) chop eting.
sonlar15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Yechim:


# --- Masala 36 ---
# Berilgan matnda palindrom bo'lgan barcha 3 harfli bo'laklarni slicing va
# for loop yordamida toping (masalan "aba", "ded").
matn5 = "abababcdedxyzwvwx"
# Yechim:


# --- Masala 37 ---
# Ro'yxatni ikki qismga bo'lib (slicing), qaysi qismning yig'indisi kattaligini
# if/else bilan aniqlang, so'ng kichik qismni katta qism oxiriga slicing orqali biriktiring.
sonlar16 = [5, 2, 9, 1, 7, 3, 8, 4]
# Yechim:


# --- Masala 38 ---
# Matritsani (ro'yxatlar ro'yxati) slicing yordamida faqat o'rtadagi qatorlarni
# va har qatordan o'rtadagi ustunlarni oling.
matritsa = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
# Yechim:


# --- Masala 39 ---
# Ro'yxatdan slicing bilan barcha mumkin bo'lgan uzunligi 4 bo'lgan ketma-ket
# bo'laklarni for loop yordamida hosil qiling va har birining yig'indisini chop eting.
sonlar17 = [1, 4, 2, 8, 5, 7, 3, 9]
# Yechim:


# --- Masala 40 ---
# Berilgan ro'yxatni slicing bilan teng bo'lmagan uchta qismga (1:3:oxiri nisbatida)
# bo'ling va eng uzun qismni if/else orqali aniqlang.
royxat9 = list(range(1, 21))
# Yechim:


# --- Masala 41 ---
# Matnni so'zlarga bo'lmasdan, faqat slicing yordamida har 5 belgidan keyin
# "-" belgisini qo'shib chiqing (while loop bilan).
matn6 = "dasturlashvaslicingmavzusi"
# Yechim:


# --- Masala 42 ---
# Ro'yxatdagi elementlarni slicing orqali "oyna" (window) qilib siljitib, har bir
# oynadagi eng katta qiymatni for loop bilan toping (window uzunligi 4).
sonlar18 = [3, 9, 1, 7, 5, 12, 2, 8, 6]
# Yechim:


# --- Masala 43 ---
# Ikki ro'yxatning umumiy (kesishgan) qismini slicing va if orqali (indekslarini
# solishtirib) qo'lda toping — set() ishlatmasdan.
royxatC = [1, 2, 3, 4, 5, 6]
royxatD = [4, 5, 6, 7, 8, 9]
# Yechim:


# --- Masala 44 ---
# Ro'yxatni slicing bilan teskari tartibga o'girib, so'ng har uchinchi elementni
# olib tashlab (yangi ro'yxat yig'ib), natijani chop eting.
sonlar19 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Yechim:


# --- Masala 45 ---
# Berilgan matndagi eng uzun bir xil harflar ketma-ketligini (masalan "aaabbbccd"
# ichida "bbb") slicing va while loop yordamida toping.
matn7 = "aaabbbccddddde"
# Yechim:


# --- Masala 46 ---
# Ro'yxatni slicing orqali 4 ta teng (yoki deyarli teng) bo'lakka bo'ling va
# har bir bo'lakning o'rtacha qiymatini hisoblab, eng kattasini if/else bilan toping.
sonlar20 = [4, 8, 15, 16, 23, 42, 7, 3, 9, 11, 2, 6]
# Yechim:


# --- Masala 47 ---
# Berilgan ro'yxatda "o'sish" ketma-ketligini (har bir element oldingisidan katta)
# slicing yordamida bo'laklab, eng uzun o'suvchi bo'lakni for/if bilan toping.
sonlar21 = [1, 2, 3, 1, 4, 5, 6, 7, 2, 3]
# Yechim:


# --- Masala 48 ---
# Ikki matnni slicing yordamida bo'lakларга bo'lib (har biri teng uzunlikda),
# mos bo'laklarni solishtirib, nechta bo'lak bir xil ekanligini toping.
matnA = "abcdefgh"
matnB = "abzdefxh"
# Yechim:


# --- Masala 49 ---
# Ro'yxatni slicing bilan ikkiga bo'lib, birinchi yarmini teskari, ikkinchi
# yarmini to'g'ri tartibda birlashtirib, natijaviy ro'yxat palindrom ekanini
# if/else orqali tekshiring.
royxat10 = [1, 2, 3, 3, 2, 1]
# Yechim:


# --- Masala 50 ---
# Katta ro'yxatni (1 dan 50 gacha) slicing yordamida 5 tadan bo'laklarga bo'ling,
# har bir bo'lakdagi barcha sonlar 3 ga bo'linsa "Barchasi 3 ga bo'linadi",
# aks holda "Yo'q" deb for/if/else bilan chop eting.
royxat11 = list(range(1, 51))
# Yechim: