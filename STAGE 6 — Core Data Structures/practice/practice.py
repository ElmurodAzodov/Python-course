# -*- coding: utf-8 -*-
"""
PYTHON DATA STRUCTURES — AMALIYOT MASALALARI (200 ta)
Mavzu: List, Tuple, Set, Dictionary
(faqat if-else, for/while sikllari va stringlar bilan yechiladi — funksiyasiz)

Fayl tuzilishi:
  - Har bir masala alohida izoh (comment) blokida berilgan.
  - Yechimingizni har bir masaladan keyin, xuddi shu joyga, oddiy kod
    (o'zgaruvchilar, if-else, for/while, list/tuple/set/dict amallari)
    yordamida yozing. Funksiya (def) ishlatish shart emas.
  - Qiyinchilik darajasi asta-sekin oshib boradi:
      1-50    -> OSON
      51-100  -> O'RTA
      101-150 -> QIYIN
      151-200 -> JUDA MURAKKAB
  - Mavzular (List/Tuple/Set/Dict) har bir daraja ichida aralashtirilgan.
"""


# ======================================================================
# DARAJA 1 — OSON (1-50-MASALALAR)
# ======================================================================

# ----------------------------------------------------------------------
# Masala 1 [LIST]
# Bo'sh list yarating va uni 'natija' nomli o'zgaruvchiga saqlang. Keyin uni
# ekranga chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 2 [LIST]
# [10, 20, 30, 40, 50] listini yarating va uning birinchi hamda oxirgi
# elementini alohida-alohida chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 3 [LIST]
# "salom" so'zini list() funksiyasi yordamida harflar listiga aylantiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 4 [LIST]
# [1, 2, 3] listini list() funksiyasi yordamida tuple'dan hosil qiling: avval
# (1,2,3) tuple yarating, so'ng listga aylantiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 5 [LIST]
# 5 ta noldan iborat list yarating (masalan, [0,0,0,0,0]) — multiplikatsiya
# operatoridan foydalaning.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 6 [TUPLE]
# (1, 2, 3, 4) tuple'ini yarating va uzunligini len() bilan chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 7 [TUPLE]
# Bitta elementdan iborat tuple yarating (masalan, faqat 7 sonidan) va uning
# turini type() bilan tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 8 [TUPLE]
# ("olma", "nok", "uzum") tuple'ining ikkinchi elementini chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 9 [SET]
# {1, 2, 2, 3, 3, 3} setini yarating va natijada nechta unik element qolganini
# chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 10 [SET]
# "mississippi" so'zidan set() yordamida unik harflar to'plamini hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 11 [SET]
# Bo'sh set yarating (set() funksiyasi bilan, {} emas) va sababini
# komментariyda tushuntiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 12 [DICT]
# {"ism": "Ali", "yosh": 20} dictionary yarating va "ism" kalitiga mos
# qiymatni chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 13 [DICT]
# Yuqoridagi dictionary'ga "shahar": "Samarqand" juftligini qo'shing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 14 [DICT]
# dict() funksiyasi yordamida a=1, b=2, c=3 kalit-qiymatli dictionary
# yarating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 15 [LIST]
# fruits = ["olma", "nok", "behi"] listiga append() metodi bilan "uzum"
# so'zini qo'shing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 16 [LIST]
# numbers = [5, 3, 8, 1] listini sort() metodi bilan o'sish tartibida
# saralang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 17 [LIST]
# numbers = [5, 3, 8, 1] listini reverse() metodi bilan teskari tartibga
# o'tkazing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 18 [LIST]
# colors = ["qizil", "sariq", "ko'k"] listidan pop() metodi yordamida oxirgi
# elementni olib tashlang va uni alohida o'zgaruvchida saqlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 19 [LIST]
# numbers = [1, 2, 3, 4, 5] listining indeks 1 dan 3 gacha (3-chi kirmaydi)
# qismini slicing orqali oling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 20 [LIST]
# numbers = [1, 2, 3, 4, 5] listini [::-1] slicing yordamida teskari tartibda
# chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 21 [TUPLE]
# person = ("Vali", 25) tuple'ini name, age o'zgaruvchilariga unpacking orqali
# ajrating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 22 [TUPLE]
# a = 3, b = 7 qiymatlarini vaqtinchalik o'zgaruvchisiz, tuple unpacking (a, b
# = b, a) orqali almashtiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 23 [SET]
# a = {1, 2, 3} va b = {3, 4, 5} setlari uchun union() (birlashma) natijasini
# chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 24 [SET]
# a = {1, 2, 3} va b = {2, 3, 4} setlari uchun intersection() (kesishma)
# natijasini chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 25 [DICT]
# student = {"ism": "Laylo", "ball": 87} dictionary'sidan get() metodi bilan
# "ball" qiymatini oling, agar mavjud bo'lmasa 0 qaytarsin.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 26 [DICT]
# student dictionary'sining barcha kalitlarini keys() metodi bilan, barcha
# qiymatlarini values() metodi bilan chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 27 [LIST]
# numbers = [1,2,3,4,5,6,7,8,9,10] listidan faqat juft sonlarni list
# comprehension yordamida ajratib oling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 28 [LIST]
# 1 dan 10 gacha bo'lgan sonlarning kvadratlaridan iborat list comprehension
# yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 29 [LIST]
# matrix = [[1,2],[3,4],[5,6]] nested listining matrix[1][0] elementini chop
# eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 30 [TUPLE]
# t = (10, 20, 30) tuple'ini o'zgartirishga (t[0] = 99) urinib ko'ring va
# qanday xatolik chiqishini komментариyda yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 31 [SET]
# s = {"olma", "nok"} setiga add() metodi bilan "uzum" elementini qo'shing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 32 [SET]
# s = {"olma", "nok", "uzum"} setidan discard() metodi bilan "nok" elementini
# xatosiz o'chiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 33 [DICT]
# narxlar = {"non": 3000, "sut": 8000} dictionary'sida "non" narxini update()
# metodi bilan 3500 ga o'zgartiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 34 [DICT]
# narxlar dictionary'sidan pop() metodi bilan "sut" kalitini o'chiring va
# qiymatini chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 35 [LIST]
# raqamlar = [10, 20, 30] listidagi 20 sonining index() metodi orqali o'rnini
# toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 36 [LIST]
# raqamlar = [1, 2, 2, 3, 2, 4] listida 2 soni nechta borligini count() metodi
# bilan aniqlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 37 [LIST]
# bo'sh list yarating, keyin uchta shahar nomini (Toshkent, Samarqand, Buxoro)
# append() bilan birma-bir qo'shing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 38 [TUPLE]
# (1, 2, 3) va (4, 5, 6) tuple'larini + operatori orqali birlashtirib, yangi
# tuple hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 39 [SET]
# ids = [101, 102, 103, 101, 104, 102] listidan set() yordamida takroriy
# elementlarni tozalang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 40 [DICT]
# config = {"host": "localhost", "port": 8080} dictionary'sida "port"
# mavjudligini 'in' operatori bilan tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 41 [LIST]
# numbers = [4, 8, 15, 16, 23, 42] listini clear() metodi bilan butunlay
# bo'shating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 42 [LIST]
# old_list = [1, 2, 3] listining copy() metodi yordamida mustaqil nusxasini
# yarating va nusxaga 4 sonini qo'shib, asl list o'zgarmasligini tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 43 [TUPLE]
# numbers = (5, 10, 15, 20) tuple'ida 15 soni bor-yo'qligini 'in' operatori
# bilan tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 44 [SET]
# a = {1,2,3,4} va b = {3,4,5,6} setlari uchun symmetric_difference()
# natijasini toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 45 [DICT]
# biriktirilgan = dict(shahar="Buxoro", aholi=280000) dictionary'sini yarating
# va ikkala qiymatini chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 46 [LIST]
# 1 dan 20 gacha bo'lgan sonlardan faqat 3 ga bo'linadiganlarini list
# comprehension bilan oling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 47 [LIST]
# so'zlar = ["olma", "behi", "anor"] listidagi har bir so'zni katta harflarga
# o'tkazuvchi yangi list yarating (list comprehension, .upper()).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 48 [TUPLE]
# coordinates = (41.31, 69.24) tuple'idan lat, lon o'zgaruvchilarini unpacking
# orqali oling va ularni chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 49 [SET]
# a = {10, 20, 30} setining b = {10, 20, 30, 40} setining subset (qism
# to'plami) ekanligini issubset() bilan tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 50 [DICT]
# talaba = {"ism": "Nodir"} dictionary'siga setdefault() metodi orqali "kurs":
# 1 qiymatini qo'shing (agar mavjud bo'lmasa).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ======================================================================
# DARAJA 2 — O'RTA (51-100-MASALALAR)
# ======================================================================

