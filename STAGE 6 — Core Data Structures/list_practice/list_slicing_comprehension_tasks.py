# ^ Python dasturlash tilida
# ^ list creation, indexing, slicing, list comprehension, nested list mavzulariga
# ^ TOPSHIRIQ

# 1.
# 0 dan 10 gacha bo‘lgan juft sonlardan iborat list yarating.
# List comprehension ishlating.

# nums1 = [x for x in range(11) if x % 2 == 0]
# print(nums1)

# 2.
# Quyidagi listdan:
# • birinchi elementni
# • oxirgi elementni
# index yordamida ekranga chiqaring.
# colors = ["red", "green", "blue", "yellow"]

# colors = ["red", "green", "blue", "yellow"]
# print(colors[0], colors[-1])

# 3.
# Berilgan listdan faqat o‘rtadagi 3 ta elementni slicing yordamida ajratib oling.
# numbers = [10, 20, 30, 40, 50, 60, 70]

# numbers = [10, 20, 30, 40, 50, 60, 70]
# middle = numbers[2:5]
# print(middle)

# 4.
# Quyidagi listdagi barcha sonlarni 2 baravar oshirib, yangi list yarating.
# nums = [1, 2, 3, 4, 5]

# nums = [1, 2, 3, 4, 5]
# double = [x * 2 for x in nums]
# print(double)

# 5.
# Berilgan stringni listga aylantiring va faqat birinchi 4 ta harfni slicing yordamida oling.
# word = "Python"

# word = "Python"
# l = list(word)[0:4]
# print(l)

# 6.
# 0 dan 100 gacha bo‘lgan sonlardan 3 ga ham, 5 ga ham bo‘linadigan sonlardan iborat list yarating (list comprehension bilan).

# l = [i for i in range(100) if i % 3 == 0 and i % 5 == 0]
# print(l)

# 7.
# Berilgan listdan faqat string elementlarni olib, katta harfga o‘girib, yangi list
# yarating.
# data = [1, "python", True, "list", 3.14, "code"]

# data = [1, "python", True, "list", 3.14, "code"]

# new_list = [item.upper() for item in data if isinstance(item, str)]

# print(new_list)

# 8.
# 0 dan 20 gacha bo‘lgan sonlardan:
# • juft sonlar → kvadratga
# • toq sonlar → kubga
# o‘zgartirilgan list yarating.

# numbers = [x**2 if x % 2 == 0 else x**3 for x in range(21)]
# print(numbers)

# 9.
# Quyidagi nested listdan faqat markazdagi 2×2 qismni slicing orqali ajratib oling:
# matrix = [
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]
# ]

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(matrix[1:3])

# 10.
# Listni slicing yordamida teskari aylantiring, lekin reverse() ishlatmang.

# matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(matrix[::-1])

# 11.
# Quyidagi listda har 3-elementni olib, yangi list yarating:
# numbers = list(range(1, 31))

# numbers = list(range(1, 31))
# new_list = numbers[::3]
# print(new_list)

# 12.
# Stringlardan iborat list berilgan. Har bir so‘zning faqat oxirgi harfidan iborat list
# yarating.
# words = ["python", "java", "golang", "rust"]

# words = ["python", "java", "golang", "rust"]
# l = [i[-1] for i in words]
# print(l)

# 13.
# List ichidagi ichki listlarning faqat birinchi elementlarini ajratib oling:
# data = [[1,2,3],[4,5,6],[7,8,9]]

# data = [[1,2,3],[4,5,6],[7,8,9]]
# l = [i[0] for i in data]
# print(l)

# 14.
# Berilgan listdan slicing yordamida:
# • birinchi 3 elementni o‘chiring
# • oxirgi 2 elementni qoldiring

# data = [10, 20, 30, 40, 50, 60, 70]
# new_list = data[3:]
# print(new_list)

# last_two = data[-2:]
# print(last_two)

# 15.
# 0 dan 50 gacha bo‘lgan sonlardan palindrom bo‘lgan sonlar ro‘yxatini tuzing
# (masalan: 11, 22, 33).

# l = [i for i in range(50) if str(i) == str(i)[::-1]]
# print(l)

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

# matrix = [[1 if i == j else 0 for j in range(5)] for i in range(5)]

# for row in matrix:
#     print(row)

# tushunish uchun
# matrix = []

# for i in range(5):
#     row = []
#     for j in range(5):
#         if i == j:
#             row.append(1)
#         else:
#             row.append(0)
#     matrix.append(row)
# print(matrix)

# 17.
# Quyidagi listdan:
# • juft indexdagi elementlar → bitta list
# • toq indexdagi elementlar → boshqa list
# data = [10, 20, 30, 40, 50, 60, 70]

# 18.
# Stringlardan iborat listdan har bir so‘zning o‘rtadagi harfini ajratib oling
# (so‘z uzunligi doim toq deb hisoblang).

# words = ["python", "level", "world", "radar"]
# middle_letters = [word[len(word)//2] for word in words]
# print(middle_letters)

# 19.
# 0–100 oralig‘ida:
# • faqat raqamlari yig‘indisi 10 dan katta bo‘lgan sonlar listini tuzing.

# # numbers = [i for i in range(100) if (i // 10 + i % 10) > 10]
# numbers = [i for i in range(101) if sum(int(d) for d in str(i)) > 10]

# print(numbers)

# 20.
# Berilgan nested listni tekis (flat) listga aylantiring (list comprehension bilan):
# matrix = [[1,2],[3,4],[5,6]]

# matrix = [[1,2],[3,4],[5,6]]
# flat_list = [element for row in matrix for element in row]

# print(flat_list)

# 21.
# Quyidagi listni slicing yordamida:
# • birinchi yarmini
# • ikkinchi yarmini
# ikki alohida listga ajrating.
# nums = [1,2,3,4,5,6,7,8]

# nums = [1,2,3,4,5,6,7,8]

# mid = len(nums) // 2

# first_half = nums[:mid]
# second_half = nums[mid:]

# print(first_half)
# print(second_half)

# 22.
# Stringdan list yarating va:
# • faqat har ikkinchi harfni
# • teskari tartibda chiqaring.
# text = "programming"

text = "programming"
result = list(text)[1::2][::-1]
print(result)

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
