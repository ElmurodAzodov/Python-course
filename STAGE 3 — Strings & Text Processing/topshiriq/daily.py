# 1. "Hello World" matnini string sifatida o‘zgaruvchiga saqlang va ekranga 
# chiqaring.

# text = "Hello World"
# print(text)

# 2. Foydalanuvchidan ism kiriting, uni string o‘zgaruvchiga saqlab, ekranga 
# chiqaring.

# name = input()
# print(name)

# 3. Bitta (' ') va ikkita (" ") qo‘shtirnoq yordamida string yarating. 

# a = 'Hello'
# b = "World"
# print(a, b)

# 4. Bo‘sh string yarating va uning uzunligini ekranga chiqaring. 

# s = ""
# print(len(s))

# 5. Uch qatorli matnni """ """ yordamida string sifatida saqlang.

# text = """Salom
# Bu uch qatorli
# Matn"""
# print(text)

# 6. "Python" so‘zining birinchi harfini ekranga chiqaring.

# word = "Python"
# print(word[0])

# 7. "Python" so‘zining oxirgi harfini musbat indeks orqali chiqaring.

# word = "Python"
# print(word[5])

# 8. "Python" so‘zining oxirgi harfini manfiy indeks orqali chiqaring. 

# word = "Python"
# print(word[-1])

# 9. Foydalanuvchi kiritgan so‘zning ikkinchi harfini ekranga chiqaring. 

# word = input()
# print(word[1])

# 10. "Computer" so‘zining 3-indeksidagi belgini ekranga chiqaring.

# word = "Computer"
# print(word[3])

# 11. Foydalanuvchidan ikkita so‘z kiriting va ularni bitta stringga birlashtiring. 

# a = input()
# b = input()
# text = a + " " + b
# print(text)

# 12. "12345" ko‘rinishidagi qiymatni string sifatida saqlang va ekranga chiqaring. 

# s = "12345"
# print(s)

# 13. Maxsus belgilar (@, #, $) ishtirok etgan string yarating. 

# text = "@home#123$"
# print(text)

# 14. Ichida bo‘sh joylar (space) mavjud bo‘lgan stringga misol keltiring.

# text = "Hello World Python"
# print(text)

# 15. Foydalanuvchi kiritgan so‘zning uzunligini va o‘rtadagi harfini ekranga chiqaring. 

# word = input("So'z kiriting: ")
# length = len(word)
# middle = length // 2
# print(length)
# print(word[middle])

# 16. Agar so‘z uzunligi 1 ga teng bo‘lsa, faqat shu harfni ekranga chiqaring. 

# word = input("So'z kiriting: ")
# if len(word) == 1:
#     print(word[0])
# else:
#     print(word)

# 17. "Programming" so‘zidagi har bir indeksga mos belgini alohida-alohida ekranga chiqaring. 

# word = "Programming"
# i = 0
# while i < len(word):
#     print(i, word[i])
#     i += 1

# 18. Foydalanuvchi kiritgan indeks bo‘yicha stringdan belgi chiqaring. Agar indeks noto‘g‘ri bo‘lsa, hech narsa chiqarmang.

# word = input("Matn kiriting: ")
# index = int(input("Indeks kiriting: "))

# if 0 <= index < len(word):
#     print(word[index])

# 19. Foydalanuvchidan ism va familiya kiriting hamda bitta to‘liq ism stringini 
# yarating.

# name = input("Ismingizni kiriting: ")
# surname = input("Familiyangizni kiriting: ")
# full_name = name + " " + surname
# print(full_name)

# 20. Telefon raqamni string sifatida saqlang va uning formatini o‘zgartirmasdan 
# chiqaring.

# phone = "+998901234567"
# print(phone)

# 21. Unicode belgilar ishtirok etgan string yarating (masalan, o‘zbek harflari bilan). 

# text = "Oʻzbekiston – goʻzal yurt"
# print(text)

# 22. Harf, raqam va maxsus belgilar aralashgan string yarating va saqlang.
# Indexing

# text = "User123@site"
# print(text)

# 23. Stringning birinchi va oxirgi harfini bir qatorda ekranga chiqaring.

# word = input("Matn kiriting: ")
# print(word[0], word[-1])

# 24. Agar string bo‘sh bo‘lsa, indekslash amali bajarilmasligini ta’minlang.

# word = input("Matn kiriting: ")

# if len(word) > 0:
#     print(word[0])
# else:
#     print("Indekslash amali bajarilmaydi")

# 25. Foydalanuvchi kiritgan matndan quyidagilarni alohida-alohida ekranga chiqaring: 
# • birinchi belgi 
# • oxirgi belgi 
# • o‘rtadagi belgi

text = input()
length = len(text)

if length > 0:
    first = text[0]
    last = text[-1]
    middle = text[length // 2]
    print(first)
    print(last)
    print(middle)