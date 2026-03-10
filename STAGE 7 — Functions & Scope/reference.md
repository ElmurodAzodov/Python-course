
# **STAGE 7 — Functions & Scope**

<br><br>

## 📝 Function Definitions (def name():)

### Funktsiya nima va nima uchun kerak?

Funktsiya - bu dasturning ma'lum bir vazifani bajaradigan qayta ishlatiladigan qismi. Real hayotda funktsiyaga o'xshash misollar:

- **Choynak** - suvni qaynatish vazifasini bajaradi, har safar ishlatganda bir xil ishni qiladi
- **Mikroto'lqinli pech** - taomni isitish vazifasini bajaradi
- **Kalkulyator** - matematik amallarni bajaradi

Dasturlashda funktsiyalar:
- Kodekni qayta ishlatish imkonini beradi
- Kodekni tartibli qiladi
- Murakkab masalalarni kichik qismlarga bo'lishga yordam beradi
- Xatolarni topish va tuzatishni osonlashtiradi

### `def` kalit so'zi va funktsiya yaratish

Python'da funktsiya `def` kalit so'zi bilan yaratiladi. Sintaksis:

```python
def funktsiya_nomi():
    # funktsiya tanasi
    # bajariladigan kodlar
```

Keling, eng oddiy funktsiyani yaratamiz:

```python
def salom_ber():
    print("Assalomu alaykum!")
    print("Python dasturlash tiliga xush kelibsiz!")
```

Bu funktsiya hech qanday parametr qabul qilmaydi va hech qanday qiymat qaytarmaydi. U faqat ikkita qator matnni konsolga chiqaradi.

### Funktsiya nomlash qoidalari

Funktsiya nomlari quyidagi qoidalarga amal qilishi kerak:

1. **Harflar, raqamlar va pastki chiziq (_) dan iborat bo'lishi mumkin**
2. **Raqam bilan boshlanishi mumkin emas**
3. **Python kalit so'zlari bilan bir xil bo'lmasligi kerak** (if, else, for, while, def va h.k.)
4. **Kichik harflardan foydalanish tavsiya etiladi**
5. **Bir necha so'zdan iborat bo'lsa, pastki chiziq bilan ajrating** (snake_case)

```python
# To'g'ri nomlar
def hisobla_oshxona():
    pass

def get_user_name():
    pass

def calculate_total_price():
    pass

# Noto'g'ri nomlar
# def 2hisobla():  # Raqam bilan boshlangan
# def if():        # Python kalit so'zi
# def my-function():  # Chiziqcha ishlatilgan
```

### Funktsiya tanasi (indentation - joy tashlash)

Python'da funktsiya tanasi **indentation** (4 bo'sh joy yoki 1 tab) bilan ajratiladi:

```python
def oddiy_funktsiya():
    print("Bu qator 4 bo'sh joy bilan boshlangan")
    print("Bu ham 4 bo'sh joy")
    print("Funktsiya ichidagi barcha qatorlar bir xil indentatsiyaga ega")

print("Bu qator funktsiyadan tashqarida")
```

**Muhim**: Agar indentatsiya noto'g'ri bo'lsa, Python xatolik beradi:

```python
def notogri_funktsiya():
    print("To'g'ri indentatsiya")
  print("Noto'g'ri indentatsiya")  # IndentationError: unindent does not match any outer indentation level
```

### `pass` - bo'sh funktsiya

Ba'zida funktsiyani keyinroq to'ldirish uchun bo'sh qoldirish kerak bo'ladi. Python bo'sh funktsiyani tushunmaydi, shuning uchun `pass` kalit so'zidan foydalanamiz:

```python
def hali_tayyor_emas():
    pass  # Bu funktsiya hali hech narsa qilmaydi

def keyin_yoziladi():
    pass  # Keyinchalik kod yozish uchun joy

# Bu funktsiyani chaqirish hech narsa qilmaydi
hali_tayyor_emas()
```

### Amaliy misollar

**1-misol: Oddiy funktsiya**

```python
def talaba_haqida():
    """Talaba haqida ma'lumot chiqaruvchi funktsiya"""
    print("Ism: Alisher")
    print("Yosh: 20")
    print("Fakultet: Axborot texnologiyalari")
    print("Kurs: 2")

# Funktsiyani chaqirish
talaba_haqida()
```

**Natija:**
```
Ism: Alisher
Yosh: 20
Fakultet: Axborot texnologiyalari
Kurs: 2
```

**2-misol: Matematik amallar**

```python
def aylana_hisobla():
    """Aylana parametrlarini hisoblovchi funktsiya"""
    radius = 5
    pi = 3.14159
    
    diametr = 2 * radius
    uzunlik = 2 * pi * radius
    yuza = pi * radius ** 2
    
    print(f"Aylana radiusi: {radius}")
    print(f"Diametri: {diametr}")
    print(f"Uzunligi: {uzunlik:.2f}")
    print(f"Yuzasi: {yuza:.2f}")

# Funktsiyani chaqirish
aylana_hisobla()
```

**Natija:**
```
Aylana radiusi: 5
Diametri: 10
Uzunligi: 31.42
Yuzasi: 78.54
```

**3-misol: Bir necha funktsiya yaratish**

```python
def nonushta():
    """Nonushta menyusi"""
    print("Bugungi nonushta:")
    print("- Choy")
    print("- Non")
    print("- Tuxum")
    print("- Sariyog'")

def tushlik():
    """Tushlik menyusi"""
    print("Bugungi tushlik:")
    print("- Osh")
    print("- Salat")
    print("- Non")
    print("- Kompot")

def kechki_ovqat():
    """Kechki ovqat menyusi"""
    print("Bugungi kechki ovqat:")
    print("- Sho'rva")
    print("- Kabob")
    print("- Sabzavotlar")
    print("- Choy")

# Kunlik menyuni chiqarish
print("=== 1-KUN MENYUSI ===")
nonushta()
print()  # Bo'sh qator
tushlik()
print()
kechki_ovqat()
```

**4-misol: Hisob-kitob funktsiyalari**

```python
def dollar_hisobla():
    """Dollarni so'mga aylantiruvchi funktsiya"""
    kurs = 12500  # 1 dollar = 12500 so'm
    dollar = 100
    
    som = dollar * kurs
    
    print(f"{dollar} dollar = {som} so'm")
    print(f"Kurs: 1 dollar = {kurs} so'm")

def foiz_hisobla():
    """Foiz hisoblovchi funktsiya"""
    summa = 1000000
    foiz = 12
    muddat = 3  # yil
    
    daromad = summa * foiz / 100 * muddat
    umumiy = summa + daromad
    
    print(f"Boshlang'ich summa: {summa} so'm")
    print(f"Yillik foiz: {foiz}%")
    print(f"Muddat: {muddat} yil")
    print(f"Daromad: {daromad} so'm")
    print(f"Umumiy summa: {umumiy} so'm")

# Hisob-kitoblarni bajarish
print("=== VALYUTA HISOBLASH ===")
dollar_hisobla()
print("\n=== FOIZ HISOBLASH ===")
foiz_hisobla()
```

### Keng qamrovli amaliy misol

Keling, bitta katta misol orqali funktsiyalarni yanada yaxshiroq tushunaylik:

```python
# Talabalar jurnali dasturi

def talaba_qoshish():
    """Yangi talaba qo'shish"""
    print("\n--- YANGI TALABA QO'SHISH ---")
    print("1. Alisher")
    print("2. Madina")
    print("3. Bekzod")
    print("4. Dilnoza")
    print("5. Sherzod")
    talaba = input("Talabani tanlang (1-5): ")
    
    if talaba == "1":
        print("Alisher jurnalga qo'shildi")
    elif talaba == "2":
        print("Madina jurnalga qo'shildi")
    elif talaba == "3":
        print("Bekzod jurnalga qo'shildi")
    elif talaba == "4":
        print("Dilnoza jurnalga qo'shildi")
    elif talaba == "5":
        print("Sherzod jurnalga qo'shildi")
    else:
        print("Noto'g'ri tanlov!")

def baho_qoyish():
    """Talabaga baho qo'yish"""
    print("\n--- BAHO QO'YISH ---")
    print("Talabalar ro'yxati:")
    print("1. Alisher - 3-baho")
    print("2. Madina - 2-baho") 
    print("3. Bekzod - 4-baho")
    print("4. Dilnoza - 1-baho")
    print("5. Sherzod - 3-baho")
    
    talaba = input("Talabani tanlang (1-5): ")
    baho = input("Yangi bahoni kiriting (1-5): ")
    
    print(f"Talabaga {baho} baho qo'yildi")

def ortacha_baho():
    """O'rtacha bahoni hisoblash"""
    print("\n--- O'RTACHA BAHO ---")
    print("1-fan: 4.5")
    print("2-fan: 3.8")
    print("3-fan: 4.2")
    print("4-fan: 3.9")
    print("5-fan: 4.7")
    
    ortacha = (4.5 + 3.8 + 4.2 + 3.9 + 4.7) / 5
    print(f"O'rtacha baho: {ortacha:.2f}")

def dars_jadvali():
    """Dars jadvalini ko'rsatish"""
    print("\n--- DARS JADVALI ---")
    print("Dushanba: 9:00 - Matematika")
    print("Dushanba: 11:00 - Fizika")
    print("Seshanba: 9:00 - Ingliz tili")
    print("Seshanba: 11:00 - Dasturlash")
    print("Chorshanba: 9:00 - Ma'lumotlar bazasi")
    print("Chorshanba: 11:00 - Web dasturlash")
    print("Payshanba: 9:00 - Algoritmlar")
    print("Payshanba: 11:00 - Python")
    print("Juma: 9:00 - Amaliyot")
    print("Juma: 11:00 - Seminar")

def statistika():
    """Guruh statistikasi"""
    print("\n--- GURUH STATISTIKASI ---")
    print("Jami talabalar: 25")
    print("O'g'il bolalar: 15")
    print("Qiz bolalar: 10")
    print("A'lochilar: 5")
    print("Yaxshilar: 12")
    print("Qoniqarli: 8")
    print("Davomat: 92%")

def asosiy_menu():
    """Asosiy menyu"""
    print("\n" + "="*40)
    print("TALABALAR JURNALI DASTURI")
    print("="*40)
    print("1. Yangi talaba qo'shish")
    print("2. Baho qo'yish")
    print("3. O'rtacha bahoni ko'rish")
    print("4. Dars jadvali")
    print("5. Guruh statistikasi")
    print("6. Chiqish")
    print("="*40)

# Asosiy dastur
print("TALABALAR JURNALI DASTURIGA XUSH KELIBSIZ!")

while True:
    asosiy_menu()
    tanlov = input("Tanlovingizni kiriting (1-6): ")
    
    if tanlov == "1":
        talaba_qoshish()
    elif tanlov == "2":
        baho_qoyish()
    elif tanlov == "3":
        ortacha_baho()
    elif tanlov == "4":
        dars_jadvali()
    elif tanlov == "5":
        statistika()
    elif tanlov == "6":
        print("Dastur tugadi. Xayr!")
        break
    else:
        print("Noto'g'ri tanlov! Iltimos, 1 dan 6 gacha son kiriting.")
    
    input("\nDavom etish uchun Enter tugmasini bosing...")
```

### Muhim eslatmalar

1. **Funktsiya nomi uning vazifasini ifodalashi kerak** - `hisobla()`, `chiqar()`, `saqla()` kabi
2. **Har bir funktsiya bitta vazifani bajarishi kerak** - bir funktsiyada hamma narsani qilishdan saqlaning
3. **Funktsiyalarni imkon qadar qisqa va tushunarli qilib yozing**
4. **Indentatsiyaga e'tibor bering** - Python uchun bu juda muhim
5. **Funktsiyalarni chaqirishdan oldin ularni yaratish kerak**
---
<br>
<br>
<br>
<br>
<br>

## 📞 Calling Functions (invocation)

### Funktsiyani chaqirish nima?

Funktsiyani chaqirish - bu yaratilgan funktsiyani ishga tushirish, uning kodini bajarish demakdir. Funktsiya yaratilgan (def bilan) bo'lsa ham, u chaqirilmaguncha hech qanday amal bajarilmaydi. Xuddi mashina motoriga o'xshaydi - motor bor, lekin uni ishga tushirmaguncha (chaqirmaguncha) harakatlanmaydi.

### Funktsiyani chaqirish sintaksisi

Funktsiyani chaqirish uchun uning nomini yozib, oxiriga qavs `()` qo'yish kerak:

```python
# Funktsiya yaratish
def salom_ber():
    print("Salom, dunyo!")

# Funktsiyani chaqirish
salom_ber()  # Natija: Salom, dunyo!
```

### Funktsiyani bir necha marta chaqirish

Funktsiyani xohlagancha ko'p marta chaqirish mumkin:

```python
def tabrikla():
    print("Tabriklaymiz!")

# Bir necha marta chaqirish
tabrikla()  # 1-marta
tabrikla()  # 2-marta
tabrikla()  # 3-marta

print("Bayram tugadi...")

tabrikla()  # Yana chaqirish
```

**Natija:**
```
Tabriklaymiz!
Tabriklaymiz!
Tabriklaymiz!
Bayram tugadi...
Tabriklaymiz!
```

### Funktsiyani o'zgaruvchi orqali chaqirish

Funktsiyani o'zgaruvchiga ham biriktirish mumkin:

```python
def ayt_hello():
    print("Hello, World!")

# Funktsiyani o'zgaruvchiga biriktirish
my_func = ayt_hello

# O'zgaruvchi orqali chaqirish
my_func()  # Hello, World!
ayt_hello()  # Hello, World! (asl nomi bilan ham ishlaydi)
```

### Funktsiyalarni ketma-ket chaqirish

Bir necha funktsiyani ketma-ket chaqirish:

```python
def non_yes():
    print("Non qovurildi")

def choy_demle():
    print("Choy damlandi")

def tuxum_pishir():
    print("Tuxum pishirildi")

# Nonushta tayyorlash jarayoni
print("Nonushta tayyorlanmoqda...")
print("-" * 30)

non_yes()
choy_demle()
tuxum_pishir()

print("-" * 30)
print("Nonushta tayyor!")
```

### Funktsiya ichida boshqa funktsiyani chaqirish

Funktsiyalar bir-birini chaqirishi mumkin:

```python
def xush_kelibsiz():
    print("Xush kelibsiz!")

def ism_so rash():
    print("Ismingiz nima?")

def salomlash():
    xush_kelibsiz()      # Birinchi funktsiyani chaqirish
    ism_so rash()        # Ikkinchi funktsiyani chaqirish
    print("Dastur boshlandi!")

# Asosiy funktsiyani chaqirish
salomlash()
```

**Natija:**
```
Xush kelibsiz!
Ismingiz nima?
Dastur boshlandi!
```

### Murakkab misol: Funktsiyalar o'zaro aloqasi

```python
def menyu_ko rsat():
    """Menyuni ko'rsatish"""
    print("\n=== RESTORAN MENYUSI ===")
    print("1. Milliy taomlar")
    print("2. Yevropa taomlari") 
    print("3. Shirinliklar")
    print("4. Ichimliklar")

def milliy_taomlar():
    """Milliy taomlar ro'yxati"""
    print("\n--- MILLIY TAOMLAR ---")
    print("• Osh - 25000 so'm")
    print("• Sho'rva - 18000 so'm")
    print("• Manti - 22000 so'm")
    print("• Kabob - 30000 so'm")

def yevropa_taomlari():
    """Yevropa taomlari ro'yxati"""
    print("\n--- YEVROPA TAOMLARI ---")
    print("• Pizza - 45000 so'm")
    print("• Pasta - 35000 so'm")
    print("• Steyk - 55000 so'm")
    print("• Salat - 20000 so'm")

def shirinliklar():
    """Shirinliklar ro'yxati"""
    print("\n--- SHIRINLIKLAR ---")
    print("• Tort - 30000 so'm")
    print("• Pirojniy - 15000 so'm")
    print("• Muzqaymoq - 12000 so'm")
    print("• Halva - 10000 so'm")

def ichimliklar():
    """Ichimliklar ro'yxati"""
    print("\n--- ICHIMLIKLAR ---")
    print("• Choy - 5000 so'm")
    print("• Kofe - 12000 so'm")
    print("• Sharbat - 15000 so'm")
    print("• Mineral suv - 4000 so'm")

def buyurtma_qabul():
    """Buyurtma qabul qilish"""
    print("\nBuyurtmangizni kiriting:")
    taom = input("Taom nomi: ")
    miqdor = int(input("Miqdori: "))
    print(f"Siz {miqdor} dona {taom} buyurtma qildingiz.")

def restoran_dasturi():
    """Asosiy restoran dasturi"""
    print("RESTORAN DASTURIGA XUSH KELIBSIZ!")
    
    while True:
        menyu_ko rsat()
        tanlov = input("\nBo'limni tanlang (1-5, 0=chiqish): ")
        
        if tanlov == "1":
            milliy_taomlar()
            buyurtma_qabul()
        elif tanlov == "2":
            yevropa_taomlari()
            buyurtma_qabul()
        elif tanlov == "3":
            shirinliklar()
            buyurtma_qabul()
        elif tanlov == "4":
            ichimliklar()
            buyurtma_qabul()
        elif tanlov == "0":
            print("Rahmat! Xush kelib qoldingiz!")
            break
        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

# Dasturni ishga tushirish
restoran_dasturi()
```

### Rekursiv chaqiruv (o'zini o'zi chaqirish)

Funktsiya o'zini o'zi chaqirishi mumkin. Bu **rekursiya** deb ataladi:

```python
def sanoq(n):
    """n dan 1 gacha sanaydigan rekursiv funktsiya"""
    if n <= 0:  # To'xtash sharti
        print("Bajarildi!")
        return
    
    print(f"Sanoq: {n}")
    sanoq(n - 1)  # O'zini o'zi chaqirish

# Funktsiyani chaqirish
sanoq(5)
```

**Natija:**
```
Sanoq: 5
Sanoq: 4
Sanoq: 3
Sanoq: 2
Sanoq: 1
Bajarildi!
```

### Faktorial hisoblash (rekursiv misol)

```python
def faktorial(n):
    """n! (faktorial) hisoblovchi rekursiv funktsiya"""
    if n <= 1:  # Bazaviy holat
        return 1
    else:
        return n * faktorial(n - 1)  # Rekursiv chaqiruv

# Faktoriallarni hisoblash
print("Faktoriallar:")
for i in range(1, 8):
    print(f"{i}! = {faktorial(i)}")
```

**Natija:**
```
Faktoriallar:
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
```

### Amaliy misollar to'plami

**1-misol: Bank hisob tizimi**

