
# **STAGE 7 — Functions & Scope**

<br><br>

## 🧩 FUNCTION DEFINITIONS (Funksiya yaratish)

Funksiya — bu ma’lum bir vazifani bajaradigan, qayta ishlatiladigan kod blokidir.
U yordamida kod:

* ♻️ takrorlanmaydi
* 📖 o‘qilishi osonlashadi
* 🧱 modullarga bo‘linadi
* 🛠 qo‘llab-quvvatlash osonlashadi

Python’da funksiya **`def`** kalit so‘zi bilan yaratiladi.

---

# 🏗 1. Funksiya sintaksisi (eng asosiy ko‘rinish)

```python
def function_name(parameters):
    """Docstring (ixtiyoriy)"""
    # funksiya tanasi
    return value  # ixtiyoriy
```

### 📌 Qismlari:

| Qism            | Ma’nosi                          |
| --------------- | -------------------------------- |
| `def`           | Funksiya boshlanishini bildiradi |
| `function_name` | Funksiya nomi                    |
| `parameters`    | Kiruvchi qiymatlar (ixtiyoriy)   |
| `:`             | Funksiya tanasi boshlanishi      |
| `return`        | Natija qaytaradi (ixtiyoriy)     |

---

# ▶️ 2. Eng sodda funksiya

```python
def greet():
    print("Salom!")
```

📞 chaqirish:

```python
greet()
```

🟢 Natija:

```
Salom!
```

---

# 📥 3. Parametrli funksiya

Parametr — funksiya ichida ishlatiladigan o‘zgaruvchi.

```python
def greet(name):
    print("Salom,", name)
```

📞 chaqirish:

```python
greet("Ali")
```

🟢 Natija:

```
Salom, Ali
```

👉 `name` — parametr
👉 `"Ali"` — argument

---

# 📦 4. Bir nechta parametrlar

```python
def add(a, b):
    print(a + b)
```

```python
add(5, 3)
```

🟢 Natija:

```
8
```

---

# 🔁 5. Return ishlatiladigan funksiya

`return` funksiyadan qiymat qaytaradi.

```python
def add(a, b):
    return a + b
```

```python
natija = add(4, 6)
print(natija)
```

🟢 Natija:

```
10
```

👉 `return` bo‘lmasa funksiya `None` qaytaradi.

---

# 🚫 6. Return bo‘lmasa nima bo‘ladi?

```python
def test():
    print("Hello")
```

```python
x = test()
print(x)
```

🟢 Natija:

```
Hello
None
```

---

# 🔢 7. Default parametrli funksiya

Parametrga standart qiymat berish mumkin.

```python
def greet(name="Mehmon"):
    print("Salom,", name)
```

```python
greet()
greet("Ali")
```

🟢 Natija:

```
Salom, Mehmon
Salom, Ali
```

---

# 📛 8. Keyword parametrlar bilan funksiya

Argumentlarni nomi bilan uzatish mumkin.

```python
def info(name, age):
    print(name, age)
```

```python
info(age=20, name="Ali")
```

🟢 Natija:

```
Ali 20
```

👉 Tartib muhim emas bo‘ladi.

---

# 📚 9. Aralash parametrlar

```python
def info(name, age=18):
    print(name, age)
```

```python
info("Ali")
info("Vali", 25)
```

🟢 Natija:

```
Ali 18
Vali 25
```

---

# 📏 10. Ko‘p qiymat qaytarish

```python
def calc(a, b):
    return a+b, a*b
```

```python
s, k = calc(4, 5)
print(s, k)
```

🟢 Natija:

```
9 20
```

👉 Python tuple qaytaradi.

---

# 🧱 11. Funksiya ichida funksiya

```python
def outer():
    def inner():
        print("Ichki funksiya")
    inner()
```

```python
outer()
```

🟢 Natija:

```
Ichki funksiya
```

---

# 🧼 12. Toza funksiya yozish qoidalari

✔ Funksiya bitta vazifa bajarishi kerak
✔ Nomi aniq bo‘lsin (`calculate_total` yaxshi, `func1` yomon)
✔ Parametrlar ortiqcha bo‘lmasin
✔ Return ishlatish tavsiya etiladi
✔ Funksiya qisqa bo‘lsin

---

# 📄 13. Docstring bilan funksiya

Funksiya nima qilishini yozish.

```python
def add(a, b):
    """Ikki sonni qo‘shadi va natija qaytaradi"""
    return a + b
```

```python
help(add)
```

---
<br><br><br><br><br>

## 📞 CALLING FUNCTIONS (Funksiyani chaqirish)

Funksiyani yaratish — bu faqat uni yozish.
Ammo u **ishlashi uchun uni chaqirish kerak**.

👉 Funksiyani chaqirish — bu uning nomini yozib, qavs ochib yopishdir.

---

# 🧩 1. Eng oddiy chaqirish

```python
def greet():
    print("Salom!")
```

📞 chaqirish:

```python
greet()
```

🟢 Natija:

```
Salom!
```

👉 Qavs bo‘lmasa funksiya ishlamaydi.

