# **STAGE 7 — Functions & Scope**
<br>
<br>
## 📝 Function Definitions (`def name():`) — Python funksiyalarini yaratish

Python’da **function (funksiya)** — bu **ma'lum vazifani bajaradigan qayta ishlatiladigan kod bloki**.
Funksiya yordamida kod **tartibli, qisqa va tushunarli** bo‘ladi.

---

# 🎯 1. Funksiya nima?

Oddiy qilib aytganda:

> **Function — biror ishni bajarish uchun yozilgan kodlar to‘plami.**

Masalan:

* sonlarni qo‘shish
* salomlashish
* ma’lumotni tekshirish
* hisoblashlar qilish

Funksiya yozib qo‘yilsa, uni **istalgan joyda chaqirib ishlatish mumkin**.

---

# 🧠 2. Funksiya yaratish sintaksisi

Python’da funksiya **`def`** kalit so‘zi bilan yaratiladi.

```python
def function_name():
    kodlar
```

### Strukturasi

| Qism            | Vazifasi                         |
| --------------- | -------------------------------- |
| `def`           | funksiya boshlanishini bildiradi |
| `function_name` | funksiya nomi                    |
| `()`            | parametrlar joyi                 |
| `:`             | funksiya tanasi boshlanishi      |
| `indentation`   | funksiya ichidagi kod            |

---

# ✨ 3. Eng oddiy funksiya

### Misol

```python
def say_hello():
    print("Salom!")
```

Bu funksiya **faqat salom chiqaradi**.

⚠️ Lekin hozircha u ishlamaydi.
Funksiya **faqat yaratiladi**, bajarilmaydi.

---

# 🚀 4. Funksiya qanday ishlaydi?

Jarayon:

```
1️⃣ Funksiya aniqlanadi (define)
2️⃣ Python uni xotirada saqlaydi
3️⃣ Chaqarilganda ishlaydi
```

Misol:

```python
def say_hello():
    print("Salom!")

say_hello()
```

Natija

```
Salom!
```

---

# 📌 5. Bir nechta qatorli funksiya

Funksiya ichida **ko‘p qatorli kodlar** yozish mumkin.

```python
def introduce():
    print("Mening ismim Ali")
    print("Men Python o'rganayapman")
    print("Bu funksiya misoli")
```

Chaqarish:

```python
introduce()
```

Natija

```
Mening ismim Ali
Men Python o'rganayapman
Bu funksiya misoli
```

---

# 📦 6. Funksiya nega kerak?

Agar funksiya bo‘lmasa:

```python
print("Salom!")
print("Salom!")
print("Salom!")
print("Salom!")
```

Funksiya bilan:

```python
def greet():
    print("Salom!")

greet()
greet()
greet()
greet()
```

### Afzalliklari

✅ kodni takrorlamaydi
✅ kodni qisqartiradi
✅ o‘qish oson
✅ katta dasturlarni boshqarish oson

---

# 🧩 7. Funksiya nomlash qoidalari

Python’da funksiya nomi:

### ✔ To‘g‘ri

```python
def calculate_sum():
def print_user():
def check_password():
```

### ❌ Noto‘g‘ri

```python
def 1function():      # raqam bilan boshlanmaydi
def my-function():    # - ishlatilmaydi
def class():          # reserved keyword
```

---

# 📏 8. Python naming convention (PEP8)

Funksiya nomlari **snake_case** bo‘ladi.

✔ to‘g‘ri

```python
def calculate_area():
def get_user_name():
def print_report():
```

❌ noto‘g‘ri

```python
def CalculateArea()
def getUserName()
```

---

# 🔎 9. Funksiya chaqirilganda nima bo‘ladi?

Misol:

```python
def test():
    print("Funksiya ishladi")

print("Boshlanish")
test()
print("Tugadi")
```

Natija

```
Boshlanish
Funksiya ishladi
Tugadi
```

Jarayon:

```
Program boshlanadi
↓
print("Boshlanish")
↓
test() chaqiriladi
↓
funksiya ichidagi kod bajariladi
↓
dastur davom etadi
```

---

# 💡 10. Bir nechta funksiya yaratish

```python
def greet():
    print("Salom!")

def bye():
    print("Xayr!")

greet()
bye()
```

Natija

```
Salom!
Xayr!
```

---

# 🧪 11. Real mini misol

