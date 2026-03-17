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

<br>
<br>
<br>
<br>
<br>

# 📊 Built-in Exception Hierarchy (Python)

## 📚 Exception Hierarchy nima?

Python’da barcha exceptionlar **bitta katta ierarxiya (tree)** ko‘rinishida tashkil qilingan.

Oddiy qilib aytganda:

> Har bir exception — bu boshqa bir umumiy exceptiondan **meros olgan (inheritance)** klass.

Bu tizim yordamida:

* exceptionlarni guruhlash mumkin
* umumiy xatolarni bir joyda ushlash mumkin
* kodni ancha toza va boshqariladigan qilish mumkin

---

## 🌳 Asosiy ierarxiya (soddalashtirilgan)

```text
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      │
      ├── TypeError
      ├── ValueError
      ├── IndexError
      ├── KeyError
      ├── FileNotFoundError
      ├── ImportError
      └── RuntimeError
```

---

## 🧠 Eng yuqori daraja: `BaseException`

```python
print(issubclass(Exception, BaseException))  # True
```

📌 `BaseException` — bu **barcha exceptionlarning eng yuqori ota klassi**

Lekin odatda:

> ❗ `BaseException` ni ushlash tavsiya etilmaydi

Sababi:

* `SystemExit` (dastur chiqishi)
* `KeyboardInterrupt` (Ctrl+C)

ham shu klassdan meros oladi

---

## 🎯 Asosiy ishlatiladigan klass: `Exception`

📌 Dasturchilar odatda quyidagini ishlatadi:

```python
try:
    x = int("abc")
except Exception as e:
    print("Xatolik:", e)
```

👉 `Exception` — bu:

* deyarli barcha oddiy xatolarni qamrab oladi
* eng ko‘p ishlatiladigan ota klass

---

## 🔢 Muhim ichki (built-in) exceptionlar

### ➗ ArithmeticError

Matematik xatolar uchun umumiy klass

#### Misol:

```python
print(10 / 0)
```

Natija:

```text
ZeroDivisionError
```

📌 `ZeroDivisionError` → `ArithmeticError` dan kelib chiqqan

---

### 🔤 TypeError

Noto‘g‘ri turdagi ma’lumot ishlatilganda

```python
print("10" + 5)
```

---

### 🔢 ValueError

To‘g‘ri tur, lekin noto‘g‘ri qiymat

```python
int("abc")
```

---

### 📍 IndexError

List indeks noto‘g‘ri bo‘lsa

```python
nums = [1, 2, 3]
print(nums[5])
```

---

### 🔑 KeyError

Dictionary ichida mavjud bo‘lmagan kalit

```python
data = {"name": "Ali"}
print(data["age"])
```

---

### 📂 FileNotFoundError

Fayl topilmasa

```python
open("file.txt")
```

---

### 📦 ImportError

Modulni import qilishda xato

```python
import not_existing_module
```

---

### ⚙️ RuntimeError

Umumiy runtime xatolar

---

## 🔗 Inheritance qanday ishlaydi?

```python
print(issubclass(ZeroDivisionError, ArithmeticError))  # True
print(issubclass(ArithmeticError, Exception))          # True
```

👉 Bu degani:

```
ZeroDivisionError → ArithmeticError → Exception → BaseException
```

---

## 🧪 Amaliy misol

```python
try:
    x = 10 / 0
except ArithmeticError:
    print("Matematik xato yuz berdi!")
```

📌 Natija:

```text
Matematik xato yuz berdi!
```

👉 Nega ishladi?

Chunki:

* `ZeroDivisionError`
* `ArithmeticError` dan meros olgan

---

## 🧩 Bir nechta darajada ushlash

```python
try:
    x = int("abc")
except ValueError:
    print("Value xatosi")
except Exception:
    print("Boshqa xato")
```

📌 Muhim:

* kichik (specific) exceptionlar yuqorida yoziladi
* katta (general) pastda yoziladi

---

## ⚠️ Muhim qoidalar

### 1️⃣ Har doim specific exception ishlatish

❌ Yomon:

```python
except Exception:
    pass
```

✅ Yaxshi:

```python
except ValueError:
    print("Noto'g'ri qiymat")
```

---

### 2️⃣ Exception tartibi muhim

❌ Noto‘g‘ri:

```python
except Exception:
    ...
except ValueError:
    ...
```

👉 Bu yerda `ValueError` hech qachon ishlamaydi

---

### 3️⃣ BaseException ishlatmaslik

❌

```python
except BaseException:
    ...
```

👉 Bu hatto `Ctrl+C` ni ham ushlab qoladi

---

<br>
<br>
<br>
<br>
<br>

# 🛡️ try / except (Basic Handling)

## 📚 try / except nima?

`try / except` — bu Python’da **exceptionlarni ushlash va boshqarish mexanizmi**.

Oddiy qilib aytganda:

> Dastur xato bersa ham **to‘xtab qolmasligi** uchun ishlatiladi.

---

## ⚙️ Qanday ishlaydi?

```python
try:
    # xato chiqishi mumkin bo‘lgan kod
except:
    # xato bo‘lsa ishlaydigan kod
```

### 🔄 Jarayon:

1️⃣ `try` ichidagi kod bajariladi
2️⃣ Agar xato bo‘lmasa → `except` ishlamaydi
3️⃣ Agar xato bo‘lsa → `except` ishga tushadi
4️⃣ Dastur davom etadi

---

## 💻 Eng oddiy misol

```python
try:
    x = 10 / 0
except:
    print("Xatolik yuz berdi!")
```

📌 Natija:

```text
Xatolik yuz berdi!
```

👉 Dastur **to‘xtab qolmadi**

---

## 🎯 Real hayotiy misol

Foydalanuvchi inputi bilan ishlash:

```python
try:
    age = int(input("Yoshingizni kiriting: "))
    print("Sizning yoshingiz:", age)
except:
    print("Iltimos, faqat son kiriting!")
```

👉 Agar foydalanuvchi `"abc"` kiritsa:

* `ValueError` chiqadi
* `except` uni ushlab qoladi

---

## 🎯 Aniq exception bilan ishlash

❗ Har doim aniq exception ishlatish tavsiya qilinadi

```python
try:
    x = int("abc")
except ValueError:
    print("Bu yerda ValueError yuz berdi!")
```

---

## 🔍 Bir nechta kodlar bilan

```python
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except ValueError:
    print("Son kiriting!")
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas!")
```

---

## 🧠 Exception obyektini olish

```python
try:
    x = int("abc")
except ValueError as e:
    print("Xato:", e)
```

📌 Natija:

```text
Xato: invalid literal for int() with base 10: 'abc'
```

👉 `e` — exception obyekt

---

## 🧪 Kod ishlash oqimi

```python
try:
    print("1-qadam")
    x = 10 / 0
    print("2-qadam")
except:
    print("Xato ushlanib qoldi")
```

📌 Natija:

```text
1-qadam
Xato ushlanib qoldi
```

👉 `2-qadam` ishlamadi, chunki xato oldinroq yuz berdi

---

## ⚠️ try / except ishlamaydigan holat

```python
try:
    if True
        print("Hello")
except:
    print("Xato")
```

👉 Bu **SyntaxError**, ushlanmaydi ❌

---

## 📌 Muhim qoidalar

### 1️⃣ try ichida faqat kerakli kod bo‘lsin

❌ Yomon:

```python
try:
    a = int(input())
    b = int(input())
    print(a / b)
    print("Hello")
```

👉 Qayerda xato bo‘lganini aniqlash qiyin

---

### 2️⃣ except bo‘sh qoldirilmasin

❌ Yomon:

```python
except:
    pass
```

👉 Xatoni yashirib yuboradi

---

### 3️⃣ Har doim specific exception ishlatish

❌

```python
except:
    print("Xato")
```

✅

```python
except ValueError:
    print("Noto'g'ri qiymat")
```

---

## 🧩 Mini loyiha

```python
while True:
    try:
        num = int(input("Son kiriting: "))
        print("Natija:", 100 / num)
        break
    except ValueError:
        print("Iltimos, son kiriting!")
    except ZeroDivisionError:
        print("0 kiritmang!")
```

👉 Foydalanuvchi to‘g‘ri qiymat kiritmaguncha davom etadi

---

<br>
<br>
<br>
<br>
<br>

# 🔢 Multiple `except` Blocks (Bir nechta except ishlatish)

## 📚 Multiple `except` nima?

Python’da bitta `try` blok uchun **bir nechta `except` bloklar** yozish mumkin.

Oddiy qilib aytganda:

> Har xil turdagi xatolarni **alohida-alohida ushlash** uchun ishlatiladi.

---

## ⚙️ Sintaksis

```python
try:
    # xato chiqishi mumkin bo‘lgan kod
except ErrorType1:
    # 1-xato uchun
except ErrorType2:
    # 2-xato uchun
except ErrorType3:
    # 3-xato uchun
```

---

## 💻 Oddiy misol

```python
try:
    x = int(input("Son kiriting: "))
    result = 100 / x
    print(result)

except ValueError:
    print("❗ Bu son emas!")

except ZeroDivisionError:
    print("❗ 0 ga bo‘lish mumkin emas!")
```

---

## 🔍 Qanday ishlaydi?

1️⃣ `try` ichidagi kod bajariladi
2️⃣ Agar xato yuz bersa
3️⃣ Python **mos keladigan `except` blokni** topadi
4️⃣ Faqat o‘sha blok ishlaydi
5️⃣ Qolganlari o‘tkazib yuboriladi

---

## 🧠 Muhim: faqat BIRTA ishlaydi