```python
greet   # ❌ bu faqat funksiya obyektini ko‘rsatadi
greet() # ✅ bu uni ishga tushiradi
```

---

# 📥 2. Argument bilan chaqirish

Agar funksiya parametr olsa, chaqirishda qiymat berish kerak.

```python
def greet(name):
    print("Salom,", name)
```

```python
greet("Ali")
```

🟢 Natija:

```
Salom, Ali
```

👉 `"Ali"` — argument

---

# 📦 3. Bir nechta argumentlar bilan chaqirish

```python
def add(a, b):
    print(a + b)
```

```python
add(3, 5)
```

🟢 Natija:

```
8
```

👉 Argumentlar tartibi muhim.

```python
add(5, 3)  # boshqa natija bo‘lishi mumkin
```

---

# 🔑 4. Keyword bilan chaqirish

Argumentni nomi bilan uzatish mumkin.

```python
def info(name, age):
    print(name, age)
```

```python
info(age=20, name="Ali")
```

🟢 Natija:

```
Ali 20
```

👉 Tartib muhim emas.

---

# ⚙️ 5. Default parametrli funksiyani chaqirish

```python
def greet(name="Mehmon"):
    print("Salom,", name)
```

```python
greet()
greet("Ali")
```

🟢 Natija:

```
Salom, Mehmon
Salom, Ali
```

👉 Argument bermasak default ishlaydi.

---

# 🔁 6. Return qiymatni qabul qilib chaqirish

```python
def add(a, b):
    return a + b
```

```python
natija = add(4, 6)
print(natija)
```

🟢 Natija:

```
10
```

👉 Funksiya chaqirilganda qiymat qaytaradi.

---

# 📤 7. Return qiymatni bevosita ishlatish

```python
def add(a, b):
    return a + b
```

```python
print(add(3, 7))
```

🟢 Natija:

```
10
```

👉 Funksiya boshqa funksiya ichida ham chaqirilishi mumkin.

---

# 🧮 8. Funksiya ichida funksiya chaqirish

```python
def square(x):
    return x * x

def show(num):
    print(square(num))
```

```python
show(5)
```

🟢 Natija:

```
25
```

---

# 🔂 9. Bir nechta marta chaqirish

Funksiyani istalgancha marta ishlatish mumkin.

```python
def greet(name):
    print("Salom,", name)
```

```python
greet("Ali")
greet("Vali")
greet("Hasan")
```

🟢 Natija:

```
Salom, Ali
Salom, Vali
Salom, Hasan
```

👉 Bu funksiyaning eng katta foydasi — qayta ishlatish.

---

# 🧠 10. Funksiya chaqirilish jarayoni qanday ishlaydi?

1️⃣ Python funksiya nomini topadi
2️⃣ Argumentlarni parametrga joylaydi
3️⃣ Funksiya tanasini bajaradi
4️⃣ Agar `return` bo‘lsa qiymat qaytaradi
5️⃣ Funksiya tugaydi

---

# 🚫 11. Eng ko‘p uchraydigan xatolar

### ❌ Argument yetishmaydi

```python
def add(a, b):
    return a+b

add(5)  # xato
```

👉 Sabab: 2 ta parametr bor, 1 ta argument berildi.

---

### ❌ Ortib ketgan argument

```python
add(5, 3, 1)  # xato
```

👉 Funksiya faqat 2 ta parametr qabul qiladi.

---

### ❌ Qavs unutildi

```python
greet   # ishlamaydi
```

👉 Funksiya chaqirilmaydi.

---
<br><br><br><br><br>
## 📊 PARAMETERS vs ARGUMENTS

(*Parametrlar va Argumentlar farqi*)

Bu mavzu funksiyalarni tushunishda **eng muhim asoslardan biri**.
Ko‘pchilik yangi o‘rganuvchilar aynan shu joyda adashadi.

---

# 🧩 1. Eng qisqa ta’rif

* **Parameter** → funksiya yaratilganda yoziladigan o‘zgaruvchi
* **Argument** → funksiyani chaqirganda beriladigan haqiqiy qiymat

👉 Oddiy qilib:

```
Parameter = funksiya ichidagi o‘zgaruvchi
Argument  = funksiya chaqirilganda berilgan qiymat
```

---

# 🏗 2. Misol orqali tushunish

```python
def greet(name):   # name → PARAMETER
    print("Salom,", name)
```

```python
greet("Ali")       # "Ali" → ARGUMENT
```

👉 `name` — parametr
👉 `"Ali"` — argument

---

# 📦 3. Bir nechta parametr va argument

```python
def add(a, b):     # a, b → PARAMETER
    print(a + b)
```

```python
add(3, 5)          # 3, 5 → ARGUMENT
```

👉 `a` va `b` — parametr
👉 `3` va `5` — argument

---

# 🧠 4. Muhim qoida

📌 Parametrlar funksiya **yaratilganda** mavjud
📌 Argumentlar funksiya **chaqirilganda** paydo bo‘ladi

---

# 🔁 5. Bir parametr — turli argumentlar

```python
def square(x):
    print(x * x)
```

```python
square(2)
square(5)
square(10)
```

👉 `x` har doim parametr
👉 argument esa o‘zgarib boradi