```python
def show_menu():
    print("1 - Start")
    print("2 - Settings")
    print("3 - Exit")

show_menu()
```

Natija

```
1 - Start
2 - Settings
3 - Exit
```

---

# 🏗 12. Funksiya ichida funksiya

Nazariy jihatdan mumkin:

```python
def outer():
    def inner():
        print("Ichki funksiya")

    inner()

outer()
```

Natija

```
Ichki funksiya
```

---

<br>
<br>
<br>
<br>
<br>
# 📞 Calling Functions (Invocation) — Funksiyani chaqirish

Oldingi darsda biz **funksiyani yaratishni (`def`)** o‘rgandik.
Endi esa **funksiyani qanday ishga tushirish (chaqirish)** ni o‘rganamiz.

> **Calling a function (invocation)** — bu **yaratilgan funksiyani bajarish uchun uni chaqirish jarayoni**.

---

# 🎯 1. Funksiyani chaqirish nima?

Funksiya **`def` bilan yaratiladi**, lekin **chaqirilmaguncha ishlamaydi**.

### Misol

```python
def greet():
    print("Salom!")
```

Bu yerda funksiya **faqat yaratilgan**.

Uni ishlatish uchun:

```python
greet()
```

Natija

```
Salom!
```

---

# 🧠 2. Funksiya chaqirish sintaksisi

Funksiyani chaqirish juda oddiy:

```python
function_name()
```

### Strukturasi

| Qism            | Vazifa                     |
| --------------- | -------------------------- |
| `function_name` | funksiya nomi              |
| `()`            | funksiyani ishga tushiradi |

---

# ✨ 3. To‘liq misol

```python
def say_hello():
    print("Hello!")
```

Funksiyani chaqirish:

```python
say_hello()
```

Natija

```
Hello!
```

---

# 🔄 4. Bir funksiyani ko‘p marta chaqirish

Funksiyaning eng katta afzalligi — **uni cheksiz marta ishlatish mumkin**.

```python
def greet():
    print("Salom!")

greet()
greet()
greet()
```

Natija

```
Salom!
Salom!
Salom!
```

---

# 🧩 5. Dastur oqimi (Execution Flow)

Python kodni **yuqoridan pastga** o‘qiydi.

Misol:

```python
def hello():
    print("Funksiya ishladi")

print("Boshlanish")
hello()
print("Tugadi")
```

Natija

```
Boshlanish
Funksiya ishladi
Tugadi
```

### Jarayon

```
1️⃣ print("Boshlanish")
2️⃣ hello() chaqiriladi
3️⃣ funksiya ichidagi kod bajariladi
4️⃣ dastur davom etadi
```

---

# ⚠️ 6. Funksiya chaqirilmasa nima bo‘ladi?

```python
def hello():
    print("Hello")
```

Natija:

```
Hech narsa chiqmaydi
```

Sababi:

> Funksiya **chaqirilmagan**.

---

# 🧪 7. Bir nechta funksiyani chaqirish

```python
def greet():
    print("Salom")

def bye():
    print("Xayr")

greet()
bye()
```

Natija

```
Salom
Xayr
```

---

# 🔗 8. Funksiya ichidan boshqa funksiyani chaqirish

Funksiya boshqa funksiyani ham chaqirishi mumkin.

```python
def greet():
    print("Salom")

def start():
    print("Dastur boshlandi")
    greet()

start()
```

Natija

```
Dastur boshlandi
Salom
```

---

# 🧭 9. Funksiya chaqirilish tartibi

Misol:

```python
def first():
    print("Birinchi funksiya")

def second():
    print("Ikkinchi funksiya")

second()
first()
```

Natija

```
Ikkinchi funksiya
Birinchi funksiya
```

Python **chaqirilgan tartibda** bajaradi.

---

# ⚡ 10. Funksiya chaqirishni o‘zgaruvchiga saqlash

Funksiya natijasi ba’zan o‘zgaruvchiga saqlanadi.

Misol:

```python
def greet():
    print("Salom!")

result = greet()
```

Natija

```
Salom!
```

Lekin `result` qiymati:

```
None
```

Sababi — funksiya **hech narsa qaytarmadi**.

---

# 🏗 11. Real misol (mini dastur)

```python
def show_menu():
    print("1 - Start")
    print("2 - Settings")
    print("3 - Exit")

print("Menu:")
show_menu()
```

