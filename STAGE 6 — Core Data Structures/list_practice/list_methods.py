
#^ Python dasturlash tilida  
#^ List metodlari va Mutability mavzulariga 
#^ TOPSHIRIQ

# 1. 
# List yarating: [10, 20, 30] 
# Oxiriga 40 ni append() bilan qo‘shing va ekranga chiqaring. 

# l = [10, 20, 30]
# l.append(40)
# print(l)

# 2. 
# Bo‘sh list yarating. 
# Foydalanuvchidan 3 ta son olib append() bilan listga qo‘shing. 

numbers = []

for i in range(3):
    num = int(input(f"{i+1}-sonni kiriting: "))
    numbers.append(num)

print("List:", numbers)

# 3. 
# ["apple", "banana", "cherry"] listidan "banana" ni remove() bilan o‘chiring. 

# 4. 
# Berilgan list: [1, 2, 3, 4, 5] 
# 3-indexga 99 ni insert() bilan qo‘shing. 

# 5. 
# Foydalanuvchidan 5 ta so‘z olib listga joylang. 
# Eng ko‘p takrorlangan so‘zni count() bilan toping. 

# 6. 
# List: [10, 20, 30, 20, 40, 20] 
# Barcha 20 larni remove() yordamida o‘chiring. 

# 7. 
# Ikki list bor: 
# a = [1,2,3] 
# b = [4,5,6] 
# Ularni extend() yordamida birlashtiring. 

# 8. 
# Foydalanuvchidan 7 ta son oling. 
# Listni o‘sish va kamayish tartibida chiqaring. 
 
# 9. 
# List: [5,4,3,2,1] 
# Avval sort(), keyin reverse() ishlatib natijani ko‘rsating. 
 
# 10. 
# Listdan eng katta va eng kichik sonni sort() va pop() orqali toping. 
 
# 11. 
# List: [1,2,3,4,5] 
# .copy() bilan nusxa oling va faqat nusxani o‘zgartiring. 
 
# 12. 
# Foydalanuvchi kiritgan listdan faqat juft sonlarni yangi listga joylang. 
 
# 13. 
# List: [1,1,2,2,3,3,4] 
# Takrorlangan elementlarni o‘chirib, faqat unikal list yarating. 
# 14. 
# 2D list yarating (matritsa): 
# matrix = [ 
# [1,2,3], 
# [4,5,6], 
# [7,8,9] 
# ] 
# Foydalanuvchi bergan index bo‘yicha elementni o‘zgartiring. 

# 15. 
# Nested listni deepcopy() bilan nusxalab, faqat nusxani o‘zgartiring. 

# 16. 
# Foydalanuvchi kiritgan sonlardan: 
# • Musbatlar 
# • Manfiylar 
# • Nol 
# uchun 3 ta alohida list yarating. 

# 17. 
# Listni qo‘shimcha list ishlatmasdan teskari qiling (reverse() ishlatmasdan). 

# 18. 
# Berilgan listda eng uzun ketma-ket o‘suvchi sonlar qatorini toping. 
# Misol: 
# [1,2,3,1,2,3,4,5] 
# Natija: [1,2,3,4,5] 

# 19. 
# Listda eng ko‘p uchragan element(lar)ni toping. 
# Agar bir nechta bo‘lsa, hammasini chiqaring. 

# 20. 
# Mini loyiha: 
# Kontaktlar dasturi yarating 
# List ichida dict saqlang: 
# contacts = [ 
# {"name":"Ali", "phone":"99890..."} 
# ] 
# Funksiyalar: 
# Qo‘shish 
# O‘chirish 
# Qidirish 
# Saralash (name bo‘yicha) 
# Nusxa olish