---

# 🔑 6. Keyword argumentlar

Argumentni nomi bilan berish mumkin.

```python
def info(name, age):
    print(name, age)
```

```python
info(age=20, name="Ali")
```

👉 `name`, `age` → parametr
👉 `"Ali"`, `20` → argument

---

# ⚙️ 7. Default parametrlar bilan bog‘liqligi

```python
def greet(name="Mehmon"):  # default PARAMETER
    print("Salom,", name)
```

```python
greet()        # argument yo‘q → default ishladi
greet("Ali")   # argument bor → default bekor bo‘ldi
```

👉 Parametr default qiymatga ega bo‘lishi mumkin
👉 Argument esa ixtiyoriy beriladi

---

# 📏 8. Pozitsion argumentlar

```python
def subtract(a, b):
    print(a - b)
```

```python
subtract(10, 3)
```

👉 10 → `a` ga
👉 3 → `b` ga

Tartib muhim!

---

# 🚫 9. Xato misol

```python
def add(a, b):
    print(a + b)

add(5)   # ❌ argument yetishmaydi
```

👉 2 ta parametr bor, 1 ta argument berildi.

---

# 📊 10. Vizual jadval

| Holat              | Parametr    | Argument    |
| ------------------ | ----------- | ----------- |
| Funksiya yozish    | ✅ mavjud    | ❌ yo‘q      |
| Funksiya chaqirish | ❌ yo‘q      | ✅ mavjud    |
| Kod ichida         | o‘zgaruvchi | qiymat      |
| Qayerda yoziladi   | `def` da    | chaqirishda |

---

# 🧠 11. Real hayot analogiyasi

Funksiya — bu **retsept** 🍲
Parametr — retseptdagi bo‘sh joy
Argument — haqiqiy mahsulot

Masalan:

```
Retsept: "X ni qo‘sh"
Parametr: X
Argument: kartoshka
```

---
<br><br><br><br><br>


## 📤 RETURN VALUES (Funksiyadan qiymat qaytarish)

Funksiya faqat kod bajarib qo‘yishi mumkin…
yoki **natija qaytarishi ham mumkin**.

👉 Natija qaytarish uchun `return` ishlatiladi.

Bu — funksiyalarning eng muhim xususiyatlaridan biri.

---

# 🧩 1. `return` nima qiladi?

`return` funksiyani:

1️⃣ to‘xtatadi
2️⃣ qiymatni tashqariga chiqaradi
3️⃣ chaqirilgan joyga natija yuboradi

---

# 🏗 2. Eng sodda misol

```python
def add(a, b):
    return a + b
```

```python
x = add(3, 5)
print(x)
```

🟢 Natija:

```
8
```

👉 Funksiya hisoblab, natijani qaytardi.

---

# 🆚 3. `print` va `return` farqi

### ❌ print ishlatilsa

```python
def add(a, b):
    print(a + b)

x = add(3, 5)
print(x)
```

🟢 Natija:

```
8
None
```

👉 `print` faqat ekranga chiqaradi
👉 qiymat qaytarmaydi

---

### ✅ return ishlatilsa

```python
def add(a, b):
    return a + b
```

👉 qiymat qaytadi
👉 saqlash mumkin
👉 boshqa joyda ishlatish mumkin

---

# 📥 4. Return qiymatni ishlatish

```python
def square(x):
    return x * x
```

```python
print(square(4))
```

🟢 Natija:

```
16
```

---

# 🔁 5. Return boshqa funksiya ichida ishlatilishi

```python
def square(x):
    return x*x

def show(num):
    return square(num) + 10
```

```python
print(show(5))
```

🟢 Natija:

```
35
```

👉 Funksiyalar zanjir hosil qiladi.

---

# 🧮 6. Bir nechta qiymat qaytarish

Python bir nechta qiymatni tuple sifatida qaytaradi.

```python
def calc(a, b):
    return a+b, a*b
```

```python
s, k = calc(4, 5)
print(s, k)
```

🟢 Natija:

```
9 20
```

---

# 🚫 7. Return yozilmasa nima bo‘ladi?

```python
def test():
    pass

print(test())
```

🟢 Natija:

```
None
```

👉 Python avtomatik `None` qaytaradi.

---

# ⛔ 8. Return’dan keyingi kod ishlamaydi

```python
def test():
    return 5
    print("Hello")  # bu bajarilmaydi
```

👉 `return` funksiyani darhol tugatadi.

---

# 🔀 9. Shartli return

```python
def check(num):
    if num > 0:
        return "Musbat"
    else:
        return "Manfiy"
```

```python
print(check(5))
print(check(-2))
```

🟢 Natija:

```
Musbat
Manfiy
```

---

# 🧠 10. Return qachon ishlatiladi?

✔ Natija kerak bo‘lsa
✔ Hisob-kitob bo‘lsa
✔ Qiymatni saqlash kerak bo‘lsa
✔ Funksiyalarni bog‘lash kerak bo‘lsa

---

