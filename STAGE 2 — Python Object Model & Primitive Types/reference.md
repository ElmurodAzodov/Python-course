
# **STAGE 2 — Python Object Model & Primitive Types**
---
# 🧠 **Everything Is an Object (Python’da hamma narsa — obyekt)**

## 🎯 Asosiy g‘oya

**Python’da mavjud bo‘lgan HAMMA NARSA — obyekt.**

Bu degani:

* sonlar
* matnlar
* funksiyalar
* klasslar
* list, dict, tuple
* hatto `None` va `True`

➡️ **barchasi obyekt** va ularning:

* **turi (type)**
* **identifikatori (id)**
* **atributlari**
* **metodlari**

mavjud.

---

## 1️⃣ Obyekt nima?

Python’da **obyekt** — bu:

> **xotirada joy egallagan, ma’lum bir turga ega bo‘lgan va o‘z xatti-harakatlari (methods) bo‘lgan qiymat**

Har bir obyekt 3 ta asosiy qismdan iborat:

| Qism         | Tavsif                |
| ------------ | --------------------- |
| **Value**    | Saqlanayotgan qiymat  |
| **Type**     | Obyektning turi       |
| **Identity** | Xotiradagi noyob joyi |

---

## 2️⃣ Oddiy misol: son ham obyekt

```python
x = 10
```

Bu yerda:

* `10` → **int obyekt**
* `x` → shu obyektga **reference**

Tekshirib ko‘ramiz:

```python
print(type(x))
print(id(x))
```

👉 Natija:

```
<class 'int'>
140723456789456
```

🔑 Demak:

* `10` — obyekt
* `int` — uning turi
* `id(x)` — xotiradagi joyi

---

## 3️⃣ String ham obyekt

```python
s = "Hello"
```

```python
print(type(s))
print(id(s))
```

String obyekt:

* o‘z metodlariga ega
* xotirada yashaydi

```python
print(s.upper())
print(s.lower())
```

➡️ `.upper()`, `.lower()` — **string obyekt metodlari**

---

## 4️⃣ Funksiya ham obyekt 😮

Bu Python’ning juda kuchli jihati.

```python
def greet():
    print("Salom")
```

```python
print(type(greet))
```

Natija:

```
<class 'function'>
```

Funksiya:

* o‘zgaruvchiga berilishi mumkin
* argument sifatida uzatiladi
* return qilinadi

```python
x = greet
x()
```

👉 `greet` — bu ham obyekt!

---

## 5️⃣ List, tuple, dict — obyektlar

```python
lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {"a": 1}
```

```python
print(type(lst))
print(type(tpl))
print(type(dct))
```

Natija:

```
<class 'list'>
<class 'tuple'>
<class 'dict'>
```

Ularning har biri:

* xotirada obyekt
* o‘z metodlariga ega

```python
lst.append(4)
print(lst)
```

---

## 6️⃣ Hatto `None`, `True`, `False` ham obyekt

```python
x = None
y = True
z = False
```

```python
print(type(x))
print(type(y))
```

Natija:

```
<class 'NoneType'>
<class 'bool'>
```

👉 `NoneType` — alohida obyekt turi.

---

## 7️⃣ Class ham obyekt

```python
class Person:
    pass
```

```python
print(type(Person))
```

Natija:

```
<class 'type'>
```

➡️ Klass — **type klassining obyektidir**

Bu juda muhim tushuncha:

> Python’da **klasslar ham obyekt**

---

## 8️⃣ Obyekt metodlari va atributlari

Har bir obyekt o‘ziga tegishli metodlarga ega.

```python
x = 5
print(dir(x))
```

Bu:

* `__add__`
* `__sub__`
* `__str__`

kabi **maxsus metodlar**ni ko‘rsatadi.

```python
print(x.__add__(3))  # 5 + 3
```

---

## 9️⃣ Operatorlar ham metod chaqiradi

```python
a = 5
b = 3

print(a + b)
```

Aslida bu:

```python
print(a.__add__(b))
```

🔑 Operatorlar → obyekt metodlari

---

## 🔟 Nima uchun “Everything is an Object” muhim?

Bu tushuncha sizga:

✅ Python qanday ishlashini chuqur tushunishga

✅ Mutability / Immutability farqini anglashga

✅ Argument passing (pass by object reference) ni tushunishga

✅ Bug va xotira muammolarini yechishga

✅ Advanced Python (OOP, decorators, metaclasses) o‘rganishga

asos bo‘ladi.

---

## 🧩 Kichik tajriba (mustaqil mashq)