# ----------------------------------------------------------------------
# Masala 51 [LIST]
# numbers = [3, 1, 4, 1, 5, 9, 2, 6] listidan takroriy elementlarni olib
# tashlab, lekin asl tartibni saqlab qoladigan yangi list hosil qiling (set
# ishlatmasdan, tsikl orqali).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 52 [LIST]
# matrix = [[1,2,3],[4,5,6],[7,8,9]] uchun har bir qatordagi elementlar
# yig'indisidan iborat yangi list yarating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 53 [LIST]
# So'zlardan iborat words = ["banan", "olma", "behi", "uzum"] listini har bir
# so'zning uzunligi bo'yicha sort() metodiga key parametr berib saralang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 54 [LIST]
# numbers = [1,2,3,4,5,6,7,8,9,10] listini ikkiga — juft va toq sonlar listiga
# — bitta list comprehension yordamisiz, oddiy tsikl bilan ajrating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 55 [LIST]
# nested = [[1,2],[3,4]] listini nested[:] orqali "sayoz nusxalab" (shallow
# copy), so'ng nested_copy[0][0] ni o'zgartirib, bu asl listga ham ta'sir
# qilishini isbotlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 56 [LIST]
# 1 dan 50 gacha sonlardan faqat tub sonlarni (prime) list comprehension va
# yordamchi funksiya yordamida ajratib oling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 57 [TUPLE]
# students = [("Ali", 90), ("Vali", 85), ("Guli", 95)] list of tuple'lardan
# har birini for sikl bilan unpacking qilib, "Ism: X, Ball: Y" ko'rinishida
# chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 58 [TUPLE]
# numbers = (5, 12, 3, 8, 20, 1) tuple'idan min() va max() qiymatlarini bitta
# funksiya orqali (min_max deb nomlang) qaytaring va unpacking bilan qabul
# qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 59 [TUPLE]
# data = (1, (2, 3), (4, (5, 6))) — bir necha qavatli nested tuple'ni to'liq
# unpacking orqali barcha 6 ta sonni alohida o'zgaruvchilarga ajrating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 60 [TUPLE]
# raqamlar = (1,2,3,4,5,6,7,8) tuple'ini a, *b, c = raqamlar ko'rinishida
# unpacking qilib, birinchi, oxirgi va o'rtadagilarni alohida chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 61 [SET]
# matn1 = "python dasturlash" va matn2 = "dasturlash tili" so'zlaridagi umumiy
# so'zlarni set operatsiyalari yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 62 [SET]
# 1 dan 30 gacha bo'lgan sonlardan 3 ga bo'linadiganlar to'plami bilan 5 ga
# bo'linadiganlar to'plamining kesishmasini (ya'ni 15 ga bo'linadiganlarni)
# set orqali toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 63 [SET]
# a = {1,2,3,4,5} va b = {4,5,6,7,8} berilgan. a - b va b - a natijalarini
# alohida hisoblab, ular symmetric_difference'ga tengligini tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 64 [DICT]
# so'zlar = ["olma", "nok", "olma", "uzum", "nok", "olma"] listidan har bir
# so'z nechta marta takrorlanganini hisoblovchi dictionary (chastota lug'ati)
# tuzing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 65 [DICT]
# matn = "salom dunyo salom python" jumlasidagi har bir so'zning necha marta
# uchraganini dictionary orqali hisoblang (split() metodidan foydalaning).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 66 [DICT]
# narxlar = {"non": 3000, "sut": 8000, "tuxum": 1500} dictionary'sidan qiymati
# 3000 dan katta bo'lgan mahsulotlarni yangi dictionary sifatida ajratib oling
# (dict comprehension).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 67 [DICT]
# d1 = {"a":1, "b":2} va d2 = {"b":3, "c":4} dictionary'larini update() metodi
# bilan birlashtiring va "b" kaliti qanday qiymat olishini tushuntiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 68 [DICT]
# talabalar = {"Ali": 85, "Vali": 92, "Guli": 78} dictionary'sidan eng yuqori
# ballga ega talabani (ism va ball) max() funksiyasi va key parametri
# yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 69 [LIST]
# sonlar = [12, 45, 3, 67, 23, 89, 1] listining eng katta ikkita elementini
# sort() dan foydalanmasdan, faqat tsikl bilan toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 70 [LIST]
# shopping = ["non", "sut", "tuxum"] listiga foydalanuvchidan input() orqali
# yangi mahsulot nomini olib, insert(0, ...) yordamida ro'yxat boshiga
# qo'shing (kodni yozing, input() chaqiruvini ham qo'shing).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 71 [TUPLE]
# records = [("olma", 5, 3000), ("nok", 3, 4500)] — har bir tuple (nom, soni,
# narxi) dan iborat. Har biri uchun umumiy narxni (soni*narxi) hisoblab,
# natijalarni chop eting.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 72 [SET]
# ro'yxat_a = [1,2,2,3,4,4,5] va ro'yxat_b = [3,4,5,6,7] berilgan. Ikkala
# listda ham uchraydigan, lekin faqat bir marta chiqadigan elementlarni set
# orqali toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 73 [DICT]
# inventar = {"olma": 50, "nok": 30, "uzum": 0} dictionary'sidan qiymati 0
# bo'lgan mahsulotlarni topib, ularning nomlarini list ko'rinishida chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 74 [LIST]
# matrix = [[1,2,3],[4,5,6],[7,8,9]] ni transponirlang (qator va ustunlarni
# almashtiring), natija yangi nested list bo'lsin.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 75 [LIST]
# list1 = [1,2,3] va list2 = [4,5,6] larni zip() funksiyasi yordamida juftlab,
# [(1,4),(2,5),(3,6)] ko'rinishidagi list hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 76 [TUPLE]
# ("Toshkent", "Samarqand", "Buxoro", "Xiva") tuple'ini enumerate() bilan
# aylanib, har bir shahar oldiga tartib raqamini chiqaring (1-Toshkent,
# 2-Samarqand, ...).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 77 [SET]
# harflar1 = set("dasturlash") va harflar2 = set("algoritm") — ikkala so'zda
# umumiy bo'lmagan harflarni (symmetric_difference) toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 78 [DICT]
# telefon_kitobi = {} bo'sh dictionary yarating, so'ng foydalanuvchidan 3
# marta ism va telefon raqamini so'rab, dictionary'ga qo'shib boring (input()
# ishlatilsin).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 79 [LIST]
# sonlar = [5, -3, 8, -1, 0, 12, -7] listidan faqat manfiy sonlarni ajratib,
# ularning yig'indisini hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 80 [LIST]
# gaplar = ["Salom dunyo", "Python juda qiziq", "Men dasturlashni yaxshi
# ko'raman"] listidagi har bir gapdagi so'zlar sonini list comprehension bilan
# hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 81 [TUPLE]
# kunlar = ("Dush", "Sesh", "Chor", "Pay", "Jum", "Shan", "Yak") tuple'idan
# faqat dam olish kunlarini (oxirgi ikkitasini) slicing orqali ajrating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 82 [SET]
# a = {"Python", "Java", "C++"} va b = {"Java", "JavaScript", "Go"} — ikkala
# setda birga qo'shilgan, lekin har biri faqat bir marta chiqadigan tillar
# ro'yxatini toping va uni sortlangan list qilib chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 83 [DICT]
# sinf_jurnali = {"Ali": [80,90,85], "Vali": [70,75,60]} — har bir talaba
# uchun baholar o'rtachasini hisoblab, yangi dictionary {ism: o'rtacha}
# shaklida chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 84 [LIST]
# temperature = [23, 25, 19, 30, 28, 17, 22] haftalik harorat listidan eng
# issiq va eng sovuq kunning index()ini toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 85 [LIST]
# raqamlar = list(range(1, 21)) listini list comprehension yordamida faqat 3
# yoki 5 ga bo'linadigan sonlarga filtrlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 86 [TUPLE]
# vector1 = (2, 3) va vector2 = (4, 5) — ikkala vektorni qo'shib yangi tuple
# (x1+x2, y1+y2) hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 87 [SET]
# matn = "the quick brown fox jumps over the lazy dog" jumlasidagi unik
# harflar sonini (bo'shliqsiz) set yordamida hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 88 [DICT]
# buyurtma = {"pizza": 2, "cola": 3, "burger": 1} dictionary'sidagi barcha
# mahsulotlar sonini values() yordamida yig'indisini chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 89 [LIST]
# ism_familiya = ["Ali Karimov", "Vali Rashidov", "Guli Yusupova"] listidan
# faqat familiyalarni split() va list comprehension bilan ajratib oling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 90 [LIST]
# sonlar = [1,2,3,4,5] va koef = [10,20,30,40,50] — ikkala listni index
# bo'yicha ko'paytirib, yangi list [10,40,90,160,250] hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 91 [TUPLE]
# nuqtalar = [(1,2), (3,4), (5,6)] — har bir nuqtaning x va y koordinatalari
# yig'indisini hisoblab, natijalarni list qilib chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 92 [SET]
# sinf_a = {"Ali","Vali","Guli","Doston"} va sinf_b =
# {"Vali","Nodira","Doston","Aziz"} — faqat sinf_a'da bo'lgan, sinf_b'da
# bo'lmagan talabalarni toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 93 [DICT]
# mahsulotlar = {"laptop": 8000000, "telefon": 3500000, "planshet": 2500000} —
# narxi bo'yicha kamayish tartibida saralangan (mahsulot, narx) juftliklari
# listini, values() dan foydalanib eng kattasidan boshlab qidirib topish yo'li
# bilan (tayyor sort/lambda ishlatmasdan, faqat sikllar bilan) hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 94 [LIST]
# matn = "Bu juda qiziqarli dastur" jumlasini so'zlarga ajrating va har bir
# so'zni teskari tartibda yozib, yangi jumla hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 95 [LIST]
# sonlar = [4, 2, 9, 7, 5, 1, 8] listidan medianani (o'rtacha qiymatni) sort()
# yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 96 [TUPLE]
# rang_kod = ("qizil", 255, 0, 0) tuple'idan nomi va RGB qiymatlarini alohida
# unpacking qilib, "Rang: qizil, RGB: (255,0,0)" ko'rinishida chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 97 [SET]
# harflar = set("abcdefg") va unlilar = {"a","e"} — undosh harflarni (harflar
# - unlilar) difference orqali toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 98 [DICT]
# lug'at = {"salom": "hello", "rahmat": "thank you"} — foydalanuvchidan so'z
# kiritilganda uning tarjimasini get() bilan qaytaruvchi, topilmasa "Tarjima
# topilmadi" deb chiqaruvchi kod yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 99 [LIST]
# ikki_olchov = [[1,2,3],[4,5,6],[7,8,9]] listidagi barcha elementlarning
# yig'indisini nested tsikl orqali hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 100 [LIST]
# kitoblar =
# [{"nom":"Alkimyogar","yil":1988},{"nom":"1984","yil":1949},{"nom":"Sariq
# devni minib","yil":1965}] — dictionary'lardan iborat listni "yil" kaliti
# bo'yicha, faqat for sikli va list metodlari (masalan insert yoki
# almashtirish) yordamida, tayyor sort()/sorted() ishlatmasdan o'sish
# tartibida saralang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ======================================================================
# DARAJA 3 — QIYIN (101-150-MASALALAR)
# ======================================================================