# 📊 11. Return ishlatiladigan real misol

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total
```

```python
summa = calculate_total(12000, 3)
print("Jami:", summa)
```

🟢 Natija:

```
Jami: 36000
```

---
<br><br><br><br><br>

## ⚙️ DEFAULT ARGUMENTS (Standart qiymatli parametrlar)

Ba’zan funksiya chaqirilganda argument berilmasligi mumkin.
Shunday holatlar uchun parametrga **oldindan qiymat berib qo‘yish** mumkin.

👉 Bu qiymat **default argument** deyiladi.

---

# 🧩 1. Asosiy sintaksis

```python
def function_name(parameter=default_value):
    ...
```

👉 Parametrga `=` orqali qiymat beriladi.

---

# 🏗 2. Eng sodda misol

```python
def greet(name="Mehmon"):
    print("Salom,", name)
```

```python
greet()
greet("Ali")
```

🟢 Natija:

```
Salom, Mehmon
Salom, Ali
```

👉 Argument bermasak default ishlaydi
👉 Bersak default o‘rniga yangi qiymat olinadi

---

# 📦 3. Bir nechta default parametrlar

```python
def power(base, exponent=2):
    print(base ** exponent)
```

```python
power(5)
power(5, 3)
```

🟢 Natija:

```
25
125
```

👉 Default qiymat ko‘pincha **eng odatiy holat** uchun beriladi.

---

# 🧠 4. Default argument qanday ishlaydi?

1️⃣ Funksiya yaratilganda default qiymat saqlanadi
2️⃣ Chaqirilganda argument tekshiriladi
3️⃣ Agar argument bo‘lmasa → default ishlaydi
4️⃣ Agar argument bo‘lsa → default e’tiborga olinmaydi

---

# 🔑 5. Default parametrlar tartibi (MUHIM!)

👉 Default parametrlar **oddiy parametrdan keyin yoziladi**

### ❌ noto‘g‘ri

```python
def func(a=5, b):
    pass
```

👉 xato beradi

---

### ✅ to‘g‘ri

```python
def func(a, b=5):
    pass
```

👉 Har doim:

```
oddiy parametr → default parametr
```

---

# 📥 6. Keyword bilan ishlatish

```python
def info(name, age=18, city="Toshkent"):
    print(name, age, city)
```

```python
info("Ali")
info("Ali", 25)
info("Ali", city="Samarqand")
```

🟢 Natija:

```
Ali 18 Toshkent
Ali 25 Toshkent
Ali 18 Samarqand
```

👉 Istalgan default parametrni alohida o‘zgartirish mumkin.

---

# 🔁 7. Default argumentlar qayta ishlatiladi

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst
```

```python
print(add_item(1))
print(add_item(2))
```

🟢 Natija:

```
[1]
[1, 2]
```

👉 Sabab: default list **bir marta yaratiladi** va saqlanadi.

---

# 🛑 8. Mutable default argument muammosi

List, dict, set kabi o‘zgaruvchan turlar default bo‘lsa ehtiyot bo‘lish kerak.

### ❌ xavfli usul

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst
```

---

### ✅ to‘g‘ri usul

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

👉 Bu professional Python’da **eng muhim qoidalardan biri**.

---

# 🧾 9. Default argumentlar qachon ishlatiladi?

✔ Parametr ko‘pincha bir xil qiymatga ega bo‘lsa
✔ Funksiyani chaqirishni osonlashtirish uchun
✔ Optional parametrlar uchun
✔ API va kutubxona yozishda

---
<br><br><br><br><br>
## 🔑 KEYWORD ARGUMENTS (Nom bilan uzatiladigan argumentlar)

Funksiyani chaqirganda argumentlarni faqat tartib bilan emas,
**parametr nomi orqali ham uzatish mumkin**.

👉 Bu usul **keyword arguments** deyiladi.

---

# 🧩 1. Asosiy g‘oya

Oddiy chaqirish (pozitsion):

```python
def info(name, age):
    print(name, age)

info("Ali", 20)
```

👉 `"Ali"` → `name`
👉 `20` → `age`

---

### 🔑 Keyword bilan chaqirish

```python
info(age=20, name="Ali")
```

🟢 Natija bir xil:

```
Ali 20
```

👉 Endi tartib muhim emas
👉 Muhimi — nom to‘g‘ri yozilishi

---

# 🏗 2. Keyword arguments sintaksisi

```python
function(parameter=value)
```

Masalan:

```python
print(sep="-", end="!")
```

👉 Bu ham keyword argument ishlatilishi.

---

# 📦 3. Aralash chaqirish (pozitsion + keyword)

```python
def person(name, age, city):
    print(name, age, city)
```

```python
person("Ali", age=20, city="Toshkent")
```

🟢 Natija:

```
Ali 20 Toshkent
```

👉 Pozitsion argumentlar avval yoziladi
👉 Keyin keywordlar keladi

---

# 🚫 4. Xato tartib

```python
person(name="Ali", 20, "Toshkent")
```

👉 Bu xato beradi

📌 Qoida:

```
pozitsion → keyword
```

aksincha bo‘lmaydi.

---

# ⚙️ 5. Default parametrlar bilan juda yaxshi ishlaydi

```python
def info(name, age=18, city="Toshkent"):
    print(name, age, city)