```python
a = 10
b = a

print(id(a))
print(id(b))
```

❓ Savol:

* `a` va `b` bir xil obyektmi?

➡️ Keyingi mavzu: **Object Identity** shu savolga chuqur javob beradi 😉

---
# 🆔 **Object Identity (Obyekt identifikatsiyasi)**

## 🎯 Asosiy g‘oya

Python’da har bir obyekt 3 ta asosiy xususiyatga ega:

1️⃣ **Identity** — xotiradagi noyob manzil
2️⃣ **Type** — obyekt turi
3️⃣ **Value** — obyekt qiymati

👉 **Object identity** — bu obyektning **xotiradagi noyob joyi**.

---

## 1️⃣ `id()` funksiyasi

Python’da obyekt identifikatorini ko‘rish uchun `id()` ishlatiladi.

```python
x = 10
print(id(x))
```

* `id()` → obyektning **noyob identifikatori**
* Bir vaqtning o‘zida ikki obyektning `id` si bir xil bo‘lishi mumkin emas

---

## 2️⃣ Identity ≠ Value

Ikki obyektning **qiymati bir xil bo‘lishi mumkin**, lekin **identity boshqa** bo‘lishi mumkin.

```python
a = 1000
b = 1000

print(a == b)   # True (qiymati teng)
print(a is b)   # False (obyekt boshqa)
```

* `==` → value tekshiradi
* `is` → identity tekshiradi

---

## 3️⃣ `is` va `==` farqi (JUDA MUHIM)

| Operator | Tekshiradi         |
| -------- | ------------------ |
| `==`     | Qiymat tengmi      |
| `is`     | Xuddi shu obyektmi |

### Misol:

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # True
print(x is y)  # False
```

➡️ Qiymatlar bir xil, lekin obyektlar boshqa.

---

## 4️⃣ Reference tushunchasi

Python’da:

> O‘zgaruvchi obyektni saqlamaydi,
> **obyektga reference (ishora)** qiladi.

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

➡️ `a` va `b` **bir xil obyektga ishora qiladi**

```python
a.append(4)
print(b)  # [1, 2, 3, 4]
```

---

## 5️⃣ Identity va mutability bog‘liqligi

### Mutable obyekt:

```python
x = [1, 2]
print(id(x))

x.append(3)
print(id(x))  # id o‘zgarmaydi
```

➡️ Obyekt o‘zgardi, identity o‘zgarmadi

---

### Immutable obyekt:

```python
x = 10
print(id(x))

x = x + 1
print(id(x))  # id o‘zgardi
```

➡️ Yangi obyekt yaratildi

---

## 6️⃣ Integer caching (Python optimizatsiyasi)

Python kichik sonlarni **oldindan keshlab qo‘yadi**:

```python
a = 10
b = 10

print(a is b)  # True
```

Ammo:

```python
a = 1000
b = 1000

print(a is b)  # False
```

🔑 Bu:

* implementation detail
* `is` bilan sonlarni taqqoslash **xato amaliyot**

---

## 7️⃣ String interning

```python
a = "hello"
b = "hello"

print(a is b)  # True
```

Ammo:

```python
a = "".join(["he", "llo"])
b = "hello"

print(a == b)  # True
print(a is b)  # False
```

---

## 8️⃣ None bilan `is` ishlatiladi

`None` — yagona obyekt (singleton).

```python
x = None

if x is None:
    print("None")
```

❌ Noto‘g‘ri:

```python
if x == None:
    pass
```

---

## 9️⃣ Funksiya argumentlari va identity

```python
def add_item(lst):
    lst.append(100)

my_list = [1, 2, 3]
add_item(my_list)

print(my_list)
```

➡️ Bir xil obyektga reference uzatildi

---

## 🔟 Identity bilan bog‘liq keng tarqalgan xatolar

❌ `is` bilan string/son taqqoslash

❌ Mutable obyektni kutilmagan joyda o‘zgartirish

❌ Copy o‘rniga reference olish

### To‘g‘ri nusxa olish:

```python
import copy

