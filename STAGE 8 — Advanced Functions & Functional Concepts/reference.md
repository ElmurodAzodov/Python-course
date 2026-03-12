# **STAGE 8 — Advanced Functions & Functional Concepts**

<br>
<br>

# ⭐ Functions as First-Class Objects — Python’da Funksiyalar obyekt sifatida

Python’da **funksiyalar oddiy obyektlar kabi ishlaydi**.
Bu degani funksiyalarni:

* 📦 o‘zgaruvchiga **saqlash**
* 📤 boshqa funksiyaga **argument sifatida uzatish**
* 📥 funksiya ichidan **qaytarish**

mumkin.

> **First-Class Object** — dasturda oddiy qiymat (int, str, list) kabi ishlatilishi mumkin bo‘lgan obyekt.

Python’da **funksiyalar ham first-class object** hisoblanadi.

---

# 🎯 1. Funksiyani o‘zgaruvchiga saqlash (Assign)

Funksiyani **o‘zgaruvchiga assign qilish** mumkin.

### Misol

```python
def greet(name):
    return f"Salom {name}"
```

Endi funksiyani o‘zgaruvchiga beramiz:

```python
say_hello = greet
```

Chaqarish:

```python
print(say_hello("Ali"))
```

Natija

```
Salom Ali
```

📌 Muhim:

```python
say_hello = greet
```

bu yerda **()` ishlatilmaydi`**, chunki biz **funksiyani chaqirmayapmiz**, balki **reference ni saqlayapmiz**.

---

# 🧠 2. Funksiya obyekt ekanini tekshirish

Funksiya ham obyekt bo‘lgani uchun uni tekshirish mumkin.

```python
def add(a, b):
    return a + b
```

```python
print(type(add))
```

Natija:

```
<class 'function'>
```

Demak **funksiya ham obyekt**.

---

# 📦 3. Funksiyani list yoki dict ichida saqlash

Funksiyalar **data structure ichida ham saqlanishi mumkin**.

### Misol

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

List ichida:

```python
operations = [add, multiply]

print(operations[0](2, 3))
print(operations[1](2, 3))
```

Natija

```
5
6
```

---

# 📤 4. Funksiyani argument sifatida uzatish (Pass)

Funksiyani boshqa funksiyaga **argument sifatida berish mumkin**.

### Misol

```python
def greet(name):
    return f"Salom {name}"
```

```python
def execute(func, value):
    return func(value)
```

Chaqarish:

```python
print(execute(greet, "Ali"))
```

Natija

```
Salom Ali
```

📌 Jarayon

```
execute(greet, "Ali")

func = greet
value = "Ali"

→ greet("Ali")
```

---

# 🔁 5. Real misol (callback function)

Funksiyani argument sifatida berish **callback** deyiladi.

```python
def square(x):
    return x * x
```

```python
def process_number(func, number):
    return func(number)
```

Chaqarish:

```python
print(process_number(square, 5))
```

Natija

```
25
```

Bu pattern **map, filter, sorting** kabi joylarda ishlatiladi.

---

# 📥 6. Funksiya ichidan funksiya qaytarish (Return)

Funksiya boshqa funksiyani **return** qilishi mumkin.

### Misol

```python
def get_greeter():
    
    def greet(name):
        return f"Salom {name}"
    
    return greet
```

Chaqarish:

```python
greeter = get_greeter()

print(greeter("Ali"))
```

Natija

```
Salom Ali
```

📌 Jarayon

```
get_greeter()
   ↓
return greet
   ↓
greeter = greet
```

---

# 🧩 7. Funksiya yaratish factory pattern

Bu usul **function factory** deyiladi.

```python
def power_factory(exponent):

    def power(number):
        return number ** exponent

    return power
```

Chaqarish:

```python
square = power_factory(2)
cube = power_factory(3)

print(square(4))
print(cube(4))
```

Natija

```
16
64
```

📌 Mapping

```
square → exponent = 2
cube → exponent = 3
```

---

# 🔗 8. Funksiya reference vs funksiya chaqirish

### Reference

```python
func = greet
```

Bu **funksiya manzilini saqlaydi**.

### Call

```python
func = greet()
```

Bu **funksiyani ishlatadi**.

