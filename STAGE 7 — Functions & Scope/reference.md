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

# 🔑 Keyword Arguments (`func(x=1, y=2)`) — Nom bilan argument berish

Python’da funksiyani chaqirganda argumentlarni **parametr nomi bilan berish** mumkin.
Bu **keyword arguments** deyiladi.

> **Keyword Argument** — argumentni parametr nomi bilan aniq ko‘rsatib berish.

---

# 🎯 1. Keyword argument nima?

Oddiy chaqirishda argumentlar **tartib bo‘yicha** beriladi.

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

Bu **positional argument** deyiladi.

---

# ✨ 2. Keyword argument ishlatish

Argumentni **parametr nomi bilan** berish mumkin.

```python
introduce(name="Ali", age=20)
```

Natija

```
Ism: Ali
Yosh: 20
```

Bu yerda:

```
name="Ali"
age=20
```

→ **keyword arguments**

---

# 🧠 3. Keyword argumentning afzalligi

Keyword argument bilan **argument tartibi muhim bo‘lmaydi**.

### Misol

```python
introduce(age=20, name="Ali")
```

Natija

```
Ism: Ali
Yosh: 20
```

Python **nom bo‘yicha moslashtiradi**.

---

# 📊 4. Positional vs Keyword arguments

| Positional   | Keyword           |
| ------------ | ----------------- |
| tartib muhim | tartib muhim emas |
| `func(1, 2)` | `func(x=1, y=2)`  |
| qisqaroq     | aniqroq           |

---

# 🧩 5. Aralashtirib ishlatish

Python’da **positional va keyword argumentlarni birga ishlatish mumkin**.

```python
def student(name, age, city):
    print(name, age, city)
```

Chaqirish:

```python
student("Ali", age=20, city="Tashkent")
```

Natija

```
Ali 20 Tashkent
```

---

# ⚠️ Muhim qoida

**Positional argumentlar har doim keywordlardan oldin keladi.**

### ❌ Xato

```python
student(name="Ali", 20, city="Tashkent")
```

Xato:

```
SyntaxError
```

---

### ✔ To‘g‘ri

```python
student("Ali", age=20, city="Tashkent")
```

---

# 🔄 6. Default arguments bilan ishlatish

Keyword argumentlar **default argumentlar bilan juda yaxshi ishlaydi**.

```python
def connect(host="localhost", port=8000):
    print("Host:", host)
    print("Port:", port)
```

Chaqirish:

```python
connect(port=9000)
```

Natija

```
Host: localhost
Port: 9000
```

Bu yerda:

```
host → default
port → o‘zgartirilgan
```

---

# 🧪 7. Real misol

```python
def create_user(username, email, active=True):
    print("Username:", username)
    print("Email:", email)
    print("Active:", active)
```

Chaqirish:

```python
create_user(
    username="ali123",
    email="ali@mail.com",
    active=False
)
```

Natija

```
Username: ali123
Email: ali@mail.com
Active: False
```

---

# 📦 8. O‘qilishi oson kod

Keyword argumentlar **katta loyihalarda juda muhim**.

### Positional

```python
create_user("ali123", "ali@mail.com", False)
```

Tushunish qiyin.

---

### Keyword

```python
create_user(
    username="ali123",
    email="ali@mail.com",
    active=False
)
```

Juda **tushunarli**.

---

# 🧭 9. Matematik misol

```python
def power(base, exponent):
    return base ** exponent
```

Positional:

```python
print(power(2, 3))
```

Natija

```
8
```

Keyword:

```python
print(power(base=2, exponent=3))
```

Natija

```
8
```

---

# 🏗 10. Real mini dastur

```python
def order(product, quantity, price):
    total = quantity * price
    print("Product:", product)
    print("Total:", total)
```

Chaqirish:

```python
order(product="Laptop", quantity=2, price=800)
```

Natija

```
Product: Laptop
Total: 1600
```

---

<br>
<br>
<br>
<br>
<br>

# 📏 Variable-Length Arguments (`*args`, `**kwargs`) — Cheksiz argumentlar

Ba’zan funksiyaga **aniq sonli argumentlar emas**, balki **har qanday sonli argument** berilishi kerak bo‘ladi.
Buning uchun Python’da **`*args`** va **`**kwargs`** ishlatiladi.

> **`*args`** — positional arguments (ro‘yxat shaklida)
> **`**kwargs`** — keyword arguments (lug‘at shaklida)

---

# 🎯 1. `*args` nima?

`*args` — bu **funksiya parametriga berilgan barcha positional argumentlarni tuple shaklida qabul qiladi**.

### Sintaksis

```python id="z2tkm0"
def function_name(*args):
    for arg in args:
        print(arg)
```

---

# ✨ 2. Oddiy misol (`*args`)

```python id="c1oyhm"
def greet(*names):
    for name in names:
        print("Salom", name)
```

Chaqirish:

```python id="h4b5gk"
greet("Ali", "Vali", "Sardor")
```

Natija:

```id="8ylkpv"
Salom Ali
Salom Vali
Salom Sardor
```

> `names` → tuple: `("Ali", "Vali", "Sardor")`

---

# 📊 3. `**kwargs` nima?

`**kwargs` — bu **keyword argumentlarni lug‘at (dictionary) shaklida qabul qiladi**.

### Sintaksis

```python id="r3s0e7"
def function_name(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
```

---

# 🧩 4. Oddiy misol (`**kwargs`)

```python id="m1z5ku"
def introduce(**info):
    for key, value in info.items():
        print(key, ":", value)
```

Chaqirish:

```python id="f8tm0w"
introduce(name="Ali", age=20, city="Tashkent")
```

Natija:

```id="q8rk3p"
name : Ali
age : 20
city : Tashkent
```

> `info` → dictionary: `{"name":"Ali","age":20,"city":"Tashkent"}`

---

# 🔄 5. `*args` va `**kwargs` birga ishlatish

```python id="j2p7me"
def func(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
```

```python id="b6a1gr"
func(1, 2, 3, a=10, b=20)
```

Natija:

```id="n8kqxp"
Positional: (1, 2, 3)
Keyword: {'a': 10, 'b': 20}
```

---

# ⚠️ 6. Tartib qoidasi

1️⃣ Positional argumentlar → normal parameters
2️⃣ `*args` → cheksiz positional argumentlar
3️⃣ Keyword argumentlar → normal parameters
4️⃣ `**kwargs` → cheksiz keyword argumentlar

```python id="k2fs1r"
def example(a, b, *args, x=5, **kwargs):
    pass
```

---

# 🧪 7. Real misol: matematik

```python id="d7q6zt"
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```

```python id="e1l9pv"
print(sum_all(1, 2, 3, 4, 5))
```

Natija:

```id="m9r4tw"
15
```

---

# 📦 8. Real misol: foydalanuvchi info

```python id="p5xk7c"
def show_user(*args, **kwargs):
    print("Names:", args)
    print("Details:", kwargs)
```

```python id="s4wq8j"
show_user("Ali", "Vali", age=20, city="Tashkent")
```

Natija:

```id="h6t7rw"
Names: ('Ali', 'Vali')
Details: {'age': 20, 'city': 'Tashkent'}
```

---

# 🔗 9. Default parametr bilan birga ishlatish

```python id="k8y8pq"
def greet(greeting="Salom", *names):
    for name in names:
        print(greeting, name)
```

```python id="m5n2rw"
greet("Hello", "Ali", "Vali")
```

Natija:

```id="y2v1xz"
Hello Ali
Hello Vali
```

Agar greeting default qiymatda bo‘lsa:

```python id="q9k1as"
greet(None, "Ali")
```

Natija:

```id="j4z8po"
None Ali
```

---

# 🏗 10. Mini real dastur

```python id="d8s3qk"
def order_summary(customer, *items, **prices):
    print("Customer:", customer)
    print("Items:", items)
    print("Prices:", prices)
```

```python id="m7r4lt"
order_summary("Ali", "Laptop", "Mouse", Laptop=1000, Mouse=50)
```

Natija:

```id="b2x5pw"
Customer: Ali
Items: ('Laptop', 'Mouse')
Prices: {'Laptop': 1000, 'Mouse': 50}
```

---

<br>
<br>
<br>
<br>
<br>

# 🔢 Keyword-Only Arguments (`*, arg`) — Faqat nom bilan argument

Python 3 da **`*` belgisidan keyin yozilgan parametrlar faqat keyword argument sifatida berilishi mumkin**.
Bu **positional argument bilan aralashib ketmasligi** uchun ishlatiladi.

> Keyword-only argument → faqat **parametr nomi bilan chaqirilishi mumkin**.

---

# 🎯 1. Sintaksis

```python id="5r7v8q"
def func(a, b, *, c, d):
    print(a, b, c, d)
```

* `a, b` → positional yoki keyword argument bo‘lishi mumkin
* `c, d` → **faqat keyword argument**

---

# ✨ 2. Oddiy misol

```python id="d1kz5t"
def greet(name, *, greeting="Salom"):
    print(f"{greeting} {name}!")
```

Chaqirish:

```python id="q7y4hk"
greet("Ali", greeting="Hello")
```

Natija:

```id="r3k5mv"
Hello Ali!
```

---

# ⚠️ 3. Keyword-only argumentni positional berib bo‘lmaydi

```python id="n2x8kp"
greet("Ali", "Hello")
```

Natija:

```id="m8r7qt"
TypeError: greet() takes 1 positional argument but 2 were given
```

> `greeting` faqat keyword argument sifatida berilishi mumkin.

---

# 📊 4. Default qiymat bilan ishlatish

```python id="p4s1vy"
def connect(host="localhost", *, port=8000):
    print("Host:", host)
    print("Port:", port)
```

```python id="k5w9lt"
connect(port=9000)
```

Natija:

```id="s3j4hv"
Host: localhost
Port: 9000
```

* `host` → default, positional yoki keyword bo‘lishi mumkin
* `port` → keyword-only

---

# 🧩 5. Bir nechta keyword-only argument

```python id="b7v2kq"
def order(product, *, quantity=1, discount=0):
    print("Product:", product)
    print("Quantity:", quantity)
    print("Discount:", discount)
```

```python id="f4n9rm"
order("Laptop", quantity=2, discount=100)
```

Natija:

```id="h3t6vx"
Product: Laptop
Quantity: 2
Discount: 100
```

---

# 🔄 6. Positional va keyword-only aralash

```python id="a5r1gn"
def func(a, b, *, c, d=10):
    print(a, b, c, d)
```

```python id="k9s8mv"
func(1, 2, c=5)
```

Natija:

```id="v3r9kx"
1 2 5 10
```

* `c` → keyword-only, qiymat berilishi majbur
* `d` → default qiymat, keyword-only

---

# 🧪 7. Real misol: foydalanuvchi yaratish

```python id="j8p3nh"
def create_user(username, *, is_admin=False, active=True):
    print("Username:", username)
    print("Admin:", is_admin)
    print("Active:", active)
```

```python id="m1x7lg"
create_user("ali123", is_admin=True)
```

Natija:

```id="r4v2tp"
Username: ali123
Admin: True
Active: True
```

---

# ⚠️ 8. Keyword-only argument majburiy bo‘lishi

Agar default qiymat berilmasa, chaqirishda **majburiy** bo‘ladi:

```python id="p9z6kl"
def func(a, *, b):
    print(a, b)
```

```python id="k3t9hv"
func(1)
```

Natija:

```id="f7n4qt"
TypeError: func() missing 1 required keyword-only argument: 'b'
```

---

# 📦 9. Keyword-only argumentning afzalligi

* Kod **o‘qilishi aniq bo‘ladi**
* Positional argumentlar bilan aralashmaydi
* Default qiymat berish va majburiy qilish mumkin
* Katta professional kodlarda juda qulay

---

# 🏗 10. Mini real dastur

```python id="c4t2nx"
def send_email(to, *, subject="No Subject", cc=None):
    print("To:", to)
    print("Subject:", subject)
    print("CC:", cc)
```

```python id="s8v3ml"
send_email("user@mail.com", subject="Hello", cc="boss@mail.com")
```

Natija:

```id="r7y1hw"
To: user@mail.com
Subject: Hello
CC: boss@mail.com
```

* `to` → positional yoki keyword
* `subject`, `cc` → keyword-only

---

<br>
<br>
<br>
<br>
<br>

# 🌐 Scope Rules — Python’da o‘zgaruvchilar ko‘lami

Python’da **o‘zgaruvchi qayerda ishlatilishi mumkinligi** **scope (ko‘lam)** bilan belgilanadi.
Scope tushunchasi **kodni tartibli va xatoliksiz yozish** uchun muhim.

> Scope → o‘zgaruvchining **mavjudligi va ko‘rinishi**.

---

# 🎯 1. Scope turlari

Python’da 3 ta asosiy scope mavjud:

| Scope        | Tavsif                                                              |
| ------------ | ------------------------------------------------------------------- |
| **Local**    | Funksiya yoki blok ichida yaratilgan o‘zgaruvchi                    |
| **Global**   | Dastur bo‘yicha mavjud o‘zgaruvchi                                  |
| **Built-in** | Python tomonidan oldindan belgilangan o‘zgaruvchilar va funksiyalar |

---

# ✨ 2. Local Scope

* Funksiya ichida yaratilgan o‘zgaruvchi **faqat shu funksiya ichida mavjud**.
* Funksiya tashqarisida **ko‘rinmaydi**.

### Misol

```python id="local1"
def my_func():
    x = 10   # local
    print("Inside:", x)

my_func()
```

Natija:

```id="local2"
Inside: 10
```

```python id="local3"
print(x)  # ❌ NameError
```

Sababi: `x` faqat **local scope** da mavjud.

---

# 📦 3. Global Scope

* Funksiya tashqarisida yaratilgan o‘zgaruvchi **barcha kod bo‘yicha mavjud**.

```python id="global1"
y = 5  # global

def my_func():
    print("Inside:", y)

my_func()
print("Outside:", y)
```

Natija:

```id="global2"
Inside: 5
Outside: 5
```

---

# ⚠️ 4. Local va Global aralashuvi

Agar funksiya ichida **xuddi shunday nomdagi o‘zgaruvchi** yaratilsa, u **local** bo‘ladi va globalni ustidan yozmaydi.

```python id="localglobal1"
z = 50  # global

def my_func():
    z = 10  # local
    print("Inside:", z)

my_func()
print("Outside:", z)
```

Natija:

```id="localglobal2"
Inside: 10
Outside: 50
```

---

# 🧩 5. `global` keyword

* Agar funktsiyada global o‘zgaruvchini o‘zgartirmoqchi bo‘lsangiz **`global`** ishlatishingiz kerak.

```python id="globalkey1"
count = 0  # global

def increment():
    global count
    count += 1

increment()
print(count)
```

Natija:

```id="globalkey2"
1
```

---

# 🔄 6. Built-in Scope

* Python **o‘zining oldindan belgilangan funksiyalari va konstantalari**.
* Misol: `print()`, `len()`, `range()`, `int`, `str`

```python id="builtin1"
print(len("Hello"))  # print va len → built-in
```

Natija:

```id="builtin2"
5
```

---

# 🧠 7. Scope diagrammasi (LEGB)

Python **LEGB qoidasiga** amal qiladi:

1️⃣ **Local** – funksiya ichidagi o‘zgaruvchilar
2️⃣ **Enclosing** – ichki funksiya tashqarisidagi funksiya scope
3️⃣ **Global** – fayl bo‘yicha
4️⃣ **Built-in** – Python oldindan belgilangan

```text
x = 5  # global

def outer():
    x = 10  # enclosing

    def inner():
        x = 20  # local
        print(x)  # 20

    inner()
    print(x)  # 10

print(x)  # 5
```

---

# 🧪 8. Enclosing Scope misol

```python id="enclosing1"
def outer():
    y = 100

    def inner():
        print(y)  # enclosing

    inner()

outer()
```

Natija:

```id="enclosing2"
100
```

* `y` → **enclosing scope**, ichki funksiya tomonidan ko‘rinadi.

---

# 📌 9. Global o‘zgaruvchini o‘qish

```python id="globalread1"
x = 50  # global

def my_func():
    print(x)  # o‘qish mumkin

my_func()
```

Natija:

```id="globalread2"
50
```

⚠️ Lekin o‘zgartirish uchun **`global x`** kerak.

---

# 🔗 10. Local scope amaliy misol

```python id="localsum1"
def sum_numbers(a, b):
    result = a + b  # local
    return result

print(sum_numbers(3, 7))
```

Natija:

```id="localsum2"
10
```

* `result` → faqat **funksiya ichida mavjud**, tashqarida ko‘rinmaydi.

---

# 🏗 11. Mini real dastur

```python id="scopeapp1"
count = 0  # global

def add_to_count(n):
    global count
    count += n
    print("Inside function:", count)

add_to_count(5)
print("Outside function:", count)
```

Natija:

```id="scopeapp2"
Inside function: 5
Outside function: 5
```

---

<br>
<br>
<br>
<br>
<br>

# 🏠 Local vs Global Scope (`global` keyword) — Local va Global o‘zgaruvchilar

Python’da **local va global scope** tushunchasi kodni tushunish va xatolardan saqlanish uchun juda muhim.
**`global`** kalit so‘zi esa global o‘zgaruvchini funksiya ichida o‘zgartirish imkonini beradi.

---

# 🎯 1. Local o‘zgaruvchi

* **Funksiya ichida yaratiladi**
* **Faqat shu funksiya ichida ko‘rinadi**
* Tashqaridan **ko‘rinmaydi**

### Misol

```python id="local1"
def my_func():
    x = 10  # local
    print("Inside function:", x)

my_func()
```

Natija:

```id="local2"
Inside function: 10
```

```python id="local3"
print(x)  # ❌ NameError
```

---

# 📦 2. Global o‘zgaruvchi

* **Funksiya tashqarisida yaratiladi**
* **Dastur bo‘yicha mavjud**
* Funksiya ichida o‘qilishi mumkin

### Misol

```python id="global1"
y = 5  # global

def my_func():
    print("Inside function:", y)

my_func()
print("Outside function:", y)
```

Natija:

```id="global2"
Inside function: 5
Outside function: 5
```

---

# ⚠️ 3. Local vs Global aralashuvi

Agar funksiya ichida **xuddi shu nomdagi o‘zgaruvchi** yaratilsa:

```python id="localglobal1"
z = 50  # global

def my_func():
    z = 10  # local
    print("Inside function:", z)

my_func()
print("Outside function:", z)
```

Natija:

```id="localglobal2"
Inside function: 10
Outside function: 50
```

> Local o‘zgaruvchi globalni ustidan yozmaydi.

---

# 🔑 4. `global` kalit so‘zi

* Funksiya ichida **global o‘zgaruvchini o‘zgartirish** uchun ishlatiladi.

```python id="globalkey1"
count = 0  # global

def increment():
    global count
    count += 1

increment()
print(count)
```

Natija:

```id="globalkey2"
1
```

> `global count` → funksiya ichida global `count` o‘zgaruvchisiga murojaat qilamiz.

---

# 🧩 5. Global o‘zgaruvchini faqat o‘qish

Agar faqat **o‘qish** kerak bo‘lsa, `global` ishlatish shart emas:

```python id="globalread1"
x = 100  # global

def print_x():
    print(x)  # globalni o‘qish mumkin

print_x()
```

Natija:

```id="globalread2"
100
```

---

# 🔄 6. Global o‘zgaruvchini yozish vs local

```python id="mix1"
value = 10  # global

def change_value():
    value = 20  # local
    print("Inside:", value)

change_value()
print("Outside:", value)
```

Natija:

```id="mix2"
Inside: 20
Outside: 10
```

> Agar **globalni o‘zgartirmoqchi bo‘lsangiz**, `global value` kerak.

---

# 🧪 7. Real misol: hisoblagich

```python id="counter1"
counter = 0  # global

def add_one():
    global counter
    counter += 1
    print("Counter inside:", counter)

add_one()
add_one()
print("Counter outside:", counter)
```

Natija:

```id="counter2"
Counter inside: 1
Counter inside: 2
Counter outside: 2
```

---

# 🔗 8. Nested function va `global`

```python id="nested1"
x = 5  # global

def outer():
    x = 10  # enclosing

    def inner():
        global x
        x = 20  # global
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)
```

Natija:

```id="nested2"
Inner: 20
Outer: 10
Global: 20
```

> `global x` → tashqi global `x` ga murojaat qildi, enclosing scope ga ta’sir qilmaydi.

---

<br>
<br>
<br>
<br>
<br>

# 🔢 LEGB Rule — Local → Enclosing → Global → Built-in

Python’da **o‘zgaruvchi qayerdan topilishini aniqlash** uchun **LEGB qoidasi** ishlatiladi.
Bu **Local, Enclosing, Global, Built-in** so‘zlarining qisqartmasi.

> LEGB → Python o‘zgaruvchilarni **qayerdan qidiradi** degan tartibni belgilaydi.

---

# 🎯 1. LEGB tartibi

1️⃣ **Local (L)** → Funksiya ichidagi o‘zgaruvchilar
2️⃣ **Enclosing (E)** → Ichki funksiya tashqarisidagi funksiya scope
3️⃣ **Global (G)** → Fayl bo‘yicha global o‘zgaruvchilar
4️⃣ **Built-in (B)** → Python oldindan belgilangan funksiyalar va konstantalar

---

# ✨ 2. Local Scope misol

```python id="legblocal1"
def func():
    x = 10  # local
    print(x)

func()
```

Natija:

```id="legblocal2"
10
```

* `x` → **Local**, LEGB bo‘yicha birinchi topilgan.

---

# 🔄 3. Global Scope misol

```python id="legbglobal1"
x = 5  # global

def func():
    print(x)  # local yo‘q, globaldan topiladi

func()
```

Natija:

```id="legbglobal2"
5
```

* Local topilmadi → Globaldan olindi.

---

# 🧩 4. Enclosing Scope misol (Nested function)

```python id="legbenclosing1"
def outer():
    x = 10  # enclosing

    def inner():
        print(x)  # local yo‘q, enclosingdan topiladi

    inner()

outer()
```

Natija:

```id="legbenclosing2"
10
```

* `x` → **Enclosing** scope dan topildi.

---

# 🧠 5. Built-in Scope misol

```python id="legbbuiltin1"
print(len("Hello"))  # len → built-in
```

Natija:

```id="legbbuiltin2"
5
```

* Local, Enclosing, Global topilmadi → **Built-in** ishlatildi.

---

# ⚠️ 6. LEGB qarama-qarshi misol

```python id="legbmix1"
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local birinchi

    inner()
    print(x)  # enclosing
```

```python id="legbmix2"
outer()
print(x)  # global
```

Natija:

```id="legbmix3"
local
enclosing
global
```

---

# 🔗 7. `nonlocal` bilan enclosing scope o‘zgartirish

* Ichki funksiya tashqi funksiya o‘zgaruvchisini o‘zgartirish uchun **`nonlocal`** ishlatiladi.

```python id="legbnonlocal1"
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
```

Natija:

```id="legbnonlocal2"
20
```

* Local yo‘q → nonlocal enclosing ni o‘zgartirdi.

---

# 🏗 8. Real misol

```python id="legbreal1"
x = 1  # global

def outer():
    x = 2  # enclosing

    def inner():
        x = 3  # local
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)
```

Natija:

```id="legbreal2"
Inner: 3
Outer: 2
Global: 1
```

* Local → Enclosing → Global → Built-in
* Har bir scope faqat kerak bo‘lganda topiladi.

---

<br>
<br>
<br>
<br>
<br>

# 📄 Docstrings — Funksiya dokumentatsiyasi va `help()`

Python’da funksiyalarni **tushunarli va professional yozish** uchun **docstring** ishlatiladi.
Bu funksiya nima qiladi, qanday argument qabul qiladi va qanday natija beradi — **shu ma’lumotni saqlaydi**.

> Docstring → funksiya ichidagi birinchi qatorli **ko‘rsatma matni**

---

# 🎯 1. Docstring sintaksisi

* **Uch qo‘shtirnoq** (`""" """`) ichida yoziladi
* Funksiya, klass yoki modulni **hujjatlash** uchun ishlatiladi

```python id="doc1"
def function_name():
    """Bu funksiya nima qilishini tushuntiradi"""
    pass
```

---

# ✨ 2. Oddiy misol

```python id="doc2"
def greet(name):
    """Foydalanuvchiga salom beradi"""
    print("Salom", name)
```

* `greet.__doc__` orqali docstringga murojaat qilish mumkin:

```python id="doc3"
print(greet.__doc__)
```

Natija:

```id="doc4"
Foydalanuvchiga salom beradi
```

---

# 🔄 3. Docstringda parametrlar va qaytish qiymatlari

```python id="doc5"
def add(a, b):
    """
    Ikkita sonni qo‘shadi va natijani qaytaradi.

    Parametrlar:
    a (int): Birinchi son
    b (int): Ikkinchi son

    Qaytadi:
    int: Ikkala son yig‘indisi
    """
    return a + b
```

* `help(add)` orqali funksiyani ko‘rish mumkin:

```python id="doc6"
help(add)
```

Natija:

```id="doc7"
Help on function add in module __main__:

add(a, b)
    Ikkita sonni qo‘shadi va natijani qaytaradi.
    
    Parametrlar:
    a (int): Birinchi son
    b (int): Ikkinchi son
    
    Qaytadi:
    int: Ikkala son yig‘indisi
```

---

# 🧩 4. Docstringning foydasi

1️⃣ Kodni **o‘qish oson bo‘ladi**
2️⃣ **Team work** da tushunishni osonlashtiradi
3️⃣ Professional Python kod standartlariga mos
4️⃣ `help()` va IDE da avtomatik ko‘rinadi

---

# 🧠 5. Multi-line docstring

```python id="doc8"
def multiply(a, b):
    """
    Ikkita sonni ko‘paytiradi.

    Parametrlar:
    a (int): Birinchi son
    b (int): Ikkinchi son

    Qaytadi:
    int: Ko‘paytma
    """
    return a * b
```

* Docstring ko‘p qatorli bo‘lishi mumkin
* Har bir qator 80 ta belgidan oshmasligi tavsiya qilinadi

---

# 📦 6. Klasslarda docstring

```python id="doc9"
class Car:
    """
    Avtomobil klassi.

    Attributes:
        make (str): Brend
        model (str): Model
    """
    def __init__(self, make, model):
        self.make = make
        self.model = model
```

```python id="doc10"
help(Car)
```

* Klass atributlari va metodlari ham docstring bilan hujjatlanadi

---

# 🏗 7. Real misol: professional funksiya

```python id="doc11"
def rectangle_area(width, height):
    """
    To‘g‘ri to‘rtburchak maydonini hisoblaydi.

    Parametrlar:
    width (float): Kenglik
    height (float): Balandlik

    Qaytadi:
    float: Maydon
    """
    return width * height
```

```python id="doc12"
help(rectangle_area)
```

Natija:

```
To‘g‘ri to‘rtburchak maydonini hisoblaydi.

Parametrlar:
width (float): Kenglik
height (float): Balandlik

Qaytadi:
float: Maydon
```

---

# 📌 8. `__doc__` vs `help()`

| Usul           | Foydasi                                              |
| -------------- | ---------------------------------------------------- |
| `func.__doc__` | Docstring matnini oladi                              |
| `help(func)`   | To‘liq hujjat va funksiya signature bilan ko‘rsatadi |

```python id="doc13"
print(rectangle_area.__doc__)
help(rectangle_area)
```

---

<br>
<br>
<br>
<br>
<br>

# ✨ Clean Function Design — Toza va tartibli funksiyalar

Python’da kodni **o‘qilishi oson, qayta ishlatiladigan va xatolarsiz** qilish uchun **clean function design** qoidasiga amal qilinadi.

> Toza funksiya → **faqat bitta vazifani bajaradi**, **side-effectsiz** ishlaydi va **aniq natija qaytaradi**.

---

# 🎯 1. Single Responsibility Principle (SRP)

* **Har bir funksiya faqat bitta vazifani bajarishi kerak.**
* Shu bilan kod **o‘qilishi oson va test qilinishi qulay** bo‘ladi.

### ❌ Noto‘g‘ri misol

```python id="srp1"
def process_user(name, age):
    print(f"User: {name}, Age: {age}")  # print qilmoqda
    return f"{name} is {age} years old"  # string qaytaradi
```

* Bu funksiya **bir vaqtning o‘zida print va return qiladi**
* **Single responsibility** buzilgan.

---

### ✔ To‘g‘ri misol

```python id="srp2"
def format_user(name, age):
    """Foydalanuvchi ma’lumotini formatlaydi"""
    return f"{name} is {age} years old"

def print_user(user_info):
    """Ma’lumotni ekranga chiqaradi"""
    print(user_info)
```

```python id="srp3"
user = format_user("Ali", 20)
print_user(user)
```

* Har bir funksiya **faqat bitta vazifani bajaradi**

---

# 🧠 2. Pure Functions (Toza funksiyalar)

**Pure function** — bu:

1️⃣ **Faqat argumentlarga bog‘liq**
2️⃣ **Hech qanday tashqi holatni o‘zgartirmaydi**
3️⃣ **Har doim bir xil input → bir xil output beradi**

---

### ❌ Noto‘g‘ri misol (side-effect)

```python id="pure1"
total = 0

def add_to_total(x):
    global total
    total += x
```

* Funksiya **global o‘zgaruvchini o‘zgartiradi** → side-effect
* Pure function emas.

---

### ✔ To‘g‘ri misol (pure function)

```python id="pure2"
def add(x, y):
    return x + y
```

* **Hech narsani o‘zgartirmaydi**, faqat natija qaytaradi
* Har doim x=2, y=3 → return 5

---

# 🔄 3. Arguments va Return Values

* Toza funksiyalar **argumentni o‘zgartirmaydi**
* Natija **return orqali** beriladi

```python id="pure3"
def capitalize_name(name):
    return name.upper()
```

```python id="pure4"
name = "ali"
new_name = capitalize_name(name)
print(name)      # ali
print(new_name)  # ALI
```

* Original `name` o‘zgarmadi → side-effect yo‘q

---

# 📦 4. Readable va Maintainable

Clean function design:

1️⃣ **Single Responsibility** → bitta vazifa
2️⃣ **Pure** → side-effectsiz
3️⃣ **Readable** → nomi va docstring tushunarli
4️⃣ **Reusable** → boshqa joyda ishlatish mumkin

---

# 🏗 5. Real misol: foydalanuvchi ma’lumotlari

```python id="clean1"
def calculate_age(birth_year, current_year):
    """Yoshni hisoblaydi"""
    return current_year - birth_year

def format_user_info(name, age):
    """Foydalanuvchi ma’lumotini formatlaydi"""
    return f"{name} is {age} years old"

def print_user_info(info):
    """Ma’lumotni ekranga chiqaradi"""
    print(info)
```

```python id="clean2"
age = calculate_age(2000, 2026)
info = format_user_info("Ali", age)
print_user_info(info)
```

Natija:

```id="clean3"
Ali is 26 years old
```

* Har bir funksiya **faqat bitta vazifani bajaradi**
* Kod **toza, tushunarli va qayta ishlatiladigan**

---

# 🧩 6. Mini real dastur: matematik

```python id="clean4"
def multiply(a, b):
    """Ikki sonni ko‘paytiradi"""
    return a * b

def square(x):
    """Sonning kvadratini hisoblaydi"""
    return multiply(x, x)

print(square(5))
```

Natija:

```id="clean5"
25
```

* `multiply` → faqat ko‘paytiradi
* `square` → faqat kvadrat hisoblaydi

---