```python
try:
    x = int("abc")
except ValueError:
    print("ValueError")
except Exception:
    print("Boshqa xato")
```

📌 Natija:

```text
ValueError
```

👉 Faqat birinchi mos kelgan `except` ishlaydi

---

## ⚠️ Tartib muhim!

❗ `except` bloklar **yuqoridan pastga qarab tekshiriladi**

---

### ❌ Noto‘g‘ri tartib

```python
try:
    x = int("abc")

except Exception:
    print("General error")

except ValueError:
    print("Value error")
```

👉 Bu yerda:

* `Exception` hamma xatoni ushlaydi
* `ValueError` hech qachon ishlamaydi ❌

---

### ✅ To‘g‘ri tartib

```python
try:
    x = int("abc")

except ValueError:
    print("Value error")

except Exception:
    print("General error")
```

👉 Avval **specific**, keyin **general**

---

## 🔗 Bir nechta exceptionni bitta blokda ushlash

```python
try:
    x = int(input("Son kiriting: "))
    print(10 / x)

except (ValueError, ZeroDivisionError):
    print("❗ Xato kiritish!")
```

👉 Bu yerda:

* 2 xil exception
* 1 ta `except` blok

---

## 🧠 Exception obyekt bilan

```python
try:
    x = int("abc")

except ValueError as e:
    print("Xato:", e)
```

---

## 🧪 Murakkabroq misol

```python
try:
    numbers = [10, 20, 30]
    index = int(input("Index kiriting: "))
    print(numbers[index])

except ValueError:
    print("❗ Index son bo‘lishi kerak!")

except IndexError:
    print("❗ Bunday indeks yo‘q!")

except Exception as e:
    print("❗ Boshqa xato:", e)
```

---

## 📌 Qachon ishlatiladi?

Multiple `except` quyidagi holatlarda juda foydali:

* turli xil xatolarni ajratish kerak bo‘lsa
* foydalanuvchiga aniq xabar berish uchun
* debuggingni osonlashtirish uchun

---

## ⚠️ Muhim qoidalar

### 1️⃣ Specific → General tartib

```python
except ValueError:
    ...
except Exception:
    ...
```

---

### 2️⃣ Har bir exception uchun alohida logika

```python
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas")

except ValueError:
    print("Noto‘g‘ri qiymat")
```

---

### 3️⃣ Ortiqcha umumiy except ishlatmaslik

❌

```python
except Exception:
    print("Xato")
```

👉 Xatoni aniqlash qiyin bo‘ladi

---

<br>
<br>
<br>
<br>
<br>

# ➕ `else` Clause (runs if no exception)

## 📚 `else` nima?

Python’da `else` bloki `try / except` bilan birga ishlatiladi va:

> `else` — faqat **xato bo‘lmagan holatda** ishlaydi

---

## ⚙️ Sintaksis

```python
try:
    # xato chiqishi mumkin bo‘lgan kod
except SomeError:
    # xato bo‘lsa ishlaydi
else:
    # xato bo‘lmasa ishlaydi
```

---

## 🔄 Qanday ishlaydi?

1️⃣ `try` blok bajariladi
2️⃣ Agar xato yuz bersa → `except` ishlaydi
3️⃣ Agar xato bo‘lmasa → `else` ishlaydi
4️⃣ `except` ishlagan bo‘lsa → `else` ishlamaydi

---

## 💻 Oddiy misol

```python
try:
    x = int("10")
except ValueError:
    print("Xato!")
else:
    print("Hammasi to‘g‘ri:", x)
```

📌 Natija:

```text
Hammasi to‘g‘ri: 10
```

---

## ❗ Xato bo‘lsa

```python
try:
    x = int("abc")
except ValueError:
    print("Xato yuz berdi!")
else:
    print("Bu chiqmaydi")
```

📌 Natija:

```text
Xato yuz berdi!
```

👉 `else` ishlamadi

---

## 🎯 Nega `else` kerak?

Ko‘pincha odamlar hamma kodni `try` ichiga yozib yuboradi ❌

Lekin to‘g‘ri yondashuv:

> `try` ichida faqat **xato chiqishi mumkin bo‘lgan kod** bo‘lishi kerak

Qolgan xavfsiz kod → `else` ichida yoziladi

---

## 🧠 To‘g‘ri foydalanish

### ❌ Noto‘g‘ri

```python
try:
    x = int(input("Son: "))
    print("Natija:", x * 2)
except ValueError:
    print("Xato")
```

👉 Bu yerda `print` ham `try` ichida (keraksiz)

---

### ✅ To‘g‘ri

```python
try:
    x = int(input("Son: "))
except ValueError:
    print("Xato")
else:
    print("Natija:", x * 2)
```

👉 Kod:

* toza
* aniq
* tushunarli

---

## 🧪 Real misol

```python
try:
    a = int(input("a: "))
    b = int(input("b: "))
    result = a / b
except ValueError:
    print("Son kiriting!")
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas!")
else:
    print("Natija:", result)
```

