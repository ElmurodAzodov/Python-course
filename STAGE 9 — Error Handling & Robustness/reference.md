# **STAGE 9 — Error Handling & Robustness**

<br>
<br>

# ❌ Syntax Errors vs ⚠️ Runtime Errors (Python)

Python dasturlarida xatolar asosan **ikki turga** bo‘linadi:

1️⃣ **Syntax Errors** – kod yozish qoidalari buzilganda yuz beradi
2️⃣ **Runtime Errors (Exceptions)** – dastur ishlayotgan paytda yuz beradi

Ularni tushunish **robust (barqaror) dasturlar** yozish uchun juda muhim.

---

# ❌ Syntax Errors (Sintaksis xatolari)

## 📚 Nazariya

**Syntax Error** — bu Python tilining **grammatika qoidalari buzilganda** yuzaga keladigan xatodir.

Oddiy qilib aytganda:

> Python interpreter kodingizni **o‘qiy olmaydi**.

Bu xatolar **dastur ishga tushishidan oldin** aniqlanadi.

Agar syntax error bo‘lsa:

* dastur **umuman ishga tushmaydi**
* Python **qaysi qatorda xato borligini ko‘rsatadi**
* xato **interpretatsiya jarayonida** aniqlanadi

Python parser kodingizni tekshiradi va noto‘g‘ri yozilgan joyni topadi.

---

## 🧠 Eng ko‘p uchraydigan Syntax Errorlar

| Xato turi               | Misol              |
| ----------------------- | ------------------ |
| Qavs yopilmagan         | `print("Hello"`    |
| Ikki nuqta unutildi     | `if x > 5`         |
| Notog‘ri indentatsiya   | `IndentationError` |
| Notog‘ri keyword yozish | `pritn()`          |

---

## 💻 Misol 1 — Qavs yopilmagan

```python
print("Hello World"
```

Natija:

```
SyntaxError: '(' was never closed
```

Sababi:

Python `(` qavs ochilganini ko‘radi lekin yopilmagan.

To‘g‘ri yozilishi:

```python
print("Hello World")
```

---

## 💻 Misol 2 — `:` belgisi unutildi

```python
x = 10

if x > 5
    print("x katta")
```

Natija:

```
SyntaxError: expected ':'
```

To‘g‘ri yozilishi:

```python
x = 10

if x > 5:
    print("x katta")
```

---

## 💻 Misol 3 — Indentation xatosi

Python’da **indentatsiya juda muhim**.

```python
if True:
print("Hello")
```

Natija:

```
IndentationError: expected an indented block
```

To‘g‘ri yozilishi:

```python
if True:
    print("Hello")
```

---

## 📌 Muhim xususiyatlari

| Xususiyat             | Tavsif                         |
| --------------------- | ------------------------------ |
| Qachon yuz beradi     | Dastur ishga tushishidan oldin |
| Python nima qiladi    | Kodni parse qiladi             |
| try/except ishlaydimi | ❌ Yo‘q                         |
| Sababi                | Noto‘g‘ri yozilgan kod         |

---

# ⚠️ Runtime Errors (Exceptions)

## 📚 Nazariya

**Runtime Error** — bu dastur **ishlayotgan paytda** yuzaga keladigan xatodir.

Python kodni o‘qiy oladi, lekin **ishlash jarayonida muammo chiqadi**.

Masalan:

* 0 ga bo‘lish
* mavjud bo‘lmagan faylni ochish
* noto‘g‘ri indeksga murojaat qilish

Bu xatolar Python’da **Exception** deb ataladi.

---

## 🧠 Eng ko‘p uchraydigan Runtime Errors

| Exception           | Sababi                     |
| ------------------- | -------------------------- |
| `ZeroDivisionError` | 0 ga bo‘lish               |
| `TypeError`         | noto‘g‘ri turdagi ma'lumot |
| `ValueError`        | noto‘g‘ri qiymat           |
| `IndexError`        | list indeks xatosi         |
| `KeyError`          | dictionary key yo‘q        |
| `FileNotFoundError` | fayl topilmadi             |

---

## 💻 Misol 1 — ZeroDivisionError

```python
x = 10
y = 0

result = x / y
print(result)
```

Natija:

```
ZeroDivisionError: division by zero
```

Sababi:

Matematik jihatdan **0 ga bo‘lish mumkin emas**.

---

## 💻 Misol 2 — IndexError

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Natija:

```
IndexError: list index out of range
```

Sababi:

Listda faqat **0,1,2 indekslar mavjud**.

---

## 💻 Misol 3 — TypeError

```python
age = "25"
result = age + 5
```

Natija:

```
TypeError: can only concatenate str (not "int")
```

Sababi:

Python **string va integerni qo‘sha olmaydi**.

