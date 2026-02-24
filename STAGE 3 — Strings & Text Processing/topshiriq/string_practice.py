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

# s = "Python"
# print("Birinchi belgi:", s[0])
# print("   Oxirgi belgi:", s[-1])

# 9. String uzunligini chiqar va o‘rtadagi belgini aniqlang.

# s = "Python"
# length = len(s)
# middle_index = length // 2
# print("String uzunligi:", length)
# print("   O'rtadagi belgi:", s[middle_index])

# 10. Stringni teskari qilib chiqar.

# s = "Python"
# print("Teskari string:", s[::-1])

# 11. So‘z olib, har bir belgini indekslari bilan chiqar.

# s = "Python"
# print("Belgilar indekslari bilan:")
# for i, char in enumerate(s):
#     print(f"   Indeks {i}: {char}")

# 12. Faqat juft indeksdagi belgilarni chiqar.

# s = "Python"
# print("Juft indeksdagi belgilar:", s[0::2])

# 13. Faqat toq indeksdagi belgilarni chiqar.

# s = "Python"
# print("Toq indeksdagi belgilar: ", s[1::2])

# 14. Oxirgi 4 ta belgini ajratib ol.

# s = "Python programming language"
# print("Oxirgi 4ta belgi: ", s[-4:])

# 15. O‘rtadagi 3 ta belgini chiqar.

# s = "Python"
# mid = len(s) // 2
# print(s[mid-1:mid+2])

# 16. Birinchi yarmini ajratib ol.

# s = "Python"
# first_half = s[:len(s)//2]
# print(first_half)

# 17. Ikkinchi yarmini ajratib ol.

# s = "Python"
# second_half = s[len(s)//2:]
# print(second_half)

# 18. Stringni 3 xil usulda teskariga o‘gir:
#     slicing, loop, reversed()

# s = "Python programming language"
# print(s[::-1])

# rev = ""
# for harf in s:
#     rev = harf + rev
# print(rev)

# print("".join(reversed(s)))

# -----------------------
# STRING METHODS
# -----------------------

# 19. Matnni upper(), lower(), title() ko‘rinishida chiqar.

# matn = "  salom dunyo, python dasturlash tili  "
# print("Upper:", matn.upper())
# print("Lower:", matn.lower())
# print("Title:", matn.title())

# 20. Barcha "a" harflarini "@" ga almashtir.

# matn = "  salom dunyo, python dasturlash tili  "
# a_almashtir = matn.replace('a', '@')
# print("a harflari @ ga almashtirildi:", a_almashtir)

# 21. Matnda nechta "a" borligini hisobla.

# matn = "  salom dunyo, python dasturlash tili  "
# a_soni = matn.count('a')
# print(f"Matnda {a_soni} ta 'a' harfi bor")

# 22. Bosh va oxiridagi bo‘sh joylarni olib tashla.

# matn = "  salom dunyo, python dasturlash tili  "
# tozalangan = matn.strip()
# print("Bo'sh joylardan tozalangan matn:", tozalangan)

# 23. Vergul bilan ajratilgan matnni listga ajrat.

# vergulli_matn = "olma,anor,banan,uzum"
# list_holat = vergulli_matn.split(',')
# print("List holati:", list_holat)

# 24. Listdagi so‘zlarni "-" bilan birlashtir.

# words = ["python", "is", "fun"]
# joined = "-".join(words)
# print(joined)

# 25. Matn faqat harflardan iboratmi tekshir.

# text1 = "HelloWorld"
# print(text1.isalpha())

# 26. Matn faqat raqamlardan iboratmi tekshir.

# text2 = "123456"
# print(text2.isdigit())

# 27. Email @gmail.com bilan tugaydimi tekshir.

# email = "user@gmail.com"
# print(email.endswith("@gmail.com"))

# 28. Matn "Hello" bilan boshlanadimi tekshir.

# text = "Hello world"
# print(text.startswith("Hello"))

# -----------------------
# ANALYSIS TASKS
# -----------------------

# 29. Palindrom ekanligini tekshir.

# word = "radar"
# if word == word[::-1]:
#     print(True)
# else:
#     print(False)


# 30. Matndagi so‘zlar sonini aniqlang.

# text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci. Aenean nec lorem."
# print(len(text.split()))

# 31. Eng uzun so‘zni top.

# text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci. Aenean nec lorem."
# words = text.split()
# eng_uzun = ""
# for i in words:
#     if len(i) > len(eng_uzun):
#         eng_uzun = i
# print(eng_uzun)

# 32. Eng qisqa so‘zni top.

# gap = input("Gap kiriting: ")
# sozlar = gap.split()

# if len(sozlar) > 0:
#     eng_qisqa = sozlar[0]

#     for soz in sozlar:
#         if len(soz) < len(eng_qisqa):
#             eng_qisqa = soz

#     print("Eng qisqa so'z:", eng_qisqa)
#     print("Uzunligi:", len(eng_qisqa))
# else:
#     print("Gap kiritilmadi.")

# 33. Katta harflar sonini aniqlang.

# gap = input("Gap kiriting: ")

# katta_soni = 0

# for belgi in gap:
#     if belgi.isupper():
#         katta_soni += 1

# print("Katta harflar soni:", katta_soni)

# 34. Kichik harflar sonini aniqlang.

# gap = input("Gap kiriting: ")

# kichik_soni = 0

# for belgi in gap:
#     if belgi.islower():
#         kichik_soni += 1

# print("Kichik harflar soni:", kichik_soni)

# 35. Raqamlar sonini aniqlang.

# gap = input("Gap kiriting: ")

# raqam_soni = 0

# for belgi in gap:
#     if belgi.isdigit():
#         raqam_soni += 1

# print("Raqamlar soni:", raqam_soni)

# 36. Barcha raqamlarni ajratib yangi string yarat.

# new_string = ""
# text = "Lorem 12ipsum 5set, dolor set1"
# for i in text:
#     if i.isdigit():
#         new_string += i
# print(new_string)

# 37. Barcha bo‘shliqlarni olib tashla.

# text = "Lorem 12ipsum 5set, dolor set1"
# natija = text.replace(" ", "")
# print(natija)

# 38. Har bir so‘zning birinchi harfini katta qil (title() ishlatmasdan).

# text = "Lorem 12ipsum 5set, dolor set1"
# list = text.split()
# text_update = ""
# for i in list:
#     text_update += i[0].upper() + i[1:] + " "
# print(text_update)
    
# 39. So‘zlar tartibini teskariga o‘gir (harflarni emas).

# text = "Python is great"
# reversed = " ".join(text.split(" ")[::-1])
# print(reversed)

# -----------------------
# ADVANCED TASKS
# -----------------------

# 40. Substring necha marta uchrashini hisobla (count ishlatmasdan).

matn = "salom salom dunyo salom"
sub = "salom"

soni = 0
for i in range(len(matn) - len(sub) + 1):
    if matn[i:i+len(sub)] == sub:
        soni += 1

print("Substring soni:", soni)

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