---

## 🔍 Muhim farq

| Holat         | Nima ishlaydi |
| ------------- | ------------- |
| Xato bo‘ldi   | `except`      |
| Xato bo‘lmadi | `else`        |

---

## ⚠️ Muhim qoidalar

### 1️⃣ `else` faqat xato bo‘lmasa ishlaydi

```python
try:
    ...
except:
    ...
else:
    ...
```

---

### 2️⃣ `else` ichida xavfsiz kod yoziladi

```python
else:
    print("Bu yerda xato yo‘q")
```

---

### 3️⃣ `else` majburiy emas

👉 `try / except` o‘zi ham ishlayveradi

---

## 🧩 Ishlash oqimi

```text
try → (xato?) → ha → except
             → yo‘q → else
```

---

<br>
<br>
<br>
<br>
<br>

# 🔚 `finally` Clause (always runs, cleanup)

## 📚 `finally` nima?

`finally` — bu `try / except` blokidan keyin yoziladigan qism bo‘lib:

> `finally` — **har doim ishlaydi (xato bo‘lsa ham, bo‘lmasa ham)**

---

## ⚙️ Sintaksis

```python
try:
    # xato chiqishi mumkin bo‘lgan kod
except SomeError:
    # xato bo‘lsa ishlaydi
finally:
    # har doim ishlaydi
```

---

## 🔄 Qanday ishlaydi?

1️⃣ `try` bajariladi
2️⃣ Agar xato bo‘lsa → `except` ishlaydi
3️⃣ Agar xato bo‘lmasa → `except` o‘tkazib yuboriladi
4️⃣ **Har ikkala holatda ham `finally` ishlaydi**

---

## 💻 Oddiy misol (xatosiz)

```python
try:
    print("Hello")
finally:
    print("Finally ishladi")
```

📌 Natija:

```text
Hello
Finally ishladi
```

---

## 💻 Xato bo‘lsa ham ishlaydi

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Xato yuz berdi")
finally:
    print("Finally ishladi")
```

📌 Natija:

```text
Xato yuz berdi
Finally ishladi
```

---

## 🎯 Muhim xususiyat

👉 `finally`:

* `except` ishlasa ham ishlaydi ✅
* `except` ishlamasa ham ishlaydi ✅
* doim oxirida bajariladi

---

## 🧠 To‘liq struktura

```python
try:
    ...
except:
    ...
else:
    ...
finally:
    ...
```

### 🔍 Ishlash tartibi:

```text
try → exception? → ha → except → finally
                → yo‘q → else → finally
```

---

## 🧪 Real misol (fayl bilan ishlash)

```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Fayl topilmadi!")
finally:
    print("Fayl yopildi (yoki yopilishi kerak)")
```

👉 Bu yerda `finally`:

* fayl ochilgan yoki ochilmagan bo‘lsa ham ishlaydi

---

## ⚠️ Resurslarni tozalash (cleanup)

`finally` ko‘pincha quyidagilar uchun ishlatiladi:

* fayl yopish
* database ulanishni yopish
* network connection yopish
* memory cleanup

---

## 💻 To‘g‘ri cleanup misoli

```python
file = None

try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Fayl yo‘q")
finally:
    if file:
        file.close()
        print("Fayl yopildi")
```

---

## ⚠️ Muhim holat: return bilan

```python
def test():
    try:
        return 1
    finally:
        print("Finally ishladi")

print(test())
```

📌 Natija:

```text
Finally ishladi
1
```

👉 `return` bo‘lsa ham `finally` ishlaydi

---

## ❗ Muhim ogohlantirish

```python
def test():
    try:
        return 1
    finally:
        return 2
```

📌 Natija:

```text
2
```

👉 `finally` ichidagi `return` — oldingisini bekor qiladi ⚠️

---

## 📌 Muhim qoidalar

### 1️⃣ `finally` har doim ishlaydi

```python
finally:
    print("Doim ishlaydi")
```

---

### 2️⃣ Cleanup uchun ishlatiladi

```python
file.close()
connection.close()
```

---

### 3️⃣ `finally` majburiy emas

👉 Faqat kerak bo‘lsa yoziladi

---

### 4️⃣ `return` bilan ehtiyot bo‘lish kerak

👉 `finally` ichida `return` ishlatish tavsiya etilmaydi

---

<br>
<br>
<br>
<br>
<br>

# ⬆️ Raising Exceptions (`raise`)

## 📚 `raise` nima?

`raise` — bu Python’da **sun’iy ravishda (manual) exception chiqarish** uchun ishlatiladi.

Oddiy qilib aytganda:

> `raise` — dasturchi o‘zi xato yaratadi

---

## ⚙️ Sintaksis

```python
raise ExceptionType("xabar")
```

---

## 💻 Oddiy misol

```python
age = -5