To‘g‘ri kod:

```python
age = "25"

result = int(age) + 5
print(result)
```

---

# 🔑 Syntax Error vs Runtime Error

| Xususiyat                  | Syntax Error | Runtime Error     |
| -------------------------- | ------------ | ----------------- |
| Qachon yuz beradi          | Kod yozishda | Dastur ishlaganda |
| Python kodni o‘qiy oladimi | ❌ Yo‘q       | ✅ Ha              |
| try/except ishlaydimi      | ❌ Yo‘q       | ✅ Ha              |
| Misol                      | `if x > 5`   | `10 / 0`          |

---

# 🧪 Kichik Demo

```python
# Syntax Error example
if True
    print("Hello")
```

Bu kod **umuman ishga tushmaydi**.

---

```python
# Runtime Error example
x = 10
y = 0

print(x / y)
```

Bu kod ishga tushadi, lekin **runtime vaqtida xato beradi**.

---

<br>
<br>
<br>
<br>
<br>

# ⚠️ Exceptions (What Are They?)

## 📚 Exception nima?

**Exception** — bu dastur ishlayotgan paytda yuzaga keladigan **xato (error) holati** bo‘lib, Python uni maxsus obyekt sifatida ifodalaydi.

Oddiy qilib aytganda:

> Exception — bu dastur bajarilish jarayonida sodir bo‘ladigan **kutilmagan muammo**.

Python bu muammoni:

* aniqlaydi
* to‘xtatadi (agar ushlanmasa)
* va xato haqida ma’lumot beradi

---

## ⚙️ Exception qanday ishlaydi?

Python kodni yuqoridan pastga qarab bajaradi. Agar bajarilish jarayonida muammo chiqsa:

1️⃣ Python xatoni aniqlaydi
2️⃣ Exception obyektini yaratadi
3️⃣ Dastur bajarilishini to‘xtatadi
4️⃣ Xato haqida ma’lumot chiqaradi (**traceback**)

---

## 💻 Oddiy misol

```python
x = 10
y = 0

result = x / y
print(result)
```

Natija:

```text
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    result = x / y
ZeroDivisionError: division by zero
```

---

## 🔍 Bu yerda nima bo‘ldi?

* `x / y` bajarildi
* `y = 0` bo‘lgani uchun matematik xato yuz berdi
* Python **ZeroDivisionError** exceptionini chiqardi
* dastur shu yerda to‘xtadi

---

## 🧠 Exception bu obyekt

Python’da har bir exception bu — **class (klass) asosida yaratilgan obyekt**.

Masalan:

```python
error = ValueError("Noto'g'ri qiymat")
print(type(error))
```

Natija:

```text
<class 'ValueError'>
```

Bu shuni anglatadiki:

> Exception — bu oddiy string emas, balki **obyekt (object)**

---

## 📊 Exception tarkibi

Exception odatda quyidagi ma’lumotlarni o‘z ichiga oladi:

* ❗ Xato turi (masalan: `TypeError`)
* 📝 Xabar (message)
* 📍 Qayerda yuz bergani (file, line)

---

## 🔎 Traceback nima?

**Traceback** — bu xato qayerda va qanday yuz berganini ko‘rsatadigan hisobot.

Misol:

```python
def divide(a, b):
    return a / b

print(divide(10, 0))
```

Natija:

```text
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print(divide(10, 0))
  File "main.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

---

## 📌 Traceback nimani ko‘rsatadi?

* Qaysi faylda xato bor
* Qaysi qatorda
* Qaysi funksiyada
* Qanday exception bo‘lgan

---

## 🧪 Yana misollar

### 1️⃣ TypeError

```python
x = "10"
y = 5

print(x + y)
```

Natija:

```text
TypeError: can only concatenate str (not "int")
```

---

### 2️⃣ ValueError

```python
number = int("abc")
```

Natija:

```text
ValueError: invalid literal for int()
```

---

### 3️⃣ IndexError

```python
numbers = [1, 2, 3]

print(numbers[10])
```

Natija:

```text
IndexError: list index out of range
```

---

## ⚡ Muhim xususiyatlar

| Xususiyat          | Tavsif                             |
| ------------------ | ---------------------------------- |
| Qachon yuz beradi  | Dastur ishlayotganda               |
| Python nima qiladi | Exception chiqaradi                |
| Natija             | Dastur to‘xtaydi (agar ushlanmasa) |
| Turi               | Obyekt (class asosida)             |

---

## 🧩 Exception oqimi (flow)

Quyidagi jarayon sodir bo‘ladi:

```
Kod ishlaydi → Xato yuz beradi → Exception yaratiladi → 
Dastur to‘xtaydi → Traceback chiqariladi
```

---