```python
def balans_ko rsat():
    """Joriy balansni ko'rsatish"""
    print(f"Sizning balansingiz: {balans} so'm")

def pul_qoshish():
    """Hisobga pul qo'shish"""
    global balans
    miqdor = float(input("Qancha pul qo'shmoqchisiz? "))
    balans += miqdor
    print(f"{miqdor} so'm hisobga qo'shildi")
    balans_ko rsat()

def pul_yechish():
    """Hisobdan pul yechish"""
    global balans
    miqdor = float(input("Qancha pul yechmoqchisiz? "))
    if miqdor <= balans:
        balans -= miqdor
        print(f"{miqdor} so'm hisobdan yechildi")
    else:
        print("Mablag' yetarli emas!")
    balans_ko rsat()

def bank_xizmati():
    """Asosiy bank dasturi"""
    global balans
    balans = 1000000  # Boshlang'ich balans
    
    print("BANK XIZMATIGA XUSH KELIBSIZ!")
    
    while True:
        print("\n--- XIZMATLAR ---")
        print("1. Balansni ko'rish")
        print("2. Pul qo'shish")
        print("3. Pul yechish")
        print("4. Chiqish")
        
        tanlov = input("Tanlovingiz: ")
        
        if tanlov == "1":
            balans_ko rsat()
        elif tanlov == "2":
            pul_qoshish()
        elif tanlov == "3":
            pul_yechish()
        elif tanlov == "4":
            print("Xizmatimizdan foydalanganingiz uchun rahmat!")
            break
        else:
            print("Noto'g'ri tanlov!")

# Bank dasturini ishga tushirish
bank_xizmati()
```

**2-misol: Matematik test**

```python
def savol_ber(savol, togri_javob):
    """Savol berish va javobni tekshirish"""
    print(f"\n{savol}")
    javob = input("Javobingiz: ")
    
    if javob.lower() == togri_javob.lower():
        print("To'g'ri! ✅")
        return True
    else:
        print(f"Noto'g'ri! ❌ To'g'ri javob: {togri_javob}")
        return False

def natija_chiqar(togri_javoblar, umumiy_savol):
    """Test natijasini chiqarish"""
    foiz = (togri_javoblar / umumiy_savol) * 100
    
    print("\n" + "="*40)
    print("TEST NATIJALARI")
    print("="*40)
    print(f"To'g'ri javoblar: {togri_javoblar}/{umumiy_savol}")
    print(f"Foiz: {foiz}%")
    
    if foiz >= 80:
        print("Baho: 5 (A'lo)")
    elif foiz >= 60:
        print("Baho: 4 (Yaxshi)")
    elif foiz >= 40:
        print("Baho: 3 (Qoniqarli)")
    else:
        print("Baho: 2 (Qoniqarsiz)")

def matematik_test():
    """Matematik test dasturi"""
    print("MATEMATIK TESTGA XUSH KELIBSIZ!")
    print("5 ta savolga javob bering.")
    
    togri = 0
    umumiy = 5
    
    # 1-savol
    if savol_ber("5 + 3 = ?", "8"):
        togri += 1
    
    # 2-savol
    if savol_ber("10 - 4 = ?", "6"):
        togri += 1
    
    # 3-savol
    if savol_ber("7 * 6 = ?", "42"):
        togri += 1
    
    # 4-savol
    if savol_ber("15 / 3 = ?", "5"):
        togri += 1
    
    # 5-savol
    if savol_ber("9 * 9 = ?", "81"):
        togri += 1
    
    # Natijani chiqarish
    natija_chiqar(togri, umumiy)

# Testni boshlash
matematik_test()
```

**3-misol: Ob-havo dasturi**

```python
def havo_holati(shahar):
    """Shahar bo'yicha ob-havo ma'lumoti"""
    ma_lumotlar = {
        "toshkent": {"harorat": 25, "holat": "Quyoshli", "namlik": 40},
        "samarqand": {"harorat": 23, "holat": "Bulutli", "namlik": 45},
        "buxoro": {"harorat": 28, "holat": "Quyoshli", "namlik": 30},
        "xorazm": {"harorat": 27, "holat": "Quyoshli", "namlik": 35},
        "andijon": {"harorat": 24, "holat": "Yomg'irli", "namlik": 60}
    }
    
    return ma_lumotlar.get(shahar.lower())

def havo_chiqar(shahar, ma_lumot):
    """Ob-havo ma'lumotini chiqarish"""
    if ma_lumot:
        print(f"\n{shahar.upper()} SHAHRI OB-HAVOSI")
        print("-" * 30)
        print(f"Harorat: {ma_lumot['harorat']}°C")
        print(f"Holat: {ma_lumot['holat']}")
        print(f"Namlik: {ma_lumot['namlik']}%")
        
        if ma_lumot['harorat'] > 30:
            print("Issiq! Soyada qoling.")
        elif ma_lumot['harorat'] > 20:
            print("Iliq havo. Sayr qilish uchun qulay.")
        elif ma_lumot['harorat'] > 10:
            print("Salqin. Ko'ylak kiyish tavsiya.")
        else:
            print("Sovuq. Issiq kiyining.")
    else:
        print(f"Kechirasiz, {shahar} shahri haqida ma'lumot yo'q.")

def mashhur_shaharlar():
    """Mashhur shaharlar ro'yxati"""
    print("\nMASHHUR SHAHARLAR:")
    print("• Toshkent")
    print("• Samarqand")
    print("• Buxoro")
    print("• Xorazm")
    print("• Andijon")

def ob_havo_dasturi():
    """Asosiy ob-havo dasturi"""
    print("OB-HAVO DASTURIGA XUSH KELIBSIZ!")
    
    while True:
        print("\n--- MENU ---")
        print("1. Shahar bo'yicha qidirish")
        print("2. Mashhur shaharlar ro'yxati")
        print("3. Chiqish")
        
        tanlov = input("Tanlovingiz: ")
        
        if tanlov == "1":
            shahar = input("Shahar nomini kiriting: ")
            ma_lumot = havo_holati(shahar)
            havo_chiqar(shahar, ma_lumot)
        elif tanlov == "2":
            mashhur_shaharlar()
        elif tanlov == "3":
            print("Dasturdan foydalanganingiz uchun rahmat!")
            break
        else:
            print("Noto'g'ri tanlov!")

# Dasturni ishga tushirish
ob_havo_dasturi()
```

### Muhim xususiyatlar

1. **Funktsiyani chaqirishdan oldin yaratish kerak:**
```python
# NOTO'G'RI
salom_ber()  # NameError: name 'salom_ber' is not defined
def salom_ber():
    print("Salom")

# TO'G'RI
def salom_ber():
    print("Salom")
salom_ber()  # Ishlaydi
```

2. **Qavslarni unutmaslik kerak:**
```python
def funktsiya():
    return "Bu funktsiya"

# Qavssiz chaqirish
print(funktsiya)  # <function funktsiya at 0x...> (funktsiya obyekti)

# Qavs bilan chaqirish
print(funktsiya())  # Bu funktsiya
```

3. **Funktsiya nomi muhim:**
```python
def hisobla():
    return 42

# Funktsiyani o'zgaruvchiga biriktirish
natija = hisobla()  # Funktsiya chaqiriladi, natija = 42
manzil = hisobla    # Funktsiya o'zi biriktiriladi

print(natija)  # 42
print(manzil()) # 42 (manzil orqali chaqirish)
```

4. **Funktsiyalarni ro'yxatda saqlash:**
```python
def qush():
    print("Qush sayrayapti")

def it():
    print("It hurmoqda")

def mushuk():
    print("Mushuk miyovlayapti")

# Funktsiyalarni ro'yxatda saqlash
hayvonlar = [qush, it, mushuk]

# Ro'yxat orqali chaqirish
for hayvon in hayvonlar:
    hayvon()
```

### Xatoliklar va ularni tuzatish

**1. NameError - Funktsiya topilmadi**
```python
# Xatolik
salom()  # NameError: name 'salom' is not defined

# Tuzatish
def salom():
    print("Salom")
salom()  # To'g'ri
```

**2. IndentationError - Noto'g'ri joy tashlash**
```python
# Xatolik
def salom():
print("Salom")  # IndentationError: expected an indented block

# Tuzatish
def salom():
    print("Salom")  # 4 bo'sh joy
```

**3. Qavslarni unutish**
```python
def sana():
    print("Bugun 2024")

# Xatolik (mantigan)
a = sana  # Funktsiya chaqirilmadi, a funktsiyaga tenglashdi
b = sana()  # Funktsiya chaqirildi, natija None

print(a)  # <function sana at 0x...>
print(b)  # None
```
---
<br>
<br>
<br>
<br>
<br>

## 📊 Parameters vs Arguments

### Kirish: Parameters va Arguments nima?

Funktsiyalar - bu dastur kodini qayta ishlatish imkonini beruvchi mexanizm. Lekin eng kuchli tomoni shundaki, ularga **tashqi ma'lumotlar** uzatish mumkin. Aynan shu ma'lumotlar uzatish jarayonida **parameter** va **argument** tushunchalari paydo bo'ladi.

Keling, oddiy misol bilan boshlaymiz:

```python
# Parameter - bu funktsiya yaratilayotganda qavs ichida yoziladigan o'zgaruvchi
def salom_ber(ism):  # "ism" - bu PARAMETER
    print(f"Salom, {ism}!")

# Argument - bu funktsiya chaqirilayotganda qavs ichiga beriladigan qiymat
salom_ber("Ali")     # "Ali" - bu ARGUMENT
```

**Asosiy farq:**
- **Parameter** - funktsiya ta'rifidagi "qabul qiluvchi" o'zgaruvchi
- **Argument** - funktsiyaga "uzatiladigan" haqiqiy qiymat

### Parameters (Parametrlar) - chuqur tushuncha

Parametrlar - bu funktsiya yaratilayotganda unga qanday ma'lumotlar kerakligini belgilaydigan "bo'sh joy"lar. Xuddi forma to'ldirishdagi bo'sh qatorlarga o'xshaydi:

```python
def shaxsiy_karta(ism, yosh, kasb):
    """Shaxsiy ma'lumotlarni chiqaruvchi funktsiya"""
    print("=" * 30)
    print(f"ISMI: {ism}")
    print(f"YOSHI: {yosh}")
    print(f"KASBI: {kasb}")
    print("=" * 30)

# Bu yerda ism, yosh, kasb - parametrlar
# Ular funktsiya ichida o'zgaruvchi sifatida ishlatiladi
```

### Arguments (Argumentlar) - chuqur tushuncha

Argumentlar - bu funktsiyani chaqirganda parametrlarga beriladigan haqiqiy qiymatlar:

```python
# Argumentlar bilan funktsiyani chaqirish
shaxsiy_karta("Alisher", 25, "Dasturchi")  
# "Alisher", 25, "Dasturchi" - argumentlar

shaxsiy_karta("Madina", 23, "O'qituvchi")  
# "Madina", 23, "O'qituvchi" - argumentlar
```

### Parameter turlari

Python'da parametrlarning 5 xil turi mavjud:

#### 1. Pozitsion parametrlar (Positional parameters)
Eng oddiy va keng tarqalgan parametr turi:

```python
def talaba_ma'lumot(ism, familiya, kurs):
    """Talaba ma'lumotlarini chiqarish"""
    print(f"Talaba: {ism} {familiya}")
    print(f"Kurs: {kurs}")

# Pozitsion argumentlar - berilish tartibi muhim
talaba_ma'lumot("Ali", "Valiyev", 2)
# Ism = "Ali", Familiya = "Valiyev", Kurs = 2

talaba_ma'lumot(2, "Ali", "Valiyev")  
# XATO! Tartib noto'g'ri: Ism = 2, Familiya = "Ali", Kurs = "Valiyev"
```

#### 2. Default parametrlar (Default parameters)
Agar argument berilmasa, ishlatiladigan standart qiymatlar:

```python
def mahsulot_chiqar(nom, narx, valyuta="so'm", chegirma=0):
    """Mahsulot ma'lumotlarini chiqarish"""
    chegirma_narx = narx * (1 - chegirma/100)
    
    print(f"Mahsulot: {nom}")
    print(f"Narxi: {narx} {valyuta}")
    
    if chegirma > 0:
        print(f"Chegirma: {chegirma}%")
        print(f"Chegirmali narx: {chegirma_narx} {valyuta}")

# Default parametrlar ishlatiladi
mahsulot_chiqar("Olma", 5000)
# Natija: valyuta="so'm", chegirma=0

# Default parametrlarni o'zgartirish
mahsulot_chiqar("Non", 3000, "so'm", 10)
# Natija: valyuta="so'm", chegirma=10

mahsulot_chiqar("Smartfon", 300, "$")
# Natija: valyuta="$", chegirma=0
```

**Muhim qoida:** Default parametrlar har doim oddiy parametrlardan KEYIN kelishi kerak:

```python
# TO'G'RI
def to'g'ri_funktsiya(a, b, c=10, d=20):
    pass

# NOTO'G'RI
def noto'g'ri_funktsiya(a=5, b, c):  # SyntaxError
    pass
```

### Argument turlari

#### 1. Pozitsion argumentlar (Positional arguments)
Argumentlar funktsiyadagi parametrlar tartibida beriladi:

```python
def kitob_ma'lumot(nom, muallif, yil, janr):
    print(f"Kitob: '{nom}'")
    print(f"Muallif: {muallif}")
    print(f"Yil: {yil}")
    print(f"Janr: {janr}")

# Pozitsion argumentlar - tartib muhim
kitob_ma'lumot("Dasturlash asoslari", "Karimov A.", 2023, "Darslik")
```

#### 2. Kalit so'z argumentlar (Keyword arguments)
Argumentlarni parametr nomi bilan berish:

```python
# Kalit so'z argumentlar - tartib muhim emas
kitob_ma'lumot(
    nom="Python dasturlash",
    muallif="Soliyev B.",
    yil=2024,
    janr="Kompyuter"
)

# Yoki aralashtirib ishlatish (pozitsionlar birinchi kelishi kerak)
kitob_ma'lumot(
    "Sun'iy intellekt",  # pozitsion
    muallif="Nurmatov J.",  # keyword
    yil=2023,  # keyword
    janr="Ilmiy"  # keyword
)
```

#### 3. Aralash argumentlar
Pozitsion va kalit so'z argumentlarni birgalikda ishlatish:

```python
def buyurtma(mahsulot, miqdor, manzil, telefon, to'lov_turi="naqd"):
    print(f"Mahsulot: {mahsulot}")
    print(f"Miqdor: {miqdor}")
    print(f"Manzil: {manzil}")
    print(f"Telefon: {telefon}")
    print(f"To'lov turi: {to'lov_turi}")

# Aralash argumentlar
buyurtma(
    "Noutbuk",           # pozitsion
    2,                   # pozitsion
    manzil="Toshkent",   # keyword
    telefon="+998901234567"  # keyword
)
```

### Keng qamrovli amaliy misollar

**1-misol: Restoran buyurtma tizimi**

```python
def restoran_buyurtma(
    taom_nomi,           # pozitsion parametr
    miqdor=1,            # default parametr
    qo'shimcha=None,     # default parametr
    yetkazish=False,     # default parametr
    manzil=None,         # default parametr
    telefon=None         # default parametr
):
    """Restoran buyurtmasini qayta ishlash"""
    
    print("\n" + "="*40)
    print("YANGI BUYURTMA QABUL QILINDI")
    print("="*40)
    
    # Asosiy ma'lumotlar
    print(f"Taom: {taom_nomi}")
    print(f"Miqdor: {miqdor} ta")
    
    # Qo'shimcha
    if qo'shimcha:
        print(f"Qo'shimcha: {qo'shimcha}")
    
    # Yetkazish ma'lumotlari
    if yetkazish:
        print("\nYETKAZISH MA'LUMOTLARI:")
        print(f"Manzil: {manzil}")
        print(f"Telefon: {telefon}")
        
        # Yetkazish vaqti
        from datetime import datetime, timedelta
        vaqt = datetime.now() + timedelta(minutes=45)
        print(f"Yetkazish vaqti: {vaqt.strftime('%H:%M')}")
    else:
        print("\nOlib ketish: 20 daqiqadan keyin tayyor")
    
    # Narx hisoblash
    narxlar = {
        "osh": 25000,
        "sho'rva": 18000,
        "manti": 22000,
        "kabob": 30000,
        "lag'mon": 20000
    }
    
    taom_narxi = narxlar.get(taom_nomi.lower(), 20000)
    umumiy = taom_narxi * miqdor
    
    print(f"\nHISOB:")
    print(f"{taom_narxi} so'm x {miqdor} = {umumiy} so'm")
    
    if yetkazish:
        umumiy += 5000  # yetkazish to'lovi
        print(f"Yetkazish: 5000 so'm")
    
    print(f"UMUMIY: {umumiy} so'm")
    
    return {
        "taom": taom_nomi,
        "miqdor": miqdor,
        "umumiy": umumiy,
        "yetkazish": yetkazish
    }

# Turli xil argumentlar bilan chaqirish

# 1. Minimal argumentlar
print("\n=== 1-BUYURTMA (MINIMAL) ===")
buyurtma1 = restoran_buyurtma("osh")

# 2. Miqdor bilan
print("\n=== 2-BUYURTMA (MIQDOR) ===")
buyurtma2 = restoran_buyurtma("manti", 3)

# 3. Qo'shimcha bilan
print("\n=== 3-BUYURTMA (QO'SHIMCHA) ===")
buyurtma3 = restoran_buyurtma("kabob", 2, qo'shimcha="ko'p piyoz")

# 4. Yetkazish bilan (kalit so'z argumentlar)
print("\n=== 4-BUYURTMA (YETKAZISH) ===")
buyurtma4 = restoran_buyurtma(
    "sho'rva", 
    2, 
    yetkazish=True,
    manzil="Chilonzor 19-mavze",
    telefon="+998901234567"
)

# 5. Hamma parametrlar bilan
print("\n=== 5-BUYURTMA (HAMMA PARAMETRLAR) ===")
buyurtma5 = restoran_buyurtma(
    "lag'mon",
    miqdor=4,
    qo'shimcha="qatiq",
    yetkazish=True,
    manzil="Yunusobod 12-uy",
    telefon="+998935678901"
)
```

**2-misol: Bank hisob tizimi (parametrlar bilan)**

```python
def bank_hisob(
    hisob_egasi,
    hisob_turi="joriy",
    balans=0,
    valyuta="UZS",
    kredit_limit=0,
    foiz_stavka=0
):
    """Yangi bank hisobini ochish"""
    
    print("\n" + "★"*40)
    print("YANGI BANK HISOB OCHILDI")
    print("★"*40)
    
    hisob_raqam = f"{hash(hisob_egasi) % 1000000:06d}"
    
    print(f"Hisob egasi: {hisob_egasi}")
    print(f"Hisob raqami: {hisob_raqam}")
    print(f"Hisob turi: {hisob_turi}")
    print(f"Balans: {balans} {valyuta}")
    
    if kredit_limit > 0:
        print(f"Kredit limit: {kredit_limit} {valyuta}")
    
    if foiz_stavka > 0:
        print(f"Foiz stavka: {foiz_stavka}%")
    
    return {
        "egasi": hisob_egasi,
        "raqam": hisob_raqam,
        "turi": hisob_turi,
        "balans": balans,
        "valyuta": valyuta,
        "kredit_limit": kredit_limit,
        "foiz": foiz_stavka
    }

def pul_otkaz(
    dan_hisob,
    ga_hisob,
    miqdor,
    kommentariya="",
    valyuta="UZS",
    tezkor=False
):
    """Pul o'tkazish amaliyoti"""
    
    print("\n" + "-"*40)
    print("PUL O'TKAZISH")
    print("-"*40)
    
    print(f"Kimdan: {dan_hisob['egasi']} ({dan_hisob['raqam']})")
    print(f"Kimga: {ga_hisob['egasi']} ({ga_hisob['raqam']})")
    print(f"Miqdor: {miqdor} {valyuta}")
    
    if kommentariya:
        print(f"Izoh: {kommentariya}")
    
    if tezkor:
        print("Tur: Tezkor o'tkazma")
        komissiya = miqdor * 0.01  # 1% komissiya
        print(f"Komissiya: {komissiya} {valyuta}")
        umumiy = miqdor + komissiya
    else:
        print("Tur: Oddiy o'tkazma")
        komissiya = 0
        umumiy = miqdor
    
    print(f"Jami hisobdan chiqadi: {umumiy} {valyuta}")
    
    return {
        "miqdor": miqdor,
        "komissiya": komissiya,
        "umumiy": umumiy,
        "tezkor": tezkor
    }

# Hisoblar ochish
print("\n=== HISOBLAR OCHISH ===")

hisob1 = bank_hisob("Alisher Karimov")
hisob2 = bank_hisob(
    "Madina Azizova",
    hisob_turi="jamg'arma",
    balans=1000000,
    foiz_stavka=12
)
hisob3 = bank_hisob(
    "Bobur Xasanov",
    hisob_turi="kredit",
    balans=-500000,
    valyuta="UZS",
    kredit_limit=10000000
)

# Pul o'tkazmalari
print("\n=== PUL O'TKAZMALARI ===")

otkazma1 = pul_otkaz(
    hisob2,
    hisob1,
    500000,
    kommentariya="Qarz"
)

otkazma2 = pul_otkaz(
    hisob3,
    hisob2,
    2000000,
    tezkor=True,
    kommentariya="Kredit to'lovi"
)
```

