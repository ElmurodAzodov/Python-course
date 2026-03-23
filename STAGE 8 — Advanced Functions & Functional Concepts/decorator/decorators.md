
# **Decorators**
---

# 🔹 1. Eng sodda tushuncha

👉 **Decorator — bu funksiyani “o‘rab”, unga qo‘shimcha ish qo‘shadigan narsa.**

Ya’ni:

> Funksiyaning ichini o‘zgartirmaysan, lekin unga “qo‘shimcha harakatlar” qo‘shasan

---

# 🔹 2. Real hayotdan misol

Tasavvur qil:

🍬 Sen konfet sotib olding
🎁 Uni do‘konchi qog‘ozga o‘rab berdi

* Konfet o‘zi o‘zgarmadi
* Faqat tashqi tomondan qo‘shimcha qo‘shildi

👉 **Decorator ham xuddi shu:**

* funksiya = konfet
* decorator = o‘rov (wrapper)

---

# 🔹 3. Muammo: Nega kerak?

Faraz qil bizda 10 ta funksiya bor:

```python
def a():
    print("A ishladi")

def b():
    print("B ishladi")
```

Endi har safar:

* oldin: "Boshlanish"
* keyin: "Tugadi"

chiqarishni xohlaymiz:

```python
def a():
    print("Boshlanish")
    print("A ishladi")
    print("Tugadi")
```

❌ Muammo:

* 10 ta funksiyada bir xil kod yozish kerak
* bu **yomon (copy-paste)**

---

# 🔹 4. Yechim: Decorator

Decorator yordamida **bitta joyda yozib**, hamma funksiyaga qo‘llaymiz

---

# 🔹 5. Qanday ishlaydi (asosiy mexanizm)

### 1-qadam: wrapper yozamiz

```python
def decorator(func):
    def wrapper():
        print("Boshlanish")
        func()
        print("Tugadi")
    return wrapper
```

---

### 2-qadam: ishlatamiz

```python
def hello():
    print("Salom")

hello = decorator(hello)
hello()
```

📌 Nima bo‘ldi?

👉 Python shuni qildi:

```
hello → wrapper ga aylantirildi
```

---

# 🔹 6. @ belgi — qisqa yozish

```python
@decorator
def hello():
    print("Salom")
```

Bu aslida:

```python
hello = decorator(hello)
```

---

# 🔹 7. Qadam-baqadam ishlash jarayoni

Keling sekin ko‘ramiz:

```python
@decorator
def hello():
    print("Salom")
```

### Python nima qiladi:

1. `hello` funksiyani oladi
2. `decorator(hello)` ni chaqiradi
3. ichidan `wrapper` qaytadi
4. `hello = wrapper` bo‘ladi

---

# 🔹 8. Eng muhim gap

👉 Sen `hello()` chaqiryapsan deb o‘ylaysan
👉 Aslida `wrapper()` ishlayapti

---

# 🔹 9. Vizual tushuncha

```
hello()  → wrapper()
            ↓
      Boshlanish
      Salom
      Tugadi
```

---

# 🔹 10. Qachon ishlatiladi?

Decoratorlar juda ko‘p joyda ishlatiladi:

### ✅ 1. Login tekshirish

```python
@require_login
def profile():
    pass
```

---

### ✅ 2. Vaqt o‘lchash

```python
@timer
def heavy_function():
    pass
```

---

### ✅ 3. Logging (kim nima qildi)

```python
@logger
def delete_user():
    pass
```

---

### ✅ 4. API / Django / Flask

Masalan:

```python
@login_required
def dashboard():
    pass
```

---

<br>
<br>
<br>
<br>
<br>

# 🚀 Real loyiha: Login tizimi

Tasavvur qil:

* Sayting bor
* Ba’zi funksiyalar faqat login qilgan userlar uchun

---

# ❌ 1. Decoratorsiz (yomon usul)

```python
current_user = {"logged_in": False}

def dashboard():
    if not current_user["logged_in"]:
        print("Iltimos, login qiling!")
        return
    print("Dashboardga xush kelibsiz!")

def profile():
    if not current_user["logged_in"]:
        print("Iltimos, login qiling!")
        return
    print("Profil sahifasi")
```

😬 Muammo:

* Har funksiyada bir xil kod
* Copy-paste
* Katta projectda juda yomon

---

# ✅ 2. Decorator bilan (toza yechim)

## 1-qadam: decorator yozamiz

```python
def login_required(func):
    def wrapper():
        if not current_user["logged_in"]:
            print("Iltimos, login qiling!")
            return
        return func()
    return wrapper
```

---

## 2-qadam: funksiyalarga qo‘llaymiz

```python
@login_required
def dashboard():
    print("Dashboardga xush kelibsiz!")

@login_required
def profile():
    print("Profil sahifasi")
```

---

## 3-qadam: ishlatamiz

```python
dashboard()
profile()
```

📌 Natija:

```text
Iltimos, login qiling!
Iltimos, login qiling!
```

---

## 4-qadam: login qilamiz

```python
current_user["logged_in"] = True

dashboard()
profile()
```

📌 Natija:

```text
Dashboardga xush kelibsiz!
Profil sahifasi
```

---

# 🔥 NIMA BO‘LDI BU YERDA?

Sen yozding:

```python
@login_required
def dashboard():
```

Python aslida qildi:

```python
dashboard = login_required(dashboard)
```

---

# 🧠 Ichkarida nima bo‘lyapti?

1. `dashboard` → decoratorga berildi
2. decorator → `wrapper` qaytardi
3. `dashboard = wrapper` bo‘ldi

👉 Endi `dashboard()` chaqirsang:

```text
wrapper ishlaydi:
    → login tekshiradi
    → keyin original funksiyani chaqiradi
```

---

# 🔹 Yana real misol: vaqt o‘lchash

```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Vaqt:", end - start)
    return wrapper
```

---

```python
@timer
def heavy_task():
    for i in range(10000000):
        pass
```

```python
heavy_task()
```

📌 Natija:

```text
Vaqt: 0.35
```

---

# 🔹 Yana real misol: logging

```python
def logger(func):
    def wrapper():
        print(f"{func.__name__} ishga tushdi")
        return func()
    return wrapper
```

---

```python
@logger
def delete_user():
    print("User o‘chirildi")
```

---

# 🔥 Nega decorator juda muhim?

Chunki:

* 🔁 takroriy kodni yo‘q qiladi
* 🧼 kodni toza qiladi
* ⚙️ funksiyani o‘zgartirmasdan kengaytiradi
* 🚀 katta loyihalarda juda kerak

---