if age < 0:
    raise ValueError("Yosh manfiy bo‘lishi mumkin emas!")
```

📌 Natija:

```text
ValueError: Yosh manfiy bo‘lishi mumkin emas!
```

---

## 🎯 Qachon ishlatiladi?

`raise` quyidagi holatlarda ishlatiladi:

* noto‘g‘ri input kelganda
* biznes qoidalar buzilganda
* validatsiya qilishda
* dastur noto‘g‘ri ishlashining oldini olish uchun

---

## 🧠 Muhim tushuncha

> Exception faqat xato bo‘lganda emas, **xato bo‘lishi mumkin bo‘lgan holatda ham** chiqarilishi mumkin

---

## 💻 Validatsiya misoli

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Balans yetarli emas!")
    
    return balance - amount


print(withdraw(100, 150))
```

---

## 🔍 Natija

```text
ValueError: Balans yetarli emas!
```

---

## 🧪 `raise` + `try/except`

```python
try:
    age = int(input("Yosh: "))
    
    if age < 0:
        raise ValueError("Manfiy yosh mumkin emas!")
    
except ValueError as e:
    print("Xato:", e)
```

---

## 🔁 Exceptionni qayta chiqarish

Ba’zan exceptionni ushlab, keyin yana chiqarish kerak bo‘ladi:

```python
try:
    x = int("abc")
except ValueError:
    print("Xato aniqlandi")
    raise
```

📌 Natija:

* avval `print` ishlaydi
* keyin exception yana chiqariladi

---

## 🧠 Exception obyekt bilan

```python
raise TypeError("Noto‘g‘ri ma'lumot turi")
```

---

## 🔗 Shart bilan `raise`

```python
password = "123"

if len(password) < 6:
    raise ValueError("Parol juda qisqa!")
```

---

## ⚠️ `raise` ishlaganda nima bo‘ladi?

1️⃣ Exception yaratiladi
2️⃣ Dastur to‘xtaydi (agar ushlanmasa)
3️⃣ Traceback chiqariladi

---

## 🧩 O‘z funksiyangizda ishlatish

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0 ga bo‘lish mumkin emas!")
    
    return a / b


print(divide(10, 0))
```

---

## ❗ Muhim qoidalar

### 1️⃣ To‘g‘ri exception tanlash

❌

```python
raise Exception("Xato")
```

✅

```python
raise ValueError("Noto‘g‘ri qiymat")
```

---

### 2️⃣ Tushunarli xabar yozish

```python
raise ValueError("Yosh 0 dan katta bo‘lishi kerak")
```

---

### 3️⃣ Keraksiz `raise` ishlatmaslik

👉 faqat haqiqiy xato holatlarda

---

### 4️⃣ `raise` dastur oqimini to‘xtatadi

```python
print("1")
raise ValueError("Xato")
print("2")  # bu ishlamaydi
```

---

## 🧪 Mini loyiha

```python
def register(username):
    if len(username) < 3:
        raise ValueError("Username juda qisqa!")
    
    print("Ro‘yxatdan o‘tildi!")


try:
    register("ab")
except ValueError as e:
    print("Xato:", e)
```

---

<br>
<br>
<br>
<br>
<br>

# 🔗 Exception Chaining (`raise ... from ...`)

## 📚 Exception Chaining nima?

Python’da **Exception Chaining** yordamida siz:

> bir exceptionni boshqa exceptiondan kelib chiqqan deb belgilashingiz mumkin

Oddiy qilib aytganda:

* Bir xato yuz berdi → boshqa xato bilan **bog‘lash**
* Traceback’larda **asl sababni saqlash**

---

## ⚙️ Sintaksis

```python id="a1f2gx"
try:
    # asl xato yuz beradigan kod
except OriginalException as e:
    raise NewException("Yangi xabar") from e
```

---

## 💻 Oddiy misol

```python id="b3v4ky"
try:
    x = int("abc")
except ValueError as e:
    raise RuntimeError("Funksiya ishlashda xato") from e
```

📌 Natija:

```text id="c5m7lz"
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    x = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'

The above exception was the direct cause of the following exception:

RuntimeError: Funksiya ishlashda xato
```

---

## 🔍 Nima sodir bo‘ldi?

1️⃣ `int("abc")` → `ValueError` yuz berdi
2️⃣ `except` ichida **yangi exception (`RuntimeError`)** yaratildi
3️⃣ `from e` bilan eski exception (`ValueError`) bilan bog‘landi
4️⃣ Traceback’da **asl sabab ko‘rsatildi**

---

## 🎯 Qachon ishlatiladi?

* Funksiya ichidagi xatoni **higher-level exception** bilan o‘rab olish
* **Debug qilishni osonlashtirish**
* Kodni **professional va izchil** qilish

---

## 🧠 Exception chaining vs normal raise

### ❌ Oddiy `raise`:

```python id="d7s4qv"
try:
    x = int("abc")