**3-misol: Onlayn kurs tizimi**

```python
def kurs_yaratish(
    nom,
    muallif,
    narx,
    davomiylik="3 oy",
    daraja="boshlang'ich",
    sertifikat=False,
    chegirma=0,
    til="o'zbek"
):
    """Yangi onlayn kurs yaratish"""
    
    print("\n" + "📚"*10)
    print("YANGI KURS YARATILDI")
    print("📚"*10)
    
    chegirma_narx = narx * (1 - chegirma/100)
    
    print(f"Kurs nomi: {nom}")
    print(f"Muallif: {muallif}")
    print(f"Daraja: {daraja}")
    print(f"Davomiylik: {davomiylik}")
    print(f"Til: {til}")
    print(f"Asosiy narx: {narx:,.0f} so'm")
    
    if chegirma > 0:
        print(f"Chegirma: {chegirma}%")
        print(f"Chegirmali narx: {chegirma_narx:,.0f} so'm")
    
    if sertifikat:
        print("Sertifikat: Ha")
    else:
        print("Sertifikat: Yo'q")
    
    return {
        "nom": nom,
        "muallif": muallif,
        "narx": chegirma_narx if chegirma > 0 else narx,
        "davomiylik": davomiylik,
        "daraja": daraja,
        "sertifikat": sertifikat
    }

def kursga_yozilish(
    talaba,
    kurs,
    tolov_turi="naqd",
    bonus=True,
    muddatli=False,
    oy_soni=0
):
    """Talabani kursga yozish"""
    
    print("\n" + "🎓"*10)
    print("YANGI TALABA QO'SHILDI")
    print("🎓"*10)
    
    print(f"Talaba: {talaba}")
    print(f"Kurs: {kurs['nom']}")
    print(f"Muallif: {kurs['muallif']}")
    print(f"To'lov turi: {tolov_turi}")
    
    if bonus:
        print("Bonus: 1 oy bepul")
    
    narx = kurs['narx']
    
    if muddatli and oy_soni > 0:
        oylik = narx / oy_soni
        print(f"Muddatli to'lov: {oy_soni} oy")
        print(f"Oylik to'lov: {oylik:,.0f} so'm")
        umumiy = narx + (narx * 0.05)  # 5% qo'shimcha
    else:
        umumiy = narx
    
    print(f"To'lanadigan summa: {umumiy:,.0f} so'm")
    
    return {
        "talaba": talaba,
        "kurs": kurs['nom'],
        "tolov": umumiy
    }

# Kurslar yaratish
print("\n=== KURSLAR YARATISH ===")

python_kurs = kurs_yaratish(
    "Python dasturlash",
    "Aziz Rahimov",
    500000,
    davomiylik="6 oy",
    daraja="boshlang'ich",
    sertifikat=True,
    til="o'zbek"
)

web_kurs = kurs_yaratish(
    "Web dasturlash",
    "Dilshod Karimov",
    800000,
    davomiylik="8 oy",
    daraja="o'rta",
    chegirma=15,
    sertifikat=True
)

mobile_kurs = kurs_yaratish(
    "Mobile ilovalar",
    "Jamshid Aliyev",
    1200000,
    davomiylik="4 oy",
    daraja="yuqori",
    chegirma=10,
    til="ingliz"
)

# Kursga yozilishlar
print("\n=== KURSGA YOZILISHLAR ===")

yozilish1 = kursga_yozilish(
    "Ali Valiyev",
    python_kurs,
    tolov_turi="karta",
    bonus=True
)

yozilish2 = kursga_yozilish(
    "Zarina Abdullayeva",
    web_kurs,
    tolov_turi="naqd",
    muddatli=True,
    oy_soni=3
)

yozilish3 = kursga_yozilish(
    "Sherzod Tursunov",
    mobile_kurs,
    tolov_turi="payme",
    bonus=True
)
```

**4-misol: Tibbiy konsultatsiya tizimi**

```python
def shifokor_qabul(
    bemor_ismi,
    yoshi,
    simptomlar,
    shifokor_turi="terapevt",
    shoshilinch=False,
    oldingi_tashxis=None,
    dorilar=None
):
    """Shifokor qabulini tashkil qilish"""
    
    print("\n" + "🏥"*10)
    print("YANGI TIBBIY QABUL")
    print("🏥"*10)
    
    print(f"Bemor: {bemor_ismi}")
    print(f"Yosh: {yoshi}")
    print(f"Shifokor: {shifokor_turi}")
    
    print("\nSimptomlar:")
    for i, simptom in enumerate(simptomlar, 1):
        print(f"  {i}. {simptom}")
    
    if shoshilinch:
        print("\n🚨 SHOSHILINCH QABUL!")
        navbat = "Yo'q (birinchi navbatda)"
    else:
        navbat = "20 daqiqa"
    
    print(f"Kutilayotgan vaqt: {navbat}")
    
    if oldingi_tashxis:
        print(f"\nOldingi tashxis: {oldingi_tashxis}")
    
    if dorilar:
        print("\nTavsiya etilgan dorilar:")
        for dori in dorilar:
            print(f"  • {dori}")
    
    # Qabul narxi
    narxlar = {
        "terapevt": 50000,
        "kardiolog": 100000,
        "nevrolog": 120000,
        "pediatr": 60000,
        "xirurg": 150000
    }
    
    narx = narxlar.get(shifokor_turi, 50000)
    
    if shoshilinch:
        narx *= 1.5  # 50% qo'shimcha
        print(f"\nQabul narxi (shoshilinch): {narx:,.0f} so'm")
    else:
        print(f"\nQabul narxi: {narx:,.0f} so'm")
    
    return {
        "bemor": bemor_ismi,
        "shifokor": shifokor_turi,
        "narx": narx,
        "shoshilinch": shoshilinch
    }

def laboratoriya_tahlil(
    bemor_ismi,
    tahlil_turi,
    och_qoringa=False,
    tezkor=False,
    qoshimcha_parametrlar=None
):
    """Laboratoriya tahlillarini o'tkazish"""
    
    print("\n" + "🔬"*10)
    print("LABORATORIYA TAHLILI")
    print("🔬"*10)
    
    print(f"Bemor: {bemor_ismi}")
    print(f"Tahlil turi: {tahlil_turi}")
    
    if och_qoringa:
        print("Holat: Och qoringa")
    
    if tezkor:
        print("Tur: Tezkor tahlil")
        natija_vaqti = "1 soat"
    else:
        print("Tur: Oddiy tahlil")
        natija_vaqti = "24 soat"
    
    print(f"Natija vaqti: {natija_vaqti}")
    
    if qoshimcha_parametrlar:
        print("\nQo'shimcha parametrlar:")
        for param in qoshimcha_parametrlar:
            print(f"  • {param}")
    
    # Tahlil narxlari
    narxlar = {
        "qon tahlili": 30000,
        "siydik tahlili": 20000,
        "biox kimyo": 80000,
        "gormonlar": 120000,
        "infeksiyalar": 150000
    }
    
    narx = narxlar.get(tahlil_turi.lower(), 50000)
    
    if tezkor:
        narx *= 2  # 2 barobar qimmat
    
    print(f"\nTahlil narxi: {narx:,.0f} so'm")
    
    return narx

# Shifokor qabullari
print("\n=== SHIFOKOR QABULLARI ===")

qabul1 = shifokor_qabul(
    "Olimjon Karimov",
    35,
    ["bosh og'rig'i", "isitma", "tomoq og'rig'i"],
    shifokor_turi="terapevt",
    dorilar=["Paratsetamol", "Vitamin C"]
)

qabul2 = shifokor_qabul(
    "Dilnoza Rahimova",
    28,
    ["yurak tez urishi", "nafas qisilishi"],
    shifokor_turi="kardiolog",
    shoshilinch=True,
    oldingi_tashxis="Aritmiya"
)

qabul3 = shifokor_qabul(
    "Jasur Aliyev",
    45,
    ["bel og'rig'i", "oyoq uvushishi"],
    shifokor_turi="nevrolog"
)

# Laboratoriya tahlillari
print("\n=== LABORATORIYA TAHLILLARI ===")

tahlil1 = laboratoriya_tahlil(
    "Olimjon Karimov",
    "qon tahlili",
    och_qoringa=True
)

tahlil2 = laboratoriya_tahlil(
    "Dilnoza Rahimova",
    "biox kimyo",
    tezkor=True,
    och_qoringa=True,
    qoshimcha_parametrlar=["xolesterin", "glyukoza", "temir"]
)

tahlil3 = laboratoriya_tahlil(
    "Jasur Aliyev",
    "gormonlar",
    och_qoringa=True,
    qoshimcha_parametrlar=["qalqonsimon", "insulin"]
)
```

### Parameter va Argumentlar bilan ishlashda muhim qoidalar

#### 1. Pozitsion argumentlar har doim kalit so'z argumentlardan oldin kelishi kerak:

```python
# TO'G'RI
def funktsiya(a, b, c=10, d=20):
    pass

funktsiya(1, 2, c=30, d=40)  # Pozitsion → Keyword

# NOTO'G'RI
funktsiya(a=1, 2, 3)  # SyntaxError: positional argument follows keyword argument
```

#### 2. Default parametrlar o'zgarmas qiymatlar bo'lishi kerak:

```python
# YOMASh AMALIYOT (mutable default)
def xato_qilish(mijozlar=[]):  # [] mutable - xavfli!
    mijozlar.append("yangi mijoz")
    return mijozlar

# Bu funktsiya har safar chaqirilganda bir ro'yxatga qo'shadi
print(xato_qilish())  # ['yangi mijoz']
print(xato_qilish())  # ['yangi mijoz', 'yangi mijoz']

# TO'G'RI USUL
def togri_usul(mijozlar=None):
    if mijozlar is None:
        mijozlar = []
    mijozlar.append("yangi mijoz")
    return mijozlar

print(togri_usul())  # ['yangi mijoz']
print(togri_usul())  # ['yangi mijoz']
```

#### 3. Argumentlarni paketlash va yoyish:

```python
def mahsulot_malumot(nom, narx, miqdor, yetkazib_beruvchi):
    print(f"Mahsulot: {nom}")
    print(f"Narx: {narx}")
    print(f"Miqdor: {miqdor}")
    print(f"Yetkazib beruvchi: {yetkazib_beruvchi}")

# Yoyish operatori (*) bilan
malumotlar = ["Olma", 5000, 100, "Meva Corp"]
mahsulot_malumot(*malumotlar)  # Ro'yxatni yoyish

# Lug'atni yoyish (**) bilan
malumotlar_dict = {
    "nom": "Banan",
    "narx": 8000,
    "miqdor": 50,
    "yetkazib_beruvchi": "Banana Ltd"
}
mahsulot_malumot(**malumotlar_dict)  # Lug'atni yoyish
```

### Xulosa

1. **Parameter** - funktsiya yaratilganda qavs ichida yoziladigan o'zgaruvchi
2. **Argument** - funktsiya chaqirilganda beriladigan haqiqiy qiymat
3. **Pozitsion parametrlar** - tartib bo'yicha qiymat oladi
4. **Default parametrlar** - standart qiymatga ega
5. **Kalit so'z argumentlar** - parametr nomi bilan qiymat berish
6. **Qoidalar**:
   - Default parametrlar oddiy parametrlardan keyin kelishi kerak
   - Pozitsion argumentlar kalit so'z argumentlardan oldin kelishi kerak
   - Mutable obyektlarni default parametr sifatida ishlatish xavfli

---
<br>
<br>
<br>
<br>
<br>
## 📤 Return Values (single, multiple, None)

### Return nima va nima uchun kerak?

`return` - bu funktsiyadan natija qaytarish uchun ishlatiladigan kalit so'z. Funktsiya bajarilib bo'lgach, uning natijasini dasturning boshqa qismlarida ishlatish imkonini beradi.

**Real hayotdan misol:**
- Nonvoyxonaga borib non olasiz - bu "funktsiyani chaqirish"
- Nonvoy sizga non beradi - bu "return" (qaytarish)
- Siz bu nonni uyda yeyishingiz mumkin - bu "natijadan foydalanish"

```python
# Return ishlatilmagan holat
def non_ber():
    print("Non tayyor!")  # Faqat ekranga chiqaradi

natija = non_ber()  # print() ekranga chiqaradi
print(natija)  # None - chunki funktsiya hech narsa qaytarmadi

# Return ishlatilgan holat
def non_ber_with_return():
    non = "Oq non"
    return non  # Nonni qaytaradi

nonim = non_ber_with_return()  # nonim = "Oq non"
print(f"Menda {nonim} bor")  # Menda Oq non bor
```

### Single Return Value (Yagona qiymat qaytarish)

Funktsiya bitta qiymat qaytarishi mumkin - son, matn, ro'yxat yoki boshqa har qanday obyekt:

```python
# Son qaytarish
def kvadrat(son):
    return son ** 2

natija = kvadrat(5)
print(f"5 ning kvadrati: {natija}")  # 25
print(f"10 ning kvadrati: {kvadrat(10)}")  # 100

# Matn qaytarish
def salomlash(ism):
    return f"Assalomu alaykum, {ism}!"

xabar = salomlash("Ali")
print(xabar)  # Assalomu alaykum, Ali!

# Ro'yxat qaytarish
def juft_sonlar(limit):
    juftlar = []
    for son in range(0, limit + 1, 2):
        juftlar.append(son)
    return juftlar

natija = juft_sonlar(10)
print(f"Juft sonlar: {natija}")  # Juft sonlar: [0, 2, 4, 6, 8, 10]
```

### Return bilan amaliy misollar

**1-misol: Bank hisob-kitobi**

```python
def oylik_foiz(principal, foiz_stavka, oylar):
    """
    Oylik foiz hisoblash
    principal: boshlang'ich summa
    foiz_stavka: yillik foiz (%)
    oylar: necha oy
    """
    oylik_foiz_stavka = foiz_stavka / 12 / 100
    foiz_summa = principal * oylik_foiz_stavka * oylar
    umumiy = principal + foiz_summa
    
    return umumiy  # Faqat umumiy summani qaytarish

# Return qilingan qiymatdan foydalanish
natija1 = oylik_foiz(1000000, 12, 6)
natija2 = oylik_foiz(5000000, 15, 12)

print(f"6 oydan keyin: {natija1:,.0f} so'm")
print(f"12 oydan keyin: {natija2:,.0f} so'm")

# Return qilingan qiymatni boshqa hisoblarda ishlatish
soliq = natija2 * 0.02  # 2% soliq
print(f"To'lanadigan soliq: {soliq:,.0f} so'm")
```

**2-misol: Matematik amallar**

```python
def uchburchak_yuzi(asos, balandlik):
    """Uchburchak yuzini hisoblash"""
    return (asos * balandlik) / 2

def aylana_uzunligi(radius):
    """Aylana uzunligini hisoblash"""
    return 2 * 3.14159 * radius

def tortburchak_perimetri(uzunlik, kenglik):
    """To'rtburchak perimetrini hisoblash"""
    return 2 * (uzunlik + kenglik)

# Hisob-kitoblar
uchburchak = uchburchak_yuzi(10, 5)
aylana = aylana_uzunligi(7)
tortburchak = tortburchak_perimetri(8, 4)

print("=== GEOMETRIK HISOBLAR ===")
print(f"Uchburchak yuzi: {uchburchak}")
print(f"Aylana uzunligi: {aylana:.2f}")
print(f"To'rtburchak perimetri: {tortburchak}")

# Return qilingan qiymatlarni taqqoslash
if uchburchak > tortburchak:
    print("Uchburchak yuzi kattaroq")
else:
    print("To'rtburchak perimetri kattaroq")
```

### Multiple Return Values (Bir necha qiymat qaytarish)

Python'da funktsiya bir necha qiymatni vergul bilan ajratib qaytarishi mumkin. Bu qiymatlar avtomatik ravishda tuple (kortej) shaklida qaytariladi:

```python
def talaba_ma'lumoti():
    ism = "Ali"
    yosh = 20
    fakultet = "IT"
    return ism, yosh, fakultet  # 3 ta qiymat qaytarish

# Qaytarilgan qiymatlarni olish
natija = talaba_ma'lumoti()
print(natija)  # ('Ali', 20, 'IT')
print(type(natija))  # <class 'tuple'>

# Qiymatlarni alohida o'zgaruvchilarga olish
ismi, yoshi, fakulteti = talaba_ma'lumoti()
print(f"Ism: {ismi}, Yosh: {yoshi}, Fakultet: {fakulteti}")
```

**Keng qamrovli misollar:**

**1-misol: Statistika hisoblash**

```python
def sonlar_statistikasi(sonlar):
    """
    Sonlar ro'yxati uchun turli statistik ma'lumotlar qaytarish
    """
    eng_kichik = min(sonlar)
    eng_katta = max(sonlar)
    yigindi = sum(sonlar)
    ortacha = yigindi / len(sonlar)
    uzunlik = len(sonlar)
    
    return eng_kichik, eng_katta, yigindi, ortacha, uzunlik

# Test qilish
test_sonlar = [15, 24, 36, 8, 42, 17, 31]

# 1-usul: Tuple sifatida olish
natija = sonlar_statistikasi(test_sonlar)
print("=== STATISTIKA (Tuple) ===")
print(f"Natija: {natija}")
print(f"Eng kichik: {natija[0]}")
print(f"Eng katta: {natija[1]}")
print(f"Yig'indi: {natija[2]}")
print(f"O'rtacha: {natija[3]:.2f}")
print(f"Uzunlik: {natija[4]}")

# 2-usul: Alohida o'zgaruvchilarga olish
min_son, max_son, summa, avg, count = sonlar_statistikasi(test_sonlar)
print("\n=== STATISTIKA (Alohida) ===")
print(f"Min: {min_son}, Max: {max_son}")
print(f"Sum: {summa}, O'rtacha: {avg:.2f}")
print(f"Elementlar soni: {count}")
```