# ----------------------------------------------------------------------
# Masala 101 [LIST]
# sonlar = [4, 5, 6, 7, 0, 1, 2] — aylantirilgan (rotated) saralangan listda
# berilgan sonni O(n) chiziqli qidiruv bilan toping va indexini qaytaring,
# topilmasa -1 qaytaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 102 [LIST]
# berilgan ikkita saralangan list list1 = [1,3,5,7] va list2 = [2,4,6,8,10] ni
# bitta saralangan listga birlashtiring, lekin sort() metodidan
# foydalanmasdan, merge algoritmi (ikki pointer) orqali yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 103 [LIST]
# matrix = [[1,2,3],[4,5,6],[7,8,9]] ni 90 gradusga soat strelkasi
# yo'nalishida aylantiring (natija yangi nested list bo'lsin,
# kutubxonalarsiz).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 104 [LIST]
# sonlar = [1,2,3,4,5,6,7,8,9] listini uchtadan qilib kichik listlarga bo'lib
# chiqing: [[1,2,3],[4,5,6],[7,8,9]] (umumiy uzunlik n ga bo'linmasa ham
# ishlaydigan yechim yozing).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 105 [LIST]
# sonlar = [2,7,11,15] va target = 9 berilgan. Listdagi ikkita sonning
# yig'indisi target'ga teng bo'ladigan indekslar juftligini toping (Two Sum
# masalasi, dictionary yordamida O(n) yechim).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 106 [LIST]
# matn_listi = ["anagram", "nagaram", "salom", "molas"] listidan bir-biriga
# anagram bo'lgan so'zlarni guruhlab, dictionary shaklida chiqaring (kalit —
# saralangan harflar, qiymat — so'zlar listi).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 107 [LIST]
# sonlar = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] listida eng ko'p uchraydigan
# (mode) sonni tsikl va dictionary yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 108 [LIST]
# matn = "((a+b)*(c-d))" qavslar ketma-ketligi to'g'ri joylashganligini
# list'ni stack sifatida ishlatib tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 109 [TUPLE]
# nested_data = (1, (2, 3, (4, 5)), 6, (7, (8, 9))) chuqur ichma-ich
# joylashgan tuple'dagi barcha butun sonlarni topib, ularning yig'indisini
# rekursiv funksiya yordamida hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 110 [TUPLE]
# coords = [(1,2), (4,6), (3,3), (0,0)] — har bir nuqtaning (0,0) koordinata
# boshidan masofasini hisoblab, nuqtalarni masofa bo'yicha eng yaqinidan
# uzog'iga sorted() bilan tartiblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 111 [SET]
# matn1 = "salom qanday ahvol yaxshimisiz" va matn2 = "yaxshi rahmat qanday
# siz ham" — ikkala matndagi so'zlar jaccard o'xshashligini hisoblang
# (kesishma/birlashma nisbati).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 112 [SET]
# graf = {"A": {"B","C"}, "B": {"A","D"}, "C": {"A"}, "D": {"B"}}
# ko'rinishidagi graf (dictionary of sets) berilgan. "A" tugunidan boshlab BFS
# (kenglik bo'yicha qidiruv) algoritmi yordamida barcha bog'langan tugunlarni
# toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 113 [SET]
# 1 dan 100 gacha bo'lgan sonlar orasidan Eratosfen g'alviri (Sieve of
# Eratosthenes) algoritmini set yordamida amalga oshirib, barcha tub sonlarni
# toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 114 [DICT]
# tranzaksiyalar = [{"turi":"kirim","summa":5000},{"turi":"chiqim","summa":200
# 0},{"turi":"kirim","summa":3000}] — umumiy kirim, umumiy chiqim va balansni
# hisoblovchi funksiya yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 115 [DICT]
# grafik = {} bo'sh dictionary'dan boshlab, edges =
# [("A","B"),("B","C"),("A","C")] ro'yxatidan adjacency list (qo'shnilik
# ro'yxati) shaklidagi graf tuzing (har bir tugun uchun qo'shnilar listi).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 116 [DICT]
# log_fayl = ["2024-01-01 ERROR disk full","2024-01-01 INFO
# started","2024-01-02 ERROR timeout","2024-01-02 ERROR timeout"] — har bir
# kun uchun ERROR xabarlar sonini hisoblovchi nested dictionary tuzing: {sana:
# {xabar: soni}}.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 117 [DICT]
# savdo = {"yanvar": {"olma":100,"nok":50}, "fevral": {"olma":80,"nok":70}} —
# har bir mahsulotning ikki oy davomidagi umumiy sotuvini hisoblovchi yangi
# dictionary tuzing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 118 [LIST]
# sonlar = [1,2,3,4,5,6,7,8,9,10] — slicing step (qadam) parametrini manfiy va
# musbat qiymatlar bilan sinab, [10,8,6,4,2] va [1,3,5,7,9] natijalarini bitta
# ifoda bilan hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 119 [LIST]
# parentez_muvozanati funksiyasini yozing: berilgan matndagi "()", "{}", "[]"
# qavslarning barchasi to'g'ri ochilib-yopilganini list (stack) yordamida
# tekshiradi.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 120 [TUPLE]
# namedtuple ishlatmasdan, oddiy tuple va indekslardan foydalanib "Talaba"
# ma'lumotlarini (ism, yosh, GPA) saqlovchi va GPA bo'yicha saralovchi dastur
# yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 121 [SET]
# matritsa_qatorlari = [{1,2,3},{2,3,4},{3,4,5}] — barcha qatorlarda umumiy
# (barchasida uchraydigan) elementlarni topish uchun intersection() ni ketma-
# ket qo'llang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 122 [DICT]
# so'z_grafigi = {} — matn = "men kitob o'qiyman men kino ko'raman men sport
# bilan shug'ullanaman" jumlasidan har bir so'zdan keyin qaysi so'z necha
# marta kelishini hisoblovchi (bigram chastotasi) dictionary tuzing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 123 [LIST]
# berilgan sonlar = [64, 34, 25, 12, 22, 11, 90] listini bubble sort algoritmi
# yordamida, tayyor sort() metodini ishlatmasdan qo'lda saralang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 124 [LIST]
# sonlar = [5, 2, 9, 1, 5, 6, 7, 3, 8, 4] listini insertion sort (kiritish
# orqali saralash) algoritmi yordamida, faqat while va for sikllari bilan,
# tayyor sort() ishlatmasdan saralang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 125 [LIST]
# sonlar = [10, 20, 30, 40, 50] listida binary search (ikkilik qidiruv)
# algoritmini rekursiv funksiya sifatida yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 126 [TUPLE]
# shaxmat_donalari = [("Ot", 2, 1), ("Piyoda", 4, 3), ("Vazir", 1, 4)] — har
# bir dona (nomi, x, y) tuple sifatida berilgan. Berilgan (x,y) katakka qaysi
# dona turganini toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 127 [SET]
# ikki_lug'at_orqali_anagram funksiyasi: ikki so'z bir-biriga anagram
# ekanligini Counter ishlatmasdan, faqat dictionary orqali tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 128 [DICT]
# kesh = {} bo'sh dictionary'dan boshlab, for sikli yordamida 1-dan 30-gacha
# bo'lgan Fibonachchi sonlarini bittalab hisoblab, har birini kesh[indeks] =
# qiymat ko'rinishida saqlab boring, so'ng foydalanuvchi so'ragan indeksdagi
# Fibonachchi sonini kesh['n']dan darhol chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 129 [LIST]
# matritsa = [[1,2,3],[4,5,6],[7,8,9]] ning "spiral" tartibida barcha
# elementlarini (soat strelkasi yo'nalishida aylanib) bitta list qilib
# chiqaring: [1,2,3,6,9,8,7,4,5].
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 130 [LIST]
# sonlar = [1,3,5,7,9,11,2,4] — listni ikkiga (juft va toq) ajratmasdan, aynan
# shu list ichida joyini almashtirib, avval barcha toq, keyin barcha juft
# sonlar kelishini in-place tarzda amalga oshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 131 [TUPLE]
# operatsiyalar = [("qo'shish",5,3), ("ayirish",10,4), ("ko'paytirish",6,7)] —
# har bir tuple'dagi amal nomini tekshirib, mos natijani hisoblovchi
# "kalkulyator" funksiyasi yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 132 [SET]
# matn_fayllar = {"fayl1": {"olma","nok","uzum"}, "fayl2": {"nok","behi"},
# "fayl3": {"uzum","anor"}} — barcha fayllarda birgalikda uchraydigan (kamida
# ikkitasida bor) so'zlarni toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 133 [DICT]
# invertiruemyy_indeks (inverted index) tuzing: hujjatlar = {"h1":"python juda
# qiziq", "h2":"python dasturlash tili", "h3":"dasturlash qiziq mashg'ulot"} —
# har bir so'z qaysi hujjatlarda uchrashini {so'z: {hujjat_id, ...}} shaklida
# saqlovchi dictionary tuzing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 134 [LIST]
# sonlar = [1,2,3,4,5] listining barcha mumkin bo'lgan qism to'plamlarini
# (subsets, bo'sh to'plam va o'zini ham qo'shib) rekursiya yordamida
# generatsiya qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 135 [LIST]
# sonlar_kombinatsiyasi funksiyasi: sonlar = [1,2,3] va target = 3 berilganda,
# listdagi elementlardan (takror ishlatmay) yig'indisi target'ga teng bo'lgan
# barcha kombinatsiyalarni toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 136 [TUPLE]
# vaqt_jadvali = [("09:00","10:30"), ("11:00","12:00"), ("10:00","11:30")] —
# bir-biriga to'g'ri keluvchi (overlapping) vaqt oraliqlarini topib chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 137 [SET]
# sonlar_ketma_ketligi = [100,4,200,1,3,2] listidagi eng uzun ketma-ket sonlar
# ketma-ketligining uzunligini (masalan, 1,2,3,4 -> 4) set yordamida O(n)
# vaqtda toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 138 [DICT]
# topologik_tartib uchun sodda misol: kurslar = {"Matematika2":
# ["Matematika1"], "Fizika": ["Matematika1"], "Matematika1": []} — har bir
# kursning oldin o'tilishi kerak bo'lgan kurslarini hisobga olib, to'g'ri
# o'qish tartibini (dependency resolution) dictionary va DFS asosida tuzing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 139 [LIST]
# sonlar = [3, 30, 34, 5, 9] listidagi sonlarni ularni yonma-yon qo'yganda eng
# katta sonni hosil qiladigan tartibda saralang (masalan, natija "9534330"
# bo'lishi kerak).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 140 [LIST]
# sonlar = [2, 3, 1, 1, 4] — har bir element shu joydan qancha qadam sakrash
# mumkinligini bildiradi (Jump Game). Boshidan oxirigacha yetib borish
# mumkinligini aniqlovchi funksiya yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 141 [TUPLE]
# intervallar = [(1,3), (2,6), (8,10), (15,18)] — kesishuvchi intervallarni
# birlashtirib, minimal sonli, kesishmaydigan intervallar listini hosil
# qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 142 [SET]
# sudoku_qatori = [5,3,'','','7','','','',''] kabi 9 ta elementli qatorda
# takroriy (bo'sh joylardan tashqari) raqamlar yo'qligini set yordamida
# tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 143 [DICT]
# valyuta_kurslari = {"USD":12500, "EUR":13600, "RUB":135} — foydalanuvchi
# kiritgan summani bir valyutadan boshqasiga (masalan USD dan EUR ga) UZS
# orqali konvertatsiya qiluvchi funksiya yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 144 [LIST]
# sonlar = [7,1,5,3,6,4] — aksiyalar narxi kunlar bo'yicha berilgan. Bitta
# marta sotib olib, bitta marta sotib, eng katta foyda olish mumkin bo'lgan
# qiymatni O(n) vaqtda toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 145 [LIST]
# sonlar = [-2,1,-3,4,-1,2,1,-5,4] — ketma-ket kelgan elementlarning maksimal
# yig'indisini (Kadane algoritmi) toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 146 [TUPLE]
# shartnoma_sanalari = [("2024-01-01","2024-03-01"),
# ("2024-02-15","2024-04-01")] — ikki shartnoma muddati bir-biriga to'g'ri
# kelib-kelmasligini (overlap) sana taqqoslash orqali aniqlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 147 [SET]
# ikki_massivning_kesishmasi funksiyasi: nums1 = [1,2,2,1] va nums2 = [2,2]
# berilganda, ularning kesishmasidagi har bir element takrorlanish soniga mos
# ravishda chiqishi kerak (natija: [2,2]) — bu yerda oddiy set intersection
# yetarli emasligini tushuntirib, to'g'ri yechim yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 148 [DICT]
# ikki_matn_izomorf funksiyasi: s = "egg", t = "add" — ikki so'z harflari
# orasida bir-birga mos (izomorf) almashtirish mavjudligini ikkita dictionary
# yordamida tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 149 [DICT]
# ikki_masofa_matritsasi: shaharlar orasidagi masofalar
# {("Toshkent","Samarqand"):300, ("Samarqand","Buxoro"):270,
# ("Toshkent","Buxoro"):450} dictionary shaklida berilgan. Ikki shahar
# orasidagi masofani, agar to'g'ridan-to'g'ri berilmagan bo'lsa, boshqa shahar
# orqali (masalan Toshkent-Samarqand-Buxoro) hisoblovchi funksiya yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 150 [LIST]
# sonlar = [1,5,11,5] listini ikkita teng yig'indili qism to'plamga (Partition
# Equal Subset Sum) ajratish mumkinligini dinamik dasturlash (list asosida)
# yordamida aniqlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ======================================================================
# DARAJA 4 — JUDA MURAKKAB (151-200-MASALALAR)
# ======================================================================