except ValueError:
    raise RuntimeError("Yangi xato")
```

* Natija:

  * `RuntimeError` chiqadi
  * asl `ValueError` **yo‘qoladi**
  * traceback faqat yangi exceptionni ko‘rsatadi

---

### ✅ `raise ... from ...`:

* Asl sabab saqlanadi
* Traceback aniq va tushunarli
* Debug qilish osonroq

---

## 💻 Murakkab misol

```python id="e9t8mv"
def process(data):
    try:
        num = int(data)
    except ValueError as e:
        raise RuntimeError("Data processing failed") from e

try:
    process("abc")
except RuntimeError as e:
    print("Caught:", e)
```

📌 Natija:

```text id="f1q5lj"
Caught: Data processing failed
```

Traceback esa `ValueError` sababini ham ko‘rsatadi.

---

## 🔗 Multiple exception chaining

Siz bir nechta layerlarda chaining qilishingiz mumkin:

```python id="g2v6kz"
def layer1():
    try:
        int("abc")
    except ValueError as e:
        raise KeyError("Layer1 xatosi") from e

def layer2():
    try:
        layer1()
    except KeyError as e:
        raise RuntimeError("Layer2 xatosi") from e

layer2()
```

📌 Natija:

* Traceback’da **ValueError → KeyError → RuntimeError** ketma-ketligi ko‘rinadi

---

## ⚠️ Muhim qoidalar

1️⃣ Har doim `from e` ishlatilsa **asl sabab saqlanadi**
2️⃣ `raise ...` (`from None`) → **oldingi exceptionni yashirish** mumkin

```python id="h3q7tz"
try:
    int("abc")
except ValueError:
    raise RuntimeError("Yangi xato") from None
```

* Natija: **faqat yangi exception**, asl sabab ko‘rinmaydi

---

<br>
<br>
<br>
<br>
<br>

# 🎨 Custom Exceptions (`class MyError(Exception)`)

## 📚 Custom Exception nima?

Python’da siz faqat **built-in exception**lardan foydalanishingiz shart emas.

> **Custom Exception** — bu siz o‘zingiz yaratgan, maxsus exception class.

Foydasi:

* Kodni **o‘qish oson** bo‘ladi
* **Biznes qoidalari**ni aniq ifodalash mumkin
* Exceptionlarni **turli modul va layerlarda boshqarish** osonlashadi

---

## ⚙️ Sintaksis

```python id="ce1v8q"
class MyError(Exception):
    """Maxsus exception xabari"""
    pass
```

* `Exception` dan meros oladi ✅
* Ichiga **docstring** va qo‘shimcha metodlar yozish mumkin

---

## 💻 Oddiy misol

```python id="ce2v9r"
class NegativeAgeError(Exception):
    """Yosh manfiy bo‘lsa yuz beradigan exception"""
    pass

age = -5

if age < 0:
    raise NegativeAgeError("Yosh manfiy bo‘lishi mumkin emas!")
```

📌 Natija:

```text id="ce3v1t"
NegativeAgeError: Yosh manfiy bo‘lishi mumkin emas!
```

---

## 🧠 Custom Exceptionni ushlash

```python id="ce4v2u"
try:
    raise NegativeAgeError("Xato")
except NegativeAgeError as e:
    print("Caught:", e)
```

📌 Natija:

```text id="ce5v3v"
Caught: Xato
```

---

## 🔗 Parametrli Custom Exception

Siz exception ichida **qo‘shimcha atributlar** saqlashingiz mumkin:

```python id="ce6v4w"
class InvalidTransactionError(Exception):
    def __init__(self, account, amount):
        super().__init__(f"Account {account}: invalid transaction {amount}")
        self.account = account
        self.amount = amount

raise InvalidTransactionError("12345", 1000)
```

📌 Natija:

```text id="ce7v5x"
InvalidTransactionError: Account 12345: invalid transaction 1000
```

---

## 💻 Foydali amaliy misol

```python id="ce8v6y"
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Balans yetarli emas! Balans: {balance}, Summ: {amount}")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print("Xato:", e)
```

📌 Natija:

```text id="ce9v7z"
Xato: Balans yetarli emas! Balans: 100, Summ: 150
```

---

## 🎯 Qachon custom exception ishlatish kerak?

* Biznes qoidalari bilan bog‘liq xatolar uchun
* Modul yoki kutubxona yaratishda
* Kodni **tushunarli va o‘qilishi oson qilish** uchun

---

## 🧩 Tips & Best Practices

1️⃣ **`Exception` dan meros oling**

```python id="cf1v8a"
class MyError(Exception):
    pass
```

2️⃣ **Docstring yozing** — nima uchun exception yuz beradi

3️⃣ **Qo‘shimcha atributlar qo‘shish** — foydalanuvchi yoki log uchun

4️⃣ Exceptionni **mos joyda ushlash** — try/except bilan

---

## 🔍 Ko‘p darajali exception

Siz **custom exceptionlar ierarxiyasini** yaratishingiz mumkin:

```python id="cf2v9b"
class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

