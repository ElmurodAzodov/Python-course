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