Natija

```
Menu:
1 - Start
2 - Settings
3 - Exit
```

---

# 📊 12. Stack tushunchasi (oddiy tushuntirish)

Funksiya chaqirilganda **call stack** ishlaydi.

Misol:

```python
def a():
    print("A")

def b():
    print("B")
    a()

b()
```

Natija

```
B
A
```

Jarayon

```
b() chaqirildi
↓
b() ichida a() chaqirildi
↓
a() bajarildi
↓
b() tugadi
```

---
<br>
<br>
<br>
<br>
<br>
# 📊 Parameters vs Arguments — Python’da parametr va argument

Funksiyalar bilan ishlaganda **ikkita muhim tushuncha bor**:

```
Parameters
Arguments
```

Ular ko‘pincha aralashib ketadi, lekin aslida **farqli tushunchalar**.

---

# 🎯 1. Parameter nima?

> **Parameter** — bu funksiya yaratilganda (`def`) qavs ichida yoziladigan **o‘zgaruvchi**.

### Misol

```python
def greet(name):
    print("Salom", name)
```

Bu yerda:

```
name → parameter
```

Chunki u **funksiya ichida ishlatiladigan o‘zgaruvchi**.

---

# 🎯 2. Argument nima?

> **Argument** — bu funksiya chaqirilganda parametrga beriladigan **haqiqiy qiymat**.

### Misol

```python
greet("Ali")
```

Bu yerda:

```
"Ali" → argument
```

---

# 🧠 3. Oddiy taqqoslash

| Tushuncha | Qayerda yoziladi       | Misol              |
| --------- | ---------------------- | ------------------ |
| Parameter | funksiya yaratishda    | `def greet(name):` |
| Argument  | funksiya chaqirilganda | `greet("Ali")`     |

---

# ✨ 4. To‘liq misol

```python
def greet(name):
    print("Salom", name)

greet("Ali")
```

Natija

```
Salom Ali
```

Tahlil:

```
name → parameter
"Ali" → argument
```

---

# 📦 5. Bir nechta parameter

Funksiya bir nechta parametrga ega bo‘lishi mumkin.

### Misol

```python
def add(a, b):
    print(a + b)
```

Bu yerda:

```
a → parameter
b → parameter
```

Chaqarish:

```python
add(5, 3)
```

Natija

```
8
```

Bu yerda:

```
5 → argument
3 → argument
```

---

# 🔄 6. Bir nechta chaqirish

Bir funksiya turli argumentlar bilan ishlatilishi mumkin.

```python
def greet(name):
    print("Salom", name)

greet("Ali")
greet("Vali")
greet("Sardor")
```

Natija

```
Salom Ali
Salom Vali
Salom Sardor
```

---

# 🧩 7. Parameterlar funksiya ichida ishlaydi

Parameter **faqat funksiya ichida mavjud bo‘ladi**.

```python
def show_age(age):
    print("Yosh:", age)

show_age(25)
```

Natija

```
Yosh: 25
```

Bu yerda:

```
age → parameter
25 → argument
```

---

# ⚠️ 8. Argument soni mos bo‘lishi kerak

Parameter va argument soni mos kelishi kerak.

### Xato misol

```python
def add(a, b):
    print(a + b)

add(5)
```

Xatolik

```
TypeError: missing required argument
```

Sababi:

```
2 ta parameter
1 ta argument
```

---

# ✔ To‘g‘ri misol

```python
def add(a, b):
    print(a + b)

add(5, 10)
```

Natija

```
15
```

---

# 🧪 9. Real misol

```python
def introduce(name, age):
    print("Ism:", name)
    print("Yosh:", age)

introduce("Ali", 20)
```

Natija

```
Ism: Ali
Yosh: 20
```

---

# 📊 10. Visual tushuntirish

Funksiya:

```
def add(a, b):
```

Chaqirish:

```
add(3, 7)
```

Mapping:

```
a = 3
b = 7
```

---

# 🧠 11. Parameter → argument ga qiymat berilishi

Python avtomatik ravishda qiymatlarni moslashtiradi.

```python
def multiply(x, y):
    print(x * y)

multiply(4, 5)
```

Natija

```
20
```

Jarayon:

```
x = 4
y = 5
```

---
<br>
<br>
<br>
<br>
<br>