---

# 🏗 9. Real mini dastur (dynamic behavior)

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

```python
def calculate(operation, a, b):
    return operation(a, b)
```

Chaqarish

```python
print(calculate(add, 3, 4))
print(calculate(multiply, 3, 4))
```

Natija

```
7
12
```

📌 Bu **Strategy Pattern** ga o‘xshaydi.

---

# 📊 10. First-Class Object xususiyatlari

Python’da funksiya:

| Xususiyat                     | Misol             |
| ----------------------------- | ----------------- |
| o‘zgaruvchiga assign qilish   | `f = greet`       |
| argument sifatida berish      | `execute(greet)`  |
| return qilish                 | `return greet`    |
| data structure ichida saqlash | `[add, multiply]` |

---

<br>
<br>
<br>
<br>
<br>

# λ Lambda Functions — Anonymous Functions (single expression)

Python’da **lambda function** bu **nomi bo‘lmagan (anonymous)** kichik funksiyadir.
U odatda **bitta ifoda (single expression)** dan iborat bo‘ladi.

> Lambda → tez va qisqa funksiya yozish uchun ishlatiladi.

---

# 🎯 1. Lambda sintaksisi

Oddiy funksiya:

```python
def add(a, b):
    return a + b
```

Lambda versiyasi:

```python
lambda a, b: a + b
```

📌 Sintaksis

```
lambda argumentlar : expression
```

* `lambda` → funksiya yaratadi
* `argumentlar` → parametrlar
* `expression` → natija (return avtomatik)

Lambda’da **return yozilmaydi**.

---

# 🧠 2. Oddiy lambda misol

```python
add = lambda a, b: a + b

print(add(2, 3))
```

Natija

```
5
```

Bu aslida quyidagiga teng:

```python
def add(a, b):
    return a + b
```

---

# ⚡ 3. Lambda — bir qatorli funksiya

Lambda **faqat bitta expression** ishlatadi.

✔ To‘g‘ri

```python
square = lambda x: x * x
print(square(5))
```

Natija

```
25
```

❌ Noto‘g‘ri

```python
lambda x:
    y = x * 2
    return y
```

Lambda’da:

* assignment
* ko‘p qatorli kod
* `return`

bo‘lmaydi.

---

# 📦 4. Lambda funksiyani argument sifatida berish

Lambda ko‘pincha boshqa funksiyalarga **argument sifatida beriladi**.

```python
def apply(func, value):
    return func(value)
```

Lambda bilan:

```python
result = apply(lambda x: x * 2, 5)

print(result)
```

Natija

```
10
```

---

# 🔁 5. Lambda bilan `sorted()`

Lambda ko‘pincha **sorting key** sifatida ishlatiladi.

```python
students = [
    ("Ali", 90),
    ("Vali", 75),
    ("Hasan", 85)
]
```

Ball bo‘yicha sort qilish:

```python
students.sort(key=lambda student: student[1])

print(students)
```

Natija

```
[('Vali', 75), ('Hasan', 85), ('Ali', 90)]
```

Bu yerda:

```
lambda student: student[1]
```

→ har bir studentdan **score ni oladi**.

---

# 🧩 6. Lambda bilan `map()`

Lambda **transformatsiya** uchun ishlatiladi.

```python
numbers = [1, 2, 3, 4]
```

Har bir sonni kvadrat qilish:

```python
result = list(map(lambda x: x * x, numbers))

print(result)
```

Natija

```
[1, 4, 9, 16]
```

---

# 🔍 7. Lambda bilan `filter()`

Filter **shart bo‘yicha tanlash** uchun ishlatiladi.

```python
numbers = [1,2,3,4,5,6]
```

Faqat juft sonlar:

```python
result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

Natija

```
[2, 4, 6]
```

---

# 🏗 8. Real misol

Userlar ro‘yxati:

```python
users = [
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 17},
    {"name": "Hasan", "age": 25}
]
```

Yoshi bo‘yicha sort:

```python
users.sort(key=lambda user: user["age"])

