# List
# list creation, indexing, slicing, list comprehension, nested list
# [...]
# (...) , {...}

l = []
l1 = list()
# Bo'sh list
my_list = []

# Elementlar bilan list
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", 3.14, True]

print(numbers)
print(mixed)


# my_list = []
# print(type(my_list))
# print(bool(my_list))

# numbers = [1, 2, 3, 4, 5]
# fruits = ["apple", "banana", "cherry"]
# mixed = [1, "apple", 3.14, True]
# list_aralash = [True, None, "string", 12, 12.3, KeyError]
# print(list_aralash)
# print(numbers)
# print(mixed)

# ism = list("Elmurod")
# print(ism)
# for ozgaruvchi in range(10):
#     print(ozgaruvchi)
# l = [ozgaruvchi for ozgaruvchi in range(10)]
# print(l)

# l = []
# for i in range(10):
#     if i % 2 == 0:
#         l.append(i)
# print(l)

# evens = [i for i in range(10) if i % 2 == 0]
# print(evens)


# List comprehension 
# 0 dan 9 gacha sonlar ro'yxati
numbers = [i for i in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Faqat juft sonlar
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Har bir elementni kvadratga ko‘tarish
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# String elementlardan katta harfni olish
words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
print(upper_words)


# l = [2] * 4
# print(l)

# l = [["apple", "banana"], ["Akbar", "Bobur"], 12, 12.3]
# print(l[0][1])

# nested = [[1,2,3], 2, 3]
# nested[0][0] = 9
# print(nested)


# a = []
# for i in range(10):
#     a.append(i)
# print(a)



fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0:2])


# matrix = [[1, 2, 3], [4, 5, 6, 34, 45, 57], [7, 8, 9, 12, 13]]

# print(matrix[2][3])