**2-misol: Foydalanuvchi ma'lumotlari**

```python
def foydalanuvchi_kiritish():
    """
    Foydalanuvchidan ma'lumotlarni olib, qaytarish
    """
    print("=== FOYDALANUVCHI MA'LUMOTLARI ===")
    ism = input("Ismingiz: ")
    yosh = int(input("Yoshingiz: "))
    shahar = input("Shahringiz: ")
    kasb = input("Kasbingiz: ")
    
    return ism, yosh, shahar, kasb

def yosh_tavsiyasi(yosh):
    """Yoshga qarab tavsiyalar"""
    if yosh < 18:
        return "yosh", "O'qishingiz kerak"
    elif yosh < 30:
        return "yigit", "Ishlash va o'qish"
    elif yosh < 50:
        return "o'rta", "Karyera va oila"
    else:
        return "katta", "Dam olish va oila"

# Foydalanuvchi ma'lumotlarini olish
ism, yosh, shahar, kasb = foydalanuvchi_kiritish()

# Ma'lumotlarni qayta ishlash
yosh_guruhi, tavsiya = yosh_tavsiyasi(yosh)

print("\n=== FOYDALANUVCHI PROFILI ===")
print(f"Ism: {ism}")
print(f"Yosh: {yosh} ({yosh_guruhi})")
print(f"Shahar: {shahar}")
print(f"Kasb: {kasb}")
print(f"Tavsiya: {tavsiya}")
```

**3-misol: Do'kon hisob-kitobi**

```python
def do'kon_hisobi(mahsulotlar):
    """
    Do'kondagi mahsulotlar hisobini yuritish
    Qaytaradi: (jami_summa, eng_qimmat, eng_arzon, o'rtacha_narx, shtrix_kod)
    """
    if not mahsulotlar:
        return 0, None, None, 0, "000000"
    
    narxlar = [mahsulot[1] for mahsulot in mahsulotlar]
    jami = sum(narxlar)
    eng_qimmat = max(mahsulotlar, key=lambda x: x[1])
    eng_arzon = min(mahsulotlar, key=lambda x: x[1])
    ortacha = jami / len(mahsulotlar)
    shtrix = f"{hash(jami) % 1000000:06d}"
    
    return jami, eng_qimmat, eng_arzon, ortacha, shtrix

# Mahsulotlar: (nom, narx, miqdor)
mahsulotlar = [
    ("Olma", 5000, 10),
    ("Banan", 8000, 5),
    ("Apelsin", 6000, 8),
    ("Uzum", 12000, 3),
    ("Anor", 10000, 4)
]

# Hisob-kitob
jami, qimmat, arzon, ortacha, kod = do'kon_hisobi(mahsulotlar)

print("=== DO'KON HISOBOTI ===")
print(f"Chek raqami: {kod}")
print(f"Jami summa: {jami:,.0f} so'm")
print(f"O'rtacha narx: {ortacha:,.0f} so'm")
print(f"Eng qimmat: {qimmat[0]} - {qimmat[1]:,.0f} so'm ({qimmat[2]} dona)")
print(f"Eng arzon: {arzon[0]} - {arzon[1]:,.0f} so'm ({arzon[2]} dona)")
```

### Return None

`None` - bu Python'da "hech narsa" yoki "qiymat yo'q" degan ma'noni anglatadi. Funktsiya `return` ishlatmasa yoki `return` dan keyin hech narsa yozilmasa, `None` qaytaradi:

```python
def hech_narsa_qaytarmaydi():
    print("Bu funktsiya hech narsa qaytarmaydi")

def return_none():
    print("Bu funktsiya None qaytaradi")
    return

# Ikkala funktsiya ham None qaytaradi
natija1 = hech_narsa_qaytarmaydi()
natija2 = return_none()

print(natija1)  # None
print(natija2)  # None
print(type(natija1))  # <class 'NoneType'>
```

**None bilan ishlash:**

```python
def find_user(user_id):
    """Foydalanuvchini qidirish - topilmasa None qaytaradi"""
    users = {1: "Ali", 2: "Vali", 3: "Hasan"}
    return users.get(user_id)  # Agar user topilmasa None qaytaradi

# None ni tekshirish
def user_ma'lumot(user_id):
    user = find_user(user_id)
    
    if user is None:  # None ni tekshirish (== emas, is ishlatiladi)
        print(f"User {user_id} topilmadi!")
        return None
    
    return f"User: {user}"

print(user_ma'lumot(2))  # User: Vali
print(user_ma'lumot(5))  # User 5 topilmadi! (keyin None qaytadi)
```

### Return vs Print - Muhim farq

```python
def print_ishlati():
    print("Bu ekranga chiqadi")
    print("Lekin hech narsa qaytarmaydi")

def return_ishlati():
    return "Bu qiymat qaytaradi"

# Print - faqat ekranga chiqaradi
print_ishlati()  # Ekranga chiqadi
natija_print = print_ishlati()
print(f"Print natijasi: {natija_print}")  # Print natijasi: None

# Return - qiymat qaytaradi
qaytarilgan = return_ishlati()
print(f"Return natijasi: {qaytarilgan}")  # Return natijasi: Bu qiymat qaytaradi

# Return qilingan qiymat bilan ishlash
matn = return_ishlati()
print(matn.upper())  # BU QIYMAT QAYTARADI
```

### Murakkab return misollari

**1-misol: RESTORAN TIZIMI**

```python
def restoran_hisoblash(buyurtmalar, mijoz_turi="oddiy", aksiya=False):
    """
    Restoran buyurtmasini hisoblash
    Qaytaradi: (jami_summa, chegirma, soliq, umumiy, bonus)
    """
    if not buyurtmalar:
        return 0, 0, 0, 0, 0
    
    # Jami summa
    jami = sum(buyurtmalar.values())
    
    # Chegirma
    chegirma = 0
    if mijoz_turi == "vip":
        chegirma = jami * 0.15  # 15% chegirma
    elif mijoz_turi == "doimiy":
        chegirma = jami * 0.10  # 10% chegirma
    elif aksiya:
        chegirma = jami * 0.05   # 5% aksiya
    
    # Soliq (12%)
    soliq = (jami - chegirma) * 0.12
    
    # Umumiy to'lov
    umumiy = jami - chegirma + soliq
    
    # Bonus ball
    bonus = int(umumiy / 1000)  # Har 1000 so'm uchun 1 ball
    
    return jami, chegirma, soliq, umumiy, bonus

def hisobni_chiqarish(jami, chegirma, soliq, umumiy, bonus):
    """Hisobni chiroyli qilib chiqarish"""
    print("\n" + "="*40)
    print("RESTORAN HISOBI")
    print("="*40)
    print(f"Jami summa: {jami:>15,.0f} so'm")
    
    if chegirma > 0:
        print(f"Chegirma: {chegirma:>16,.0f} so'm")
        print(f"Chegirmadan keyin: {jami - chegirma:>10,.0f} so'm")
    
    print(f"Soliq (12%): {soliq:>14,.0f} so'm")
    print("-"*40)
    print(f"UMUMIY: {umumiy:>19,.0f} so'm")
    print(f"Bonus ball: {bonus:>16}")
    print("="*40)

# Buyurtmalar
buyurtma1 = {
    "osh": 25000,
    "sho'rva": 18000,
    "salat": 15000
}

buyurtma2 = {
    "kabob": 30000,
    "non": 3000,
    "choy": 5000,
    "manti": 22000
}

# Turli mijozlar uchun hisoblar
print("=== ODDIY MIJOZ ===")
jami, chegirma, soliq, umumiy, bonus = restoran_hisoblash(buyurtma1, "oddiy")
hisobni_chiqarish(jami, chegirma, soliq, umumiy, bonus)

print("\n=== VIP MIJOZ (AKSIYA) ===")
jami, chegirma, soliq, umumiy, bonus = restoran_hisoblash(buyurtma2, "vip", aksiya=True)
hisobni_chiqarish(jami, chegirma, soliq, umumiy, bonus)

# Bonuslarni yig'ish
jami_bonus = 0
for i in range(3):
    jami, chegirma, soliq, umumiy, bonus = restoran_hisoblash(buyurtma1)
    jami_bonus += bonus

print(f"\n3 ta buyurtma uchun jami bonus: {jami_bonus}")
```

**2-misol: O'QUV MARKAZI TIZIMI**

```python
def talaba_baholari(baholar):
    """
    Talaba baholarini tahlil qilish
    Qaytaradi: (o'rtacha, maksimal, minimal, harf_baho, status, tavsiya)
    """
    if not baholar:
        return 0, 0, 0, 'F', 'Yomon', "Baholar mavjud emas"
    
    ortacha = sum(baholar) / len(baholar)
    maks = max(baholar)
    min_baho = min(baholar)
    
    # Harf baho
    if ortacha >= 90:
        harf = 'A'
        status = "A'lo"
        tavsiya = "Grant asosida o'qish"
    elif ortacha >= 80:
        harf = 'B'
        status = "Yaxshi"
        tavsiya = "Kontrakt asosida o'qish"
    elif ortacha >= 70:
        harf = 'C'
        status = "O'rtacha"
        tavsiya = "Qo'shimcha mashg'ulotlar"
    elif ortacha >= 60:
        harf = 'D'
        status = "Qoniqarli"
        tavsiya = "Repetitor tavsiya etiladi"
    elif ortacha >= 50:
        harf = 'E'
        status = "Past"
        tavsiya = "Qayta imtihon"
    else:
        harf = 'F'
        status = "Yomon"
        tavsiya = "Kursni takrorlash"
    
    return ortacha, maks, min_baho, harf, status, tavsiya

def kurs_tahlili(barcha_talabalar):
    """
    Barcha talabalar tahlili
    Qaytaradi: (guruh_ortacha, eng_yaxshi, eng_past, a'lochilar_soni, yomonlar_soni)
    """
    if not barcha_talabalar:
        return 0, None, None, 0, 0
    
    guruh_ortacha = sum(talaba[1] for talaba in barcha_talabalar) / len(barcha_talabalar)
    eng_yaxshi = max(barcha_talabalar, key=lambda x: x[1])
    eng_past = min(barcha_talabalar, key=lambda x: x[1])
    
    a'lochilar = sum(1 for talaba in barcha_talabalar if talaba[1] >= 90)
    yomonlar = sum(1 for talaba in barcha_talabalar if talaba[1] < 60)
    
    return guruh_ortacha, eng_yaxshi, eng_past, a'lochilar, yomonlar

# Talabalar ma'lumotlari
talabalar = [
    ("Ali Valiyev", [85, 90, 78, 92, 88]),
    ("Dilnoza Azizova", [92, 95, 89, 94, 96]),
    ("Bobur Karimov", [72, 68, 75, 70, 65]),
    ("Madina Rahimova", [98, 94, 96, 92, 95]),
    ("Jasur Tursunov", [55, 60, 58, 62, 51])
]

print("=== TALABALAR TAHLILI ===")
for ism, baholar in talabalar:
    ortacha, maks, min_baho, harf, status, tavsiya = talaba_baholari(baholar)
    
    print(f"\nTalaba: {ism}")
    print(f"Baholar: {baholar}")
    print(f"O'rtacha: {ortacha:.1f}")
    print(f"Eng yaxshi: {maks}")
    print(f"Eng past: {min_baho}")
    print(f"Harf baho: {harf}")
    print(f"Status: {status}")
    print(f"Tavsiya: {tavsiya}")
    print("-" * 30)

# Guruh tahlili
guruh_talabalari = [(ism, talaba_baholari(baholar)[0]) for ism, baholar in talabalar]
guruh_ort, eng_yax, eng_past, a'lochi, yomon = kurs_tahlili(guruh_talabalari)

print("\n=== GURUH TAHLILI ===")
print(f"Guruh o'rtachasi: {guruh_ort:.1f}")
print(f"Eng yaxshi talaba: {eng_yax[0]} ({eng_yax[1]:.1f})")
print(f"Eng past talaba: {eng_past[0]} ({eng_past[1]:.1f})")
print(f"A'lochilar soni: {a'lochi}")
print(f"Yomonlar soni: {yomon}")
```

**3-misol: VALYUTA AYIRBOSHLASH TIZIMI**

```python
def valyuta_ayirboshlash(summa, dan, ga, kurslar, komissiya=0.01):
    """
    Valyuta ayirboshlash hisobi
    Qaytaradi: (natija, kurs, komissiya_summa, umumiy, eski_balans, yangi_balans)
    """
    if dan not in kurslar or ga not in kurslar:
        return None, None, None, None, None, None
    
    # Kurslar orqali hisoblash
    if dan == "USD":
        asosiy = summa
    else:
        asosiy = summa / kurslar[dan]
    
    if ga == "USD":
        natija = asosiy
    else:
        natija = asosiy * kurslar[ga]
    
    # Komissiya
    kom_summa = natija * komissiya
    umumiy = natija - kom_summa
    
    return natija, kurslar[ga], kom_summa, umumiy, summa, umumiy

def bank_operatsiyalari():
    """Bank operatsiyalari simulyatsiyasi"""
    # Kurslar (USD ga nisbatan)
    kurslar = {
        "USD": 1,
        "UZS": 12500,
        "EUR": 1.08,
        "RUB": 0.011,
        "GBP": 1.25
    }
    
    # Mijoz balanslari
    mijozlar = {
        "Ali": {"USD": 1000, "UZS": 5000000, "EUR": 500},
        "Vali": {"USD": 500, "EUR": 1000, "GBP": 200},
        "Hasan": {"UZS": 10000000, "RUB": 50000}
    }
    
    print("=== BANK OPERATSIYALARI ===")
    
    for mijoz, balans in mijozlar.items():
        print(f"\nMijoz: {mijoz}")
        print(f"Joriy balans: {balans}")
        
        # USD dan UZS ga
        if "USD" in balans:
            natija, kurs, kom, umumiy, eski, yangi = valyuta_ayirboshlash(
                balans["USD"], "USD", "UZS", kurslar
            )
            if natija:
                print(f"\nUSD -> UZS ({kurs} so'm):")
                print(f"  {balans['USD']} USD = {natija:,.0f} UZS")
                print(f"  Komissiya (1%): {kom:,.0f} UZS")
                print(f"  Beriladigan: {umumiy:,.0f} UZS")
        
        # EUR dan USD ga
        if "EUR" in balans:
            natija, kurs, kom, umumiy, eski, yangi = valyuta_ayirboshlash(
                balans["EUR"], "EUR", "USD", kurslar
            )
            if natija:
                print(f"\nEUR -> USD (kurs: {kurs}):")
                print(f"  {balans['EUR']} EUR = {natija:.2f} USD")
                print(f"  Komissiya (1%): {kom:.2f} USD")
                print(f"  Beriladigan: {umumiy:.2f} USD")

# Test qilish
bank_operatsiyalari()
```

### Return va funksiya dizayni

**Yaxshi return dizayni qoidalari:**

1. **Funktsiya bitta vazifani bajarishi kerak**
```python
# YOMON - ikkala vazifani bajaradi
def hisobla_va_chiqar(son):
    kvadrat = son ** 2
    print(f"Kvadrat: {kvadrat}")
    return kvadrat

# YAXSHI - ajratilgan
def hisobla_kvadrat(son):
    return son ** 2

def chiqar_natija(natija):
    print(f"Natija: {natija}")
```

2. **Return qiymatlari izchil bo'lishi kerak**
```python
# YOMON - har xil tur qaytaradi
def find_user_bad(user_id):
    if user_id == 1:
        return "Ali"
    elif user_id == 2:
        return ["Vali", 25]
    else:
        return None

# YAXSHI - izchil tur qaytaradi
def find_user_good(user_id):
    users = {1: "Ali", 2: "Vali"}
    return users.get(user_id)  # Har doim str yoki None
```

3. **Return qilish yoki qilmaslikni aniq belgilash**
```python
def process_data(data, return_result=True):
    """
    Ma'lumotni qayta ishlash
    Agar return_result=True bo'lsa, natijani qaytaradi
    Aks holda None qaytaradi
    """
    result = data.upper()
    
    if return_result:
        return result
    else:
        print(f"Natija: {result}")
        return None
```

### Return bilan ishlashda muhim nuqtalar

1. **Return dan keyingi kod bajarilmaydi**
```python
def test_return():
    print("Bu qator bajariladi")
    return "Tugadi"
    print("Bu qator bajarilmaydi!")  # Hech qachon ishlamaydi
```

2. **Funktsiya bir necha return ga ega bo'lishi mumkin**
```python
def baholash(baho):
    if baho >= 90:
        return "A'lo"
    elif baho >= 80:
        return "Yaxshi"
    elif baho >= 70:
        return "O'rtacha"
    else:
        return "Past"
```

3. **Return qiymatini saqlash shart emas**
```python
def salom_ber():
    return "Assalomu alaykum"

# Return qiymatini saqlash shart emas
salom_ber()  # Bu ishlaydi, lekin natija yo'qoladi

# Yoki saqlash mumkin
natija = salom_ber()
print(natija)
```
---
<br>
<br>
<br>
<br>
<br>
## ⚙️ Default Arguments (def func(x=5))

### Default Arguments nima?

Default argumentlar - bu funktsiya yaratilayotganda parametrlarga beriladigan standart (odatiy) qiymatlardir. Agar funktsiyani chaqirishda ushbu parametr uchun argument berilmasa, avtomatik ravishda shu standart qiymat ishlatiladi.

**Real hayotdan misol:**
- **Restoran menyusi**: Aksariyat taomlar bilan birga non ham beriladi (default). Agar mijoz "nonsiz" desa, unda non berilmaydi.
- **Telefon sozlamalari**: Telefon yangi sotib olinganda "Standart rejim"da ishlaydi (default). Foydalanuvchi xohlasa sozlamalarni o'zgartirishi mumkin.

```python
# Oddiy misol
def salom_ber(ism="Dunyo"):
    """Agar ism berilmasa, "Dunyo" ga salom beradi"""
    print(f"Salom, {ism}!")

salom_ber("Ali")      # Salom, Ali!
salom_ber()           # Salom, Dunyo!  (default qiymat ishlatildi)
```

### Default Argumentlarning Sintaksisi

Default argumentlar funktsiya ta'rifida parametrga `=` belgisi orqali qiymat berish orqali yaratiladi:

```python
def funktsiya_nomi(parametr1=default_qiymat1, parametr2=default_qiymat2):
    # funktsiya tanasi
    pass
```

### Default Argumentlarning Asosiy Qoidalari

**1-Qoida: Default parametrlar har doim oddiy parametrlardan KEYIN kelishi kerak**

```python
# TO'G'RI
def to'g'ri_funktsiya(a, b, c=10, d=20):
    """a va b majburiy, c va d ixtiyoriy"""
    print(f"a={a}, b={b}, c={c}, d={d}")

to'g'ri_funktsiya(1, 2)           # a=1, b=2, c=10, d=20
to'g'ri_funktsiya(1, 2, 3)        # a=1, b=2, c=3, d=20
to'g'ri_funktsiya(1, 2, 3, 4)     # a=1, b=2, c=3, d=4

# NOTO'G'RI
def noto'g'ri_funktsiya(a=5, b, c):  # SyntaxError: non-default argument follows default argument
    pass
```

