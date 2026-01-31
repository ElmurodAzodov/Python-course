
# if1
# son = int(input("Butun son kiriting: "))

# if son > 0:
#     print(f"Siz {son} sonini kiritdingiz, uni 1ga oshirganda {son+1} ga teng")
# else:
#     print("Manfiy son kiritdingiz!")

# if2
# son = int(input("Butun son kiriting: "))

# if son > 0:
#     print(f"Siz {son} musbat sonini kiritdingiz, uni 1ga oshirganda {son+1} ga teng")
# else:
#     print(f"Siz {son} manfiy sonini kiritdingiz, uni 2ga kamaytirganda {son-2} ga teng")

# if3
# son = int(input("Butun son kiriting: "))

# if son > 0:
#     print(f"Siz {son} musbat sonini kiritdingiz, uni 1ga oshirganda {son+1} ga teng")
# elif son == 0:
#     print(f"Siz {son} sonini kiritdingiz, uni 10ga o'zlashtirganda {son+10} ga teng")
# else:
#     print(f"Siz {son} manfiy sonini kiritdingiz, uni 2ga kamaytirganda {son-2} ga teng")

# if4
# son1 = int(input("1-butun sonni kiriting: "))
# son2 = int(input("2-butun sonni kiriting: "))
# son3 = int(input("3-butun sonni kiriting: "))

# musbat_sonlar = 0

# if son1 > 0:
#     musbat_sonlar += 1
# if son2 > 0:
#     musbat_sonlar += 1
# if son3 > 0:
#     musbat_sonlar += 1

# print(f"Jami {musbat_sonlar} ta son!")

# if 5
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# musbat = 0
# manfiy = 0


# if a > 0:
#     musbat += 1
# else:
#     if a < 0:
#         manfiy += 1

# if b > 0:
#     musbat += 1
# else:
#     if b < 0:
#         manfiy += 1

# if c > 0:
#     musbat += 1
# else:
#     if c < 0:
#         manfiy += 1

# print("Musbat sonlar:", musbat)
# print("Manfiy sonlar:", manfiy)

# if6
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))

# if son1 > son2:
#     print("Birinchi son ikkinchi sondan katta")
# else:
#     print("Ikkinchi son birinchi sondan katta")

# if7
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))

# if a < b:
#     print("Kichik son:", a)
# else:
#     print("Kichik son:", b)

# if8
# a = int(input("Birinchi son: "))
# b = int(input("Ikkinchi son: "))

# if a > b:
#     print("Katta son:", a)
#     print("Kichik son:", b)
# else:
#     print("Katta son:", b)
#     print("Kichik son:", a)

# if9
# A = float(input("A sonini kiriting: "))
# B = float(input("B sonini kiriting: "))

# if A > B:
#     A, B = B, A

# print("A:", A, "B:", B)

# if10
# A = int(input("A son: "))
# B = int(input("B son: "))

# if A != B:
#     A = B = A + B
# else:
#     A = B = 0

# print("A:", A, "B:", B)

# if11
# A = int(input("A son: "))
# B = int(input("B son: "))

# if A != B:
#     if A > B:
#         B = A
#     else:
#         A = B
# else:
#     A = B = 0

# print("A:", A, "B:", B)

# if12
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))

# if a <= b and a <= c:
#     min_son = a
# elif b <= a and b <= c:
#     min_son = b
# else:
#     min_son = c

# print("Eng kichik son:", min_son)

# if13

a = int(input("Birinchi sonni kiriting: \n"))
b = int(input("Ikkinchi sonni kiriting: \n"))
c = int(input("Uchinchi sonni kiriting: \n"))

if a > b and b > c:
    print(f"{b} soni {a} va {c} sonlari orasida yotadi")
elif b > a and a > c:
    print(f"{a} soni {b} va {c} sonlari orasida yotadi")
else:
    print(f"{c} soni {a} va {b} sonlari orasida yotadi")