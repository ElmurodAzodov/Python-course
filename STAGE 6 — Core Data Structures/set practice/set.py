# =========================================
#           SET MAVZUSI – 20 TOPSHIRIQ
# =========================================


# 1-topshiriq
# Set yaratib, takroriy elementlar qanday yo‘qolishini ko‘rsating.
# {1,2,3,3,4,4} setini yarating va natijani chiqaring.
# Nima uchun ayrim sonlar faqat bir marta chiqayotganini izohlang (kommentariyada).



# 2-topshiriq
# numbers = [5,5,6,7,7,8]
# Uni setga o‘tkazing va natijani chiqaring.
# Takroriy elementlar nima bo‘lganini tushuntiring.


# 3-topshiriq
# "programming" so‘zidan unique harflarni toping va ekranga chiqaring.
# Takroriy harflar nechta ekanini aniqlang.


# 4-topshiriq
# Bo‘sh set yarating.
# add() metodi yordamida unga 10 sonini qo‘shing.
# Natijani chiqaring.


# 5-topshiriq
# s = {1,2,3}
# update() metodi yordamida [4,5,6] elementlarini qo‘shing.
# Natijani chiqaring.


# 6-topshiriq
# s = {10,20,30,40}
# remove() metodi yordamida 20 sonini o‘chiring.
# Natijani chiqaring.


# 7-topshiriq
# s = {1,2,3}
# discard() yordamida mavjud bo‘lmagan 10 sonini o‘chirishga harakat qiling.
# Xatolik chiqadimi? Natijani kuzating.


# 8-topshiriq
# s = {100,200,300}
# pop() metodini ishlating.
# Qaysi element o‘chganini va qolgan setni chiqaring.


# 9-topshiriq
# s = {1,2,3,4,5}
# clear() metodi yordamida barcha elementlarni o‘chiring.
# Natijani chiqaring.


# 10-topshiriq
# ids = [101,102,103,101,104,102]
# Takroriy IDlarni olib tashlab, unique IDlar setini hosil qiling.


# 11-topshiriq
# A = {1,2,3,4}
# B = {3,4,5,6}
# Union (birlashtirish) amalini:
#   - union() metodi
#   - | operatori
# yordamida bajaring.


# 12-topshiriq
# Yuqoridagi A va B setlari uchun intersection (kesishma) amalini:
#   - intersection()
#   - & operatori
# yordamida bajaring.


# 13-topshiriq
# A va B setlari uchun difference (farq) amalini hisoblang:
#   - A - B
#   - B - A


# 14-topshiriq
# A va B setlari uchun symmetric difference (simmetrik farq) ni toping:
#   - symmetric_difference()
#   - ^ operatori


# 15-topshiriq
# X = {1,2}
# Y = {1,2,3,4}
# X Y ning subsetimi?
# Y X ning supersetimi?
# Natijani chiqaring.


# 16-topshiriq
# group1 = {"Ali","Vali","Hasan","Husan"}
# group2 = {"Hasan","Husan","Zafar","Olim"}
# Toping:
#   - Ikkala guruhda ham bor talabalar
#   - Faqat birinchi guruhdagilar
#   - Barcha talabalar (takrorsiz)


# 17-topshiriq
# nums = [1,2,2,3,3,3,4,5,5]
# Takroriy elementlarni aniqlang.
# Unique elementlarni set yordamida ajrating.


# 18-topshiriq
# text = "data science"
# Bo‘sh joyni hisobga olmasdan unique belgilarni toping.
# Ularning sonini chiqaring.


# 19-topshiriq
# A = {1,2,3,4}
# B = {3,4,5,6}
# C = {4,5,6,7}
# Toping:
#   - Faqat A da bor elementlar
#   - A va B kesishmasi
#   - Uchalasida ham mavjud elementlar
#   - Kamida ikkita setda mavjud elementlar

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 5, 6, 7}
only_in_A = A - (B | C)
print("Faqat A da:", only_in_A)

A_and_B = A & B
print("A va B kesishmasi:", A_and_B)

all_three = A & B & C
print("Uchalasida ham bor:", all_three)

at_least_two = (A & B) | (A & C) | (B & C)
print("Kamida ikkita setda:", at_least_two)

# 20-topshiriq
# registered_users = {"ali","vali","hasan"}
# new_users = ["vali","zafar","olim","ali","sardor"]
# Toping:
#   - Yangi foydalanuvchilar ichidan ro‘yxatdan o‘tmaganlar
#   - Ro‘yxatni yangilang (duplicate bo‘lmasin)
#   - Oxirgi foydalanuvchilar sonini chiqaring

# registered_users = {"ali","vali","hasan"}
# new_users = ["vali","zafar","olim","ali","sardor"]
# new_users_set = set(new_users)
# not_registered = registered_users.difference(new_users)
# print(not_registered)

# updated_users = registered_users.union(new_users_set)
# print(updated_users)

# total_users = len(updated_users)
# print(total_users)