```

```python
info("Ali", city="Samarqand")
```

🟢 Natija:

```
Ali 18 Samarqand
```

👉 Faqat kerakli parametrni o‘zgartirdik
👉 Qolganlari default qoldi

---

# 🧠 6. Keyword arguments qachon ishlatiladi?

✔ Parametrlar ko‘p bo‘lsa
✔ Funksiya aniq o‘qilsin desa
✔ Default parametrlar bo‘lsa
✔ API / library yozishda

Masalan:

```python
create_user(name="Ali", age=20, is_admin=True)
```

👉 Bu juda tushunarli ko‘rinadi.

---

# 📊 7. Pozitsion vs Keyword

| Usul      | Afzalligi              | Kamchiligi          |
| --------- | ---------------------- | ------------------- |
| Pozitsion | qisqa yoziladi         | chalkashishi mumkin |
| Keyword   | aniq va o‘qilishi oson | biroz uzunroq       |

---

# 🧾 8. Real misol

```python
def order(product, quantity, price, discount=0):
    total = quantity * price - discount
    print(product, "=", total)
```

```python
order("Laptop", price=1000, quantity=2, discount=100)
```

🟢 Natija:

```
Laptop = 1900
```

👉 Tartib muhim bo‘lmadi
👉 Kod o‘qilishi yaxshilandi

---
## 📏 VARIABLE-LENGTH ARGUMENTS (`*args`, `**kwargs`)

Ba’zan funksiya nechta argument olishini oldindan bilmaymiz.
Shunda Python bizga **o‘zgaruvchan uzunlikdagi argumentlar** beradi.

👉 2 xil turi bor:

* `*args` → cheksiz pozitsion argumentlar
* `**kwargs` → cheksiz keyword argumentlar

---

# 🧩 1. `*args` nima?

`*args` funksiyaga kelgan **barcha ortiqcha pozitsion argumentlarni tuple sifatida** yig‘adi.

---

### 🏗 Misol

```python
def numbers(*args):
    print(args)
```

```python
numbers(1, 2, 3, 4)
```

🟢 Natija:

```
(1, 2, 3, 4)
```

👉 `args` — tuple bo‘ladi
👉 ichida barcha argumentlar saqlanadi

---

# 📦 2. `*args` bilan hisoblash

```python
def total(*nums):
    return sum(nums)
```

```python
print(total(1, 2, 3))
print(total(5, 10, 15, 20))
```

🟢 Natija:

```
6
50
```

👉 Argumentlar soni cheklanmagan

---

# 🧠 3. `*args` nomi majburiy emas

```python
def test(*numbers):
    print(numbers)
```

👉 `*` muhim, nom ixtiyoriy.

---

# 🔑 4. `**kwargs` nima?

`**kwargs` funksiyaga kelgan **barcha keyword argumentlarni dict sifatida** yig‘adi.

---

### 🏗 Misol

```python
def info(**kwargs):
    print(kwargs)
```

```python
info(name="Ali", age=20, city="Toshkent")
```

🟢 Natija:

```
{'name': 'Ali', 'age': 20, 'city': 'Toshkent'}
```

👉 `kwargs` — dictionary bo‘ladi

---

# 📊 5. `**kwargs` bilan ishlash

```python
def show(**data):
    for key, value in data.items():
        print(key, "=", value)
```

```python
show(name="Ali", age=20)
```

🟢 Natija:

```
name = Ali
age = 20
```

---

# 🔁 6. `*args` va `**kwargs` birga

```python
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
```

```python
demo(1, 2, 3, name="Ali", age=20)
```

🟢 Natija:

```
Args: (1, 2, 3)
Kwargs: {'name': 'Ali', 'age': 20}
```

---

# 📏 7. Parametrlar tartibi (MUHIM!)

Funksiya yozishda tartib qat’iy:

```
oddiy parametrlar
→ *args
→ default parametrlar
→ **kwargs
```

---

### ✅ To‘g‘ri misol

```python
def func(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)
```

---

### ❌ Noto‘g‘ri

```python
def func(**kwargs, *args):
    pass
```

👉 Python xato beradi.

---

# 🧠 8. Qachon ishlatiladi?

✔ Argumentlar soni noma’lum bo‘lsa
✔ Universal funksiyalar yozishda
✔ Wrapper funksiyalar
✔ Framework / kutubxona yozishda
✔ Config parametrlar yig‘ishda

---

# 📦 9. Real hayot misoli

```python
def order(product, *extras, **details):
    print("Product:", product)
    print("Extras:", extras)
    print("Details:", details)
