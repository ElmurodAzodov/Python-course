# string - upper()

# str = "Hello world!"
# katta = str.upper()
# print(katta)


# -----------------------
# def qoshish(a, b):
#     return a+b
# natija = qoshish(1,2)
# print(natija)

# -----------------------

# def sum(a, b):
#     # print(a+b)
#     return a+b

# natija = sum(11, 212312313)
# print(natija)
# -----------------------


# def salom(ism = "Elmurod"):
#     print("Salom", ism)

# salom("Developer")

# ----------------------


# def info(ism, yosh, malumoti):
#     print(f"Natija holatiga ko'ra uning ismi {ism}, yoshi esa {yosh}, va u {malumoti} toifali")

# info(yosh = 12, malumoti="oliy", ism="Akmal")
# # info("Akmal", 12, "o'qimagan")

# ---------------------------------------------

# def sum(a, b):
#     return a+b

# def summ(d, c):
#     print(sum(d, c))

# summ(2, 3)
# M = []

# def func(a, l = None):
#     if l is None:
#         l = []
#         l.append(a)
#     return l

# print(func(2))


# -----------------------------------------------

#! Funksiya



# def summ(a, b):
#     return a+b

# print(summ(1, 2))

# -----------------------------

# def summ(b, a = 4, c=7):
#     return a + b + c
# print(summ(1, 3))

# -----------------------------------

# def greet(*names):
#     for name in names:
#         print("Salom", name, type(name))
        
# greet(1, 2, 3, 4, "Ali", True)

# -------------------------------------

# def introduce(**info):
#     for key, value in info.items():
#         print(key, ":", value)
# introduce(name="Ali", age=20, city="Tashkent")
# -------------------------------------------------
# def introduce(**info):
#     for i in info.values():
#         print(i)
# introduce(name="Ali", age=20, city="Tashkent")

# ------------------------------------------------
# def func(*sonlar, **lugat):
#     print(sonlar, type(sonlar))
#     print(lugat, type(lugat))
#     return type(sonlar), type(lugat)
# print(func(1, 2, 34, name = "Ali", name1 = "Vali"))

# print(type(func()))

# ---------------------------------------------------------

# def greet(greeting, greet, name, *names):
#     print(greeting, greet, name, names)
        
# greet("Hello", "Ali")

# ---------------------------------------------------------

# def funksiya(a, b, *c, d=8):
#     print(a, b, c, d)

# print(funksiya(1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17))

# --------------------------------------------------------------
import math

c = 1
def sum(a, b):
    global c # Local
    c = 10
    return a + b + c
print(sum(1, 2))

print(c)