# ----------------------------------------------------------------------
# Masala 151 [LIST]
# LRU Cache (eng uzoq vaqt ishlatilmagan elementni chiqarib tashlash)
# g'oyasini list (tartib uchun) va dictionary (qiymatlar uchun) yordamida
# amalga oshiring: amallar = [("put","a",1), ("put","b",2), ("get","a"),
# ("put","c",3)] kabi amallar ro'yxatini for sikli bilan ketma-ket bajaring,
# sig'im=2 bo'lganda eng uzoq ishlatilmagan elementni o'chiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 152 [LIST]
# sonlar_streami: cheksiz keladigan sonlar oqimidan istalgan vaqtda oxirgi k
# ta sonning o'rtachasini O(1) vaqtda qaytaruvchi "Moving Average" klassini
# list orqali yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 153 [LIST]
# matritsalarni_ko'paytirish: A (m x n) va B (n x p) o'lchamli ikkita nested
# list (matritsa) berilganda, ularning ko'paytmasi bo'lgan yangi matritsani
# kutubxonalarsiz hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 154 [LIST]
# 4x4 shaxmat taxtasida (nested list, 0 — bo'sh, 1 — ferz) tasodifiy
# joylashtirilgan 4 ta ferz orasida bir-biriga xavf soladigan (bir qator, bir
# ustun yoki bir diagonalda turgan) juftliklar sonini faqat ichma-ich for
# sikllari bilan hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 155 [LIST]
# sonlar_massivi = [1,2,3] — uchta elementning barcha mumkin bo'lgan o'rin
# almashtirishlarini (permutatsiyalarini) faqat uchta ichma-ich for sikli
# yordamida (itertools va rekursiyasiz) qo'lda generatsiya qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 156 [LIST]
# eng_uzun_o'sib_boruvchi_ketma_ketlik (LIS): sonlar = [10,9,2,5,3,7,101,18]
# listida eng uzun o'sib boruvchi qism ketma-ketlik uzunligini dinamik
# dasturlash (DP list) yordamida O(n log n) yoki O(n^2) da toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 157 [LIST]
# sayohatchi_sotuvchi_masalasi (TSP) ning kichik versiyasi: 4 ta shahar
# orasidagi masofalar nested list (matritsa) ko'rinishida berilgan. Barcha
# shaharlarni bir marta aylanib chiqib, boshlang'ich shaharga qaytishning eng
# qisqa yo'lini, oldindan tayyorlangan barcha marshrut variantlari listi
# (masalan 6 ta variant) ustidan for sikli bilan yurib, eng kichigini tanlash
# orqali toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 158 [TUPLE]
# faqat tuple'lardan foydalanib (list ishlatmasdan) "o'zgarmas stack"
# g'oyasini amalga oshiring: har safar yangi element "qo'shilganda" eski tuple
# asosida yangi, kattaroq tuple hosil qiling (masalan stack=(); stack = stack
# + (1,); stack = stack + (2,) va h.k.), so'ng oxirgi elementni "chiqarish"
# uchun stack = stack[:-1] dan foydalanib, bir nechta amallar ketma-ketligini
# for sikli bilan bajaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 159 [TUPLE]
# koordinatalar_klasterlash: nuqtalar = [(1,1),(1,2),(2,1),(8,8),(8,9),(9,8)]
# — Evklid masofasi asosida oddiy "eng yaqin qo'shni" klasterlash algoritmini
# (kutubxonalarsiz) yozib, nuqtalarni ikki klasterga ajrating.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 160 [SET]
# graf_rang_berish (Graph Coloring): graf = {"A":{"B","C"}, "B":{"A","C"},
# "C":{"A","B","D"}, "D":{"C"}} — greedy algoritm yordamida har bir tugunga,
# qo'shni tugunlar bilan bir xil rang tushmaydigan tarzda minimal sondagi
# ranglarni tayinlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 161 [SET]
# union_find (Disjoint Set Union) tuzilmasini dictionary va set yordamida
# amalga oshirib, berilgan edges = [(1,2),(2,3),(4,5)] ro'yxatidan nechta
# bog'langan komponent borligini aniqlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 162 [SET]
# eng_qisqa_so'z_zanjiri (Word Ladder): begin = "hit", end = "cog",
# so'zlar_ro'yxati = {"hot","dot","dog","lot","log","cog"} — har safar bitta
# harf almashtirib begin dan end ga borishning eng qisqa qadamlar sonini BFS
# va set yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 163 [DICT]
# trie_daraxti (prefix tree) g'oyasini ichma-ich dictionary'lar yordamida
# amalga oshiring: so'zlar = ["kot", "kod", "kodlash"] listidagi har bir
# so'zni harflab, dictionary ichiga ichma-ich joylab qo'shib boring (for sikli
# bilan), so'ng berilgan "kod" prefiksi shu tuzilmada mavjudligini tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 164 [DICT]
# LFU (eng kam ishlatilgan elementni chiqarish) g'oyasini amalga oshiring: har
# bir kalitning necha marta so'ralganini alohida dictionary'da (masalan
# chastota) hisoblab boring, sig'im=3 ga to'lganda amallar =
# [("put","a",1),("put","b",2),("get","a"),("put","c",3),("put","d",4)]
# ro'yxatini for sikli bilan bajarib, eng kam chastotali kalitni o'chiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 165 [DICT]
# sinonimlar_grafida_narxlarni_hisoblash: ekvivalensiyalar =
# [("a","b"),("b","c")], qiymatlar = [2.0, 3.0], so'rovlar =
# [("a","c"),("b","a"),("a","e")] — a/b=2, b/c=3 kabi nisbatlar asosida
# so'ralgan nisbatlarni graf (dictionary of dict) va DFS orqali hisoblang,
# topilmasa -1.0 qaytaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 166 [LIST]
# sudoku_yechuvchi: 9x9 nested list ko'rinishidagi to'liqsiz sudoku jadvalini
# backtracking algoritmi va set (qator/ustun/blok tekshiruvi uchun) yordamida
# to'liq yeching.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 167 [LIST]
# matritsada_orol_soni (Number of Islands): grid =
# [[1,1,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]] — 0/1 lardan iborat matritsada
# bir-biriga tutash (yuqori/past/chap/o'ng) 1 lardan tashkil topgan "orollar"
# sonini DFS/BFS va set (ziyorat qilinganlarni belgilash) orqali toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 168 [LIST]
# ustuvorlik navbati (Priority Queue) g'oyasini oddiy list yordamida (heapq
# ishlatmasdan) amalga oshiring: qiymatlarni list'ga qo'shib boring, har safar
# navbatdan "olish" kerak bo'lganda listning eng kichik elementini topib, uni
# min() va remove() (yoki tsikl) yordamida chiqarib tashlang; buni amallar =
# [("qo'shish",5),("qo'shish",2),("olish",),("qo'shish",8),("olish",)]
# ro'yxati asosida sinab ko'ring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 169 [TUPLE]
# vaqt_zonasi_konvertori: sozlamalar = (("Toshkent", 5), ("Moskva", 3),
# ("London", 0), ("Nyu-York", -5)) — UTC farqlari asosida bir shahardagi
# vaqtni boshqa shahar vaqtiga o'girib beruvchi funksiya yozing (soat,
# shahar1, shahar2 argumentlari bilan).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 170 [SET]
# eng_kichik_qamrab_oluvchi_intervalllar_soni: nuqtalar to'plamlari =
# [{1,2,3},{2,3,4},{5,6},{6,7,8}] — bu to'plamlarni bog'langan (kesishuvchi)
# guruhlarga birlashtirib, nechta mustaqil guruh borligini set operatsiyalari
# orqali aniqlang (union-find yoki iterativ birlashtirish bilan).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 171 [DICT]
# vazifalar_rejalashtiruvchisi: vazifalar = {"A": {"muddat":2,"foyda":100},
# "B": {"muddat":1,"foyda":19}, "C": {"muddat":2,"foyda":27}, "D":
# {"muddat":1,"foyda":25}} — har bir vazifani belgilangan muddatgacha bajarib,
# umumiy foydani maksimal qiladigan tartibni greedy algoritm bilan toping (Job
# Sequencing masalasi).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 172 [LIST]
# matritsa_yo'lini_topish: grid = [[1,3,1],[1,5,1],[4,2,1]] — chap yuqori
# burchakdan o'ng past burchakkacha faqat o'ngga yoki pastga yurib, yo'l
# ustidagi sonlar yig'indisi eng kichik bo'ladigan yo'lni dinamik dasturlash
# (DP jadval sifatida nested list) bilan toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 173 [LIST]
# eng_uzun_umumiy_qism_ketma_ketlik (LCS): s1 = "ABCBDAB", s2 = "BDCABA" —
# ikki satrning eng uzun umumiy qism ketma-ketligini dinamik dasturlash
# jadvali (2D list) yordamida toping va uzunligini qaytaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 174 [LIST]
# knapsack_masalasi (0/1 Ryukzak): og'irliklar = [1,3,4,5], qiymatlar =
# [1,4,5,7], sig'im = 7 — har bir buyumni yoki olish, yoki olmaslik sharti
# bilan maksimal qiymat to'plash mumkin bo'lgan variantni DP (2D list)
# yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 175 [TUPLE]
# poligon_yuzasi (Shoelace formula): cho'qqilar = [(0,0),(4,0),(4,4),(0,4)] —
# koordinatalar tuple'lari ro'yxati asosida ko'pburchakning yuzasini Shoelace
# formulasi bilan hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 176 [SET]
# eng_kichik_o'zgarish_masofasi (Levenshtein distance) ni set/dict aralashmasi
# bilan emas, balki to'liq DP (2D list) yordamida hisoblab, ikkita so'z
# ("kitten", "sitting") orasidagi minimal tahrirlash masofasini toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 177 [DICT]
# moliyaviy_tranzaksiyalar_grafida_qarzlarni_kamaytirish: qarzlar =
# [("A","B",10), ("B","C",5), ("A","C",5)] (A B ga 10, B C ga 5, A C ga 5
# qarzdor) — har bir shaxsning yakuniy balansini dictionary orqali hisoblab,
# minimal sonli tranzaksiyalar bilan barcha qarzlarni yopish rejasini tuzing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 178 [LIST]
# sensor_ma'lumotlarini_tekislash (data smoothing): o'lchovlar = [10, 12, 11,
# 50, 13, 12, 14, 60, 15] — median filter (har bir nuqta atrofidagi 3 ta
# qiymat medianasi) yordamida keskin sakrashlarni (outlier) tekislovchi list
# hosil qiling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 179 [LIST]
# matritsa_determinantini_hisoblash: 3x3 yoki undan katta nested list
# ko'rinishidagi matritsaning determinantini rekursiv "kofaktorlar bo'yicha
# yoyish" (cofactor expansion) usuli bilan, kutubxonalarsiz hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 180 [TUPLE]
# GPS_marshrut_optimallashtirish: manzillar = [("uy",0,0), ("do'kon",3,4),
# ("ish",6,8), ("maktab",1,1)] — koordinatalar (nom,x,y) tuple ko'rinishida
# berilgan, "uy"dan boshlab barcha manzillarni eng qisqa umumiy masofa bilan
# aylanib chiqish tartibini greedy nearest-neighbor algoritmi bilan toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 181 [SET]
# ijtimoiy_tarmoq_tavsiyasi: do'stlik = {"Ali":{"Vali","Guli"},
# "Vali":{"Ali","Doston"}, "Guli":{"Ali","Doston"}, "Doston":{"Vali","Guli"}}
# — "Ali" uchun "do'stlarning do'stlari, lekin hali do'st bo'lmaganlar"
# tavsiyasini set operatsiyalari bilan toping va har bir nomzod uchun umumiy
# do'stlar sonini hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 182 [DICT]
# so'rovlar_keshi = {} — so'rovlar = ["a","b","a","c","b","a"] ro'yxati
# bo'yicha for sikli bilan yurib, agar so'rov keshda bo'lmasa
# "hisoblanmoqda..." deb chop etib natijani (masalan uzunligini) hisoblab
# keshga saqlang, agar keshda bo'lsa to'g'ridan-to'g'ri keshdan oling — shu
# tarzda takroriy hisoblashning oldini oling.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 183 [LIST]
# matn_siqish_algoritmi (Run-Length Encoding): satr = "aaabbbcccdaa" — ketma-
# ket takrorlanuvchi belgilarni (belgi, soni) juftliklaridan iborat listga
# siqib, so'ng orqaga (dekodlab) qayta tiklovchi ikkita funksiya yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 184 [LIST]
# matritsa_ustida_konvolyutsiya: rasm = 5x5 nested list, yadro (kernel) = 3x3
# nested list — oddiy 2D konvolyutsiya amalini (rasmni yadro bilan
# "o'tkazish") kutubxonalarsiz, faqat nested tsikllar bilan amalga oshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 185 [TUPLE]
# shaxmat_ot_yurishi: 5x5 shaxmat taxtasida ot (0,0) katakdan turibdi. Otning
# shu katakdan bir yurishda borishi mumkin bo'lgan barcha katta-kichik (x,y)
# koordinatalarini (tuple ko'rinishida) sakkizta mumkin bo'lgan yo'nalish
# bo'yicha topib, taxta chegarasidan chiqib ketmaydiganlarini list qilib
# chiqaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 186 [SET]
# eng_kam_sondagi_avtobuslar_bekati_bilan_barcha_shaharlarni_qamrab_olish (Set
# Cover masalasi): shaharlar = {1,2,3,4,5,6,7}, bekatlar = [{"B1":{1,2,3}},
# {"B2":{2,4}}, {"B3":{3,4,5}}, {"B4":{4,5,6,7}}] — greedy set cover algoritmi
# bilan barcha shaharlarni qamrab oluvchi minimal sondagi bekatlarni tanlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 187 [DICT]
# qoidalar = {"NP": ["Det N", "N"], "VP": ["V NP"], "S": ["NP VP"]} —
# soddalashtirilgan grammatika qoidalari dictionary shaklida berilgan.
# Berilgan "S" belgisini shu qoidalar bo'yicha ochib, hosil bo'lishi mumkin
# bo'lgan barcha ketma-ketliklarni (masalan "NP VP" -> "Det N V NP" -> "Det N
# V Det N" yoki "Det N V N") faqat while sikli va string almashtirish
# (replace) yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 188 [LIST]
# sonlar_ketma_ketligidan_maksimal_kvadrat (Maximal Square): matritsa =
# [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]] — faqat 1 lardan tashkil
# topgan eng katta kvadrat maydonni dinamik dasturlash (2D list) yordamida
# toping va uning yuzasini qaytaring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 189 [LIST]
# taxta = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] va so'z =
# "ABCC" — 2D harflar taxtasida berilgan so'zning har bir keyingi harfi
# oldingi harfga faqat gorizontal yoki vertikal qo'shni (bir marta ishlatilgan
# katakka qaytmasdan) joylashgan yo'l mavjudligini, boshlanish nuqtasi
# sifatida taxtadagi har bir "A" katakdan boshlab, ichma-ich for/while
# sikllari va bir yordamchi "ziyorat qilingan katakchalar" listi bilan
# tekshiring.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 190 [TUPLE]
# eng_yaqin_k_ta_nuqta (K Closest Points): nuqtalar =
# [(1,3),(-2,2),(5,8),(0,1)] va k=2 — koordinata boshiga eng yaqin k ta
# nuqtani, masofalarni tuple sifatida saqlab, sorted() yordamida toping (heapq
# ishlatmasdan).
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 191 [SET]
# minimal_yoyuvchi_daraxt (Minimum Spanning Tree) ning soddalashtirilgan
# Kruskal algoritmi: qirralar =
# [("A","B",1),("B","C",2),("A","C",3),("C","D",4)] (tugun1,tugun2,og'irlik) —
# union-find (set orqali) yordamida minimal umumiy og'irlikdagi bog'lovchi
# daraxtni toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 192 [DICT]
# moliyaviy_portfel_muvozanatlashtirish: portfel = {"aksiya_A":
# {"ulush":0.4,"joriy_narx":120,"boshlang'ich_narx":100}, "aksiya_B":
# {"ulush":0.6,"joriy_narx":80,"boshlang'ich_narx":100}} — har bir aksiyaning
# foyda/zarar foizini hisoblab, portfelni qayta muvozanatlash uchun qaysi
# aksiyalarni sotish yoki sotib olish kerakligini aniqlovchi hisobot
# dictionary orqali tuzing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 193 [LIST]
# eng_uzun_palindromik_qism_satr (Longest Palindromic Substring): satr =
# "babadada" — berilgan satrdagi eng uzun palindrom (orqa-oldiga bir xil
# o'qiladigan) qism satrni dinamik dasturlash (2D list) yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 194 [LIST]
# eng_uzun_qavslar_ketma_ketligi (Longest Valid Parentheses): satr = ")()())"
# — faqat to'g'ri joylashgan qavslardan tashkil topgan eng uzun qism satr
# uzunligini stack (list) yordamida toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 195 [LIST]
# suv_saqlash_masalasi (Trapping Rain Water): balandliklar =
# [0,1,0,2,1,0,1,3,2,1,2,1] — har bir ustun orasida qancha yomg'ir suvi
# to'planishi mumkinligini ikki pointer usuli bilan hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 196 [TUPLE]
# 3D_vektor_amallari: v1 = (1,2,3) va v2 = (4,5,6) tuple ko'rinishidagi 3
# o'lchamli vektorlarning skalyar (dot) va vektor (cross) ko'paytmalarini
# kutubxonalarsiz hisoblovchi funksiyalar yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 197 [SET]
# eng_kichik_farqli_ikki_massiv_elementi: nums1 = [1,2,3,10] va nums2 =
# [2,3,4,5] — nums1 elementidan nums2 elementini ayirganda hosil bo'ladigan
# eng kichik musbat farqni set/sorted yordamida samarali toping.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 198 [DICT]
# student_reyting_tizimi: baholar = {"Ali":[85,90,78], "Vali":[92,88,95],
# "Guli":[70,75,80]} — har bir talabaning o'rtacha bahosi, eng yuqori va eng
# past bahosini hisoblab, natijalarni reyting (o'rtacha bo'yicha kamayish
# tartibida) shaklida chiqaruvchi to'liq hisobot funksiyasi yozing.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 199 [LIST]
# maqsad_satr = "PYTHON" va boshlang'ich = "AAAAAA" — random modulidan
# foydalanib, har bir "avlod"da tasodifiy bitta harfni maqsad satrdagi mos
# harfga almashtirib boring va while sikli yordamida, joriy satr maqsad satrga
# teng bo'lguncha, necha "avlod" (iteratsiya) ketganini hisoblang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing:



# ----------------------------------------------------------------------
# Masala 200 [DICT]
# moliyaviy_operatsiyalar_jurnali: operatsiyalar =
# [{"sana":"2024-01-01","kategoriya":"oziq-ovqat","summa":50000},
# {"sana":"2024-01-02","kategoriya":"transport","summa":15000},
# {"sana":"2024-01-01","kategoriya":"oziq-ovqat","summa":30000}] —
# kategoriyalar bo'yicha va sanalar bo'yicha guruhlangan ikkita alohida
# hisobotni (nested dictionary) tuzing hamda eng ko'p xarajat qilingan
# kategoriyani aniqlang.
# ----------------------------------------------------------------------
# Yechimingizni shu yerga yozing: