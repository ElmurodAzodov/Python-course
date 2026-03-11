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
# 📤 Return Values (single, multiple, None) — Funksiyadan qiymat qaytarish

Python’da funksiya **natija qaytarishi** mumkin.
Bu **`return`** kalit so‘zi orqali amalga oshiriladi.

> **Return value** — funksiya bajarilgandan keyin tashqariga beriladigan natija.

---

# 🎯 1. `return` nima?

`return` — funksiya ichidagi natijani **funksiyadan tashqariga yuboradi**.

### Sintaksis

```python
def function_name():
    return value
```

---

# ✨ 2. Oddiy return (single value)

Funksiya **bitta qiymat qaytarishi** mumkin.

### Misol

```python
def add(a, b):
    return a + b
```

Funksiyani chaqirish:

```python
result = add(5, 3)
print(result)
```

Natija

```
8
```

### Jarayon

```
a = 5
b = 3
a + b = 8
return 8
```

---

# 🧠 3. `return` bo‘lmasa nima bo‘ladi?

Agar funksiya `return` ishlatmasa, Python **`None` qaytaradi**.

### Misol

```python
def greet():
    print("Salom")

result = greet()

print(result)
```

Natija

```
Salom
None
```

Sababi:

```
Funksiya qiymat qaytarmadi
→ Python avtomatik None qaytardi
```

---

# 📦 4. `return` va `print` farqi

Ko‘pchilik bu ikkalasini adashtiradi.

| print                            | return                  |
| -------------------------------- | ----------------------- |
| faqat ekranga chiqaradi          | qiymatni qaytaradi      |
| funksiyadan tashqariga chiqmaydi | natijani saqlash mumkin |

### Misol

```python
def add(a, b):
    print(a + b)
```

```
add(5, 3)
```

Natija

```
8
```

Lekin:

```
x = add(5,3)
print(x)
```

Natija

```
8
None
```

---

### To‘g‘ri usul

```python
def add(a, b):
    return a + b
```

```
x = add(5,3)
print(x)
```

Natija

```
8
```

---

# 🧩 5. `return` funksiya bajarilishini to‘xtatadi

`return` bajarilgandan keyin **funksiya tugaydi**.

### Misol

```python
def test():
    print("Start")
    return
    print("End")
```

```
test()
```

Natija

```
Start
```

Sababi:

```
return dan keyingi kod ishlamaydi
```

---

# 🔢 6. Multiple return values (bir nechta qiymat)

Python funksiya **bir nechta qiymat qaytarishi** mumkin.

### Misol

```python
def calculate(a, b):
    return a + b, a * b
```

Chaqarish:

```python
result = calculate(4, 3)
print(result)
```

Natija

```
(7, 12)
```

Python bu yerda **tuple** qaytaradi.

---

# 📊 7. Multiple return ni alohida o‘zgaruvchiga olish

```python
def calculate(a, b):
    return a + b, a * b
```

```
sum_value, product = calculate(4, 3)

print(sum_value)
print(product)
```

Natija

```
7
12
```

Mapping:

```
sum_value = 7
product = 12
```

---

# 🧪 8. Real misol

```python
def get_user():
    name = "Ali"
    age = 20
    return name, age
```

```
name, age = get_user()

print(name)
print(age)
```

Natija

```
Ali
20
```

---

# ⚠️ 9. Return bilan shart ishlatish

Funksiya turli qiymat qaytarishi mumkin.

```python
def check_number(n):
    if n > 0:
        return "Positive"
    else:
        return "Negative"
```

```
print(check_number(5))
print(check_number(-2))
```

Natija

```
Positive
Negative
```

---

# 🧭 10. `return None`

Ba'zan funksiya **hech qanday natija bermasligini aniq ko‘rsatish uchun** `None` qaytariladi.

```python
def do_nothing():
    return None
```

```
print(do_nothing())
```

Natija

```
None
```

---

# 🏗 11. Real mini dastur

