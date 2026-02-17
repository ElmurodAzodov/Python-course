"""
===========================================================
PYTHON STRING MASTERY – 83 TA TOPSHIRIQ
String Creation • Indexing • Slicing • Immutability
String Methods • Searching • Replacing
===========================================================
"""


# =========================================================
# 1–50: STRING CREATION, INDEXING, METHODS VA AMALIYOT
# =========================================================


# -----------------------
# STRING CREATION
# -----------------------

# 1. Foydalanuvchidan ism so‘ra va "Salom, <ism>!" ko‘rinishida chiqar.

# name = input("Ismingizni kiriting: ")
# print(f"Assalomu alaykum, {name}!")

# 2. Single quotes va double quotes yordamida 2 xil string yarat va chiqar.

# str1 = 'string 1'
# str2 = "string 2"
# print(str1, str2)

# 3. Triple quotes yordamida 3 qatorli matn yarat.

# triple = """This is a
# multi-line
# string"""
# print(triple)

# 4. Ikki stringni + operatori yordamida birlashtir.

# str1 = "Salom"
# str2 = "Dunyo"
# result = str1 + " " + str2
# print(result)

# 5. Berilgan stringni 5 marta takrorlab chiqar.

# str = "Text"
# print(str * 5)

# 6. Raw string yordamida path chiqar:
#    C:\Users\Admin\Desktop

# path = r"C:\Users\Admin\Desktop"
# print(path)

# 7. Sonni str() yordamida stringga aylantir va "Yosh: <son>" ko‘rinishida chiqar.

# son = 12
# son = str(son)
# print(f"Yosh: {son}")


# -----------------------
# INDEXING & BASIC TASKS
# -----------------------

# 8. Berilgan stringning birinchi va oxirgi belgisini chiqar.

s = "Python"
print("8. Birinchi belgi:", s[0])
print("   Oxirgi belgi:", s[-1])

# 9. String uzunligini chiqar va o‘rtadagi belgini aniqlang.
# 10. Stringni teskari qilib chiqar.
# 11. So‘z olib, har bir belgini indekslari bilan chiqar.
# 12. Faqat juft indeksdagi belgilarni chiqar.
# 13. Faqat toq indeksdagi belgilarni chiqar.
# 14. Oxirgi 4 ta belgini ajratib ol.
# 15. O‘rtadagi 3 ta belgini chiqar.
# 16. Birinchi yarmini ajratib ol.
# 17. Ikkinchi yarmini ajratib ol.
# 18. Stringni 3 xil usulda teskariga o‘gir:
#     slicing, loop, reversed()


# -----------------------
# STRING METHODS
# -----------------------

# 19. Matnni upper(), lower(), title() ko‘rinishida chiqar.
# 20. Barcha "a" harflarini "@" ga almashtir.
# 21. Matnda nechta "a" borligini hisobla.
# 22. Bosh va oxiridagi bo‘sh joylarni olib tashla.
# 23. Vergul bilan ajratilgan matnni listga ajrat.
# 24. Listdagi so‘zlarni "-" bilan birlashtir.
# 25. Matn faqat harflardan iboratmi tekshir.
# 26. Matn faqat raqamlardan iboratmi tekshir.
# 27. Email @gmail.com bilan tugaydimi tekshir.
# 28. Matn "Hello" bilan boshlanadimi tekshir.


# -----------------------
# ANALYSIS TASKS
# -----------------------

# 29. Palindrom ekanligini tekshir.
# 30. Matndagi so‘zlar sonini aniqlang.
# 31. Eng uzun so‘zni top.
# 32. Eng qisqa so‘zni top.
# 33. Katta harflar sonini aniqlang.
# 34. Kichik harflar sonini aniqlang.
# 35. Raqamlar sonini aniqlang.
# 36. Barcha raqamlarni ajratib yangi string yarat.
# 37. Barcha bo‘shliqlarni olib tashla.
# 38. Har bir so‘zning birinchi harfini katta qil (title() ishlatmasdan).
# 39. So‘zlar tartibini teskariga o‘gir (harflarni emas).


# -----------------------
# ADVANCED TASKS
# -----------------------

# 40. Substring necha marta uchrashini hisobla (count ishlatmasdan).
# 41. Oddiy password validator:
#     - kamida 8 belgi
#     - 1 ta katta harf
#     - 1 ta kichik harf
#     - 1 ta raqam
# 42. Maxsus belgilarni olib tashla (faqat harf va raqam qolsin).
# 43. Matnni snake_case ga o‘zgartir.
# 44. CamelCase formatga o‘zgartir.
# 45. Eng ko‘p takrorlangan harfni top.
# 46. Har bir harf nechta marta takrorlanganini dictionary ko‘rinishida chiqar.
# 47. Caesar cipher (shift=3) yoz.
# 48. Matndan barcha palindrom so‘zlarni ajratib ol.
# 49. Mini template engine yoz:
#     text = "Salom {name}, yoshingiz {age}"
# 50. Katta matnda:
#     - nechta so‘z
#     - nechta gap
#     - nechta harf
#     - nechta raqam
#     aniqlovchi funksiya yoz.


# =========================================================
# 51–83: SLICING • IMMUTABILITY • SEARCHING • REPLACING
# =========================================================


# -----------------------
# SLICING
# -----------------------

# 51. "Programming" dan:
#     - dastlabki 5 belgi
#     - oxirgi 4 belgi
#     - teskari ko‘rinish

# 52. Har 2-belgini ajrat.
# 53. Birinchi harfni slicing bilan kichik qil (immutability).


# -----------------------
# VALIDATION
# -----------------------

# 54. Username validator:
#     - faqat harf va raqam
#     - kamida 5 belgi
#     - "_" bilan boshlanmasin

# 55. Email tekshiruvchi.
# 56. Palindrom (bo‘shliq va registr hisobga olinmasin).


# -----------------------
# SEARCHING & REPLACING
# -----------------------

# 57. So‘zlarni ichma-ich teskariga aylantir.
# 58. Birinchi va oxirgi so‘zni almashtir.
# 59. "Python" nechta marta qatnashganini aniqlang.
# 60. Matnni tozalab, "python" → "Java" qil.
# 61. Telefon raqam formatlash.
# 62. Karta raqamini masklash.
# 63. So‘z uzunliklarini chiqar.
# 64. Case-insensitive replace.
# 65. Stringni 3-belgilik bloklarga bo‘lish.
# 66. Eng uzun so‘zni topish.
# 67. find() va index() farqini tekshir.
# 68. So‘zlarni alfabet tartiblash.


# -----------------------
# SENIOR TASKS
# -----------------------

# 69. Kuchli password tekshiruvchi.
# 70. replace() ishlatmasdan custom replace yoz.
# 71. HTML taglarni olib tashla.
# 72. Word frequency counter.
# 73. CamelCase → snake_case.
# 74. snake_case → CamelCase.
# 75. Overlapping substring hisoblash.
# 76. Dynamic template engine.
# 77. Text compression.
# 78. Text decompression.
# 79. Mini console text editor.
# 80. Caesar cipher (advanced).
# 81. Case-insensitive search engine.
# 82. Log analyzer (ERROR/WARNING/INFO).
# 83. Smart title formatter (and, or, the, of kichik qolsin).


# =========================================================
# END OF FILE
# =========================================================