```

```python
order("Pizza", "Cheese", "Sauce", size="Large", price=12)
```

🟢 Natija:

```
Product: Pizza
Extras: ('Cheese', 'Sauce')
Details: {'size': 'Large', 'price': 12}
```

---
<br> <br> <br> <br> <br>

## 🌐 SCOPE RULES (O‘zgaruvchilar ko‘rinish doirasi)

**Scope** — bu o‘zgaruvchi qayerda mavjudligi va qayerdan foydalanish mumkinligini bildiradi.

👉 Oddiy qilib:

> O‘zgaruvchi qaysi joyda “ko‘rinadi” — shu uning scope’i.

Python’da bu qoidalar funksiyalarni tushunishda **juda muhim**.

---

# 🧩 1. Scope nima uchun kerak?

Scope:

* 🛡 o‘zgaruvchilar to‘qnashuvini oldini oladi
* 🧠 kodni tartibli qiladi
* 📦 funksiyalarni mustaqil qiladi
* 🔒 global o‘zgaruvchilarni cheklaydi

---

# 🏠 2. Local scope (mahalliy scope)

Funksiya ichida yaratilgan o‘zgaruvchi **faqat shu funksiya ichida mavjud**.

```python
def test():
    x = 10
    print(x)
```

```python
test()
print(x)   # xato
```

👉 `x` faqat funksiya ichida yashaydi
👉 tashqaridan ko‘rinmaydi

---

# 🌍 3. Global scope

Funksiya tashqarisida yaratilgan o‘zgaruvchi — global.

```python
x = 10

def show():
    print(x)

show()
```

🟢 Natija:

```
10
```

👉 Global o‘zgaruvchini funksiya ichida o‘qish mumkin.

---

# ⚠️ 4. Globalni o‘zgartirish muammosi

```python
x = 10

def change():
    x = 5
    print(x)

change()
print(x)
```

🟢 Natija:

```
5
10
```

👉 Funksiya ichida yangi local `x` yaratildi
👉 global o‘zgarmadi

---

# 🔑 5. Globalni o‘zgartirish (`global` kalit so‘zi)

```python
x = 10

def change():
    global x
    x = 5
```

```python
change()
print(x)
```

🟢 Natija:

```
5
```

👉 `global` — tashqi o‘zgaruvchini o‘zgartirishga ruxsat beradi.

---

# 🧠 6. Scope darajalari

Python’da 4 xil scope bor.

Bu **LEGB qoidasiga** kiradi.

---

# 🔢 7. LEGB qoidasi

Python o‘zgaruvchini qidirishda quyidagi tartibni ishlatadi:

```
L → Local
E → Enclosing
G → Global
B → Built-in
```

---

## 📍 L — Local

Funksiya ichidagi o‘zgaruvchi.

```python
def f():
    x = 5
    print(x)
```

---

## 📍 E — Enclosing

Ichma-ich funksiyalar scope’i.

```python
def outer():
    x = 10
    def inner():
        print(x)
    inner()
```

👉 `inner` tashqi funksiyadan o‘zgaruvchi oldi.

---

## 📍 G — Global

Fayl darajasidagi o‘zgaruvchi.

```python
x = 100
```

---

## 📍 B — Built-in

Python’ning ichki funksiyalari.

```python
print(len("hello"))
```

👉 `len`, `print` — built-in scope’da.

---

# 🔁 8. LEGB ishlash tartibi

Python o‘zgaruvchini qidiradi:

1️⃣ Local’da
2️⃣ Enclosing’da
3️⃣ Global’da
4️⃣ Built-in’da

Topilmasa → **NameError**

---

# 🚫 9. Xato misol

```python
def test():
    print(x)

test()
```

👉 Agar `x` globalda ham yo‘q bo‘lsa → xato

---
<br> <br> <br> <br> <br>

## 🏠 LOCAL vs GLOBAL SCOPE

Python’da o‘zgaruvchilar **qayerda yaratilgani** ularning scope’ini belgilaydi.
Bu **Local** va **Global** scope farqi orqali tushuniladi.

---

# 🧩 1. Global scope (Global o‘zgaruvchilar)

Global o‘zgaruvchi **funksiya tashqarisida yaratiladi** va fayl bo‘ylab mavjud bo‘ladi.

```python
x = 100  # global

def show():
    print(x)  # globalni o‘qiyapmiz

show()
print(x)    # global ham ko‘rinadi
```

🟢 Natija:

```
100
100
```

👉 Global o‘zgaruvchi **o‘qilishi mumkin**, lekin **o‘zgartirish uchun `global` kerak**.

---

# ⚡ 2. Local scope (Mahalliy o‘zgaruvchilar)

Local o‘zgaruvchi **faqat funksiya ichida yaratiladi**.

```python
def test():
    y = 50  # local
    print(y)

test()
# print(y)  # ❌ xato, y local
```

🟢 Natija:

```
50
```

👉 Tashqaridan local o‘zgaruvchiga kira olmaysiz.

---

# 🔑 3. Globalni local ichida o‘qish

Funksiya ichida global o‘zgaruvchini o‘qish mumkin:

```python
x = 10

def read():
    print(x)  # globalni o‘qiyapmiz

read()
```

🟢 Natija:

```
10
```

---

# ⚙️ 4. Local o‘zgaruvchi globalni “yopadi”

Agar local bilan global bir nomda bo‘lsa:

```python
x = 10  # global

def test():
    x = 5  # local
    print(x)

test()
print(x)  # global qoladi
```

🟢 Natija:

```
5
10
```

👉 Local x globalni “shadow” qiladi, lekin globalni o‘zgartirmaydi.

---

# 🔄 5. Globalni local ichida o‘zgartirish

```python
x = 10

