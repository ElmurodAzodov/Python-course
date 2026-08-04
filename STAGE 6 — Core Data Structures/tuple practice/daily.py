# sonlar = (1, 2, 3, 4, 5)
# aralash = ("Elmurod", 24, True, False, None, 2+4)
# son = 2.5
# print(sonlar, son, aralash)
# print(type(sonlar), type(son), type(aralash))

#*______________________________________________________________________

# my_tuple = (
#     1,
#     2,
#     3,
#     "Elmurod",
#     "Dasturchi",
#     True,
#     False,
#     (1, 2, 3, 4, 5),
#     [1, 2, 3, 4, 5],
#     {"ism": "Elmurod", "mutaxassisligi": "Dasturiy injiniring",},
#     None
# )
# print(my_tuple)
# print(type(my_tuple))

#*______________________________________________________________________

# sonlar = (2,)
# print(sonlar, type(sonlar))

#*______________________________________________________________________

# a = 10
# b = 20
# c = 30
# my_tuple = a, b, c
# print(my_tuple, type(my_tuple))

#*______________________________________________________________________

# son = 2,
# print(son, type(son))

#*______________________________________________________________________

# my_tuple = (10, 20, 30, 5)

# a, b, c, d = my_tuple
# print(a)
# print(b)
# print(c)

#*______________________________________________________________________

sonlar = (1,2,3,4,5,6,7,8,9,10)
a, b, *c, d, e = sonlar

print(a)
print(b)
print(c)
print(d)
print(e)
