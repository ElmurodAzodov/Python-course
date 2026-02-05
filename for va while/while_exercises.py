
#^ 0. 1 dan 10 gacha bo‘lgan sonlarni while yordamida ekranga chiqar.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#^ 1. 1 dan n gacha bo‘lgan sonlar yig‘indisini hisobla (n foydalanuvchidan 
#^ olinadi).
# n = int(input("Son kiriting: "))
# i = 1
# y = 0
# while i <= n:
#     y += i
#     i += 1
# print(y)
#^ 2. Juft sonlarni 1 dan 20 gacha ekranga chiqar. 
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1
#^ 3. Foydalanuvchi 0 kiritmaguncha son kiritishni davom ettir, oxirida nechta 
#^ son kiritilganini chiqar. 

# count = 1
# while True:
#     x = int(input("Son kiriting (0 to‘xtatadi): "))
#     if x == 0:
#         break
#     count += 1

# print("Kiritilgan sonlar soni:", count)

#^ 4. Berilgan sonning kvadratini 5 marta ekranga chiqar. 

# i = 0
# son = int(input("Son kiriting: "))
# while i < 5:
#     print(son ** 2)
#     i += 1
    

#^ 6. Berilgan sonning raqamlari yig‘indisini top. 

# n = int(input("Son kiriting: "))
# s = 0

# while n > 0:
#     s += n % 10
#     n //= 10

# print("Raqamlar yig‘indisi:", s)
    
#^ 7. Berilgan sonni teskari yozuvda chiqar (masalan: 123 → 321). 

# n = int(input("Son kiriting: "))
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10

# print("Teskari son:", rev)

#^ 8. 1 dan 100 gacha bo‘lgan 3 ga bo‘linadigan sonlarni chiqar. 

# i = 1

# while i <= 100:
#     if i % 3 == 0:
#         print(i, end=" ")
#     i += 1

#^ 9. Foydalanuvchi manfiy son kiritmaguncha sonlar kiritadi, oxirida eng 
#^ katta sonni chiqar.

eng_katta = None

while True:
    son = int(input("Son kiriting: "))
    
    if son < 0:
        break
    
    if eng_katta == None or son > eng_katta:
        eng_katta = son

print("Eng katta son:", eng_katta)



#^ 10. Berilgan sonning faktorialini while yordamida hisobla. 
#^ 11. Berilgan son tub (prime) yoki yo‘qligini while yordamida aniqla. 
#^ 12. Foydalanuvchi son kiritadi, dastur faqat juft son kiritilmaguncha davom 
#^ etadi. 
#^ 13. Berilgan son palindrom ekanligini aniqla (masalan: 1221). 
#^ 14. Foydalanuvchi sonlar kiritadi, 0 kiritilganda to‘xtaydi, oxirida o‘rtacha 
#^ qiymatni chiqar. 
#^ 15. while yordamida Fibonacci ketma-ketligining dastlabki n ta hadini 
#^ chiqar.