a = [1, 2]
b = a.copy()        # shallow copy
c = copy.deepcopy(a)
```

---

## 📌 Xulosa

✔ Har bir obyekt — noyob identity’ga ega

✔ `id()` → xotira manzili

✔ `is` → identity tekshiradi

✔ `==` → qiymatni tekshiradi

✔ Mutable obyekt → identity o‘zgarmaydi

✔ Immutable obyekt → yangi obyekt yaratiladi

✔ `None` bilan `is` ishlatiladi

---
## **🔄 Object Mutability**

ni **chuqur nazariy + aniq va ko‘p misollar bilan** tushuntirib beraman.

Bu mavzu:

* **Object Identity**
* **Dynamic Typing**
* **Function arguments**
* **Bug’larning katta qismi**

bilan bevosita bog‘liq.

---

# 🔄 **Object Mutability (Obyektning o‘zgaruvchanligi)**

## 🎯 Asosiy g‘oya

**Mutability** — bu obyekt **yaratilgandan keyin o‘z ichki qiymatini o‘zgartira olishi yoki olmasligi**.

* **Mutable** → o‘zgartirish mumkin
* **Immutable** → o‘zgartirish mumkin emas

---

## 1️⃣ Mutable va Immutable obyektlar

### ❄️ Immutable (o‘zgarmas)

* `int`
* `float`
* `bool`
* `str`
* `tuple`
* `frozenset`

```python
x = 10
x = x + 1  # yangi obyekt
```

---

### 🔥 Mutable (o‘zgaruvchan)

* `list`
* `dict`
* `set`
* `bytearray`

```python
lst = [1, 2]
lst.append(3)  # o‘sha obyekt o‘zgardi
```

---

## 2️⃣ id() orqali mutability’ni tushunish

### Immutable misol:

```python
x = "hello"
print(id(x))

x = x + " world"
print(id(x))
```

➡️ `id` o‘zgardi → yangi obyekt

---

### Mutable misol:

```python
lst = [1, 2]
print(id(lst))

lst.append(3)
print(id(lst))
```

➡️ `id` o‘zgarmadi → o‘sha obyekt

---

## 3️⃣ Nima uchun bu muhim?

Mutability **kutilmagan xatolarga** olib kelishi mumkin.

### Misol:

```python
a = [1, 2, 3]
b = a

b.append(4)
print(a)
```

➡️ `a` ham o‘zgardi 😨

---

## 4️⃣ Function argument va mutability

```python
def add_item(lst):
    lst.append(100)

items = [1, 2, 3]
add_item(items)

print(items)
```

➡️ Sabab: `lst` va `items` bir xil obyekt

---

### Xavfsiz usul:

```python
def add_item(lst):
    lst = lst.copy()
    lst.append(100)
    return lst
```

---

## 5️⃣ Immutable obyektlar funksiyada

```python
def increment(x):
    x += 1
    return x

a = 10
b = increment(a)

print(a)  # 10
print(b)  # 11
```

➡️ `a` o‘zgarmadi

---

## 6️⃣ Mutable inside immutable?

```python
t = ([1, 2], [3, 4])
t[0].append(99)

print(t)
```

➡️ Tuple immutable, lekin ichidagi list mutable!

---

## 7️⃣ Default argument trap (JUDAYAM MUHIM)

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
```

❌ Natija:

```
[1]
[1, 2]
```

### To‘g‘ri usul:

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 8️⃣ Mutability va copy

### Shallow copy:

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)
print(a)
```

➡️ Ichki list shared

---

### Deep copy:

```python
import copy

c = copy.deepcopy(a)
c[0].append(100)

print(a)
print(c)
```

---

## 9️⃣ Qachon mutable, qachon immutable ishlatish?

| Holat         | Tavsiya   |
| ------------- | --------- |
| Xavfsizlik    | Immutable |
| Performance   | Mutable   |
| Key sifatida  | Immutable |
| Global data   | Immutable |
| Configuration | Immutable |

---
# 🔢 **Integers (int) in Python**

## 🎯 Asosiy g‘oya

Python’da **int** — bu:

> **cheksiz aniqlikdagi (arbitrary precision) butun son obyektlari**

C/C++ dagidek 32-bit yoki 64-bit bilan cheklanmagan.

---

## 1️⃣ int yaratish (Integer Creation)

```python
a = 10
b = -5
c = 0
```

```python
print(type(a))
```

Natija:

```
<class 'int'>
```

---

## 2️⃣ Katta sonlar bilan ishlash (Arbitrary Precision)

```python
big = 10**100
print(big)
```

➡️ Overflow yo‘q
➡️ Faqat xotira bilan cheklanadi

---

## 3️⃣ int — immutable obyekt

```python
x = 10
print(id(x))

x += 1
print(id(x))
```

➡️ Yangi obyekt yaratildi

---

## 4️⃣ int va object identity

```python
a = 5
b = 5

print(a is b)   # True (kichik sonlar cache qilinadi)
```

```python
a = 1000
b = 1000

