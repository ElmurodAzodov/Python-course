# 1. 
#* 1 dan 10 gacha bo‘lgan sonlarni for yordamida ekranga chiqaring. 
# for i in range(1, 11):
#     print(i)
# 2. 
#* 1 dan 10 gacha bo‘lgan juft sonlarni chiqaring (if ishlating). 
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
# 3. 
#* 1 dan 10 gacha bo‘lgan toq sonlarni chiqaring.
# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)
# 4. 
#* Foydalanuvchi son kiritadi. 
#* 1 dan shu songacha bo‘lgan sonlarni chiqaring.
# son = int(input("Son kiriting: ")) 
# for i in range(1, son+1):
#     print(i)
# 5. 
#* 1 dan 20 gacha bo‘lgan sonlardan 5 ga karrali bo‘lganlarini chiqaring.
# for i in range(1, 21):
#     if i % 5 == 0:
#         print(i)
# 6. 
#* 1 dan 10 gacha bo‘lgan sonlarning yig‘indisini hisoblang.
# natija = 0
# for i in range(1, 11):
#      natija += i
# print(natija)
# 7. 
#* 1 dan 20 gacha bo‘lgan sonlardan juftlarning yig‘indisini toping. 
# for i in range(1, 21):
    
# 8. 
#* Foydalanuvchi son kiritadi. 
#* Shu son tub (prime) yoki yo‘qligini for va if else yordamida aniqlang. 
# son = int(input("Son kiriting: "))
# tub = True

# if son < 2:
#     tub = False
# for i in range(2, son):
#     if son % i == 0:
#         tub = False
#         break
# if tub:
#     print("Tub son")
# else:
#     print("Tub emas")
# 9. 
#* Berilgan ro‘yxat: 
#* sonlar = [3, 7, 2, 9, 12, 5] 
#* Faqat 5 dan katta sonlarni ekranga chiqaring.
# sonlar = [3, 7, 2, 9, 12, 5]
# for i in sonlar:
#     if i > 5:
#         print(i)
# 10. 
#* 1 dan 50 gacha bo‘lgan sonlardan 3 ga ham, 5 ga ham bo‘linadigan sonlarni 
#* chiqaring. 
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
# 11. 
#* 1 dan 100 gacha bo‘lgan sonlardan tub sonlarni chiqaring. 
# for son in range(2, 101):
#     tub = True
#     for i in range(2, son):
#         if son % i == 0:
#             tub = False
#             break

#     if tub:
#         print(son)

# 12. 
#* Berilgan ro‘yxatdagi eng katta sonni for yordamida toping. 
#* (max() ishlatish mumkin emas)
# sonlar = [4, 7, 2, 9, 1, 5]

# eng_katta = sonlar[0]

# for son in sonlar:
#     if son > eng_katta:
#         eng_katta = son

# print("Eng katta son:", eng_katta)

# 13. 
#* Foydalanuvchi kiritgan sonning faktorialini for yordamida hisoblang. 
# n = int(input("Son kiriting: "))

# faktorial = 1

# for i in range(1, n + 1):
#     faktorial *= i

# print("Faktorial:", faktorial)

# 14. 
#* Berilgan matndagi unli harflar sonini hisoblang. 
#* (Masalan: a, e, i, o, u)
# matn = input("Matn kiriting: ")

# unlilar = "aeiouAEIOU"
# sanoq = 0

# for harf in matn:
#     if harf in unlilar:
#         sanoq += 1

# print("Unli harflar soni:", sanoq)

# 15. 
#* 1 dan 50 gacha bo‘lgan sonlar uchun: 
#* - agar son 3 ga bo‘linsa → "Fizz" 
#* - agar 5 ga bo‘linsa → "Buzz" 
#* - agar 3 va 5 ga bo‘linsa → "FizzBuzz" 
#* - aks holda sonning o‘zini chiqaring 
#* (for + if elif else)
for son in range(1, 51):
    if son % 3 == 0 and son % 5 == 0:
        print("FizzBuzz")
    elif son % 3 == 0:
        print("Fizz")
    elif son % 5 == 0:
        print("Buzz")
    else:
        print(son)
