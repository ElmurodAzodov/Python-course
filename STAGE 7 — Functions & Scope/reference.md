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