print(users)
```

Natija

```
[
 {'name': 'Vali', 'age': 17},
 {'name': 'Ali', 'age': 20},
 {'name': 'Hasan', 'age': 25}
]
```

---

# 📊 9. Lambda vs normal function

| Oddiy funksiya                   | Lambda                   |
| -------------------------------- | ------------------------ |
| `def` bilan yoziladi             | `lambda` bilan           |
| bir nechta qator bo‘lishi mumkin | faqat 1 expression       |
| return yoziladi                  | return avtomatik         |
| katta funksiyalar uchun          | kichik funksiyalar uchun |

Misol

```python
def square(x):
    return x * x
```

Lambda:

```python
lambda x: x * x
```

---

# 📌 10. Lambda qachon ishlatiladi

Lambda odatda ishlatiladi:

✔ `map()`
✔ `filter()`
✔ `sorted()`
✔ `min()` / `max()`
✔ callback funksiyalar

Katta funksiyalar uchun **def ishlatiladi**.

---

<br>
<br>
<br>
<br>
<br>

# 🗺️ `map()` — Iterable elementlarini transform qilish

Python’da **`map()`** funksiyasi iterable (list, tuple, set va hokazo) ichidagi **har bir elementga funksiya qo‘llab yangi qiymatlar yaratadi**.

> `map()` → har bir elementni **o‘zgartirib (transform)** yangi iterable qaytaradi.

---

# 🎯 1. `map()` sintaksisi

```python
map(function, iterable)
```

📌 Parametrlar

* **function** → har bir elementga qo‘llanadigan funksiya
* **iterable** → list, tuple, set va hokazo

`map()` natijada **map object** qaytaradi, shuning uchun odatda `list()` bilan o‘giriladi.

---

# 🧠 2. Oddiy misol

List ichidagi sonlarni **kvadrat qilish**.

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))
```

Natija

```
[1, 4, 9, 16]
```

📌 Jarayon

```
square(1) → 1
square(2) → 4
square(3) → 9
square(4) → 16
```

---

# ⚡ 3. `map()` + lambda

Ko‘pincha `map()` bilan **lambda function** ishlatiladi.

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * x, numbers))

print(result)
```

Natija

```
[1, 4, 9, 16]
```

Bu eng ko‘p ishlatiladigan pattern.

---

# 📦 4. Stringlarni transform qilish

Har bir ismni **katta harfga** o‘tkazish.

```python
names = ["ali", "vali", "hasan"]

result = list(map(str.upper, names))

print(result)
```

Natija

```
['ALI', 'VALI', 'HASAN']
```

Bu yerda funksiya sifatida **`str.upper`** ishlatilgan.

---

# 🔁 5. Ikki iterable bilan `map()`

`map()` bir nechta iterable bilan ham ishlaydi.

```python
def add(a, b):
    return a + b

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

result = list(map(add, nums1, nums2))

print(result)
```

Natija

```
[5, 7, 9]
```

📌 Jarayon

```
add(1,4)
add(2,5)
add(3,6)
```

---

# 🧩 6. Real misol

Mahsulot narxlarini **10% oshirish**.

```python
prices = [100, 200, 300]
```

```python
new_prices = list(map(lambda p: p * 1.1, prices))

print(new_prices)
```

Natija

```
[110.0, 220.0, 330.0]
```

---

# 🏗 7. `map()` vs for loop

### `for` loop bilan

```python
numbers = [1,2,3,4]

result = []

for n in numbers:
    result.append(n*n)

print(result)
```

Natija

```
[1,4,9,16]
```

---

### `map()` bilan

```python
numbers = [1,2,3,4]

result = list(map(lambda x: x*x, numbers))

print(result)
```

Natija

```
[1,4,9,16]
```

📌 `map()` **qisqaroq va functional style**.

---

# 📊 8. `map()` qachon ishlatiladi

`map()` ishlatiladi:

✔ list elementlarini transform qilish
✔ matematik operatsiyalar
✔ string transformatsiya
✔ functional programming

---

# 📌 9. Muhim eslatma

`map()` natijasi **iterator** bo‘ladi.

```python
numbers = [1,2,3]

result = map(lambda x: x*2, numbers)

print(result)
```

Natija

```
<map object at 0x...>
```

Shuning uchun:

```python
print(list(result))
```

---

<br>
<br>
<br>
<br>
<br>