```python
def rectangle_area(width, height):
    return width * height
```

```
area = rectangle_area(5, 4)

print("Area:", area)
```

Natija

```
Area: 20
```

---
<br>
<br>
<br>
<br>
<br>
# ⚙️ Default Arguments (`def func(x=5)`) — Standart qiymatli parametrlar

Python funksiyalarida **parameterlarga oldindan qiymat berish** mumkin.
Bu **default argument** deyiladi.

> **Default Argument** — agar funksiya chaqirilganda qiymat berilmasa, **oldindan belgilangan qiymat ishlatiladi**.

---

# 🎯 1. Default argument nima?

Funksiya yaratilayotganda parametrga **standart qiymat** beriladi.

### Sintaksis

```python
def function_name(parameter=value):
    kod
```

---

# ✨ 2. Eng oddiy misol

```python
def greet(name="Mehmon"):
    print("Salom", name)
```

Funksiyani chaqirish:

```python
greet()
```

Natija

```
Salom Mehmon
```

Sababi:

```
name = "Mehmon" (default qiymat)
```

---

# 🧠 3. Argument berilsa nima bo‘ladi?

Agar argument berilsa, **default qiymat ishlatilmaydi**.

```python
def greet(name="Mehmon"):
    print("Salom", name)
```

```python
greet("Ali")
```

Natija

```
Salom Ali
```

Jarayon

```
name = "Ali"
```

---

# 📊 4. Default argument qanday ishlaydi

Funksiya:

```python
def greet(name="Mehmon"):
```

Chaqirish:

```
greet()
```

Mapping:

```
name = "Mehmon"
```

Agar:

```
greet("Ali")
```

Mapping:

```
name = "Ali"
```

---

# 🧩 5. Bir nechta default argument

Funksiya bir nechta default parametrga ega bo‘lishi mumkin.

```python
def introduce(name="Mehmon", age=18):
    print("Ism:", name)
    print("Yosh:", age)
```

Chaqirish:

```python
introduce()
```

Natija

```
Ism: Mehmon
Yosh: 18
```

---

# 🔄 6. Ba'zilarini o‘zgartirish

```python
def introduce(name="Mehmon", age=18):
    print("Ism:", name)
    print("Yosh:", age)
```

```python
introduce("Ali")
```

Natija

```
Ism: Ali
Yosh: 18
```

Mapping:

```
name = "Ali"
age = 18
```

---

# 🧪 7. Barcha argumentlarni berish

```python
def introduce(name="Mehmon", age=18):
    print("Ism:", name)
    print("Yosh:", age)
```

```python
introduce("Ali", 20)
```

Natija

```
Ism: Ali
Yosh: 20
```

---

# ⚠️ 8. Default argument tartibi

Python’da **default parametrlar oxirida bo‘lishi kerak**.

### ❌ Xato

```python
def test(a=5, b):
    print(a, b)
```

Xatolik:

```
SyntaxError
```

---

### ✔ To‘g‘ri

```python
def test(a, b=5):
    print(a, b)
```

---

# 📦 9. Real misol

```python
def power(base, exponent=2):
    return base ** exponent
```

Chaqirish:

```python
print(power(5))
```

Natija

```
25
```

Chunki:

```
exponent = 2
```

---

Agar exponent berilsa:

```python
print(power(5, 3))
```

Natija

```
125
```

---

# 🧭 10. Default argument bilan amaliy misol

```python
def connect(host="localhost", port=8000):
    print("Host:", host)
    print("Port:", port)
```

```python
connect()
```

Natija

```
Host: localhost
Port: 8000
```

---

```python
connect("google.com", 443)
```

Natija

```
Host: google.com
Port: 443
```

---

# 🏗 11. Mini real dastur

```python
def greet_user(name="User"):
    return "Hello " + name
```

```python
print(greet_user())
print(greet_user("Ali"))
```

Natija

```
Hello User
Hello Ali
```

---
<br>
<br>
<br>
<br>
<br>
