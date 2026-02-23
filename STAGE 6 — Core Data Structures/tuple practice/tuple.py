# ============================================
# PYTHON TUPLES: PACKING, UNPACKING, IMMUTABILITY
# TOPSHIRIQLAR TO‘PLAMI (30 TA)
# ============================================

# 1. Uchta butun sonni alohida o‘zgaruvchilarga yozing
#    va tuple packing yordamida bitta tuple yarating.
#    Natijani ekranga chiqaring.



# 2. String, float va boolean qiymatlardan iborat tuple yarating
#    va uning type() ni tekshiring.

mixin = (str, float, bool)
print(type(mixin))

# 3. Bitta elementli tuple yarating.
#    Vergul bo‘lmasa nima bo‘lishini kod orqali isbotlang.


# 4. Ism, yosh va kasbdan iborat tuple yarating.
#    Unpacking yordamida ularni alohida o‘zgaruvchilarga ajrating
#    va ekranga chiqaring.


# 5. Ichida 3 ta son bo‘lgan list yarating.
#    Unpacking yordamida list elementlarini alohida o‘zgaruvchilarga ajrating.


# 6. 5 ta elementdan iborat tuple yarating.
#    first, *middle, last usuli bilan unpack qiling
#    va har birini alohida chiqaring.


# 7. Quyidagi tuple ni unpack qiling:
#    (1, (2, 3), 4)
#    Natijani to‘liq ekranga chiqaring.


# 8. Ikki o‘zgaruvchi yarating va
#    tuple unpacking (swapping) yordamida qiymatlarini almashtiring.


# 9. Funksiya yozing, u ikkita son qaytarsin.
#    Qaytgan qiymatlarni unpack qilib ekranga chiqaring.


# 10. Tuple immutable ekanligini isbotlash uchun
#     uning elementini o‘zgartirib ko‘ring
#     va qanday xato chiqishini izohlang.


# 11. 5 ta turli tipdagi elementdan iborat tuple yarating.
#     Unpacking orqali faqat string va int qiymatlarni alohida oling.


# 12. (1, 2, 3, 4, 5, 6) tuple ni
#     a, *b, c usuli bilan unpack qiling
#     va b ichida nechta element borligini aniqlang.


# 13. Ichida list bo‘lgan tuple yarating.
#     Tuple ichidagi listga yangi element qo‘shing
#     va natijani ekranga chiqaring.


# 14. List va tuple farqini kod orqali ko‘rsating
#     (list o‘zgaradi, tuple o‘zgarmaydi).


# 15. (x, y) ko‘rinishidagi koordinata tuple yarating.
#     Uni funksiya ichida unpack qilib ishlating.


# 16. Quyidagi nested tuple ni to‘liq unpack qiling:
#     (1, (2, (3, 4)), 5)


# 17. Tuple ni dict uchun key sifatida ishlating.
#     Natijani ekranga chiqaring.


# 18. Quyidagi ko‘rinishda tuple yarating:
#     (("Ali", 20), ("Vali", 22), ("Gani", 19))
#     Har bir talabani unpack qilib chiqaring.


# 19. Tuple immutable ekanligini buzmasdan,
#     uning birinchi elementini almashtirib
#     yangi tuple yarating.


# 20. Funksiya tuple qaytarsin.
#     Unpacking vaqtida o‘zgaruvchilar soni mos kelmasa
#     nima bo‘lishini tekshiring.


# 21. Ichida tuple va list bo‘lgan murakkab tuple yarating.
#     Qaysi qismini o‘zgartirish mumkin, qaysisini mumkin emasligini ko‘rsating.


# 22. Tuple ichida list bo‘lsa,
#     u dict uchun key bo‘la oladimi yoki yo‘qligini tekshiring.


# 23. (a, b, c, d, e) tuple dan
#     unpacking yordamida faqat b va d ni oling,
#     qolganlarini e’tiborsiz qoldiring.


# 24. Tuple unpacking yordamida
#     juft indeksdagi va toq indeksdagi elementlarni ajrating.


# 25. Funksiya yozing:
#     u tuple qabul qilsin va
#     * operator yordamida faqat o‘rta elementlarni qaytarsin.


# 26. Tuple immutable bo‘lsa ham,
#     oxirgi elementi o‘zgargandek ko‘rinadigan
#     yangi tuple yarating.


# 27. Quyidagi tuple ni to‘liq unpack qiling:
#     (id, name, (math, physics, english))


# 28. Funksiya yozing:
#     u tuple qabul qilsin va
#     unpacking orqali min va max qiymatlarni topib qaytarsin.


# 29. Real hayotga o‘xshash model yarating:
#     (user_name, (country, city), age)
#     Barcha qiymatlarni unpack qilib chiqaring.


# 30. Katta tuple berilgan bo‘lsin.
#     Unpacking yordamida:
#     - boshidagi 2 ta element
#     - oxiridagi 2 ta element
#     - o‘rtadagi elementlarni alohida listga ajrating.