print(a is b)   # False (odatda)
```

⚠️ `is` bilan son taqqoslamang — `==` ishlating

---

## 5️⃣ Arithmetic operators

| Operator | Ma’nosi                   |
| -------- | ------------------------- |
| `+`      | qo‘shish                  |
| `-`      | ayirish                   |
| `*`      | ko‘paytirish              |
| `/`      | bo‘lish (float qaytaradi) |
| `//`     | butun bo‘lish             |
| `%`      | qoldiq                    |
| `**`     | daraja                    |

```python
print(7 / 2)   # 3.5
print(7 // 2)  # 3
print(7 % 2)   # 1
print(2 ** 3)  # 8
```

---

## 6️⃣ int va float o‘zaro ishlashi

```python
x = 5 + 2.0
print(x, type(x))
```

➡️ Natija:

```
7.0 <class 'float'>
```

➡️ Python avtomatik type promotion qiladi

---

## 7️⃣ int konversiya (type casting)

```python
int("10")      # 10
int(3.9)       # 3
int(True)      # 1
int(False)     # 0
```

❌ Xato:

```python
int("10.5")    # ValueError
```

---

## 8️⃣ Binary, Octal, Hexadecimal integers

### Binary (2-lik)

```python
b = 0b1010
print(b)  # 10
```

### Octal (8-lik)

```python
o = 0o12
print(o)  # 10
```

### Hexadecimal (16-lik)

```python
h = 0xA
print(h)  # 10
```

---

## 9️⃣ Bitwise operators (asosiy)

| Operator | Ma’nosi     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | left shift  |    |
| `>>`     | right shift |    |

```python
a = 5  # 101
b = 3  # 011

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
```

---

## 🔟 int metodlari

```python
x = 10

print(x.bit_length())
print(bin(x))
print(hex(x))
print(oct(x))
```

---

## 1️⃣1️⃣ int va bool munosabati

```python
print(isinstance(True, int))  # True
```

➡️ `bool` → `int` subclass

```python
True == 1    # True
False == 0  # True
```

---

## 1️⃣2️⃣ int bilan keng tarqalgan xatolar

❌ `is` bilan taqqoslash

❌ `/` dan int kutish

❌ string → int noto‘g‘ri konversiya

---

## 📌 Xulosa

✔ `int` — immutable obyekt

✔ Cheksiz aniqlik

✔ Arithmetic + bitwise operatorlar

✔ int ↔ float avtomatik konversiya

✔ `bool` — int subclass

✔ Kichik int’lar cache qilinadi

---
# 🔟 **Floating-Point Numbers (float) in Python**

## 🎯 Asosiy g‘oya

Python’dagi `float`:

> **IEEE 754 double-precision (64-bit)** suzuvchi nuqtali sonlar asosida ishlaydi.
---
Shuning uchun:

* hamma o‘nlik sonlar **aniq ifodalanmaydi**
* **kichik xatoliklar (precision error)** paydo bo‘ladi
---
## *IEE 754 haqida qisqacha*

**IEEE 754** — bu **suzuvchi nuqtali sonlarni (floating-point numbers)** kompyuterda qanday saqlash va hisoblashni belgilovchi **xalqaro standart**.
Python’da `float` tipi **IEEE 754 double precision (64-bit)** standartiga asoslanadi.

### Python’da bu nimani anglatadi?

Python’da:

```python
x = 0.1
```

`x` aniq `0.1` emas, balki **unga eng yaqin bo‘lgan ikkilik (binary) qiymat** sifatida saqlanadi.

### IEEE 754 (64-bit) tuzilishi

`float` 3 qismdan iborat:

1. **Sign (1 bit)** – musbat yoki manfiy
2. **Exponent (11 bit)** – daraja
3. **Mantissa / Fraction (52 bit)** – aniqlik

### Nega ba’zan hisoblar “xato” ko‘rinadi?

Masalan:

```python
print(0.1 + 0.2)
```

Natija:

```text
0.30000000000000004
```

Sababi:
`0.1` va `0.2` **ikkilik sanoq sistemasida aniq ifodalanmaydi**, IEEE 754 esa taxminiy qiymat saqlaydi.

### Buni qanday hal qilish mumkin?

1. **Yumaloqlash (round)**

```python
round(0.1 + 0.2, 2)
```

2. **decimal moduli (moliyaviy hisoblar uchun)**

```python
from decimal import Decimal

Decimal("0.1") + Decimal("0.2")
```

3. **math.isclose** (taqqoslashda)

```python
import math
math.isclose(0.1 + 0.2, 0.3)
```
---
---