class APIError(AppError):
    pass
```

* `AppError` — umumiy ota class
* `DatabaseError` va `APIError` — specific exceptionlar

---

<br>
<br>
<br>
<br>
<br>

# 📦 `contextlib` — Context Managers & Helpers

Python’da `contextlib` moduli **context manager’lar yaratish va xatolarni boshqarish** uchun foydalidir.

> Context manager — bu **resursni ochish va yopishni avtomatlashtirish** imkonini beruvchi blok (`with` statement bilan ishlatiladi).

---

## ⚙️ `@contextmanager` decorator

`@contextmanager` yordamida siz **o‘z context manager** yaratishingiz mumkin, **class yozmasdan**.

### Sintaksis

```python id="ctx1"
from contextlib import contextmanager

@contextmanager
def my_context():
    # setup (resursni ochish)
    print("Enter context")
    try:
        yield "something"  # qiymatni return qilgandek
    finally:
        # cleanup (resursni yopish)
        print("Exit context")
```

### Misol ishlatish

```python id="ctx2"
with my_context() as value:
    print("Inside context:", value)
```

📌 Natija:

```text id="ctx3"
Enter context
Inside context: something
Exit context
```

* `yield` — context ichidagi qiymat
* `finally` — context tugagach **har doim ishlaydi**

---

## ⚡ `suppress()` — exception’larni yashirish

`contextlib.suppress()` yordamida **specific exception’larni yashirishingiz** mumkin.

### Sintaksis

```python id="ctx4"
from contextlib import suppress

with suppress(FileNotFoundError):
    open("nofile.txt")  # agar FileNotFoundError bo‘lsa, e’tiborsiz qoladi
```

📌 Natija:

* Fayl topilmasa xato chiqmaydi
* Dastur davom etadi

---

### Bir nechta exception

```python id="ctx5"
with suppress(FileNotFoundError, PermissionError):
    open("nofile.txt")
```

---

## 🔁 `redirect_stdout()` — chiqishni boshqa joyga yo‘naltirish

`contextlib.redirect_stdout()` yordamida `print()` chiqishini **fayl yoki obyektga yo‘naltirish** mumkin.

### Misol: faylga yo‘naltirish

```python id="ctx6"
from contextlib import redirect_stdout

with open("output.txt", "w") as f:
    with redirect_stdout(f):
        print("Hello file!")
```

📌 Natija:

* `output.txt` faylida `"Hello file!"` yoziladi
* Konsolga hech nima chiqmaydi

---

### Misol: string buffer’ga yo‘naltirish

```python id="ctx7"
import io
from contextlib import redirect_stdout

buffer = io.StringIO()

with redirect_stdout(buffer):
    print("Hello buffer!")

print("Captured:", buffer.getvalue())
```

📌 Natija:

```text id="ctx8"
Captured: Hello buffer!
```

---

## 🧠 Qaysi holatlarda foydali?

* Fayl ochish / yopish
* Network connection ochish / yopish
* Resource cleanup avtomatik
* Xatolarni yashirish (e’tiborsiz qilish)
* Konsol chiqishini faylga yo‘naltirish

---

<br>
<br>
<br>
<br>
<br>

# 🔄 Retry Logic (`tenacity` library)

## 📚 Retry Logic nima?

Ba’zan dasturda **xato vaqtinchalik bo‘lishi** mumkin:

* Network ulanish xatosi
* API chaqiruv muvaffaqiyatsiz bo‘lishi
* Fayl vaqtincha band bo‘lishi

**Retry Logic** — bu xatolik yuz berganda **kodni avtomatik qayta urinish (retry)** mexanizmi.

Python’da buning uchun eng mashhur kutubxona — [`tenacity`](https://pypi.org/project/tenacity/).

---

## ⚙️ O‘rnatish

```bash
pip install tenacity
```

---

## 💻 Eng oddiy misol

```python id="ten1"
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3))
def task():
    print("Urinish")
    raise ValueError("Xato yuz berdi")

task()
```

📌 Natija:

* Funksiya **3 marta urinish qiladi**
* Har safar xato yuz beradi, so‘ng exception chiqadi

---

## 🔄 Retry bilan muvaffaqiyatli urinish

```python id="ten2"
import random
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(5))
def task():
    x = random.randint(0, 1)
    print("Urinish:", x)
    if x == 0:
        raise ValueError("Xato")
    return "Muvaffaqiyat!"

print(task())
```

* Agar `x == 1` bo‘lsa → urinish muvaffaqiyatli
* Kod **automatik qayta urinadi** xato bo‘lsa

---

## ⚡ Qo‘shimcha parametrlar

### 1️⃣ `wait_fixed` — har urinish orasida kutish

```python id="ten3"
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))  # 2 soniya kutadi
def task():
    print("Urinish")
    raise ValueError("Xato")