**2-Qoida: Default qiymatlar funktsiya yaratilganda bir marta hisoblanadi**

```python
import datetime

def vaqtni_chiqar(vaqt=datetime.datetime.now()):
    """Default qiymat funktsiya yaratilganda hisoblanadi"""
    print(f"Vaqt: {vaqt}")

print("Birinchi chaqirish:")
vaqtni_chiqar()  # Yaratilgan vaqtdagi vaqt

print("Ikkinchi chaqirish (1 soniya keyin):")
import time
time.sleep(1)
vaqtni_chiqar()  # Hali ham birinchi vaqt (o'zgarmaydi)
```

### Default Argumentlar bilan Amaliy Misollar

**1-misol: Pitsa buyurtma tizimi**

```python
def pitsa_buyurtma(
    turi="Margarita",
    olcham="o'rta",
    qoshimcha=None,
    yetkazish_manzili=None,
    soni=1
):
    """
    Pitsa buyurtma qilish funktsiyasi
    - turi: pitsa turi (default: Margarita)
    - olcham: kichik, o'rta, katta (default: o'rta)
    - qoshimcha: qo'shimcha masalliqlar (default: None)
    - yetkazish_manzili: manzil (default: None - olib ketish)
    - soni: pitsa soni (default: 1)
    """
    
    print("\n" + "="*40)
    print("🍕 PITSA BUYURTMA")
    print("="*40)
    
    # Asosiy ma'lumotlar
    print(f"Pitsa turi: {turi}")
    print(f"O'lcham: {olcham}")
    print(f"Soni: {soni}")
    
    # Qo'shimchalar
    if qoshimcha:
        if isinstance(qoshimcha, list):
            print(f"Qo'shimchalar: {', '.join(qoshimcha)}")
        else:
            print(f"Qo'shimcha: {qoshimcha}")
    
    # Yetkazish
    if yetkazish_manzili:
        print(f"Yetkazish manzili: {yetkazish_manzili}")
        yetkazish_narxi = 5000
        print(f"Yetkazish narxi: {yetkazish_narxi} so'm")
    else:
        print("Yetkazish: Olib ketish (bepul)")
        yetkazish_narxi = 0
    
    # Narx hisoblash
    narxlar = {
        "Margarita": {"kichik": 25000, "o'rta": 35000, "katta": 45000},
        "Pepperoni": {"kichik": 30000, "o'rta": 40000, "katta": 50000},
        "Four Cheese": {"kichik": 35000, "o'rta": 45000, "katta": 55000},
        "Hawaii": {"kichik": 32000, "o'rta": 42000, "katta": 52000}
    }
    
    asosiy_narx = narxlar.get(turi, narxlar["Margarita"]).get(olcham, 35000)
    qoshimcha_narx = len(qoshimcha) * 3000 if qoshimcha else 0
    
    jami = (asosiy_narx * soni) + qoshimcha_narx + yetkazish_narxi
    
    print(f"\nHISOB:")
    print(f"Asosiy narx: {asosiy_narx} so'm x {soni} = {asosiy_narx * soni} so'm")
    if qoshimcha_narx > 0:
        print(f"Qo'shimchalar: {qoshimcha_narx} so'm")
    print(f"Yetkazish: {yetkazish_narxi} so'm")
    print(f"JAMI: {jami} so'm")
    
    return {
        "turi": turi,
        "olcham": olcham,
        "soni": soni,
        "qoshimcha": qoshimcha,
        "jami_narx": jami,
        "yetkazish": yetkazish_manzili is not None
    }

# Turli xil buyurtmalar
print("1-BUYURTMA - Minimal (faqat default qiymatlar)")
buyurtma1 = pitsa_buyurtma()

print("\n2-BUYURTMA - Turi va o'lcham o'zgartirilgan")
buyurtma2 = pitsa_buyurtma(turi="Pepperoni", olcham="katta")

print("\n3-BUYURTMA - Qo'shimchalar bilan")
buyurtma3 = pitsa_buyurtma(
    turi="Four Cheese",
    olcham="o'rta",
    qoshimcha=["zaytun", "qo'ziqorin", "qalampir"],
    soni=2
)

print("\n4-BUYURTMA - Yetkazish bilan")
buyurtma4 = pitsa_buyurtma(
    turi="Hawaii",
    qoshimcha="ananas",
    yetkazish_manzili="Chilonzor 19-mavze 12-uy",
    soni=3
)

print("\n5-BUYURTMA - Hamma parametrlar")
buyurtma5 = pitsa_buyurtma(
    turi="Margarita",
    olcham="katta",
    qoshimcha=["qo'ziqorin", "kolbasa"],
    yetkazish_manzili="Yunusobod 8-mavze 5-uy",
    soni=4
)
```

**2-misol: Onlayn kurs tizimi**

```python
def kursga_yozilish(
    ism,
    familiya,
    kurs_nomi,
    yosh=18,
    daraja="boshlang'ich",
    til="o'zbek",
    tolov_turi="naqd",
    chegirma_kodi=None,
    sertifikat=True,
    eshitish_tavsiyalari=True
):
    """
    Onlayn kursga yozilish funktsiyasi
    - ism, familiya: majburiy parametrlar
    - qolganlari default qiymatlarga ega
    """
    
    print("\n" + "📚"*10)
    print("KURSGA YOZILISH")
    print("📚"*10)
    
    # Shaxsiy ma'lumotlar
    print(f"F.I.Sh.: {ism} {familiya}")
    print(f"Yosh: {yosh}")
    
    # Kurs ma'lumotlari
    print(f"Kurs: {kurs_nomi}")
    print(f"Daraja: {daraja}")
    print(f"Til: {til}")
    
    # To'lov ma'lumotlari
    print(f"To'lov turi: {tolov_turi}")
    
    # Chegirma
    narx = 500000
    if chegirma_kodi:
        if chegirma_kodi == "STUDENT2024":
            chegirma = narx * 0.15
            print(f"Chegirma kodi: {chegirma_kodi} (15%)")
        elif chegirma_kodi == "NEWYEAR":
            chegirma = narx * 0.20
            print(f"Chegirma kodi: {chegirma_kodi} (20%)")
        else:
            chegirma = 0
            print(f"Chegirma kodi: {chegirma_kodi} (noto'g'ri kod)")
    else:
        chegirma = 0
        print("Chegirma kodi: ishlatilmadi")
    
    umumiy = narx - chegirma
    
    print(f"\nHISOB:")
    print(f"Kurs narxi: {narx} so'm")
    if chegirma > 0:
        print(f"Chegirma: -{chegirma} so'm")
    print(f"To'lanadigan summa: {umumiy} so'm")
    
    # Qo'shimcha xizmatlar
    if sertifikat:
        print("Sertifikat: Ha (bepul)")
    else:
        print("Sertifikat: Yo'q")
    
    if eshitish_tavsiyalari:
        print("Eshitish tavsiyalari: Yoqilgan")
    
    return {
        "talaba": f"{ism} {familiya}",
        "kurs": kurs_nomi,
        "daraja": daraja,
        "tolov": umumiy,
        "sertifikat": sertifikat
    }

# Turli xil yozilishlar
print("1-YOZILISH - Minimal ma'lumotlar")
yozilish1 = kursga_yozilish("Ali", "Valiyev", "Python dasturlash")

print("\n2-YOZILISH - Yosh va daraja ko'rsatilgan")
yozilish2 = kursga_yozilish(
    "Zarina", 
    "Azizova", 
    "Web dasturlash",
    yosh=17,
    daraja="o'rta"
)

print("\n3-YOZILISH - Chegirma kodi bilan")
yozilish3 = kursga_yozilish(
    "Bobur",
    "Karimov",
    "Data Science",
    yosh=25,
    daraja="yuqori",
    til="ingliz",
    chegirma_kodu="STUDENT2024",
    sertifikat=True
)

print("\n4-YOZILISH - Hamma parametrlar o'zgartirilgan")
yozilish4 = kursga_yozilish(
    "Madina",
    "Rahimova",
    "Mobile Development",
    yosh=22,
    daraja="o'rta",
    til="ingliz",
    tolov_turi="karta",
    chegirma_kodu="NEWYEAR",
    sertifikat=True,
    eshitish_tavsiyalari=False
)

print("\n5-YOZILISH - Kalit so'z argumentlar bilan")
yozilish5 = kursga_yozilish(
    ism="Jasur",
    familiya="Tursunov",
    kurs_nomi="Frontend Development",
    daraja="boshlang'ich",
    til="o'zbek",
    eshitish_tavsiyalari=True
)

# Statistika
yozilishlar = [yozilish1, yozilish2, yozilish3, yozilish4, yozilish5]
jami_summa = sum(yozilish['tolov'] for yozilish in yozilishlar)

print(f"\n=== STATISTIKA ===")
print(f"Jami yozilishlar: {len(yozilishlar)} ta")
print(f"Jami to'lov: {jami_summa} so'm")
print(f"O'rtacha to'lov: {jami_summa/len(yozilishlar)} so'm")
```

**3-misol: Avtomobil ijarasi tizimi**

```python
def avtomobil_ijara(
    mijoz_ismi,
    avtomobil_turi="sedan",
    kun=1,
    haydovchi=False,
    bolalar_oyindigi=False,
    navigatsiya=True,
    sugurta_turi="standart",
    tolov_valyuta="UZS",
    bonus_karta=None
):
    """
    Avtomobil ijarasi funktsiyasi
    """
    
    print("\n" + "🚗"*10)
    print("AVTOMOBIL IJARASI")
    print("🚗"*10)
    
    # Asosiy ma'lumotlar
    print(f"Mijoz: {mijoz_ismi}")
    print(f"Avtomobil turi: {avtomobil_turi}")
    print(f"Ijara muddati: {kun} kun")
    
    # Narxlar bazasi
    narxlar = {
        "sedan": 100000,
        "jip": 150000,
        "business": 250000,
        "miniven": 180000,
        "sport": 300000
    }
    
    # Asosiy narx
    kunlik_narx = narxlar.get(avtomobil_turi, 100000)
    asosiy_narx = kunlik_narx * kun
    
    print(f"\nASOSIY NARX:")
    print(f"Kunlik: {kunlik_narx} {tolov_valyuta}")
    print(f"{kun} kun uchun: {asosiy_narx} {tolov_valyuta}")
    
    # Qo'shimcha xizmatlar
    qoshimcha = 0
    
    if haydovchi:
        haydovchi_narx = 50000 * kun
        qoshimcha += haydovchi_narx
        print(f"\nHaydovchi xizmati: +{haydovchi_narx} {tolov_valyuta}")
    
    if bolalar_oyindigi:
        bolalar_narx = 20000 * kun
        qoshimcha += bolalar_narx
        print(f"Bolalar o'rindig'i: +{bolalar_narx} {tolov_valyuta}")
    
    if navigatsiya:
        navigatsiya_narx = 15000 * kun
        qoshimcha += navigatsiya_narx
        print(f"Navigatsiya: +{navigatsiya_narx} {tolov_valyuta}")
    
    # Sug'urta
    sugurta_narxlari = {
        "standart": asosiy_narx * 0.05,
        "kengaytirilgan": asosiy_narx * 0.10,
        "full": asosiy_narx * 0.15
    }
    sugurta_narx = sugurta_narxlari.get(sugurta_turi, asosiy_narx * 0.05)
    qoshimcha += sugurta_narx
    print(f"Sug'urta ({sugurta_turi}): +{sugurta_narx} {tolov_valyuta}")
    
    # Bonus karta
    chegirma = 0
    if bonus_karta:
        if bonus_karta == "GOLD":
            chegirma = (asosiy_narx + qoshimcha) * 0.15
            print(f"\nBonus karta (GOLD): -15% chegirma")
        elif bonus_karta == "SILVER":
            chegirma = (asosiy_narx + qoshimcha) * 0.10
            print(f"\nBonus karta (SILVER): -10% chegirma")
        elif bonus_karta == "BRONZE":
            chegirma = (asosiy_narx + qoshimcha) * 0.05
            print(f"\nBonus karta (BRONZE): -5% chegirma")
    
    # Jami hisob
    jami = asosiy_narx + qoshimcha - chegirma
    
    print(f"\n" + "="*40)
    print(f"JAMI HISOB:")
    print(f"Asosiy: {asosiy_narx} {tolov_valyuta}")
    print(f"Qo'shimcha xizmatlar: +{qoshimcha} {tolov_valyuta}")
    if chegirma > 0:
        print(f"Chegirma: -{chegirma} {tolov_valyuta}")
    print(f"UMUMIY: {jami} {tolov_valyuta}")
    print("="*40)
    
    return {
        "mijoz": mijoz_ismi,
        "avtomobil": avtomobil_turi,
        "kun": kun,
        "jami_narx": jami,
        "valyuta": tolov_valyuta,
        "sugurta": sugurta_turi
    }

# Turli ijaralar
print("1-IJARA - Standart (sedan, 1 kun)")
ijara1 = avtomobil_ijara("Ali Karimov")

print("\n2-IJARA - Jip, 3 kun, haydovchi bilan")
ijara2 = avtomobil_ijara(
    "Bobur Aliyev",
    avtomobil_turi="jip",
    kun=3,
    haydovchi=True
)

print("\n3-IJARA - Business, 5 kun, full paket")
ijara3 = avtomobil_ijara(
    "Dilnoza Rahimova",
    avtomobil_turi="business",
    kun=5,
    haydovchi=True,
    bolalar_oyindigi=True,
    navigatsiya=True,
    sugurta_turi="full",
    bonus_karta="GOLD"
)

print("\n4-IJARA - Miniven, 2 kun, oila uchun")
ijara4 = avtomobil_ijara(
    "Jasur Tursunov",
    avtomobil_turi="miniven",
    kun=2,
    bolalar_oyindigi=True,
    sugurta_turi="kengaytirilgan",
    bonus_karta="SILVER"
)

print("\n5-IJARA - Sport, 1 kun, bonus kartasiz")
ijara5 = avtomobil_ijara(
    "Sherzod Hamidov",
    avtomobil_turi="sport",
    kun=1,
    navigatsiya=False,
    tolov_valyuta="USD"
)
```

### Default Argumentlar bilan Bog'liq Muhim Xususiyatlar

#### 1. Mutable Default Argumentlar (Xavfli tomoni)

```python
# XAVFLI USUL - mutable default (ro'yxat, lug'at va h.k.)
def xavfli_funktsiya(element, royxat=[]):
    """Ro'yxatga element qo'shish - default ro'yxat barcha chaqiruvlar uchun bir xil"""
    royxat.append(element)
    return royxat

print(xavfli_funktsiya(1))  # [1]
print(xavfli_funktsiya(2))  # [1, 2] - kutilmagan natija!
print(xavfli_funktsiya(3))  # [1, 2, 3] - ro'yxat to'planib bormoqda

# TO'G'RI USUL
def togri_funktsiya(element, royxat=None):
    """Har safar yangi ro'yxat yaratiladi"""
    if royxat is None:
        royxat = []
    royxat.append(element)
    return royxat

print(togri_funktsiya(1))  # [1]
print(togri_funktsiya(2))  # [2] - yangi ro'yxat
print(togri_funktsiya(3))  # [3] - yangi ro'yxat
```

#### 2. Default Argumentlar va Lambda Funktsiyalar

```python
# Lambda bilan xavfli misol
def yaratish_xavfli():
    """Xavfli - lambda default argument sifatida"""
    funktsiyalar = []
    for i in range(5):
        funktsiyalar.append(lambda: i)  # i o'zgaradi
    return funktsiyalar

for f in yaratish_xavfli():
    print(f(), end=" ")  # 4 4 4 4 4 - hammasi bir xil!

# To'g'ri usul
def yaratish_togri():
    """To'g'ri - i ni default argument sifatida berish"""
    funktsiyalar = []
    for i in range(5):
        funktsiyalar.append(lambda x=i: x)  # i ning qiymati saqlanadi
    return funktsiyalar

print()
for f in yaratish_togri():
    print(f(), end=" ")  # 0 1 2 3 4
```

### Default Argumentlar bilan Murakkab Misollar

**4-misol: Filtr va Qidiruv Tizimi**

```python
def mahsulot_qidiruv(
    nom=None,
    kategoriya=None,
    narx_min=0,
    narx_max=float('inf'),
    rang=None,
    olcham=None,
    brend=None,
    mavjudligi=True,
    sort_by="narx",
    sort_order="ascending",
    limit=10,
    offset=0
):
    """
    Mahsulotlarni qidirish va filtrlash
    Barcha parametrlar default qiymatlarga ega
    """
    
    print("\n" + "🔍"*10)
    print("MAHSULOT QIDIRUV")
    print("🔍"*10)
    
    # Filtr parametrlarini ko'rsatish
    print("Qo'llanilgan filtrlar:")
    if nom:
        print(f"  Nom: {nom}")
    if kategoriya:
        print(f"  Kategoriya: {kategoriya}")
    print(f"  Narx oralig'i: {narx_min} - {narx_max if narx_max != float('inf') else 'cheksiz'}")
    if rang:
        print(f"  Rang: {rang}")
    if olcham:
        print(f"  O'lcham: {olcham}")
    if brend:
        print(f"  Brend: {brend}")
    print(f"  Mavjudligi: {'Ha' if mavjudligi else 'Yo\'q'}")
    print(f"  Sortlash: {sort_by} ({sort_order})")
    print(f"  Limit: {limit}, Offset: {offset}")
    
    # Test ma'lumotlar
    mahsulotlar = [
        {"nom": "Noutbuk Asus", "kategoriya": "elektronika", "narx": 8000000, "brend": "Asus", "mavjud": True},
        {"nom": "Noutbuk HP", "kategoriya": "elektronika", "narx": 7500000, "brend": "HP", "mavjud": True},
        {"nom": "Telefon iPhone", "kategoriya": "elektronika", "narx": 12000000, "brend": "Apple", "mavjud": False},
        {"nom": "Telefon Samsung", "kategoriya": "elektronika", "narx": 6000000, "brend": "Samsung", "mavjud": True},
        {"nom": "Krasovka Nike", "kategoriya": "kiyim", "narx": 800000, "brend": "Nike", "mavjud": True},
        {"nom": "Sumka Gucci", "kategoriya": "aksesuar", "narx": 5000000, "brend": "Gucci", "mavjud": True},
        {"nom": "Soat Rolex", "kategoriya": "aksesuar", "narx": 15000000, "brend": "Rolex", "mavjud": False},
    ]
    
    # Filtrlash
    natija = []
    for m in mahsulotlar:
        if nom and nom.lower() not in m['nom'].lower():
            continue
        if kategoriya and m['kategoriya'] != kategoriya:
            continue
        if not (narx_min <= m['narx'] <= narx_max):
            continue
        if brend and m['brend'] != brend:
            continue
        if mavjudligi and not m['mavjud']:
            continue
        natija.append(m)
    
    # Sortlash
    if sort_by == "narx":
        natija.sort(key=lambda x: x['narx'], reverse=(sort_order == "descending"))
    elif sort_by == "nom":
        natija.sort(key=lambda x: x['nom'], reverse=(sort_order == "descending"))
    
    # Limit va offset
    natija = natija[offset:offset+limit]
    
    print(f"\nTopilgan mahsulotlar: {len(natija)} ta")
    for m in natija:
        print(f"  • {m['nom']} - {m['narx']} so'm ({m['brend']})")
    
    return natija

# Turli xil qidiruvlar
print("1-QIDIRUV - Barcha mahsulotlar")
qidiruv1 = mahsulot_qidiruv()

print("\n2-QIDIRUV - Elektronika kategoriyasi")
qidiruv2 = mahsulot_qidiruv(kategoriya="elektronika")

print("\n3-QIDIRUV - 5-10 million so'm oralig'idagi mahsulotlar")
qidiruv3 = mahsulot_qidiruv(narx_min=5000000, narx_max=10000000)

print("\n4-QIDIRUV - Mavjud Asus brend mahsulotlari")
qidiruv4 = mahsulot_qidiruv(brend="Asus", mavjudligi=True)

print("\n5-QIDIRUV - Murakkab qidiruv")
qidiruv5 = mahsulot_qidiruv(
    kategoriya="elektronika",
    narx_min=5000000,
    narx_max=15000000,
    mavjudligi=True,
    sort_by="narx",
    sort_order="descending",
    limit=5
)
```

