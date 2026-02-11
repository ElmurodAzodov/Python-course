
#^ Python dasturlash tilida 
#^ list creation, indexing, slicing, list comprehension, nested list mavzulariga 
#^ TOPSHIRIQ

# 1.
# 0 dan 10 gacha bo‘lgan juft sonlardan iborat list yarating. 
# List comprehension ishlating. 

nums1 = [x for x in range(11) if x % 2 == 0]
print("1:", nums1)

# 2.
# Quyidagi listdan: 
# • birinchi elementni 
# • oxirgi elementni 
# index yordamida ekranga chiqaring. 
# colors = ["red", "green", "blue", "yellow"] 

# 3.
# numbers = [10, 20, 30, 40, 50, 60, 70] 

# 4.
# Berilgan listdan faqat o‘rtadagi 3 ta elementni slicing yordamida ajratib oling. 
# Quyidagi listdagi barcha sonlarni 2 baravar oshirib, yangi list yarating. 
# nums = [1, 2, 3, 4, 5] 

# 5.
# Berilgan stringni listga aylantiring va: 
# • faqat birinchi 4 ta harfni 
# slicing yordamida oling. 
# word = "Python" 

# 6.
# 0 dan 100 gacha bo‘lgan sonlardan 3 ga ham, 5 ga ham bo‘linadigan sonlardan 
# iborat list yarating (list comprehension bilan). 

# 7.
# Berilgan listdan faqat string elementlarni olib, katta harfga o‘girib, yangi list 
# yarating. 
# data = [1, "python", True, "list", 3.14, "code"] 

# 8.
# 0 dan 20 gacha bo‘lgan sonlardan: 
# • juft sonlar → kvadratga 
# • toq sonlar → kubga 
# o‘zgartirilgan list yarating. 

# 9.
# matrix = [ 
# [1,2,3,4], 
# [5,6,7,8], 
# Quyidagi nested listdan faqat markazdagi 2×2 qismni slicing orqali ajratib oling: 
# [9,10,11,12], 
# [13,14,15,16] 
# ]

# 10.
# Listni slicing yordamida teskari aylantiring, lekin reverse() ishlatmang. 

# 11.
# Quyidagi listda har 3-elementni olib, yangi list yarating: 
# numbers = list(range(1, 31)) 

# 12.
# Stringlardan iborat list berilgan. Har bir so‘zning faqat oxirgi harfidan iborat list 
# yarating. 
# words = ["python", "java", "golang", "rust"] 

# 13.
# List ichidagi ichki listlarning faqat birinchi elementlarini ajratib oling: 
# data = [[1,2,3],[4,5,6],[7,8,9]] 

# 14.
# Berilgan listdan slicing yordamida: 
# • birinchi 3 elementni o‘chiring 

# 15.
# • oxirgi 2 elementni qoldiring 
# 0 dan 50 gacha bo‘lgan sonlardan palindrom bo‘lgan sonlar ro‘yxatini tuzing 
# (masalan: 11, 22, 33). 

# 16.
# Nested list yarating (5×5), faqat diagonal elementlari 1, qolganlari 0 bo‘lsin. 
# Natija: 
# [ 
# [1,0,0,0,0], 
# [0,1,0,0,0], 
# [0,0,1,0,0], 
# [0,0,0,1,0], 
# [0,0,0,0,1] 
# ]

# 17.
# Quyidagi listdan: 
# • juft indexdagi elementlar → bitta list 
# • toq indexdagi elementlar → boshqa list 
# data = [10, 20, 30, 40, 50, 60, 70] 

# 18.
# Stringlardan iborat listdan har bir so‘zning o‘rtadagi harfini ajratib oling 
# (so‘z uzunligi doim toq deb hisoblang). 

# 19.
# 0–100 oralig‘ida: 
# • faqat raqamlari yig‘indisi 10 dan katta bo‘lgan sonlar listini tuzing. 

# 20.
# Berilgan nested listni tekis (flat) listga aylantiring (list comprehension bilan): 
# matrix = [[1,2],[3,4],[5,6]] 

# 21.
# Quyidagi listni slicing yordamida: 
# • birinchi yarmini 
# • ikkinchi yarmini 
# ikki alohida listga ajrating. 
# nums = [1,2,3,4,5,6,7,8] 

# 22.
# Stringdan list yarating va: 
# • faqat har ikkinchi harfni 
# • teskari tartibda chiqaring. 
# text = "programming" 

# 23.
# Nested list ichidan: 
# • faqat juft sonlarni 
# • tekis list ko‘rinishida ajrating. 

# 24.
# 0 dan 100 gacha bo‘lgan sonlardan: 
# • faqat tub sonlar listini tuzing 
# (oddiy for + list comprehension kombinatsiyasi bilan). 

# 25.
# Quyidagi listdan: 
# • ichki listlar mustaqil object bo‘ladigan qilib 
# • 3×3 nol matritsa yarating 
# taqiqlanadi: 
# [[0]*3]*3