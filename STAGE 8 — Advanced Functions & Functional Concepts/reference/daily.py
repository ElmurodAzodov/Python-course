# Stage 8

# def greet(name=0):
#     return f"Hello {name}"

# say_hello = greet

# print(say_hello("Ali")) #greet("Ali")
# print(type(say_hello))

# print(greet)

# ---------------------------------------------

# def sum(a, b):
#     return a + b
# print(sum(1, 2))

# sum = lambda a, b: a + b
# print(type(sum(1, 2)))

# print((lambda a, b: a + b)(1, 2))
# print(type((lambda a, b: a + b)(1, 2)))

# kv = lambda parametr: parametr ** 2
# print(kv(4))

# lmb = lambda: 3 + 4
# print(lmb())

# check = lambda x: "Even" if x % 2 == 0 else "Odd"

# print(check(10))
# print(check(7))


# ^ map() - map(function, iterable)
# * Listdagi har bir elementga bir xil funksiya qo‘llaydi.

# l = [2, 3, 4, 5, 6]

# def kub(a):
#     return a ** 3

# natija = list(map(kub, l))
# print(natija)

# natija = list(map(lambda a: a ** 3, l))
# print(natija)

# -------------------------------------------------

# names = ["ali", "vali", "hasan"]
# result = list(map(str.upper, names))
# print(result)


# numbers = ["1", "2", "3", "4"]
# result1 = list(map(int, numbers))
# print(result1)

# ------------------------------------------


# ^ filter() - filter(function, iterable)
# * List ichidan faqat shartga mos keladigan elementlarni qoldiradi.

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# def juft_sonlar(a):
#     return a % 2 == 0

# map_natija = list(map(lambda x: x ** 2, l))
# # filter_natija = list(filter(juft_sonlar, l))
# filter_natija = list(filter(lambda x: x % 2 == 0, l))


# print("Map:", map_natija)
# print("Filter: ", filter_natija)

# --------------------------------------------------------------

# words = ["apple", "hi", "banana", "ok"]

# result = list(filter(lambda w: len(w) > 3, words))  # funksiyada true bolsa saqlanadi, false bolsa saqlanmaydi

# print(result)


# --------------------------------------------------------------

# data = [0, 1, "", "hello", None, 5]

# result = list(filter(None, data))

# print(result)


# -----------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 6]

# result = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

# print(result)


# ^ reduce() - reduce(function, iterable, initializer)
# * Listdagi barcha elementlarni bitta natijaga yig‘adi.

# from functools import reduce

# l = [1,2,3,4,5,6,71,8,9,10]

# yigindi = reduce(lambda a, b: a + b, l, 2)
# katta = reduce(lambda a, b: a if a > b else b, l)

# print(f"Yig'indisi: {yigindi}")

# print(f"Eng kattasi {katta}")


# numbers = [1, 2, 3, 4, 5]

# result = reduce(lambda a, b: a + b, numbers)

# print(result)



#* map(function, iterable), filter(function, iterable), reduce(function, iterable, initializer)

#* Decorators

# 8ta belgi, birinchi katta harf, raqam va simvol

# Elmurod123.

#! def password_generator():
#!    pass

#& password_generator()

#& @password_generator()
#& def new_password_generator():
#&    pass:


#! eng kami 2ta raqam bo'lsin


def decorator(func):
    def wrapper():
        print("Boshlanish")
        func()
        print("Tugadi")
    return wrapper

def hello():
    print("Salom")

hello = decorator(hello)
hello()


@decorator
def hello():
    print("Salom")