**5-misol: Email Xabarnoma Tizimi**

```python
def send_email(
    to_address,
    subject="Xabarnoma",
    body="",
    cc=None,
    bcc=None,
    attachments=None,
    priority="normal",
    html=False,
    signature=True,
    auto_reply=False,
    charset="utf-8",
    timeout=30
):
    """
    Email jo'natish funktsiyasi
    - to_address: majburiy (yagona majburiy parametr)
    - qolgan barcha parametrlar default qiymatlarga ega
    """
    
    print("\n" + "📧"*10)
    print("EMAIL JO'NATISH")
    print("📧"*10)
    
    # Asosiy ma'lumotlar
    print(f"Kimga: {to_address}")
    print(f"Mavzu: {subject}")
    print(f"Prioritet: {priority}")
    print(f"Kodlash: {charset}")
    
    # CC va BCC
    if cc:
        print(f"CC: {', '.join(cc) if isinstance(cc, list) else cc}")
    if bcc:
        print(f"BCC: {', '.join(bcc) if isinstance(bcc, list) else bcc}")
    
    # Xabar formati
    print(f"Format: {'HTML' if html else 'Plain Text'}")
    
    # Xabar matni
    print(f"\nXabar matni:")
    print("-" * 40)
    if body:
        print(body)
    else:
        print("(Bo'sh xabar)")
    print("-" * 40)
    
    # Imzo
    if signature:
        print("\nImzo:")
        print("--\nHurmat bilan,\nAvtomatik xabarnoma tizimi")
    
    # Qo'shimchalar
    if attachments:
        print(f"\nQo'shimchalar: {len(attachments)} ta fayl")
        for att in attachments:
            print(f"  • {att}")
    
    # Avtomatik javob
    if auto_reply:
        print("\n⚠️ Avtomatik javob yoqilgan")
    
    # Xabarni jo'natish simulyatsiyasi
    print(f"\nXabar jo'natilmoqda... (timeout: {timeout} sekund)")
    print("✅ Xabar muvaffaqiyatli jo'natildi!")
    
    return {
        "status": "success",
        "to": to_address,
        "subject": subject,
        "priority": priority,
        "timestamp": "2024-01-15 14:30:00"
    }

# Turli xil xabarlar
print("1-XABAR - Minimal xabar")
xabar1 = send_email("user@example.com")

print("\n2-XABAR - Mavzu va matn bilan")
xabar2 = send_email(
    "admin@example.com",
    subject="Tizim yangilanishi",
    body="Hurmatli foydalanuvchi, tizim ertalab soat 3:00 da yangilanadi."
)

print("\n3-XABAR - CC va priority bilan")
xabar3 = send_email(
    "team@company.com",
    subject="Haftalik yig'ilish",
    body="Ertaga soat 10:00 da haftalik yig'ilish bo'lib o'tadi.",
    cc=["manager@company.com", "hr@company.com"],
    priority="high"
)

print("\n4-XABAR - Qo'shimchalar va HTML formatda")
xabar4 = send_email(
    "client@example.com",
    subject="Hisobot: 2024 Q1",
    body="<h1>Kvartal hisoboti</h1><p>Iltimos, qo'shimcha faylni ko'ring.</p>",
    attachments=["hisobot.pdf", "diagramma.png", "ma'lumotlar.xlsx"],
    html=True,
    signature=True
)

print("\n5-XABAR - Avtomatik javob bilan")
xabar5 = send_email(
    "support@company.com",
    subject="Yangi so'rov",
    body="Mening hisobimga kira olmayapman.",
    auto_reply=True,
    priority="high",
    timeout=60
)

print("\n6-XABAR - Hamma parametrlar bilan")
xabar6 = send_email(
    to_address="ceo@company.com",
    subject="Yillik hisobot",
    body="2024 yil yakunlari bo'yicha hisobot tayyor.",
    cc=["cfo@company.com", "coo@company.com"],
    bcc=["audit@company.com"],
    attachments=["annual_report_2024.pdf"],
    priority="high",
    html=True,
    signature=True,
    auto_reply=False,
    charset="utf-8",
    timeout=120
)
```

### Default Argumentlar bilan Bog'liq Best Practices