```

---

### 2️⃣ `wait_exponential` — exponentional kutish

```python id="ten4"
from tenacity import wait_exponential

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, max=10))
def task():
    print("Urinish")
    raise ValueError("Xato")
```

* 1s → 2s → 4s → 8s → 10s (maks)

---

### 3️⃣ `retry` shartini o‘zgartirish

```python id="ten5"
from tenacity import retry_if_exception_type

@retry(retry=retry_if_exception_type(ValueError), stop=stop_after_attempt(3))
def task():
    print("Urinish")
    raise ValueError("Xato")
```

* Faqat `ValueError` yuz berganda qayta urinish

---

## 🔍 Exception bilan ishlash

```python id="ten6"
from tenacity import RetryError

try:
    task()
except RetryError as e:
    print("Barcha urinishlar muvaffaqiyatsiz:", e)
```

* `RetryError` — **barcha urinishlar muvaffaqiyatsiz bo‘lganda** chiqariladi

---

## 🧠 Qachon foydali?

* **Network requestlar**
* **API chaqiruvlar**
* **Vaqtinchalik xatolar**
* Dastur **barqarorligini oshirish**

---

<br>
<br>
<br>
<br>
<br>

# ✨ Error Design Best Practices

Python dasturlashda **xatolarni dizayn qilish** muhim, chunki bu:

* Kodni **tushunarli va maintainable** qiladi
* Dastur **robust va fault-tolerant** bo‘ladi
* Debug va loglashni **osonlashtiradi**

---

## 1️⃣ Specific exception ishlating

❌ Yomon:

```python id="err1"
try:
    x = int("abc")
except Exception:
    print("Xato")
```

✅ Yaxshi:

```python id="err2"
try:
    x = int("abc")
except ValueError:
    print("Noto‘g‘ri qiymat")
```

* **Specific exception** → kodni tushunishni osonlashtiradi
* Faqat kerakli xatoni ushlaydi

---

## 2️⃣ Clear, descriptive messages

* Exception xabari **foydalanuvchi yoki developer uchun tushunarli bo‘lishi kerak**

```python id="err3"
raise ValueError("Yosh 0 dan katta bo‘lishi kerak")
```

* **Qisqa, aniq va kontekstual xabar**
* Traceback oson tushuniladi

---

## 3️⃣ Use custom exceptions for domain logic

* Biznes qoidalari uchun **custom exception** yaratish

```python id="err4"
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Balans yetarli emas")
```

* Kod **readable va self-documenting** bo‘ladi

---

## 4️⃣ Keep try blocks minimal

❌ Yomon:

```python id="err5"
try:
    x = int(input())
    print("Hello")
    y = 10 / 0
except ValueError:
    print("Xato")
```

✅ Yaxshi:

```python id="err6"
try:
    x = int(input())
except ValueError:
    print("Noto‘g‘ri son")

try:
    y = 10 / 0
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas")
```

* Har `try` faqat **xato chiqishi mumkin bo‘lgan kod**ni o‘z ichiga olishi kerak
* Debug osonlashadi

---

## 5️⃣ Don’t suppress exceptions silently

❌ Yomon:

```python id="err7"
try:
    x = int("abc")
except ValueError:
    pass
```

* Xatolar yashirilib ketadi → debugging qiyin

✅ Yaxshi:

```python id="err8"
try:
    x = int("abc")
except ValueError as e:
    print("Xato:", e)
```

* Xabar beriladi va xato **ko‘rinadi**

---

## 6️⃣ Use `finally` or context managers for cleanup

```python id="err9"
file = None
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("Fayl topilmadi")
finally:
    if file:
        file.close()
```

* Resurslar har doim tozalanadi
* Kod **robust** bo‘ladi

---

## 7️⃣ Chain exceptions when needed

* Oldingi xatolarni **saqlash va yuqori darajaga uzatish**

```python id="err10"
try:
    x = int("abc")
except ValueError as e:
    raise RuntimeError("Funksiya ishlashda xato") from e
```

* Traceback’da asl sabab ko‘rinadi → debugging oson

---

## 8️⃣ Retry only for transient errors

* Faqat **vaqtinchalik xatolar** uchun retry ishlating

```python id="err11"
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3))
def fetch_data():
    ...
```

* Permanent errors’ni retry qilish **noto‘g‘ri**

---

## 9️⃣ Log exceptions

* Xatolarni **loglash** – keyinchalik tahlil va debugging uchun muhim

```python id="err12"
import logging

try:
    x = int("abc")
except ValueError as e:
    logging.error("Xato yuz berdi: %s", e)
```

---

## 10 Keep user experience in mind

* Foydalanuvchiga **muvaffaqiyatli feedback berish**
* Faqat developer uchun kerakli exceptionlarni logga yozing, foydalanuvchiga **friendly message** ko‘rsating
---