## 1️⃣ float yaratish

```python
a = 3.14
b = -0.001
c = 2.0
```

```python
print(type(a))
```

Natija:

```
<class 'float'>
```

---

## 2️⃣ float — immutable obyekt

```python
x = 1.5
print(id(x))

x += 0.5
print(id(x))
```

➡️ Yangi obyekt yaratildi

---

## 3️⃣ IEEE 754 muammosi (eng muhim qism)

### Mashhur misol:

```python
print(0.1 + 0.2)
```

Natija:

```
0.30000000000000004
```

❗ Sabab:

* 0.1 va 0.2 binary tizimda **aniq ifodalanmaydi**
* Natija taxminiy bo‘ladi

---

## 4️⃣ float ichki ko‘rinishi

```python
import decimal
decimal.Decimal(0.1)
```

➡️ float juda uzun binary kasr

---

## 5️⃣ float bilan taqqoslash (XATO va TO‘G‘RI)

### ❌ XATO:

```python
x = 0.1 + 0.2
print(x == 0.3)  # False
```

---

### ✅ TO‘G‘RI (epsilon bilan):

```python
abs(x - 0.3) < 1e-9
```

---

### ✅ `math.isclose()` bilan:

```python
import math

math.isclose(x, 0.3)
```

---

## 6️⃣ float arithmetic operatorlari

```python
a = 7.0
b = 2.0

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 7️⃣ float konversiya (type casting)

```python
float(10)        # 10.0
float("3.14")    # 3.14
float(True)      # 1.0
```

❌ Xato:

```python
float("abc")     # ValueError
```

---

## 8️⃣ `round()` muammosi

```python
round(2.675, 2)
```

Natija:

```
2.67
```

❗ Sabab:

* ichki binary ifoda aniqlik muammosi

---

## 9️⃣ decimal moduli (aniq hisob-kitob uchun)

Moliyaviy hisoblar uchun **float ishlatmang** ❌

```python
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)  # 0.3
```

➡️ Har doim string orqali yarating!

---

## 🔟 float va int o‘zaro ishlashi

```python
x = 5 + 2.5
print(x, type(x))
```

➡️ Natija:

```
7.5 <class 'float'>
```

---

## 1️⃣1️⃣ float metodlari

```python
x = 3.5

print(x.is_integer())
print(x.as_integer_ratio())
```

---

## 1️⃣2️⃣ float bilan ishlash bo‘yicha tavsiyalar

| Holat           | Tavsiya           |
| --------------- | ----------------- |
| Moliyaviy hisob | `decimal.Decimal` |
| Taqqoslash      | `math.isclose()`  |
| Yuvarlash       | ehtiyot bo‘ling   |
| Aniqlik kerak   | float ishlatmang  |

---

## 📌 Xulosa

✔ `float` — immutable obyekt

✔ IEEE 754 sababli aniqlik muammolari bor

✔ `0.1 + 0.2 ≠ 0.3`

✔ `==` bilan taqqoslamang

✔ `math.isclose()` ishlating

✔ Moliyaviy hisobda `Decimal` ishlating

---
# 🔷 **Complex Numbers in Python**

## 🎯 Asosiy g‘oya

Python’da **complex** — bu:

> **a + bj** ko‘rinishidagi sonlar
> bu yerda:

* `a` → haqiqiy qism (real)
* `b` → mavhum qism (imaginary)
* `j` → √-1 (Python’da `i` emas!)

---

## 1️⃣ Complex son yaratish

### 1-usul: to‘g‘ridan-to‘g‘ri yozish

```python
z1 = 3 + 4j
z2 = -1.5 + 2j
```

```python
print(type(z1))
```

Natija:

```
<class 'complex'>
```

---

### 2-usul: `complex()` funksiyasi

```python
z = complex(3, 4)
print(z)
```

➡️ Natija:

```
(3+4j)
```

❗ String bilan:

```python
z = complex("2+5j")
```

---

## 2️⃣ Real va Imaginary qismlar

```python
z = 3 + 4j

print(z.real)  # 3.0
print(z.imag)  # 4.0
```

---

## 3️⃣ Complex — immutable obyekt

```python
z = 1 + 2j
print(id(z))

z = z + 1
print(id(z))
```

➡️ Yangi obyekt yaratildi

---

## 4️⃣ Complex arithmetic

```python
a = 2 + 3j
b = 1 - 1j

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## 5️⃣ Complex va int/float

```python
z = 2 + 3j

print(z + 2)
print(z * 2.5)
```