def change():
    global x
    x = 50

change()
print(x)
```

🟢 Natija:

```
50
```

👉 `global` kalit so‘zi bilan global qiymat o‘zgartiriladi.

---

# 🧮 6. Enclosing + local + global misol

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)

outer()
print(x)
```

🟢 Natija:

```
local
enclosing
global
```

👉 Python **LEGB qoidasiga** amal qiladi:

* `L` → inner local
* `E` → enclosing (outer)
* `G` → global
* `B` → built-in

---

# ⚠️ 7. Local va Global bilan common xatolar

### ❌ Local bilan globalni chalkashtirish

```python
x = 10

def f():
    x += 5  # x local deb qabul qilinadi
    print(x)

f()  # ❌ UnboundLocalError
```

👉 Sabab: Python local x yaratadi, lekin qiymat berilmagan.

### ✅ To‘g‘ri

```python
x = 10

def f():
    global x
    x += 5
    print(x)

f()
```

🟢 Natija:

```
15
```

---

<br> <br> <br> <br> <br>

## 🔢 LEGB RULE (Python’da o‘zgaruvchilar qidirish tartibi)

Python o‘zgaruvchini **qayerdan olishini aniqlash uchun** **LEGB qoidasini** ishlatadi.

LEGB — bu qisqartma:

```
L → Local
E → Enclosing
G → Global
B → Built-in
```

---

# 🧩 1. L — Local Scope (Mahalliy)

Funksiya ichida yaratilgan o‘zgaruvchilar **local** hisoblanadi.

```python
def f():
    x = 10  # local
    print(x)

f()
```

🟢 Natija:

```
10
```

* Faqat funksiya ichida mavjud
* Tashqaridan ko‘rinmaydi

---

# 🏗 2. E — Enclosing Scope (Tashqi funksiya)

Ichma-ich funksiyalarda tashqi funksiya scope’i **enclosing** deyiladi.

```python
def outer():
    x = 20  # enclosing
    def inner():
        print(x)  # enclosing x ga murojaat
    inner()

outer()
```

🟢 Natija:

```
20
```

* `inner()` ichida `x` topilmadi → `outer()` dan oldi

---

# 🌍 3. G — Global Scope

Fayl bo‘yicha yuqorida yaratilgan o‘zgaruvchilar **global** hisoblanadi.

```python
x = 30  # global

def show():
    print(x)  # global x ga murojaat

show()
```

🟢 Natija:

```
30
```

* Funksiya ichida o‘qish mumkin
* O‘zgartirish uchun `global` kerak

---

# 🏛 4. B — Built-in Scope

Python ichidagi oldindan belgilangan funksiyalar va o‘zgaruvchilar.

```python
print(len("hello"))  # len → built-in
```

* `len`, `max`, `min` va boshqalar
* Eng oxirgi qidiruv manbai

---

# 🔁 5. LEGB tartibi

O‘zgaruvchini qidirish tartibi:

1️⃣ **L** → Local (funksiya ichida)
2️⃣ **E** → Enclosing (tashqi funksiya ichida)
3️⃣ **G** → Global (fayl darajasida)
4️⃣ **B** → Built-in (Python’ning ichki funksiyalari)

📌 Topilmasa → `NameError`

---

# 🧮 6. Misol: barcha scope

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local
    inner()
    print(x)      # enclosing

outer()
print(x)          # global
```

🟢 Natija:

```
local
enclosing
global
```

* Python **LEGB tartibida** qidiradi
* Har bir scope topilsa, qidirishni to‘xtatadi

---

# ⚠️ 7. LEGB bilan `nonlocal` va `global`

* **nonlocal** → enclosing scope o‘zgaruvchisini o‘zgartiradi
* **global** → global scope o‘zgaruvchisini o‘zgartiradi

```python
x = 0

def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
    inner()
    print(x)

outer()  # 2
print(x) # 0
```

---

<br> <br> <br> <br> <br>

## 📄 DOCSTRINGS (Funksiya, klass va modul uchun hujjat yozish)

**Docstring** — bu funksiya, klass yoki modulning nima qilishini tushuntiruvchi **matnli hujjat**.

Python’da **uchta qo‘shtirnoq (`""" ... """`)** bilan yoziladi.

---

# 🧩 1. Asosiy sintaksis

```python
def funksiya(param1, param2):
    """Funksiya nima qilishini tushuntiradi."""
    return param1 + param2
```

👉 Docstring ixtiyoriy, lekin tavsiya etiladi

---

# 🏗 2. Docstringni chaqirish

```python
def greet(name):
    """Berilgan ism bilan salomlashadi."""
    print("Salom,", name)
```

```python
print(greet.__doc__)
```

🟢 Natija:

```
Berilgan ism bilan salomlashadi.
```

---

# 📚 3. Ko‘p qatorli docstring

```python
def add(a, b):
    """
    Ikki sonni qabul qiladi va ularni qo‘shadi.
    
    Parametrlar:
    a (int): Birinchi son
    b (int): Ikkinchi son
    
    Return:
    int: Qo‘shilgan natija
    """
    return a + b
