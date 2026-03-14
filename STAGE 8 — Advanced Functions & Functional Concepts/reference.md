# **STAGE 8 — Advanced Functions & Functional Concepts**

<br>
<br>

## ⭐ Functions as First-Class Objects (Assign, Pass, Return)

Python’da **funksiyalar ham oddiy obyektlar kabi ishlatilishi mumkin**.
Bu konsepsiya **First-Class Object** deb ataladi.

Agar biror narsa **first-class** bo‘lsa, u quyidagi imkoniyatlarga ega bo‘ladi:

✅ O‘zgaruvchiga **biriktirilishi mumkin**
✅ **Argument sifatida** boshqa funksiyaga berilishi mumkin
✅ **Funksiyadan qaytarilishi** mumkin
✅ **Ma'lumot strukturasi ichida** saqlanishi mumkin (list, dict, va hokazo)

Python’da **funksiya ham object** bo‘lgani uchun yuqoridagi barcha imkoniyatlar mavjud.

---

# 📌 1. Functionni o‘zgaruvchiga assign qilish

Funksiyani **o‘zgaruvchiga saqlash mumkin**.
Bu holda funksiya nomi emas, **funksiyaning o‘zi** assign qilinadi.

### 🧠 Nazariya

Funksiya chaqirish:

```
function_name()
```

Agar **qavs qo‘ymasak**, funksiya **chaqirilmaydi**, balki **object sifatida olinadi**.

---

### 💻 Misol

```python
def greet(name):
    return f"Hello {name}"

say_hello = greet

print(say_hello("Ali"))
```

### 📤 Output

```
Hello Ali
```

### 🔍 Tushuntirish

| Kod                 | Ma'nosi                               |
| ------------------- | ------------------------------------- |
| `greet`             | funksiya object                       |
| `say_hello = greet` | funksiya boshqa o‘zgaruvchiga berildi |
| `say_hello("Ali")`  | aslida `greet("Ali")` chaqirildi      |

---

### 📌 Funksiya object ekanini tekshirish

```python
def add(a, b):
    return a + b

print(add)
```

### 📤 Output

```
<function add at 0x0000023A...>
```

Bu shuni bildiradiki **funksiya ham xotirada obyekt**.

---

# 📌 2. Functionni argument sifatida berish

Python’da funksiya **boshqa funksiyaga argument sifatida uzatilishi mumkin**.

Bu **Higher-Order Function** deb ataladi.

📌 **Higher-Order Function** — funksiya qabul qiladigan yoki funksiya qaytaradigan funksiya.

---

### 💻 Misol

```python
def greet(name):
    return f"Hello {name}"

def execute_function(func, value):
    return func(value)

result = execute_function(greet, "Ali")

print(result)
```

### 📤 Output

```
Hello Ali
```

### 🔍 Tushuntirish

| Qadam              | Nima bo'ldi                                      |
| ------------------ | ------------------------------------------------ |
| `greet`            | funksiya object                                  |
| `execute_function` | funksiya argument sifatida funksiya qabul qiladi |
| `func(value)`      | uzatilgan funksiya chaqiriladi                   |

---

### 📌 Bir nechta funksiyalar bilan ishlash

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(func, x, y):
    return func(x, y)

print(calculate(add, 5, 3))
print(calculate(multiply, 5, 3))
```

### 📤 Output

```
8
15
```

Bu yerda:

```
calculate(add, 5, 3)
```

aslida:

```
add(5, 3)
```

---

# 📌 3. Functionni return qilish

Python’da funksiya **boshqa funksiyani qaytarishi ham mumkin**.

Bu ko‘pincha:

* decoratorlar
* closurelar
* functional programming

uchun ishlatiladi.

---

### 💻 Misol

```python
def get_greeter():
    
    def greet(name):
        return f"Hello {name}"
    
    return greet

greeter = get_greeter()

print(greeter("Ali"))
```

### 📤 Output

```
Hello Ali
```

### 🔍 Tushuntirish

| Qadam           | Nima bo'ldi                     |
| --------------- | ------------------------------- |
| `get_greeter()` | ichida yangi funksiya yaratildi |
| `return greet`  | funksiya qaytarildi             |
| `greeter`       | endi funksiya object            |

---

# 📌 4. Functionni data structure ichida saqlash

Funksiyalarni **list, dictionary, set** ichida ham saqlash mumkin.

---

### 💻 Misol (List)

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operations = [add, subtract]

print(operations[0](10, 5))
print(operations[1](10, 5))
```

### 📤 Output

```
15
5
```

---

### 💻 Misol (Dictionary)

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

calculator = {
    "add": add,
    "multiply": multiply
}

print(calculator["add"](4, 6))
print(calculator["multiply"](4, 6))
```

### 📤 Output

```
10
24
```

Bu usul **command dispatcher** va **plugin system**larda ishlatiladi.

---

# 📌 5. Functionni boshqa o‘zgaruvchiga nusxalash

Funksiya **reference** orqali beriladi.

---

### 💻 Misol

```python
def greet():
    print("Hello")

a = greet
b = greet

a()
b()
```

### 📤 Output

```
Hello
Hello
```

---

# 📌 6. Functionni boshqa funksiya ichida ishlatish

```python
def square(x):
    return x * x

def apply(func, value):
    return func(value)

print(apply(square, 5))
```

### 📤 Output

```
25
```

---

# 📌 7. Real Example (Plugin Pattern)

```python
def jpg_handler(file):
    return "Processing JPG"

def png_handler(file):
    return "Processing PNG"

handlers = {
    "jpg": jpg_handler,
    "png": png_handler
}

file_type = "png"

print(handlers[file_type]("image.png"))
```

### 📤 Output

```
Processing PNG
```

---

# 📌 Muhim eslatma

Funksiya **object sifatida uzatilganda qavs qo‘yilmaydi**.

❌ noto‘g‘ri

```python
execute_function(greet(), "Ali")
```

✔️ to‘g‘ri

```python
execute_function(greet, "Ali")
```

Sababi:

```
greet()
```

funksiyani **chaqiradi**

```
greet
```

esa **funksiya objectini beradi**

---

<br>
<br>
<br>
<br>
<br>

