
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

count = 1
while True:
    x = int(input("Son kiriting (0 to‘xtatadi): "))
    if x == 0:
        break
    count += 1

print("Kiritilgan sonlar soni:", count)

#^ 4. Berilgan sonning kvadratini 5 marta ekranga chiqar. 
#^ 6. Berilgan sonning raqamlari yig‘indisini top. 
#^ 7. Berilgan sonni teskari yozuvda chiqar (masalan: 123 → 321). 
#^ 8. 1 dan 100 gacha bo‘lgan 3 ga bo‘linadigan sonlarni chiqar. 
#^ 9. Foydalanuvchi manfiy son kiritmaguncha sonlar kiritadi, oxirida eng 
#^ katta sonni chiqar. 
#^ 10. Berilgan sonning faktorialini while yordamida hisobla. 
#^ 11. Berilgan son tub (prime) yoki yo‘qligini while yordamida aniqla. 
#^ 12. Foydalanuvchi son kiritadi, dastur faqat juft son kiritilmaguncha davom 
#^ etadi. 
#^ 13. Berilgan son palindrom ekanligini aniqla (masalan: 1221). 
#^ 14. Foydalanuvchi sonlar kiritadi, 0 kiritilganda to‘xtaydi, oxirida o‘rtacha 
#^ qiymatni chiqar. 
#^ 15. while yordamida Fibonacci ketma-ketligining dastlabki n ta hadini 
#^ chiqar.