1. **Immutable (o'zgarmas) qiymatlardan foydalaning**
```python
# YAXSHI
def yaxshi(son=0, matn="", tuple_=()):
    pass

# YOMON
def yomon(ro'yxat=[], lug'at={}, obyekt=SomeClass()):
    pass
```

2. **None dan foydalaning va ichkarida tekshiring**
```python
def process_data(data, config=None):
    if config is None:
        config = {}
    # config bilan ishlash
```

3. **Default qiymatlarni hujjatlashtiring**
```python
def create_user(
    username,
    password,
    email=None,  # Agar berilmasa, email talab qilinmaydi
    is_active=True,  # Yangi userlar aktiv holatda yaratiladi
    role="user"  # Standart rol - "user"
):
    """
    Yangi foydalanuvchi yaratish
    
    Args:
        username: Foydalanuvchi nomi (majburiy)
        password: Parol (majburiy)
        email: Email (ixtiyoriy)
        is_active: Aktivlik holati (default: True)
        role: Foydalanuvchi roli (default: "user")
    """
    pass
```

4. **Mantiqiy guruhlash**
```python
def search_products(
    # Asosiy filtrlar
    query=None,
    category=None,
    
    # Narx filtrlari
    min_price=0,
    max_price=None,
    
    # Qo'shimcha filtrlar
    in_stock=True,
    brand=None,
    
    # Sortlash va paginatsiya
    sort_by="relevance",
    sort_order="desc",
    limit=20,
    page=1
):
    pass
```

---
<br>
<br>
<br>
<br>
<br>

## 🔑 Keyword Arguments (func(x=1, y=2))

### Keyword Arguments nima?

Keyword arguments - bu funktsiyani chaqirishda parametr nomlarini aniq ko'rsatib, qiymat berish usuli. Bunda argumentlarning tartibi muhim emas, chunki ular nom orqali bog'lanadi.

**Real hayotdan misol:**
- **Dorixona**: Dori sotib olayotganda "bosh og'rig'i uchun" deb aytasiz - bu keyword argument
- **Kalkulyator**: "5 ga 3 ni qo'sh" emas, balki "son1=5, son2=3, amal=qo'shish" deb aytish

```python
# Oddiy misol
def talaba_ma'lumot(ism, yosh, kurs):
    print(f"Ism: {ism}, Yosh: {yosh}, Kurs: {kurs}")

# Keyword arguments bilan chaqirish
talaba_ma'lumot(ism="Ali", yosh=20, kurs=2)
talaba_ma'lumot(kurs=2, ism="Ali", yosh=20)  # Tartib muhim emas!
```

### Keyword Argumentsning Afzalliklari

1. **Kod o'qilishi yaxshilanadi**
2. **Argumentlar tartibi muhim emas**
3. **Qaysi parametrga qiymat berilayotgani aniq ko'rinadi**
4. **Default qiymatlarni osongina o'zgartirish mumkin**

```python
def buyurtma(mahsulot, miqdor, manzil, telefon, tolov_turi="naqd"):
    print(f"Mahsulot: {mahsulot}")
    print(f"Miqdor: {miqdor}")
    print(f"Manzil: {manzil}")
    print(f"Telefon: {telefon}")
    print(f"To'lov: {tolov_turi}")

# Keyword arguments bilan - tushunarli
buyurtma(
    mahsulot="Noutbuk",
    miqdor=2,
    manzil="Toshkent",
    telefon="+998901234567",
    tolov_turi="karta"
)

# Pozitsion argumentlar bilan - tushunish qiyinroq
buyurtma("Noutbuk", 2, "Toshkent", "+998901234567", "karta")
```

### Keyword Arguments vs Positional Arguments

```python
def hisobla(a, b, c):
    return a + b - c

# 1. Faqat positional
print(hisobla(10, 5, 3))        # 12

# 2. Faqat keyword
print(hisobla(a=10, b=5, c=3))  # 12
print(hisobla(c=3, b=5, a=10))  # 12 (tartib muhim emas)

# 3. Aralash (positional birinchi kelishi kerak)
print(hisobla(10, b=5, c=3))    # 12
print(hisobla(10, 5, c=3))      # 12

# NOTO'G'RI - keyword keyin positional
# hisobla(a=10, 5, 3)  # SyntaxError
```

### Keyword Arguments bilan Amaliy Misollar

**1-misol: Aviachipta bron qilish tizimi**

```python
def aviachipta_bron(
    ism,
    familiya,
    qayerdan,
    qayerga,
    sana,
    klass="ekonom",
    chipta_soni=1,
    bagaj=True,
    ovqat=True,
    sugurta=False,
    qaytarish_mumkin=False,
    telefon=None,
    email=None
):
    """
    Aviachipta bron qilish funktsiyasi
    """
    
    print("\n" + "✈️"*10)
    print("AVIACHTA BRON QILISH")
    print("✈️"*10)
    
    # Shaxsiy ma'lumotlar
    print(f"Yo'lovchi: {ism} {familiya}")
    print(f"Telefon: {telefon if telefon else 'Ko\'rsatilmagan'}")
    print(f"Email: {email if email else 'Ko\'rsatilmagan'}")
    
    # Parvoz ma'lumotlari
    print(f"\nPARVOZ MA'LUMOTLARI:")
    print(f"Yo'nalish: {qayerdan} -> {qayerga}")
    print(f"Sana: {sana}")
    print(f"Klass: {klass}")
    print(f"Chiptalar soni: {chipta_soni}")
    
    # Qo'shimcha xizmatlar
    print(f"\nQO'SHIMCHA XIZMATLAR:")
    print(f"Bagaj: {'Ha' if bagaj else 'Yo\'q'}")
    print(f"Ovqat: {'Ha' if ovqat else 'Yo\'q'}")
    print(f"Sug'urta: {'Ha' if sugurta else 'Yo\'q'}")
    print(f"Chiptani qaytarish: {'Ha' if qaytarish_mumkin else 'Yo\'q'}")
    
    # Narx hisoblash
    bazaviy_narx = 100  # USD
    klass_koeff = {"ekonom": 1, "business": 2.5, "first": 4}
    narx = bazaviy_narx * klass_koeff.get(klass, 1) * chipta_soni
    
    if bagaj:
        narx += 20 * chipta_soni
    if ovqat:
        narx += 15 * chipta_soni
    if sugurta:
        narx += 10 * chipta_soni
    if qaytarish_mumkin:
        narx *= 1.2
    
    print(f"\nUMUMIY NARX: ${narx:.2f}")
    
    return {
        "yo'lovchi": f"{ism} {familiya}",
        "yo'nalish": f"{qayerdan}->{qayerga}",
        "sana": sana,
        "narx": narx,
        "chiptalar": chipta_soni
    }

# Turli xil bronlar (keyword arguments bilan)
print("1-BRON - Minimal ma'lumotlar")
bron1 = aviachipta_bron(
    ism="Ali",
    familiya="Valiyev",
    qayerdan="Toshkent",
    qayerga="Moskva",
    sana="2024-06-15",
    telefon="+998901234567"
)

print("\n2-BRON - Business klass, sug'urta bilan")
bron2 = aviachipta_bron(
    ism="Zarina",
    familiya="Azizova",
    qayerdan="Samarqand",
    qayerga="Dubai",
    sana="2024-07-20",
    klass="business",
    chipta_soni=2,
    sugurta=True,
    email="zarina@email.com",
    telefon="+998935678901"
)

print("\n3-BRON - First klass, hamma xizmatlar bilan")
bron3 = aviachipta_bron(
    familiya="Karimov",
    ism="Bobur",  # Tartib muhim emas
    qayerdan="Toshkent",
    qayerga="New York",
    sana="2024-08-10",
    klass="first",
    chipta_soni=1,
    bagaj=True,
    ovqat=True,
    sugurta=True,
    qaytarish_mumkin=True,
    telefon="+998901112233"
)

print("\n4-BRON - Oilaviy sayohat")
bron4 = aviachipta_bron(
    ism="Jasur",
    familiya="Tursunov",
    qayerdan="Buxoro",
    qayerga="Istanbul",
    sana="2024-09-05",
    chipta_soni=4,
    klass="ekonom",
    bagaj=True,
    ovqat=False,
    telefon="+998945556677"
)
```

**2-misol: Onlayn ta'lim platformasi**

```python
def kurs_yozilish(
    talaba_ismi,
    talaba_familiyasi,
    kurs_nomi,
    yosh=18,
    daraja="boshlang'ich",
    til="o'zbek",
    tolov_turi="naqd",
    chegirma_kodi=None,
    sertifikat=True,
    mentor_yordami=False,
    amaliyot=True,
    loyiha_soni=1,
    davomiylik="3 oy",
    dars_vaqti=None,
    haftalik_darslar=3
):
    """
    Onlayn kursga yozilish (keyword arguments bilan)
    """
    
    print("\n" + "📚"*10)
    print("ONLAYN KURSGA YOZILISH")
    print("📚"*10)
    
    # Talaba ma'lumotlari
    print(f"Talaba: {talaba_ismi} {talaba_familiyasi}")
    print(f"Yosh: {yosh}")
    
    # Kurs ma'lumotlari
    print(f"\nKURS MA'LUMOTLARI:")
    print(f"Kurs: {kurs_nomi}")
    print(f"Daraja: {daraja}")
    print(f"Til: {til}")
    print(f"Davomiylik: {davomiylik}")
    print(f"Haftalik darslar: {haftalik_darslar} marta")
    
    if dars_vaqti:
        print(f"Dars vaqti: {dars_vaqti}")
    
    # Qo'shimcha xizmatlar
    print(f"\nQO'SHIMCHA XIZMATLAR:")
    print(f"Mentor yordami: {'Ha' if mentor_yordami else 'Yo\'q'}")
    print(f"Amaliy mashg'ulotlar: {'Ha' if amaliyot else 'Yo\'q'}")
    print(f"Loyihalar soni: {loyiha_soni}")
    print(f"Sertifikat: {'Ha' if sertifikat else 'Yo\'q'}")
    
    # Narx hisoblash
    narxlar = {
        "Python": 500000,
        "Web dasturlash": 600000,
        "Data Science": 800000,
        "Mobile Dev": 700000
    }
    
    bazaviy_narx = narxlar.get(kurs_nomi, 500000)
    
    # Darajaga qarab narx
    daraja_koeff = {
        "boshlang'ich": 1,
        "o'rta": 1.2,
        "yuqori": 1.5
    }
    narx = bazaviy_narx * daraja_koeff.get(daraja, 1)
    
    # Qo'shimcha xizmatlar narxi
    if mentor_yordami:
        narx += 200000
    if sertifikat:
        narx += 50000
    
    # Chegirma
    if chegirma_kodi == "STUDENT2024":
        chegirma = narx * 0.15
        print(f"\nChegirma kodi: {chegirma_kodi} (-15%)")
    elif chegirma_kodi == "EARLYBIRD":
        chegirma = narx * 0.10
        print(f"\nChegirma kodi: {chegirma_kodi} (-10%)")
    else:
        chegirma = 0
    
    umumiy = narx - chegirma
    
    print(f"\nHISOB:")
    print(f"Bazaviy narx: {bazaviy_narx:,.0f} so'm")
    print(f"Daraja koeffitsienti: {daraja_koeff.get(daraja, 1)}")
    print(f"Qo'shimcha xizmatlar: +{narx - bazaviy_narx:,.0f} so'm")
    if chegirma > 0:
        print(f"Chegirma: -{chegirma:,.0f} so'm")
    print(f"JAMI: {umumiy:,.0f} so'm")
    print(f"To'lov turi: {tolov_turi}")
    
    return {
        "talaba": f"{talaba_ismi} {talaba_familiyasi}",
        "kurs": kurs_nomi,
        "daraja": daraja,
        "narx": umumiy,
        "tolov_turi": tolov_turi
    }

# Turli xil yozilishlar (keyword arguments bilan)
print("1-YOZILISH - Boshlang'ich daraja")
yozilish1 = kurs_yozilish(
    talaba_ismi="Ali",
    talaba_familiyasi="Valiyev",
    kurs_nomi="Python"
)

print("\n2-YOZILISH - O'rta daraja, mentor bilan")
yozilish2 = kurs_yozilish(
    kurs_nomi="Web dasturlash",
    talaba_ismi="Zarina",
    talaba_familiyasi="Azizova",
    daraja="o'rta",
    mentor_yordami=True,
    yosh=22,
    tolov_turi="karta"
)

print("\n3-YOZILISH - Yuqori daraja, chegirma bilan")
yozilish3 = kurs_yozilish(
    talaba_ismi="Bobur",
    talaba_familiyasi="Karimov",
    kurs_nomi="Data Science",
    daraja="yuqori",
    chegirma_kodu="STUDENT2024",
    loyiha_soni=3,
    dars_vaqti="19:00-21:00",
    haftalik_darslar=4,
    telefon="+998901234567"  # Funktsiyada yo'q, lekin xatolik bo'lmaydi
)

print("\n4-YOZILISH - Intensiv kurs")
yozilish4 = kurs_yozilish(
    talaba_ismi="Madina",
    talaba_familiyasi="Rahimova",
    kurs_nomi="Mobile Dev",
    daraja="o'rta",
    mentor_yordami=True,
    sertifikat=True,
    amaliyot=True,
    loyiha_soni=5,
    davomiylik="6 oy",
    haftalik_darslar=5
)

print("\n5-YOZILISH - Minimal ma'lumotlar (faqat majburiy)")
yozilish5 = kurs_yozilish(
    talaba_ismi="Jasur",
    talaba_familiyasi="Tursunov",
    kurs_nomi="Python"
)
```

### Keyword Arguments bilan Murakkab Misollar

**3-misol: Konfiguratsiya tizimi**

```python
def server_sozlash(
    host="localhost",
    port=8080,
    debug=False,
    database=None,
    cache_size=128,
    max_connections=100,
    timeout=30,
    ssl=True,
    ssl_cert=None,
    ssl_key=None,
    logging=True,
    log_file="app.log",
    log_level="INFO",
    cors_origins=None,
    middleware=None
):
    """
    Serverni sozlash (barcha parametrlar keyword argument sifatida)
    """
    
    print("\n" + "🖥️"*10)
    print("SERVER SOZLAMALARI")
    print("🖥️"*10)
    
    # Asosiy sozlamalar
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Debug: {debug}")
    print(f"Max connections: {max_connections}")
    print(f"Timeout: {timeout} sekund")
    
    # Database sozlamalari
    if database:
        print(f"\nDATABASE SOZLAMALARI:")
        for key, value in database.items():
            print(f"  {key}: {value}")
    
    # SSL sozlamalari
    print(f"\nSSL SOZLAMALARI:")
    print(f"SSL enabled: {ssl}")
    if ssl:
        print(f"SSL Cert: {ssl_cert if ssl_cert else 'Default'}")
        print(f"SSL Key: {ssl_key if ssl_key else 'Default'}")
    
    # Caching sozlamalari
    print(f"\nCACHING SOZLAMALARI:")
    print(f"Cache size: {cache_size} MB")
    
    # Logging sozlamalari
    if logging:
        print(f"\nLOGGING SOZLAMALARI:")
        print(f"Log file: {log_file}")
        print(f"Log level: {log_level}")
    
    # CORS sozlamalari
    if cors_origins:
        print(f"\nCORS ORIGINS:")
        for origin in cors_origins:
            print(f"  • {origin}")
    
    # Middleware
    if middleware:
        print(f"\nMIDDLEWARE:")
        for m in middleware:
            print(f"  • {m}")
    
    return {
        "host": host,
        "port": port,
        "config": "loaded",
        "status": "ready"
    }

# Turli xil server konfiguratsiyalari
print("1-KONFIG - Development server")
dev_server = server_sozlash(
    host="127.0.0.1",
    port=8000,
    debug=True,
    database={
        "type": "sqlite",
        "name": "dev.db"
    },
    logging=True,
    log_level="DEBUG"
)

print("\n2-KONFIG - Production server")
prod_server = server_sozlash(
    host="0.0.0.0",
    port=443,
    debug=False,
    database={
        "type": "postgresql",
        "host": "db.example.com",
        "port": 5432,
        "name": "prod_db",
        "user": "admin",
        "password": "secret"
    },
    cache_size=1024,
    max_connections=500,
    timeout=60,
    ssl=True,
    ssl_cert="/etc/ssl/cert.pem",
    ssl_key="/etc/ssl/key.pem",
    cors_origins=["https://example.com", "https://api.example.com"],
    middleware=["auth", "cors", "compression"]
)

print("\n3-KONFIG - Testing server")
test_server = server_sozlash(
    port=8888,
    debug=True,
    database={"type": "memory"},
    logging=False,
    max_connections=10
)

print("\n4-KONFIG - Minimal server")
minimal_server = server_sozlash()  # Barcha default qiymatlar
```

**4-misol: Hisobot generatsiyasi**

```python
def hisobot_yaratish(
    ma'lumotlar,
    format="pdf",
    title="Hisobot",
    author=None,
    date=None,
    pagesize="A4",
    orientation="portrait",
    font_size=12,
    font_family="Arial",
    color=True,
    header=True,
    footer=True,
    page_numbers=True,
    watermark=None,
    encryption=False,
    password=None,
    compress=True,
    metadata=None
):
    """
    Hisobot yaratish (keyword arguments bilan)
    """
    
    print("\n" + "📊"*10)
    print("HISOBOT YARATISH")
    print("📊"*10)
    
    # Asosiy ma'lumotlar
    print(f"Sarlavha: {title}")
    print(f"Format: {format}")
    print(f"Muallif: {author if author else 'Noma\'lum'}")
    print(f"Sana: {date if date else 'Bugun'}")
    
    # Sahifa sozlamalari
    print(f"\nSAHIFA SOZLAMALARI:")
    print(f"O'lcham: {pagesize}")
    print(f"Orientatsiya: {orientation}")
    print(f"Shrift: {font_family}, {font_size}pt")
    
    # Formatlash
    print(f"\nFORMATLASH:")
    print(f"Rangli: {'Ha' if color else 'Yo\'q'}")
    print(f"Sarlavha: {'Ha' if header else 'Yo\'q'}")
    print(f"Footer: {'Ha' if footer else 'Yo\'q'}")
    print(f"Sahifa raqamlari: {'Ha' if page_numbers else 'Yo\'q'}")
    
    if watermark:
        print(f"Watermark: {watermark}")
    
    # Xavfsizlik
    print(f"\nXAVFSIZLIK:")
    print(f"Shifrlash: {'Ha' if encryption else 'Yo\'q'}")
    if encryption:
        print(f"Password: {'*' * len(password) if password else 'Yo\'q'}")
    print(f"Kompressiya: {'Ha' if compress else 'Yo\'q'}")
    
    # Metadata
    if metadata:
        print(f"\nMETADATA:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
    
    # Ma'lumotlar haqida
    print(f"\nMA'LUMOTLAR:")
    if isinstance(ma'lumotlar, list):
        print(f"Qatorlar soni: {len(ma'lumotlar)}")
        if len(ma'lumotlar) > 0:
            print(f"Ustunlar: {len(ma'lumotlar[0]) if isinstance(ma'lumotlar[0], (list, dict)) else 1}")
    elif isinstance(ma'lumotlar, dict):
        print(f"Kalitlar soni: {len(ma'lumotlar)}")
    
    print(f"\n✅ Hisobot yaratilmoqda...")
    print(f"✅ Hisobot tayyor: hisobot.{format}")
    
    return {
        "file": f"hisobot.{format}",
        "size": "2.5 MB",
        "pages": 15,
        "format": format,
        "title": title
    }

# Turli xil hisobotlar
print("1-HISOBOT - Oddiy PDF hisobot")
hisobot1 = hisobot_yaratish(
    ma'lumotlar=[1, 2, 3, 4, 5],
    title="Oylik savdo hisoboti",
    author="Marketing Dept",
    date="2024-01-15",
    color=True
)

print("\n2-HISOBOT - Excel hisobot, shifrlangan")
hisobot2 = hisobot_yaratish(
    ma'lumotlar=[
        {"mahsulot": "Noutbuk", "sotuv": 50},
        {"mahsulot": "Telefon", "sotuv": 120}
    ],
    format="xlsx",
    title="Mahsulot sotuvi",
    author="Sales Dept",
    encryption=True,
    password="secret123",
    watermark="CONFIDENTIAL",
    metadata={
        "company": "Tech Corp",
        "department": "Sales",
        "quarter": "Q1 2024"
    }
)

print("\n3-HISOBOT - Minimalistik hisobot")
hisobot3 = hisobot_yaratish(
    ma'lumotlar="Bu matnli hisobot",
    format="txt",
    title="Eslatma",
    font_size=14,
    header=False,
    footer=False,
    page_numbers=False,
    color=False
)

print("\n4-HISOBOT - Kengaytirilgan PDF")
hisobot4 = hisobot_yaratish(
    ma'lumotlar=[["Ism", "Yosh", "Shahar"], ["Ali", 25, "Toshkent"]],
    format="pdf",
    title="Xodimlar ro'yxati",
    author="HR Dept",
    pagesize="A3",
    orientation="landscape",
    font_family="Times New Roman",
    font_size=14,
    watermark="DRAFT"
)
```

### Keyword Arguments va Dictionary

**5-misol: Dictionary dan keyword arguments yaratish**

```python
def mahsulot_qoshish(nom, narx, miqdor, kategoriya, tavsif=None):
    """Mahsulot qo'shish"""
    print(f"Mahsulot qo'shildi: {nom}, {narx} so'm, {miqdor} dona")
    return {"nom": nom, "narx": narx, "miqdor": miqdor}

# Dictionary dan argumentlarni yoyish (** operatori)
mahsulot_ma'lumotlari = {
    "nom": "Noutbuk",
    "narx": 5000000,
    "miqdor": 10,
    "kategoriya": "Elektronika",
    "tavsif": "Yangi model"
}

# ** orqali dictionary ni keyword arguments ga aylantirish
mahsulot_qoshish(**mahsulot_ma'lumotlari)

# Qisman yoyish
asosiy_ma'lumotlar = {"nom": "Telefon", "narx": 3000000}
qoshimcha = {"miqdor": 15, "kategoriya": "Elektronika"}
mahsulot_qoshish(**asosiy_ma'lumotlar, **qoshimcha)
```

**6-misol: Dinamik so'rov yaratish**

```python
def so'rov_yaratish(
    method="GET",
    url=None,
    headers=None,
    params=None,
    data=None,
    json=None,
    auth=None,
    timeout=30,
    allow_redirects=True,
    verify=True,
    cert=None
):
    """
    HTTP so'rov yaratish
    """
    print("\n" + "🌐"*10)
    print("HTTP SO'ROV")
    print("🌐"*10)
    
    print(f"Method: {method}")
    print(f"URL: {url}")
    print(f"Timeout: {timeout}s")
    
    if headers:
        print(f"\nHEADERS:")
        for key, value in headers.items():
            print(f"  {key}: {value}")
    
    if params:
        print(f"\nPARAMS:")
        for key, value in params.items():
            print(f"  {key}={value}")
    
    if data:
        print(f"\nDATA: {data}")
    
    if json:
        print(f"\nJSON: {json}")
    
    if auth:
        print(f"\nAUTH: {auth}")
    
    return f"{method} so'rov tayyor"

# Turli xil so'rovlar
so'rov1 = so'rov_yaratish(
    method="GET",
    url="https://api.example.com/users",
    params={"page": 1, "limit": 10},
    headers={"Authorization": "Bearer token123"}
)

so'rov2 = so'rov_yaratish(
    method="POST",
    url="https://api.example.com/users",
    json={"name": "Ali", "email": "ali@email.com"},
    timeout=60
)

# Dinamik konfiguratsiya
def create_request_from_config(config):
    """Konfiguratsiya dictionary asosida so'rov yaratish"""
    return so'rov_yaratish(**config)

config1 = {
    "method": "DELETE",
    "url": "https://api.example.com/users/1",
    "headers": {"Authorization": "Bearer token123"},
    "timeout": 10
}

so'rov3 = create_request_from_config(config1)
```

### Keyword Arguments bilan Validatsiya

**7-misol: Forma validatsiyasi**

```python
def forma_validatsiya(
    ism=None,
    email=None,
    yosh=None,
    telefon=None,
    manzil=None,
    parol=None,
    parol_tasdiq=None,
    **qoshimcha  # Qo'shimcha keyword argumentlar
):
    """
    Forma ma'lumotlarini tekshirish
    """
    xatolar = []
    
    print("\n" + "✅"*10)
    print("FORMA VALIDATSIYASI")
    print("✅"*10)
    
    # Ism tekshirish
    if ism:
        if len(ism) < 2:
            xatolar.append("Ism juda qisqa")
        elif not ism.isalpha():
            xatolar.append("Ism faqat harflardan iborat bo'lishi kerak")
        else:
            print(f"✓ Ism: {ism}")
    
    # Email tekshirish
    if email:
        if "@" not in email or "." not in email:
            xatolar.append("Email noto'g'ri formatda")
        else:
            print(f"✓ Email: {email}")
    
    # Yosh tekshirish
    if yosh:
        try:
            yosh = int(yosh)
            if yosh < 0 or yosh > 150:
                xatolar.append("Yosh noto'g'ri")
            else:
                print(f"✓ Yosh: {yosh}")
        except:
            xatolar.append("Yosh son bo'lishi kerak")
    
    # Telefon tekshirish
    if telefon:
        telefon = str(telefon).replace(" ", "").replace("-", "")
        if not telefon.startswith("+998") or len(telefon) != 13:
            xatolar.append("Telefon +998 bilan boshlanib, 13 ta belgidan iborat bo'lishi kerak")
        else:
            print(f"✓ Telefon: {telefon}")
    
    # Parol tekshirish
    if parol and parol_tasdiq:
        if len(parol) < 6:
            xatolar.append("Parol kamida 6 belgidan iborat bo'lishi kerak")
        elif parol != parol_tasdiq:
            xatolar.append("Parollar mos kelmadi")
        else:
            print("✓ Parol: To'g'ri")
    
    # Qo'shimcha maydonlar
    if qoshimcha:
        print(f"\nQo'shimcha maydonlar:")
        for key, value in qoshimcha.items():
            print(f"  {key}: {value}")
    
    # Natija
    if xatolar:
        print("\n❌ XATOLAR:")
        for xato in xatolar:
            print(f"  • {xato}")
        return False
    else:
        print("\n✅ Forma to'g'ri to'ldirilgan")
        return True

# Turli xil formalar
forma1 = forma_validatsiya(
    ism="Ali",
    email="ali@email.com",
    yosh=25,
    telefon="+998901234567",
    parol="secret123",
    parol_tasdiq="secret123"
)

forma2 = forma_validatsiya(
    ism="A",
    email="not-email",
    yosh="yosh",
    telefon="12345",
    parol="123",
    parol_tasdiq="456"
)

forma3 = forma_validatsiya(
    ism="Zarina",
    email="zarina@email.com",
    telefon="+998935678901",
    qoshimcha_maydon="Qiymat",
    izoh="Test",
    qayerdan_bildi="Internet"
)
```

### Keyword Arguments bilan Best Practices

1. **O'qilish uchun foydalaning**
```python
# YAXSHI - tushunarli
create_user(
    username="alisher",
    email="ali@example.com",
    is_active=True,
    role="admin"
)

# YOMON - tushunish qiyin
create_user("alisher", "ali@example.com", True, "admin")
```

2. **Majburiy parametrlarni positional, ixtiyoriylarni keyword qiling**
```python
def create_post(
    title,  # majburiy positional
    content,  # majburiy positional
    author=None,  # ixtiyoriy keyword
    published=False,  # ixtiyoriy keyword
    tags=None  # ixtiyoriy keyword
):
    pass
```

3. **Consistent naming - nomlar bir xil bo'lsin**
```python
# YAXSHI
def update_user(user_id, name=None, email=None):
    pass

update_user(1, name="Ali", email="ali@email.com")

# YOMON
update_user(1, n="Ali", e="ali@email.com")
```

4. **** operatori bilan dictionary dan yoyish**
```python
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

server_start(**config)  # host="localhost", port=8080, debug=True
```

5. **Qo'shimcha keyword argumentlar uchun **kwargs**
```python
def flexible_function(required, **kwargs):
    """Qo'shimcha argumentlarni qabul qiladi"""
    print(f"Required: {required}")
    for key, value in kwargs.items():
        print(f"Optional - {key}: {value}")
```

### Keyword Arguments vs Positional Arguments - Qachon qaysi birini ishlatish?

| **Holat** | **Positional** | **Keyword** |
|-----------|---------------|-------------|
| 1-2 ta parametr | ✅ | ✅ |
| 3+ ta parametr | ❌ | ✅ |
| Majburiy parametrlar | ✅ | ✅ |
| Ixtiyoriy parametrlar | ❌ | ✅ |
| Funktsiya chaqiruv tezligi muhim | ✅ | ❌ |
| Kod o'qilishi muhim | ❌ | ✅ |
| API dizayni | ❌ | ✅ |
| Default qiymatlar | ❌ | ✅ |
---

<br>
<br>
<br>
<br>
<br>
## 📏 Variable-Length Arguments (*args, **kwargs)

### Variable-Length Arguments nima?

Variable-length arguments - bu funktsiyaga istalgan sondagi argumentlarni uzatish imkonini beruvchi mexanizm. Bu sizga oldindan aniq sonini bilmagan argumentlar bilan ishlash imkoniyatini yaratadi.

**Real hayotdan misol:**
- **Pitsa buyurtmasi**: Mijoz istalgancha qo'shimcha masalliq tanlashi mumkin
- **Avtobus chiptasi**: Yo'lovchilar soni har safar o'zgaradi
- **Kalkulyator**: Istalgancha sonlarni qo'shish mumkin

```python
# *args - positional argumentlar uchun
def summa(*args):
    """Istalgancha sonlarni qabul qilib, yig'indisini hisoblaydi"""
    return sum(args)

print(summa(1, 2, 3))           # 6
print(summa(10, 20, 30, 40, 50)) # 150
print(summa(5))                  # 5
print(summa())                   # 0

# **kwargs - keyword argumentlar uchun
def talaba_ma'lumot(**kwargs):
    """Istalgancha keyword argumentlarni qabul qiladi"""
    for kalit, qiymat in kwargs.items():
        print(f"{kalit}: {qiymat}")

talaba_ma'lumot(ism="Ali", yosh=20, kurs=2, shahar="Toshkent")
```

### *args - Positional Variable-Length Arguments

`*args` - bu istalgan sondagi positional argumentlarni qabul qilish uchun ishlatiladigan belgi. `args` nomi an'anaviy, lekin istalgan nom bo'lishi mumkin (`*numbers`, `*items` va h.k.)

```python
def misol_args(*args):
    print(f"Argumentlar soni: {len(args)}")
    print(f"Argumentlar: {args}")
    print(f"Tur: {type(args)}")  # <class 'tuple'>
    
    for i, arg in enumerate(args, 1):
        print(f"Argument {i}: {arg}")

misol_args(1, 2, 3, "salom", True)
```

**Natija:**
```
Argumentlar soni: 5
Argumentlar: (1, 2, 3, 'salom', True)
Tur: <class 'tuple'>
Argument 1: 1
Argument 2: 2
Argument 3: 3
Argument 4: salom
Argument 5: True
```

### *args bilan amaliy misollar

**1-misol: Matematik operatsiyalar**

```python
def kopaytirish(*sonlar):
    """Berilgan barcha sonlarni ko'paytiradi"""
    if not sonlar:
        return 0
    
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

def ortacha(*sonlar):
    """Berilgan sonlarning o'rtacha qiymatini hisoblaydi"""
    if not sonlar:
        return 0
    return sum(sonlar) / len(sonlar)

def max_min(*sonlar):
    """Eng katta va eng kichik qiymatlarni qaytaradi"""
    if not sonlar:
        return None, None
    return max(sonlar), min(sonlar)

def darajalar(*sonlar, daraja=2):
    """Berilgan sonlarni berilgan darajaga ko'taradi"""
    return [son ** daraja for son in sonlar]

# Test qilish
print("Ko'paytirish:")
print(f"2 * 3 * 4 = {kopaytirish(2, 3, 4)}")
print(f"5 * 10 = {kopaytirish(5, 10)}")
print(f"Hech narsa = {kopaytirish()}")

print("\nO'rtacha:")
print(f"10, 20, 30 = {ortacha(10, 20, 30)}")
print(f"5, 15, 25, 35 = {ortacha(5, 15, 25, 35)}")

print("\nMax va Min:")
max_son, min_son = max_min(45, 12, 78, 34, 56)
print(f"Sonlar: 45, 12, 78, 34, 56")
print(f"Max: {max_son}, Min: {min_son}")

print("\nDarajalar:")
print(f"2, 3, 4 ning kvadrati: {darajalar(2, 3, 4)}")
print(f"2, 3, 4 ning kubi: {darajalar(2, 3, 4, daraja=3)}")
```

**2-misol: Matn bilan ishlash**

```python
def matn_birlashtir(ajratuvchi=" ", *matnlar):
    """Berilgan matnlarni ajratuvchi bilan birlashtiradi"""
    if not matnlar:
        return ""
    return ajratuvchi.join(matnlar)

def eng_uzun_matn(*matnlar):
    """Eng uzun matnni topadi"""
    if not matnlar:
        return None
    
    eng_uzun = max(matnlar, key=len)
    return eng_uzun, len(eng_uzun)

def sozlar_soni(*matnlar):
    """Har bir matndagi so'zlar sonini hisoblaydi"""
    natija = {}
    for i, matn in enumerate(matnlar, 1):
        sozlar = len(matn.split())
        natija[f"Matn {i}"] = sozlar
    return natija

def formatla(*matnlar, kenglik=20, tomon="chap"):
    """Matnlarni berilgan kenglikda formatlaydi"""
    for matn in matnlar:
        if tomon == "chap":
            print(f"| {matn:<{kenglik}} |")
        elif tomon == "ong":
            print(f"| {matn:>{kenglik}} |")
        elif tomon == "markaz":
            print(f"| {matn:^{kenglik}} |")

# Test qilish
print("1. Matnlarni birlashtirish:")
print(matn_birlashtir("-", "Python", "dasturlash", "tili"))
print(matn_birlashtir(" | ", "Ali", "Vali", "Hasan", "Husan"))

print("\n2. Eng uzun matn:")
matn, uzunlik = eng_uzun_matn("Python", "JavaScript", "C++", "Java", "Kotlin")
print(f"Eng uzun: '{matn}' ({uzunlik} harf)")

print("\n3. So'zlar soni:")
natija = sozlar_soni(
    "Salom dunyo",
    "Python dasturlash tili",
    "Men dasturchiman"
)
for matn, sozlar in natija.items():
    print(f"{matn}: {sozlar} so'z")

print("\n4. Formatlash:")
formatla("Python", "Java", "JavaScript", "C++", kenglik=15, tomon="chap")
print()
formatla("Python", "Java", "JavaScript", "C++", kenglik=15, tomon="markaz")
```

**3-misol: Cheksiz parametrli hisoblagich**

```python
def kalkulyator(amal, *sonlar):
    """
    Istalgancha sonlar ustida amal bajaradi
    amal: '+', '*', 'max', 'min', 'avg'
    """
    if not sonlar:
        return 0
    
    if amal == '+':
        return sum(sonlar)
    elif amal == '*':
        result = 1
        for s in sonlar:
            result *= s
        return result
    elif amal == 'max':
        return max(sonlar)
    elif amal == 'min':
        return min(sonlar)
    elif amal == 'avg':
        return sum(sonlar) / len(sonlar)
    else:
        return "Noto'g'ri amal"

# Test qilish
print("=== KALKULYATOR ===")
print(f"Yig'indi: {kalkulyator('+', 1, 2, 3, 4, 5)}")
print(f"Ko'paytma: {kalkulyator('*', 2, 3, 4)}")
print(f"Maximum: {kalkulyator('max', 45, 23, 67, 12, 89)}")
print(f"Minimum: {kalkulyator('min', 45, 23, 67, 12, 89)}")
print(f"O'rtacha: {kalkulyator('avg', 10, 20, 30, 40, 50)}")
```

### **kwargs - Keyword Variable-Length Arguments

`**kwargs` - bu istalgan sondagi keyword argumentlarni qabul qilish uchun ishlatiladigan belgi. Bu argumentlar dictionary (lug'at) shaklida qabul qilinadi.

```python
def misol_kwargs(**kwargs):
    print(f"Argumentlar soni: {len(kwargs)}")
    print(f"Argumentlar: {kwargs}")
    print(f"Tur: {type(kwargs)}")  # <class 'dict'>
    
    for kalit, qiymat in kwargs.items():
        print(f"{kalit} = {qiymat}")

misol_kwargs(ism="Ali", yosh=25, shahar="Toshkent", kasb="Dasturchi")
```

**Natija:**
```
Argumentlar soni: 4
Argumentlar: {'ism': 'Ali', 'yosh': 25, 'shahar': 'Toshkent', 'kasb': 'Dasturchi'}
Tur: <class 'dict'>
ism = Ali
yosh = 25
shahar = Toshkent
kasb = Dasturchi
```

### **kwargs bilan amaliy misollar

**4-misol: Foydalanuvchi profili yaratish**

```python
def user_profile(username, **kwargs):
    """
    Foydalanuvchi profili yaratish
    username - majburiy parametr
    kwargs - ixtiyoriy qo'shimcha ma'lumotlar
    """
    profile = {
        "username": username,
        "is_active": True,
        "created_at": "2024-01-15"
    }
    
    # Qo'shimcha ma'lumotlarni qo'shish
    for key, value in kwargs.items():
        profile[key] = value
    
    return profile

def show_profile(**user_info):
    """Foydalanuvchi ma'lumotlarini chiroyli chiqarish"""
    print("\n" + "="*40)
    print("FOYDALANUVCHI PROFILI")
    print("="*40)
    
    for key, value in user_info.items():
        key = key.replace("_", " ").title()
        print(f"{key}: {value}")

# Profil yaratish
user1 = user_profile("alisher", email="ali@email.com", age=25, city="Tashkent")
user2 = user_profile("madina", email="madina@email.com", age=23, city="Samarkand", job="Developer")
user3 = user_profile("bobur", email="bobur@email.com", age=30, city="Bukhara", job="Teacher", phone="+998901234567")

# Profillarni ko'rsatish
show_profile(**user1)
show_profile(**user2)
show_profile(**user3)
```

**5-misol: Web so'rov konfiguratsiyasi**

```python
def http_request(url, method="GET", **kwargs):
    """
    HTTP so'rov yaratish
    url - majburiy
    method - default GET
    kwargs - headers, params, data, auth va h.k.
    """
    request = {
        "url": url,
        "method": method,
        "headers": kwargs.get("headers", {}),
        "params": kwargs.get("params", {}),
        "timeout": kwargs.get("timeout", 30)
    }
    
    if "data" in kwargs:
        request["data"] = kwargs["data"]
    
    if "json" in kwargs:
        request["json"] = kwargs["json"]
    
    if "auth" in kwargs:
        request["auth"] = kwargs["auth"]
    
    if "cookies" in kwargs:
        request["cookies"] = kwargs["cookies"]
    
    return request

def send_request(**request_config):
    """So'rovni jo'natish (simulyatsiya)"""
    print("\n" + "🌐"*10)
    print("SO'ROV JO'NATILMOQDA")
    print("🌐"*10)
    
    for key, value in request_config.items():
        if isinstance(value, dict):
            print(f"{key.upper()}:")
            for k, v in value.items():
                print(f"  {k}: {v}")
        else:
            print(f"{key.upper()}: {value}")
    
    print("\n✅ So'rov muvaffaqiyatli jo'natildi")
    return {"status": 200, "message": "OK"}

# Turli xil so'rovlar
req1 = http_request(
    "https://api.example.com/users",
    headers={"Authorization": "Bearer token123"},
    params={"page": 1, "limit": 10}
)

req2 = http_request(
    "https://api.example.com/users",
    method="POST",
    headers={"Content-Type": "application/json"},
    json={"name": "Ali", "email": "ali@email.com"},
    timeout=60
)

req3 = http_request(
    "https://api.example.com/login",
    method="POST",
    data={"username": "admin", "password": "secret"},
    auth=("admin", "secret"),
    cookies={"session": "abc123"}
)

# So'rovlarni jo'natish
send_request(**req1)
send_request(**req2)
send_request(**req3)
```

### *args va **kwargs birgalikda

```python
def universal_function(majburiy, *args, **kwargs):
    """
    Majburiy parametr + istalgancha positional + istalgancha keyword argumentlar
    """
    print(f"Majburiy: {majburiy}")
    
    if args:
        print(f"*args ({len(args)} ta):")
        for i, arg in enumerate(args, 1):
            print(f"  {i}: {arg}")
    
    if kwargs:
        print(f"**kwargs ({len(kwargs)} ta):")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

# Hamma turdagi argumentlar bilan chaqirish
universal_function(
    "Majburiy qiymat",
    1, 2, 3, 4, 5,  # *args
    ism="Ali",       # **kwargs
    yosh=25,
    shahar="Toshkent"
)
```

**6-misol: Konfiguratsiya tizimi**

```python
def app_configure(app_name, version="1.0.0", *modules, **settings):
    """
    Ilova konfiguratsiyasi
    app_name: majburiy
    version: default qiymat
    *modules: o'rnatiladigan modullar
    **settings: sozlamalar
    """
    config = {
        "app_name": app_name,
        "version": version,
        "modules": list(modules) if modules else [],
        "settings": settings if settings else {}
    }
    
    return config

def show_config(config):
    """Konfiguratsiyani chiroyli chiqarish"""
    print("\n" + "⚙️"*10)
    print("KONFIGURATSIYA")
    print("⚙️"*10)
    
    print(f"Ilova: {config['app_name']} v{config['version']}")
    
    if config['modules']:
        print(f"\nModullar ({len(config['modules'])}):")
        for module in config['modules']:
            print(f"  • {module}")
    
    if config['settings']:
        print(f"\nSozlamalar:")
        for key, value in config['settings'].items():
            print(f"  {key}: {value}")

# Turli xil konfiguratsiyalar
config1 = app_configure("WebApp")
config2 = app_configure("MobileApp", "2.1.0", "auth", "database", "cache")
config3 = app_configure(
    "GameApp",
    "1.5.0",
    "graphics",
    "physics",
    "sound",
    "network",
    debug=True,
    resolution="1920x1080",
    fullscreen=True,
    volume=80
)

show_config(config1)
show_config(config2)
show_config(config3)
```

### Argumentlarni yoyish (Unpacking)

**7-misol: Ro'yxat va lug'atlarni yoyish**

```python
def yoyish_misoli(a, b, c, d=None, e=None):
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

# Ro'yxatni yoyish (* operatori)
sonlar = [1, 2, 3]
yoyish_misoli(*sonlar)  # a=1, b=2, c=3

# Lug'atni yoyish (** operatori)
ma'lumotlar = {"a": 10, "b": 20, "c": 30}
yoyish_misoli(**ma'lumotlar)  # a=10, b=20, c=30

# Aralash yoyish
sonlar = [1, 2]
kwargs = {"d": 4, "e": 5}
yoyish_misoli(*sonlar, 3, **kwargs)  # a=1, b=2, c=3, d=4, e=5
```

**8-misol: Dinamik funktsiya chaqiruvi**

```python
def matematika(amal, *sonlar):
    """Matematik amallar"""
    if amal == "qo'shish":
        return sum(sonlar)
    elif amal == "ko'paytirish":
        result = 1
        for s in sonlar:
            result *= s
        return result
    elif amal == "daraja":
        return [s ** 2 for s in sonlar]

def bajaruvchi(funktsiya_nomi, *args, **kwargs):
    """
    Funktsiyani dinamik chaqirish
    """
    # Funktsiyalar lug'ati
    funktsiyalar = {
        "matematika": matematika,
        "print": print,
        "sum": sum
    }
    
    if funktsiya_nomi in funktsiyalar:
        funktsiya = funktsiyalar[funktsiya_nomi]
        return funktsiya(*args, **kwargs)
    else:
        return f"Funktsiya '{funktsiya_nomi}' topilmadi"

# Dinamik chaqiruvlar
print(bajaruvchi("matematika", "qo'shish", 1, 2, 3, 4, 5))
print(bajaruvchi("matematika", "ko'paytirish", 2, 3, 4, 5))
print(bajaruvchi("matematika", "daraja", 2, 3, 4, 5))
print(bajaruvchi("print", "Salom", "Dunyo", sep="-"))
```

### *args va **kwargs bilan murakkab misollar

**9-misol: Dekorator yaratish**

```python
def logger(func):
    """Funktsiyani chaqirilishini log qiluvchi dekorator"""
    def wrapper(*args, **kwargs):
        print(f"\n📝 Funktsiya chaqirildi: {func.__name__}")
        
        if args:
            print(f"  Positional argumentlar: {args}")
        if kwargs:
            print(f"  Keyword argumentlar: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"  Natija: {result}")
        return result
    return wrapper

@logger
def hisobla(*sonlar, amal='+'):
    if amal == '+':
        return sum(sonlar)
    elif amal == '*':
        result = 1
        for s in sonlar:
            result *= s
        return result

@logger
def talaba_yarat(ism, familiya, **ma'lumotlar):
    talaba = {
        "ism": ism,
        "familiya": familiya,
        **ma'lumotlar
    }
    return talaba

# Dekoratorlangan funktsiyalarni chaqirish
hisobla(1, 2, 3, 4, 5)
hisobla(2, 3, 4, amal='*')
talaba_yarat("Ali", "Valiyev", yosh=20, kurs=2, fakultet="IT")
```

**10-misol: Event tizimi**

```python
class EventSystem:
    def __init__(self):
        self.handlers = {}
    
    def register(self, event_name, handler):
        """Event handler ro'yxatdan o'tkazish"""
        if event_name not in self.handlers:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)
    
    def trigger(self, event_name, *args, **kwargs):
        """Eventni ishga tushirish"""
        if event_name in self.handlers:
            print(f"\n📢 Event: {event_name}")
            results = []
            for handler in self.handlers[event_name]:
                result = handler(*args, **kwargs)
                results.append(result)
            return results
        return []

# Event handlerlar
def email_handler(*args, **kwargs):
    print(f"  Email jo'natildi: {kwargs.get('to', 'Noma\'lum')}")
    return "email sent"

def sms_handler(*args, **kwargs):
    print(f"  SMS jo'natildi: {kwargs.get('phone', 'Noma\'lum')}")
    return "sms sent"

def log_handler(*args, **kwargs):
    print(f"  Log: {args}, {kwargs}")
    return "logged"

# Event tizimini ishlatish
events = EventSystem()

# Handlerlarni ro'yxatdan o'tkazish
events.register("user_created", email_handler)
events.register("user_created", sms_handler)
events.register("user_created", log_handler)
events.register("order_placed", email_handler)
events.register("order_placed", log_handler)

# Eventlarni trigger qilish
events.trigger(
    "user_created",
    "Yangi foydalanuvchi",
    to="user@email.com",
    phone="+998901234567"
)

events.trigger(
    "order_placed",
    "Buyurtma #123",
    to="customer@email.com"
)
```

### *args va **kwargs bilan best practices

**1. Aniq nomlardan foydalaning**
```python
# YAXSHI
def calculate_average(*grades):
    return sum(grades) / len(grades)

def create_profile(**personal_info):
    pass

# QABUL QILINADI
def process_data(*args, **kwargs):
    pass

# YOMON (tushunarsiz)
def func(*a, **b):
    pass
```

**2. Majburiy parametrlarni aniq belgilang**
```python
# YAXSHI
def create_user(username, email, *roles, **profile):
    """username va email majburiy, qolganlari ixtiyoriy"""
    pass

# YOMON (hamma narsa *args va **kwargs da)
def create_user(*args, **kwargs):
    # Qaysi parametr majburiy? Tushunarsiz
    pass
```

**3. *args va **kwargs ni birgalikda ishlatishda tartib muhim**
```python
def correct_order(required, *args, **kwargs):
    """To'g'ri tartib: required -> *args -> **kwargs"""
    pass

# NOTO'G'RI
# def wrong_order(*args, required, **kwargs):  # SyntaxError
#     pass
```

**4. Dokumentatsiyani unutmang**
```python
def flexible_function(param1, param2, *args, **kwargs):
    """
    Moslashuvchan funktsiya
    
    Args:
        param1: Birinchi majburiy parametr
        param2: Ikkinchi majburiy parametr
        *args: Qo'shimcha positional argumentlar
            - odatda sonlar ro'yxati
        **kwargs: Qo'shimcha keyword argumentlar
            - debug: True/False (default: False)
            - mode: 'fast' yoki 'slow' (default: 'fast')
            - callback: funksiya (ixtiyoriy)
    """
    debug = kwargs.get('debug', False)
    mode = kwargs.get('mode', 'fast')
    # ...
```

### Amaliy mashqlar

**Mashq 1: Istalgancha sonlarning statistikasi**

```python
def statistika(*sonlar, **parametrlar):
    """
    Berilgan sonlarning statistikasini hisoblaydi
    parametrlar: 
        - aniq: float (default: 2)
        - sort: True/False (default: False)
    """
    if not sonlar:
        return {}
    
    aniq = parametrlar.get('aniq', 2)
    sort = parametrlar.get('sort', False)
    
    sonlar_list = list(sonlar)
    if sort:
        sonlar_list.sort()
    
    stats = {
        "sonlar": sonlar_list,
        "soni": len(sonlar_list),
        "yigindi": round(sum(sonlar_list), aniq),
        "ortacha": round(sum(sonlar_list) / len(sonlar_list), aniq),
        "maks": max(sonlar_list),
        "min": min(sonlar_list),
        "farq": round(max(sonlar_list) - min(sonlar_list), aniq)
    }
    
    return stats

# Test
print(statistika(10, 5, 8, 12, 3, 7))
print(statistika(3.14, 2.71, 1.41, 1.73, aniq=3, sort=True))
```

**Mashq 2: Moslashuvchan formatlagich**

```python
def format_text(text, *styles, **options):
    """
    Matnni formatlash
    styles: 'bold', 'italic', 'underline', 'upper', 'lower'
    options: width, align, fillchar
    """
    result = text
    
    # Stil qo'llash
    for style in styles:
        if style == 'upper':
            result = result.upper()
        elif style == 'lower':
            result = result.lower()
        elif style == 'capitalize':
            result = result.capitalize()
        elif style == 'title':
            result = result.title()
    
    # Formatlash
    width = options.get('width', 0)
    align = options.get('align', 'left')
    fillchar = options.get('fillchar', ' ')
    
    if width > len(result):
        if align == 'left':
            result = result.ljust(width, fillchar)
        elif align == 'right':
            result = result.rjust(width, fillchar)
        elif align == 'center':
            result = result.center(width, fillchar)
    
    # Qo'shimcha effektlar
    if 'bold' in styles:
        result = f"**{result}**"
    if 'italic' in styles:
        result = f"*{result}*"
    if 'underline' in styles:
        result = f"_{result}_"
    
    return result

# Test
print(format_text("python", 'bold', 'upper'))
print(format_text("hello world", 'title', 'italic', width=30, align='center', fillchar='='))
print(format_text("test", 'underline', 'capitalize', width=20, align='right'))
```

### Xulosa

1. ***args**:
   - Istalgancha positional argumentlarni qabul qiladi
   - Tuple shaklida saqlanadi
   - Nom sifatida `*args` an'anaviy, lekin `*numbers`, `*items` ham ishlatish mumkin

2. ***kwargs**:
   - Istalgancha keyword argumentlarni qabul qiladi
   - Dictionary shaklida saqlanadi
   - Nom sifatida `**kwargs` an'anaviy

3. **Yoyish (unpacking)**:
   - `*list` - ro'yxatni positional argumentlarga yoyadi
   - `**dict` - lug'atni keyword argumentlarga yoyadi

4. **Tartib muhim**:
   ```python
   def func(majburiy, *args, default="qiymat", **kwargs):
       pass
   ```

5. **Afzalliklari**:
   - Moslashuvchanlik
   - Dekoratorlar yaratish
   - API dizayni
   - Legacy kod bilan ishlash
---
<br>
<br>
<br>
<br>
<br>