➡️ Natija:

```
(4+3j)
(5+7.5j)
```

---

## 6️⃣ Taqqoslash cheklovlari

❌ Bunday qilish mumkin emas:

```python
(1 + 2j) > (2 + 3j)  # TypeError
```

❌ `max()`, `min()` ishlamaydi

✔ Faqat `==` va `!=` ishlaydi:

```python
print(1+2j == 1+2j)
```

---

## 7️⃣ Absolute value (modul)

```python
z = 3 + 4j
print(abs(z))  # 5.0
```

➡️ √(a² + b²)

---

## 8️⃣ Complex metodlari

```python
z = 1 + 2j

print(z.conjugate())
```

➡️ Natija:

```
(1-2j)
```

---

## 9️⃣ math vs cmath

### ❌ `math` complex bilan ishlamaydi:

```python
import math
math.sqrt(-1)  # ValueError
```

---

### ✅ `cmath` — complex uchun:

```python
import cmath

z = -1
print(cmath.sqrt(z))
```

➡️ Natija:

```
1j
```

---

## 🔟 Polar form (burchak va modul)

```python
import cmath

z = 1 + 1j

r, theta = cmath.polar(z)
print(r, theta)
```

---

## 1️⃣1️⃣ Complex sonlar qayerda ishlatiladi?

✔ Elektr zanjirlar

✔ Signal processing

✔ Fourier transform

✔ Fizika

✔ Engineering

✔ Data science (kamroq)

---

## 1️⃣2️⃣ Qachon complex ishlatmaslik kerak?

❌ Moliyaviy hisoblar

❌ Oddiy arifmetik

❌ Taqqoslash talab qilinadigan joylar

---

# ✅ **Booleans in Python**

## 🎯 Asosiy g‘oya

**Boolean (`bool`)** — bu **mantiqiy tip**, faqat ikkita qiymatga ega:

* `True`
* `False`

Python’da **bool** aslida **int subclass** hisoblanadi:

```python
print(isinstance(True, int))  # True
print(True + 1)               # 2
```

---

## 1️⃣ Boolean yaratish

```python
x = True
y = False

print(type(x), type(y))
```

Natija:

```
<class 'bool'> <class 'bool'>
```

---

## 2️⃣ Boolean qiymatlar qanday hosil bo‘ladi

### a) To‘g‘ridan-to‘g‘ri

```python
a = True
b = False
```

### b) Taqqoslash operatorlari orqali

```python
print(5 > 3)   # True
print(2 == 3)  # False
print(4 <= 4)  # True
```

---

### c) Mantiqiy operatorlar

| Operator | Ma’nosi               |
| -------- | --------------------- |
| `and`    | va                    |
| `or`     | yoki                  |
| `not`    | inkor                 |
| `xor`    | eksklyuziv yoki (`^`) |

```python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
print(True ^ False)    # True
```

---

## 3️⃣ Truthy va Falsy qiymatlar

Python’da **har bir obyekt bool qiymatga ega**:

* **Falsy** (False ga teng):
  `0, 0.0, "", [], (), {}, set(), None, False`
* **Truthy** (True ga teng):
  Boshqa barcha qiymatlar

```python
if []:
    print("Truthy")
else:
    print("Falsy")  # Falsy
```

---

## 4️⃣ Boolean va int

```python
print(True + True)   # 2
print(False + 5)     # 5
print(int(True))     # 1
print(int(False))    # 0
```

---

## 5️⃣ Boolean conversion

```python
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True
print(bool([]))       # False
print(bool([1,2]))    # True
```

---

## 6️⃣ Booleans va Control Flow

```python
x = 10

if x > 5:
    print("x katta 5 dan")  # True
else:
    print("x kichik yoki teng 5")
```

```python
y = []

if not y:
    print("y bo‘sh")  # True
```

---

## 7️⃣ Boolean expressions chaining

```python
x = 10
y = 20
z = 30

print(x < y < z)  # True
```

---

## 8️⃣ Boolean bilan common pitfalls

❌ `is` bilan `True` yoki `False` taqqoslash

```python
x = (5 > 3)
print(x is True)   # True (lekin ba’zi hollarda False bo‘lishi mumkin)
print(x == True)   # True (ishonchli)
```

❌ Falsy obyektlarni noto‘g‘ri tekshirish:

```python
lst = []
if lst == True:    # Xato
    pass
```

To‘g‘ri:

```python
if lst:            # False
    pass
```

---

## 9️⃣ Boolean metodlari