```

📞 `help(add)` yordamida ham ko‘rish mumkin

---

# 🔑 4. Docstring afzalliklari

* 📖 Kod o‘qilishi osonlashadi
* 🛠 Katta loyihalarda tushunishni osonlashtiradi
* 🔍 `help()` yordamida tez hujjat olish mumkin
* 🧩 API va kutubxona yozishda zarur

---

# ⚙️ 5. Klass va modul docstring

### Klass uchun

```python
class Person:
    """Shaxs haqida ma’lumot saqlovchi klass."""
    def __init__(self, name):
        self.name = name
```

### Modul uchun

```python
"""
Bu modul matematik funksiyalarni o‘z ichiga oladi.
"""
def multiply(a, b):
    return a * b
```

---

# 🧠 6. Qoidalar

✔ Har doim uchta qo‘shtirnoq ichida yozing
✔ Qisqa, tushunarli bo‘lsin
✔ Parametrlar va return qiymatlarini izohlash tavsiya etiladi
✔ Funksiya qaysi vazifani bajarishini aytib o‘ting

---

# 🧾 7. Misol: professional docstring

```python
def calculate_total(price, quantity):
    """
    Mahsulot narxi va soni asosida jami summani hisoblaydi.
    
    Parametrlar:
    price (float): Mahsulot narxi
    quantity (int): Mahsulot soni
    
    Return:
    float: Jami summa
    """
    return price * quantity
```

📞 `help(calculate_total)` orqali ko‘rish mumkin

---

<br> <br> <br> <br> <br>

## ✨ CLEAN FUNCTION DESIGN (Toza va samarali funksiyalar yozish)

Toza funksiyalar — bu **o‘qilishi oson, qayta ishlatiladigan va xatolikka kamlik qiladigan funksiyalar**.
Python’da bu eng muhim dasturlash printsiplaridan biridir.

---

# 🧩 1. Bir vazifa — bir funksiya

Funksiya **faqat bitta vazifani bajarishi kerak**.

```python
# ❌ noto‘g‘ri
def process_data(data):
    clean_data(data)
    save_to_file(data)
    print("Done")

# ✅ to‘g‘ri
def clean_data(data):
    # tozalash
    return data

def save_to_file(data):
    # saqlash
    pass

def main():
    data = load_data()
    clean = clean_data(data)
    save_to_file(clean)
```

* Har bir funksiya **aniq vazifa bajaradi**
* Qayta ishlatish osonlashadi

---

# 📏 2. Parametrlarni aniqlik bilan belgilash

* Minimal sonli parametrlar
* Default va keyword argumentlardan oqilona foydalanish

```python
def greet(name, greeting="Salom"):
    print(f"{greeting}, {name}")
```

* Funksiya chaqirishda **aniq ma’lumot** beriladi
* Kerak bo‘lsa default ishlaydi

---

# 🧠 3. Return qiymatdan foydalanish

* Funksiya natijani **qaytarishi** kerak, aks holda u faqat yon effekt qiladi (`print` bilan cheklanadi)
* Natija boshqa funksiya yoki kodda ishlatilishi mumkin

```python
def add(a, b):
    return a + b

result = add(5, 7)
print(result)
```

---

# 🔄 4. Qayta ishlatish va modulga bo‘lish

* Funksiyani **bir marta yozib**, bir nechta joyda ishlatish
* Katta kodni **modullarga ajratish**

```python
# utils.py
def square(x):
    return x * x

# main.py
from utils import square
print(square(5))
```

---

# 🛠 5. Docstring va nomlash

* **Funksiya nomi** vazifani tushuntirishi kerak
* **Docstring** bilan qisqacha izoh yozish

```python
def calculate_total(price, quantity):
    """Mahsulot narxi va sonidan jami summani hisoblaydi."""
    return price * quantity
```

---

# ⚡ 6. Katta funksiyani bo‘laklarga ajratish

* 50 qatordan uzun funksiyalar qiyin o‘qiladi
* Ichki yordamchi funksiyalar bilan **bo‘lish**

```python
def process_order(order):
    validated = validate(order)
    total = calculate_total(validated)
    save_order(validated, total)
```

---

# ✅ 7. Qoidalar xulosasi

1️⃣ **Bitta vazifa** bajarilsin

2️⃣ **Nom va parametrlar aniq** bo‘lsin

3️⃣ **Natija qaytarilsin** (`return`)

4️⃣ **Docstring** bo‘lsin

5️⃣ **Qisqa va qayta ishlatiladigan** bo‘lsin

6️⃣ **Global o‘zgaruvchilardan imkon qadar uzoqroq** bo‘lsin

---

# 🧾 8. Misol: Clean function design

```python
def read_file(path):
    """Fayldan matnni o‘qiydi va qaytaradi."""
    with open(path, "r") as file:
        return file.read()

def count_words(text):
    """Matndagi so‘zlar sonini hisoblaydi."""
    return len(text.split())

def main():
    text = read_file("data.txt")
    total = count_words(text)
    print("So‘zlar soni:", total)

main()
```

* Har bir funksiya **aniq vazifa** bajaradi
* Kod o‘qilishi va tushunilishi oson

---