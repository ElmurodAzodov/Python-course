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
M = []

def func(a, l = None):
    if l is None:
        l = []
        l.append(a)
    return l

print(func(2))