Python’da `bool` oddiy obyekt, metodlari yo‘q (faqat int metodlari mavjud).
Ko‘proq **conversion** va **operatorlar** ishlatiladi:

```python
print(bool("Hello"))    # True
print(bool(0))          # False
```

---

# 🚫 **NoneType in Python**

## 🎯 Asosiy g‘oya

**`None`** — bu:

> “hech qanday qiymat yo‘q” degan yagona **singleton obyekt**.

* `NoneType` — uning turi
* Faqat **bitta obyekt** mavjud Python’da
* Mutable yoki immutable emas, faqat **indikator** sifatida ishlatiladi

---

## 1️⃣ `None` yaratish

```python
x = None
print(x)
print(type(x))
```

Natija:

```
None
<class 'NoneType'>
```

---

## 2️⃣ Identity

```python
a = None
b = None

print(a is b)  # True
```

✔ Sababi: Python’da **None yagona obyekt** (singleton)

---

## 3️⃣ Dynamic Typing bilan None

```python
x = 10
x = None
```

* `x` hozir `NoneType` obyektga ishora qiladi
* Dynamic typing sababli tur o‘zgarishi mumkin

---

## 4️⃣ None bilan boolean konversiya

```python
print(bool(None))  # False
```

* `None` → falsy qiymat
* `if` yoki `while` statement’larda ishlatiladi

```python
x = None
if not x:
    print("x None yoki Falsy")  # True
```

---

## 5️⃣ None va function return

Agar funksiya **return qilmasa**, u avtomatik **`None`** qaytaradi:

```python
def func():
    pass

result = func()
print(result)       # None
print(type(result)) # <class 'NoneType'>
```

---

### Amaliy misol: indikator sifatida

```python
def find_item(lst, target):
    for item in lst:
        if item == target:
            return item
    return None

result = find_item([1, 2, 3], 4)
if result is None:
    print("Topilmadi")
```

✅ `None` → yo‘qlikni bildiradi

---

## 6️⃣ None bilan taqqoslash

### To‘g‘ri usul:

```python
x = None
if x is None:
    print("X None")
```

### Noto‘g‘ri:

```python
if x == None:  # ishlaydi, lekin is preferred
    pass
```

---

## 7️⃣ NoneType bilan common pitfalls

❌ `None` bilan arithmetic:

```python
x = None
y = x + 1  # TypeError
```

❌ None bilan boolean operatorlarni aralashtirish:

```python
x = None
if x == False:  # Xato konseptual
    pass
```

---

## 8️⃣ NoneType summary

| Xususiyat               | Tavsif     |
| ----------------------- | ---------- |
| Tip                     | `NoneType` |
| Qiymat                  | `None`     |
| Singleton               | Ha         |
| Mutable                 | Yo‘q       |
| Boolean qiymat          | False      |
| Function default return | None       |
| Tekshirish              | `is None`  |

---
# 📏 **Numeric Precision in Python**

## 🎯 Asosiy g‘oya

Python’dagi **numeric precision**:

1. **int** — cheksiz aniqlik (arbitrary precision)
2. **float** — 64-bit IEEE 754 suzuvchi nuqtali son
3. **complex** — float asosida real va imaginary qismlar

❗ Shu sababli:

* int bilan arifmetik → aniq
* float bilan arifmetik → kichik xatoliklar (round-off errors)

---

## 1️⃣ int precision

```python
x = 10**100
print(x)
```

* Python’da **int cheksiz uzunlikda**
* Overflow yo‘q, faqat xotira bilan cheklangan

---

## 2️⃣ float precision (asosi)

```python
a = 0.1
b = 0.2
print(a + b)
```

Natija:

```
0.30000000000000004
```

❗ Sabab: float **binary tizimda** ifodalangan → 0.1 ≈ 0.10000000000000000555…

---

## 3️⃣ float vs int

```python
x = 10
y = 0.1

print(x + y)  # 10.1
```

* int + float → float
* float precision muammosi mavjud

---

## 4️⃣ Round-off errors

```python
print(round(2.675, 2))  # 2.67
```

* Sabab: 2.675 → binary ko‘rinishda ≈ 2.6749999999999998
* **Decimal** modul yordamida to‘g‘rilash mumkin

```python
from decimal import Decimal, ROUND_HALF_UP
d = Decimal("2.675").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(d)  # 2.68
```

---

## 5️⃣ Float comparison (to‘g‘ri usul)

❌ Xato:

```python
0.1 + 0.2 == 0.3  # False
```

✅ To‘g‘ri:

```python
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

* `math.isclose(a, b, rel_tol=1e-9)`
* `rel_tol` → relative tolerance

---

## 6️⃣ Floating-point representation

```python
import sys
print(sys.float_info)
```

* Max value, min value, epsilon (ya’ni minimal farq)
* Float epsilon → `2.220446049250313e-16`

---

## 7️⃣ Complex numbers va precision

```python
z = 0.1 + 0.2j
print(abs(z - (0.1 + 0.2j)))  # 0.0
```

* Complex → real va imaginary qism float → shuningdek, **epsilon xatolik** mavjud

---

## 8️⃣ Decimal va Fraction

### Decimal:

```python
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)  # 0.3
```

### Fraction:

```python
from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(2, 3)
print(x + y)  # 1
```

* **Decimal** → moliyaviy hisob
* **Fraction** → aniq nisbat

---

## 9️⃣ Summary — Numeric Precision in Python

| Type     | Precision          | Notes                              |
| -------- | ------------------ | ---------------------------------- |
| int      | Arbitrary          | Cheksiz uzunlik                    |
| float    | ~16 decimal digits | Binary, IEEE 754, round-off errors |
| complex  | float-based        | Real + Imaginary                   |
| Decimal  | User-defined       | Moliyaviy hisob                    |
| Fraction | Exact rational     | Ratios                             |

---
# 🔒 **Immutability Concepts in Python**

## 🎯 Asosiy g‘oya

**Immutable (o‘zgarmas) obyekt** — bu:

> Yaratilgandan keyin **ichki qiymatini o‘zgartirib bo‘lmaydigan obyekt**.

Python’da immutable obyektlar:

* `int`
* `float`
* `complex`
* `bool`
* `str`
* `tuple`
* `frozenset`
* `bytes`

Mutable obyektlar esa:

* `list`
* `dict`
* `set`
* `bytearray`

---

## 1️⃣ Immutable vs Mutable

| Obyekt turi         | Mutable / Immutable | Xulosa                                               |
| ------------------- | ------------------- | ---------------------------------------------------- |
| int, float, complex | Immutable           | Yangi qiymat → yangi obyekt                          |
| bool                | Immutable           | Yangi qiymat → yangi obyekt                          |
| str                 | Immutable           | .replace(), slicing → yangi obyekt                   |
| tuple               | Immutable           | Ichidagi element mutable bo‘lsa, u o‘zgarishi mumkin |
| list, dict, set     | Mutable             | append(), pop() → shu obyekt o‘zgardi                |

---

## 2️⃣ Immutable obyekt bilan ishlash misollari

```python
x = 10
print(id(x))

x += 5
print(id(x))  # Yangi obyekt
```

```python
s = "Hello"
s2 = s.replace("H", "J")
print(s, s2)  # Hello, Jello
```

---

## 3️⃣ Mutable obyekt bilan ishlash misollari

```python
lst = [1, 2, 3]
print(id(lst))

lst.append(4)
print(id(lst))  # Shu obyekt, id o‘zgarmadi
```

---

## 4️⃣ Tuple ichida mutable obyekt

```python
t = ([1, 2], [3, 4])
t[0].append(99)
print(t)
```

* Tuple immutable, lekin ichidagi list mutable → o‘zgardi
* Immutable container, mutable content

---

## 5️⃣ Function argument va immutability

### Mutable:

```python
def add_item(lst):
    lst.append(100)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 100]
```

### Immutable:

```python
def increment(x):
    x += 1
    return x

a = 10
b = increment(a)
print(a, b)  # 10 11
```

---

## 6️⃣ Immutable object’larning afzalliklari

✔ Xavfsiz (shared references bilan kutilmagan o‘zgarish yo‘q)

✔ Hashable → dictionary key va set element bo‘lishi mumkin (`str`, `tuple`, `frozenset`)

✔ Predictable behavior (thread-safe)

---

## 7️⃣ Mutable object’larning afzalliklari

✔ Flexible

✔ Performance → o‘zgartirish oson (copy qilmasdan)

✔ Dynamic data structures uchun zarur (`list`, `dict`)

---

## 8️⃣ Copy vs Immutable assignment

### Mutable:

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
```

### Immutable:

```python
x = 10
y = x
y += 5
print(x, y)  # 10 15
```

---

## 9️⃣ Immutability va hashing

```python
s = "Hello"
d = {s: "World"}  # OK

lst = [1,2,3]
# d = {lst: "value"}  # TypeError: unhashable type
```

* Mutable obyektlar hashable emas → dict key bo‘la olmaydi

---