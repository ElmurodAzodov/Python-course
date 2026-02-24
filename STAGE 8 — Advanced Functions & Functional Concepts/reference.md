
# **STAGE 8 — Advanced Functions & Functional Concepts**
<br> <br> <br> <br> <br>
# ⭐ Functions as First-Class Objects (Funksiyalar birinchi darajali obyektlar sifatida)

## 🧠 Asosiy g‘oya

Python’da **funksiyalar oddiy obyekt hisoblanadi**.

Bu nimani anglatadi?

👉 Funksiya:

* o‘zgaruvchiga saqlanishi mumkin
* boshqa funksiyaga argument sifatida berilishi mumkin
* funksiyadan qaytarilishi mumkin
* list, dict kabi strukturalarda saqlanishi mumkin

Ya’ni Python funksiyani **son, string yoki list bilan bir xil maqomda** ko‘radi.

Shuning uchun Python funksiyalari **first-class objects** deyiladi.

---

# 📌 1. Funksiyani o‘zgaruvchiga saqlash

Funksiya nomi aslida — funksiya obyektiga ishora qiluvchi referens.

```python
def greet(name):
    return f"Hello, {name}"

say_hello = greet   # funksiyani o‘zgaruvchiga berdik

print(say_hello("Ali"))
```

📤 Natija:

```
Hello, Ali
```

👉 Bu yerda `say_hello` ham `greet` bilan bir xil funksiyani ko‘rsatmoqda.

---

# 📌 2. Funksiyani argument sifatida uzatish

Funksiyani boshqa funksiyaga berish mumkin.

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def process(func, message):
    return func(message)

print(process(shout, "hello"))
print(process(whisper, "HELLO"))
```

📤 Natija:

```
HELLO
hello
```

👉 `func` parametriga funksiya berildi.

Bu yondashuv **functional programming** ning asosiy g‘oyalaridan biri.

---

# 📌 3. Funksiyani funksiyadan qaytarish

Funksiya boshqa funksiyani qaytarishi mumkin.

```python
def choose_operation(op):

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    if op == "add":
        return add
    else:
        return multiply

operation = choose_operation("add")
print(operation(3, 4))
```

📤 Natija:

```
7
```

👉 Bu juda muhim konsept:
**funksiya – dinamik ravishda yaratiladigan obyekt**

---

# 📌 4. Funksiyalarni strukturalarda saqlash

Funksiyalarni list yoki dict ichida ham saqlash mumkin.

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

operations = {
    "add": add,
    "sub": sub
}

print(operations["add"](10, 5))
```

📤 Natija:

```
15
```

👉 Bu dizayn pattern ko‘p joyda ishlatiladi:

* kalkulyatorlar
* buyruq tizimlari
* API routing
* plugin tizimlari

---

# 📌 5. Funksiyaning o‘zi ham obyekt

Funksiya ham boshqa obyektlar kabi:

* atributga ega
* tipga ega
* xotirada saqlanadi

```python
def hello():
    pass

print(type(hello))
```

📤 Natija:

```
<class 'function'>
```

👉 Demak Python uchun funksiya oddiy obyekt.

---

# 📌 6. Funksiyalarni inline ishlatish (callback tushunchasi)

Ko‘pincha funksiyalar boshqa funksiyaga **callback** sifatida uzatiladi.

```python
def greet(name):
    return f"Hello {name}"

names = ["Ali", "Vali", "Sami"]

result = list(map(greet, names))
print(result)
```

📤 Natija:

```
['Hello Ali', 'Hello Vali', 'Hello Sami']
```

👉 `greet` bu yerda callback sifatida ishladi.

---

# 📌 7. Nima uchun bu muhim?

First-class functions Python’ni:

✅ moslashuvchan qiladi
✅ kodni qisqartiradi
✅ decoratorlar ishlashiga asos bo‘ladi
✅ functional programming imkonini beradi
✅ frameworklar ishlashiga sabab bo‘ladi

Masalan:

* Flask routing
* Django middleware
* decorators
* callbacks
* async programming

Barchasi shu konseptga tayanadi.

---

# 🧩 Real hayotiy misol

Kalkulyatorni funksiyalar orqali yozish:

```python
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(add, 10, 5))
print(calculate(mul, 10, 5))
```

👉 Bu dizayn OOPsiz ham juda kuchli arxitektura beradi.

---
<br> <br> <br> <br> <br>

# λ Lambda Functions (Anonim funksiyalar)

## 🧠 Asosiy g‘oya

**Lambda funksiya** — bu **nomi yo‘q, qisqa, bir qatordan iborat funksiya**.

Oddiy `def` bilan yoziladigan kichik funksiyalarni tez yozish uchun ishlatiladi.

👉 Lambda funksiyalar:

* nomga ega bo‘lmaydi
* faqat **bitta expression** yoziladi
* avtomatik `return` qiladi
* qisqa kodlar uchun ideal

---

# 📌 1. Oddiy funksiya vs lambda

### Oddiy funksiya

```python
def square(x):
    return x * x

print(square(5))
```

### Lambda bilan

```python
square = lambda x: x * x
print(square(5))
```

📤 Natija:

```
25
```

👉 Ko‘rib turganingizdek, lambda:

* `def` yo‘q
* `return` yo‘q
* `{}` blok yo‘q

---

# 📌 2. Lambda sintaksisi

```python
lambda arguments: expression
```

Masalan:

```python
lambda x: x + 10
lambda a, b: a * b
lambda name: f"Hello {name}"
```

---

# 📌 3. Bir nechta parametrli lambda

```python
add = lambda a, b: a + b
print(add(3, 7))
```

📤 Natija:

```
10
```

---

# 📌 4. Lambda darhol chaqirilishi mumkin

```python
print((lambda x: x * 2)(5))
```

📤 Natija:

```
10
```

👉 Bu yerda lambda yaratilgan zahoti ishladi.

---

# 📌 5. Lambda ko‘pincha callback sifatida ishlatiladi

Lambda eng ko‘p ishlatiladigan joy:

* `map()`
* `filter()`
* `sorted()`
* `min()/max()`

---

# 📌 6. map() bilan lambda

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x**2, numbers))
print(squares)
```

📤 Natija:

```
[1, 4, 9, 16]
```

👉 Bu yerda alohida funksiya yozishga hojat qolmadi.

---

# 📌 7. filter() bilan lambda

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
```

📤 Natija:

```
[2, 4, 6]
```

👉 Lambda filtr sharti sifatida ishladi.

---

# 📌 8. sorted() bilan lambda

Eng mashhur qo‘llanishlardan biri:

```python
students = [
    ("Ali", 85),
    ("Vali", 72),
    ("Sami", 90)
]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
```

📤 Natija:

```
[('Vali', 72), ('Ali', 85), ('Sami', 90)]
```

👉 Bu yerda lambda:

* tuple ichidagi 2-element bo‘yicha saraladi

---

# 📌 9. Lambda ichida shart (if-else)

Lambda expression bo‘lgani uchun **ternary if** ishlatiladi.

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))
```

📤 Natija:

```
Odd
```

---

# 📌 10. Lambda cheklovlari

Lambda **hamma joyda ishlatilmaydi**.

❌ ichida:

* bir nechta statement bo‘lmaydi
* assignment bo‘lmaydi
* loop yozib bo‘lmaydi
* print kabi statementlar ishlatilmaydi

Masalan bu noto‘g‘ri:

```python
lambda x:
    y = x + 1   # ❌ mumkin emas
    return y
```

Lambda faqat **bitta expression** uchun.

---

# 📌 11. Qachon lambda ishlatish kerak?

Lambda yaxshi:

✅ qisqa transformatsiya
✅ callback funksiyalar
✅ map/filter/sorted
✅ functional programming

Lambda yomon:

❌ katta logika
❌ murakkab shartlar
❌ o‘qilishi qiyin bo‘lsa

👉 Qoida:

> Agar lambda o‘qilishi qiyinlashsa — oddiy funksiya yozing.

---

# 🧩 Real hayotiy misol

Mahsulotlarni narx bo‘yicha saralash:

```python
products = [
    {"name": "Phone", "price": 500},
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25}
]

sorted_products = sorted(products, key=lambda p: p["price"])
print(sorted_products)
```

👉 Bu professional kodlarda juda ko‘p ishlatiladi.

---
 <br> <br> <br> <br> <br>

# 🗺️ map() funksiyasi

## 🧠 Asosiy g‘oya

`map()` — bu Python’dagi **functional programming** vositasi bo‘lib, u **iterable ichidagi har bir elementga funksiya qo‘llaydi**.

👉 Oddiy qilib aytganda:

> map() = har bir elementni o‘zgartiradi

---

# 📌 1. map() sintaksisi

```python
map(function, iterable)
```

* `function` → har elementga qo‘llanadigan funksiya
* `iterable` → list, tuple, string va hokazo

Natijada `map` **iterator obyekt** qaytaradi.

Shuning uchun uni ko‘pincha `list()` ga o‘rab ishlatamiz.

---

# 📌 2. Oddiy misol

```python
numbers = [1, 2, 3, 4]

def square(x):
    return x ** 2

result = map(square, numbers)
print(list(result))
```

📤 Natija:

```
[1, 4, 9, 16]
```

👉 map har bir elementga `square()` ni qo‘lladi.

---

# 📌 3. Lambda bilan map()

Eng ko‘p ishlatiladigan usul 👇

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x**2, numbers))
print(result)
```

📤 Natija:

```
[1, 4, 9, 16]
```

👉 Bu professional kodlarda juda keng tarqalgan.

---

# 📌 4. map() bir nechta iterable bilan

Agar funksiya bir nechta argument olsa,
map ham bir nechta iterable qabul qiladi.

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))
print(result)
```

📤 Natija:

```
[5, 7, 9]
```

👉 map elementlarni indeks bo‘yicha juftlab ishlaydi.

---

# 📌 5. map() stringlar bilan

```python
names = ["ali", "vali", "sami"]

result = list(map(str.upper, names))
print(result)
```

📤 Natija:

```
['ALI', 'VALI', 'SAMI']
```

👉 Funksiya sifatida built-in metod ham berilishi mumkin.

---

# 📌 6. map() ni for loop bilan solishtirish

### Oddiy for loop

```python
numbers = [1, 2, 3, 4]
result = []

for n in numbers:
    result.append(n**2)
```

### map bilan

```python
result = list(map(lambda x: x**2, numbers))
```

👉 map:

* qisqa
* deklarativ
* functional uslub

---

# 📌 7. map() iterator qaytaradi

```python
nums = [1, 2, 3]

mapped = map(lambda x: x*2, nums)
print(mapped)
```

📤 Natija:

```
<map object at 0x...>
```

👉 Shuning uchun uni odatda:

```python
list(mapped)
```

ga o‘tkazamiz.

---

# 📌 8. map() ni list comprehension bilan solishtirish

### map()

```python
list(map(lambda x: x*2, nums))
```

### list comprehension

```python
[x*2 for x in nums]
```

👉 Python’da ko‘pincha **list comprehension afzal**,
lekin map quyidagi joylarda kuchli:

* mavjud funksiya bo‘lsa
* callback kerak bo‘lsa
* functional style ishlatilsa

---

# 📌 9. Real hayotiy misol

Foydalanuvchi kiritgan sonlarni integerga aylantirish:

```python
nums = input("Sonlarni kiriting: ").split()

nums = list(map(int, nums))
print(nums)
```

👉 Bu real loyihalarda juda ko‘p ishlatiladi.

---

# 📌 10. map() chaining (bir nechta map ketma-ket)

```python
nums = [1, 2, 3, 4]

result = map(lambda x: x*2, nums)
result = map(lambda x: x+1, result)

print(list(result))
```

📤 Natija:

```
[3, 5, 7, 9]
```

👉 Bu functional pipeline deyiladi.

---

# 📌 11. Qachon map ishlatish kerak?

map yaxshi:

✅ elementlarni transformatsiya qilish
✅ mavjud funksiya qo‘llash
✅ functional uslub yozish
✅ pipeline qurish

map yomon:

❌ murakkab logika

❌ ko‘p shartlar

❌ o‘qilishi qiyin bo‘lsa

👉 Qoida:

> Agar transformatsiya oddiy bo‘lsa — map ishlating
> Agar logika murakkab bo‘lsa — for yoki comprehension ishlating

---
<br> <br> <br> <br> <br>

# 🔍 filter() funksiyasi

## 🧠 Asosiy g‘oya

`filter()` — bu iterable ichidan **shartga mos keladigan elementlarni tanlab oluvchi funksiya**.

👉 Oddiy qilib:

> filter() = saralash / tanlash funksiyasi

Agar `map()` elementni o‘zgartirsa,
`filter()` elementni **qoldiradi yoki tashlab yuboradi**.

---

# 📌 1. filter() sintaksisi

```python
filter(function, iterable)
```

* `function` → True/False qaytaradigan funksiya
* `iterable` → list, tuple, string va boshqalar

Natija → **filter obyekt (iterator)**

Ko‘pincha `list()` bilan o‘raladi.

---

# 📌 2. Oddiy misol

```python
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)
print(list(result))
```

📤 Natija:

```
[2, 4, 6]
```

👉 Faqat juft sonlar qoldi.

---

# 📌 3. Lambda bilan filter()

Eng keng tarqalgan usul 👇

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)
```

📤 Natija:

```
[2, 4, 6]
```

👉 Lambda shart sifatida ishladi.

---

# 📌 4. filter() stringlar bilan

```python
names = ["Ali", "Vali", "Sami", "Aziza"]

result = list(filter(lambda name: len(name) > 4, names))
print(result)
```

📤 Natija:

```
['Aziza']
```

👉 Faqat uzunligi 4 dan katta stringlar qoldi.

---

# 📌 5. filter() True qiymatlarni ajratish

Agar `function=None` berilsa, filter **truthy qiymatlarni** qoldiradi.

```python
data = [0, 1, False, True, "", "Hello", None]

result = list(filter(None, data))
print(result)
```

📤 Natija:

```
[1, True, 'Hello']
```

👉 False qiymatlar olib tashlandi.

---

# 📌 6. filter() ni for loop bilan solishtirish

### Oddiy for loop

```python
nums = [1,2,3,4,5,6]
evens = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
```

### filter bilan

```python
evens = list(filter(lambda x: x%2==0, nums))
```

👉 filter:

* qisqa
* deklarativ
* functional style

---

# 📌 7. filter() iterator qaytaradi

```python
nums = [1,2,3]

f = filter(lambda x: x>1, nums)
print(f)
```

📤 Natija:

```
<filter object at 0x...>
```

👉 Shuning uchun odatda `list()` ishlatiladi.

---

# 📌 8. filter() vs list comprehension

### filter()

```python
list(filter(lambda x: x%2==0, nums))
```

### list comprehension

```python
[x for x in nums if x%2==0]
```

👉 Python’da ko‘pincha comprehension o‘qilishi osonroq.

Lekin filter kuchli:

* mavjud funksiya bo‘lsa
* callback ishlatilsa
* pipeline qurilsa

---

# 📌 9. Real hayotiy misol

Foydalanuvchi kiritgan email ro‘yxatidan bo‘shlarini olib tashlash:

```python
emails = ["a@mail.com", "", "b@mail.com", "", "c@mail.com"]

valid = list(filter(None, emails))
print(valid)
```

👉 Bu real backend kodlarda juda ko‘p uchraydi.

---

# 📌 10. map + filter pipeline

```python
nums = [1,2,3,4,5,6]

result = map(lambda x: x*2, nums)
result = filter(lambda x: x>5, result)

print(list(result))
```

📤 Natija:

```
[6, 8, 10, 12]
```

👉 Bu functional pipeline deyiladi.

---

# 📌 11. Qachon filter ishlatish kerak?

filter yaxshi:

✅ elementlarni tanlash
✅ oddiy shartlar
✅ pipeline qurish
✅ functional style

filter yomon:

❌ murakkab logika

❌ ko‘p shartlar

❌ o‘qilishi qiyin bo‘lsa

👉 Qoida:

> Agar faqat tanlash bo‘lsa → filter
> Agar transformatsiya bo‘lsa → map
> Agar ikkalasi bo‘lsa → pipeline

---

<br> <br> <br> <br> <br>

# 📊 reduce() funksiyasi

## 🧠 Asosiy g‘oya

`reduce()` — iterable ichidagi barcha elementlarni **bitta yakuniy qiymatga keltirib chiqaruvchi funksiya**.

👉 Oddiy qilib:

> reduce() = yig‘ish / umumlashtirish funksiyasi

Agar:

* `map()` → o‘zgartiradi
* `filter()` → tanlaydi
* `reduce()` → **hammasini bitta natijaga yig‘adi**

---

# 📌 1. reduce() qayerdan olinadi?

`reduce()` built-in emas. U **functools** modulida joylashgan.

```python
from functools import reduce
```

---

# 📌 2. reduce() sintaksisi

```python
reduce(function, iterable[, initial])
```

* `function` → 2 ta argument oladi
* `iterable` → list, tuple va hokazo
* `initial` → boshlang‘ich qiymat (ixtiyoriy)

---

# 📌 3. reduce qanday ishlaydi?

Masalan:

```python
[1, 2, 3, 4]
```

reduce qo‘llansa:

```
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

👉 Natija: **10**

---

# 📌 4. Oddiy misol — yig‘indi

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)
print(result)
```

📤 Natija:

```
10
```

👉 Bu barcha elementlarni qo‘shib chiqdi.

---

# 📌 5. reduce bosqichma-bosqich ishlashi

```python
numbers = [1,2,3,4]
```

reduce ishlashi:

```
step1: a=1, b=2 → 3
step2: a=3, b=3 → 6
step3: a=6, b=4 → 10
```

👉 Har safar oldingi natija keyingi hisobga kiradi.

---

# 📌 6. Ko‘paytma topish

```python
from functools import reduce

numbers = [1, 2, 3, 4]

product = reduce(lambda a, b: a * b, numbers)
print(product)
```

📤 Natija:

```
24
```

👉 Bu factorial hisoblashga o‘xshaydi.

---

# 📌 7. initial qiymat bilan reduce

```python
from functools import reduce

nums = [1, 2, 3]

result = reduce(lambda a, b: a + b, nums, 10)
print(result)
```

📤 Natija:

```
16
```

👉 Chunki hisoblash:

```
10 + 1 = 11
11 + 2 = 13
13 + 3 = 16
```

---

# 📌 8. reduce() string bilan

```python
from functools import reduce

words = ["Python", "is", "awesome"]

sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)
```

📤 Natija:

```
Python is awesome
```

👉 Bu stringlarni birlashtirdi.

---

# 📌 9. Eng katta elementni topish

```python
from functools import reduce

nums = [5, 8, 2, 11, 3]

maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)
```

📤 Natija:

```
11
```

👉 Bu max() funksiyasining qo‘lda yozilgan versiyasi.

---

# 📌 10. reduce vs for loop

### for loop

```python
total = 0
for n in nums:
    total += n
```

### reduce

```python
reduce(lambda a, b: a + b, nums)
```

👉 reduce:

* qisqa
* functional style
* pipeline uchun ideal

---

# 📌 11. reduce() qachon ishlatish kerak?

reduce yaxshi:

✅ yig‘indi / ko‘paytma
✅ umumlashtirish
✅ pipeline oxiri
✅ functional programming

reduce yomon:

❌ murakkab logika

❌ o‘qilishi qiyin bo‘lsa

❌ oddiy sum() bilan hal bo‘lsa

👉 Python qoidasiga ko‘ra:

> Agar built-in funksiya mavjud bo‘lsa — reduce ishlatmaslik kerak.

Masalan:

```python
sum(nums)        # yaxshi
reduce(...)      # ortiqcha
```

---

# 📌 12. map + filter + reduce pipeline

```python
from functools import reduce

nums = [1,2,3,4,5,6]

result = map(lambda x: x*2, nums)
result = filter(lambda x: x>5, result)
result = reduce(lambda a,b: a+b, result)

print(result)
```

📤 Natija:

```
36
```

👉 Bu to‘liq functional pipeline:

1. transform
2. filter
3. aggregate

---

<br> <br> <br> <br> <br>

# 🔁 Recursion (Rekursiya)

## 🧠 Asosiy g‘oya

**Rekursiya** — bu funksiya **o‘zini o‘zi chaqirishi**.

👉 Oddiy qilib:

> Funksiya muammoni kichik qismlarga bo‘lib, o‘zini qayta chaqirib yechadi.

Rekursiya matematik, algoritmik va funksional dasturlashda juda muhim.

---

# 📌 1. Rekursiyaning 2 ta asosiy qismi

Har qanday rekursiv funksiya 2 qismdan iborat bo‘ladi:

### 1️⃣ Base case (to‘xtash sharti)

Funksiya qachon to‘xtashi kerakligini belgilaydi.

### 2️⃣ Recursive case (o‘zini chaqirish)

Muammoni kichikroq shaklda qayta ishlaydi.

👉 Agar base case bo‘lmasa — **infinite recursion** bo‘ladi.

---

# 📌 2. Eng oddiy rekursiya misoli

```python
def countdown(n):
    if n == 0:           # base case
        print("Done")
    else:
        print(n)
        countdown(n-1)   # recursive call

countdown(5)
```

📤 Natija:

```
5
4
3
2
1
Done
```

👉 Har chaqirish muammoni kichraytiradi.

---

# 📌 3. Rekursiyaning klassik misoli — factorial

Matematik formula:

```
n! = n * (n-1)!
```

### Rekursiv yechim

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

📤 Natija:

```
120
```

---

# 📌 4. Rekursiya qanday ishlaydi (stack tushunchasi)

`factorial(4)` chaqirilsa:

```
factorial(4)
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1 * factorial(0)
```

So‘ng:

```
factorial(0) → 1
```

va natija orqaga hisoblanadi.

👉 Bu jarayon **call stack** orqali ishlaydi.

---

# 📌 5. Fibonacci rekursiya

Fibonacci formulasi:

```
F(n) = F(n-1) + F(n-2)
```

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))
```

📤 Natija:

```
8
```

👉 Bu rekursiyaning klassik o‘quv misoli.

---

# 📌 6. Rekursiya vs loop

### Loop bilan factorial

```python
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```

### Rekursiya bilan

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
```

👉 Rekursiya:

* qisqa
* matematikaga yaqin
* ba’zan tushunarliroq

---

# 📌 7. Rekursiya ishlatiladigan joylar

Rekursiya juda muhim algoritmlarda ishlatiladi:

✅ daraxtlar (tree traversal)
✅ graf algoritmlari
✅ DFS/BFS
✅ divide & conquer
✅ quicksort / mergesort
✅ backtracking
✅ dynamic programming

---

# 📌 8. Rekursiv fayl tizimi yurish

```python
import os

def show_files(path):
    for item in os.listdir(path):
        full = os.path.join(path, item)
        print(full)
        if os.path.isdir(full):
            show_files(full)
```

👉 Bu real rekursiv struktura.

---

# 📌 9. Rekursiya xavfi — RecursionError

Python stack cheklangan.

```python
def bad():
    return bad()

bad()
```

📤 Natija:

```
RecursionError: maximum recursion depth exceeded
```

👉 Shuning uchun base case majburiy.

---

# 📌 10. Tail recursion tushunchasi

Ba’zi tillarda tail recursion optimizatsiya qilinadi.

Python’da esa **tail recursion optimization yo‘q**.

Shuning uchun chuqur rekursiya:

* sekin ishlaydi
* xotira ko‘p yeydi

👉 Ko‘p hollarda loop yaxshiroq.

---

# 📌 11. Qachon rekursiya ishlatish kerak?

Rekursiya yaxshi:

✅ daraxt strukturalari
✅ matematik formulalar
✅ divide & conquer
✅ backtracking
✅ DFS

Rekursiya yomon:

❌ oddiy sikl ishlasa
❌ chuqur stack bo‘lsa
❌ tezlik muhim bo‘lsa

👉 Qoida:

> Agar muammo tabiatan rekursiv bo‘lsa — rekursiya ishlating.

---

# 🧩 Real hayotiy misol — nested list yig‘ish

```python
def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

print(sum_nested([1,2,[3,4,[5]]]))
```

📤 Natija:

```
15
```

👉 Bu rekursiya uchun ideal masala.

---
<br> <br> <br> <br> <br>

# 🔒 Closures (Yopiq muhitli funksiyalar)

## 🧠 Asosiy g‘oya

**Closure** — bu **ichki funksiya tashqi funksiyaning o‘zgaruvchilarini eslab qolishi**.

👉 Oddiy qilib:

> Funksiya yaratilgan muhitni unutmaydi.

Funksiya tashqaridagi o‘zgaruvchilarni saqlab qoladi va keyinchalik ishlata oladi.

---

# 📌 1. Ichki funksiya (nested function)

Avval oddiy ichki funksiyani ko‘ramiz:

```python id="ovx4p4"
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()
```

📤 Natija:

```id="fcfs3e"
Hello
```

👉 `inner()` tashqi `message` ni ko‘rdi.

Bu hali closure emas, bu oddiy nested function.

---

# 📌 2. Closure qachon paydo bo‘ladi?

Closure bo‘lishi uchun:

1️⃣ ichki funksiya bo‘lishi kerak
2️⃣ tashqi o‘zgaruvchini ishlatishi kerak
3️⃣ tashqi funksiya ichki funksiyani qaytarishi kerak

---

# 📌 3. Eng oddiy closure misoli

```python id="ho1fs7"
def outer():
    message = "Hello from closure"

    def inner():
        print(message)

    return inner

func = outer()
func()
```

📤 Natija:

```id="x8mrkb"
Hello from closure
```

👉 `outer()` tugagan bo‘lsa ham,
`inner()` hali ham `message` ni eslab turibdi.

Bu — **closure**.

---

# 📌 4. Closure qanday ishlaydi?

Python ichki funksiya uchun:

* kodni saqlaydi
* tashqi o‘zgaruvchilarni saqlaydi
* ularni xotirada yopib qo‘yadi

👉 Shuning uchun “closure” (yopilish) deyiladi.

---

# 📌 5. Parametrli closure

```python id="g5pl0h"
def multiplier(x):

    def multiply(n):
        return n * x

    return multiply

times3 = multiplier(3)
print(times3(10))
```

📤 Natija:

```id="2fpmuf"
30
```

👉 `x=3` closure ichida saqlanib qoldi.

Bu juda kuchli pattern.

---

# 📌 6. Bir nechta closure yaratish

```python id="8l6oz0"
times2 = multiplier(2)
times5 = multiplier(5)

print(times2(10))
print(times5(10))
```

📤 Natija:

```id="g7jrt0"
20
50
```

👉 Har closure o‘z muhitini alohida saqlaydi.

---

# 📌 7. Closure real hayotiy ishlatilishi

Closures quyidagi joylarda ishlatiladi:

✅ decoratorlar
✅ factory functions
✅ caching
✅ stateful functions
✅ callback yaratish
✅ dependency injection

---

# 📌 8. Stateful function yaratish

Closure orqali funksiya ichida holat saqlash mumkin.

```python id="4y1ah8"
def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()

print(c())
print(c())
print(c())
```

📤 Natija:

```id="p3fx7n"
1
2
3
```

👉 Bu yerda `count` closure ichida yashab turibdi.

---

# 📌 9. nonlocal tushunchasi

Closure ichida tashqi o‘zgaruvchini o‘zgartirish uchun:

```python id="h09mt5"
nonlocal variable
```

ishlatiladi.

Aks holda Python uni local deb hisoblaydi.

---

# 📌 10. Closure introspection (tekshirish)

```python id="bsy7o7"
print(c.__closure__)
```

👉 Bu closure ichidagi o‘zgaruvchilarni ko‘rsatadi.

---

# 📌 11. Closure vs Class

Ko‘pincha closure class o‘rnini bosishi mumkin.

### Class

```python id="sblx38"
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count
```

### Closure

```python id="d3njuy"
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

👉 Closure ko‘pincha:

* qisqa
* yengil
* functional uslub

---

# 📌 12. Qachon closure ishlatish kerak?

Closure yaxshi:

✅ decorator yozishda
✅ state saqlashda
✅ factory funksiya yaratishda
✅ callback parametr berishda

Closure yomon:

❌ murakkab logika bo‘lsa

❌ ko‘p metod kerak bo‘lsa

❌ katta tizim bo‘lsa (class yaxshi)

---
<br> <br> <br> <br> <br>

# 🎨 Decorators (Funksiyani bezovchi / o‘rab oluvchi funksiya)

## 🧠 Asosiy g‘oya

**Decorator** — bu **funksiyani o‘zgartirmasdan unga qo‘shimcha xatti-harakat qo‘shuvchi funksiya**.

👉 Oddiy qilib:

> Decorator = funksiya ustiga funksiya o‘rash

---

# 📌 1. Nega decorator kerak?

Tasavvur qiling, sizda funksiya bor:

```python id="a9rx3k"
def say_hello():
    print("Hello")
```

Endi har safar:

* vaqtini o‘lchamoqchisiz
* log yozmoqchisiz
* permission tekshirmoqchisiz

Lekin funksiyani o‘zgartirishni xohlamaysiz.

👉 Mana shu yerda decorator ishlatiladi.

---

# 📌 2. Decorator aslida closure

Decorator — bu:

1️⃣ tashqi funksiya
2️⃣ ichki wrapper funksiya
3️⃣ closure

---

# 📌 3. Oddiy decorator yozish

```python id="sy6h39"
def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper
```

Endi uni ishlatamiz:

```python id="6n7ez7"
def say_hi():
    print("Hi")

say_hi = my_decorator(say_hi)

say_hi()
```

📤 Natija:

```id="xgnubj"
Before function
Hi
After function
```

👉 Funksiya o‘zgarmadi, lekin xulqi o‘zgardi.

---

# 📌 4. Python dekorator sintaksisi

Python’da maxsus sintaksis bor:

```python id="nd77hb"
@my_decorator
def say_hi():
    print("Hi")

say_hi()
```

👉 Bu quyidagiga teng:

```python id="0sawh4"
say_hi = my_decorator(say_hi)
```

---

# 📌 5. Argumentli decorator

Wrapper parametr qabul qilishi kerak:

```python id="y0p5l4"
def my_decorator(func):

    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")

    return wrapper
```

```python id="40qom3"
@my_decorator
def greet(name):
    print(f"Hello {name}")

greet("Ali")
```

📤 Natija:

```id="qt6u2k"
Before function
Hello Ali
After function
```

---

# 📌 6. Universal decorator (*args, **kwargs)

Professional decoratorlar shunday yoziladi:

```python id="qdcjfh"
def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper
```

👉 Bu har qanday funksiyaga ishlaydi.

---

# 📌 7. Real decorator — vaqt o‘lchash

```python id="p4xq4n"
import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end-start:.4f}s")
        return result

    return wrapper
```

```python id="4qql0k"
@timer
def slow():
    time.sleep(1)

slow()
```

👉 Bu professional debug tool.

---

# 📌 8. Real decorator — ruxsat tekshirish

```python id="z6d8i5"
def require_admin(func):

    def wrapper(user):
        if user != "admin":
            print("Access denied")
            return
        return func(user)

    return wrapper
```

```python id="8c9lo2"
@require_admin
def delete_db(user):
    print("Database deleted")

delete_db("guest")
delete_db("admin")
```

👉 Bu web backendda juda ko‘p ishlatiladi.

---

# 📌 9. Bir nechta decorator qo‘llash

```python id="s3qsgb"
@timer
@my_decorator
def hello():
    print("Hello")
```

👉 Pastdagisi birinchi ishlaydi.

Ya’ni:

```id="s8l6l8"
hello = timer(my_decorator(hello))
```

---

# 📌 10. functools.wraps (MUHIM!)

Decorator metadata’ni buzadi.

```python id="puyh25"
print(hello.__name__)
```

Natija → `"wrapper"`

Buni tuzatish uchun:

```python id="14r3c7"
from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

👉 Bu professional kod standarti.

---

# 📌 11. Parametrli decorator

Decorator ham parametr olishi mumkin.

```python id="owtptv"
def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

```python id="s1a8pq"
@repeat(3)
def say_hi():
    print("Hi")

say_hi()
```

📤 Natija:

```id="c6u91h"
Hi
Hi
Hi
```

👉 Bu advanced decorator.

---

# 📌 12. Decorator ishlatiladigan joylar

Decorators real loyihalarda:

✅ Flask routing

✅ Django views

✅ caching

✅ logging

✅ authorization

✅ retry system

✅ rate limiting

✅ validation

Masalan:

```python id="c1rb5g"
@app.route("/")
def home():
    ...
```

👉 Bu ham decorator.

---

<br> <br> <br> <br> <br>

# 📝 Function Annotations (Funksiya annotatsiyalari)

## 🧠 Asosiy g‘oya

**Function annotations** — bu funksiya parametrlarining va qaytariladigan qiymatning **tipini yoki ma’nosini ko‘rsatish uchun yoziladigan qo‘shimcha ma’lumot**.

👉 Oddiy qilib:

> Annotation = funksiya haqida metadata

Muhimi:

❗ Annotation Python tomonidan majburiy tekshirilmaydi
❗ Bu faqat ma’lumot (documentation + tooling uchun)

---

# 📌 1. Oddiy annotation sintaksisi

```python
def func(param: type) -> return_type:
    ...
```

---

# 📌 2. Oddiy misol

```python
def add(a: int, b: int) -> int:
    return a + b
```

👉 Bu degani:

* `a` va `b` — `int` bo‘lishi kutiladi
* natija — `int`

Lekin Python baribir tekshirmaydi:

```python
print(add("3", "4"))
```

📤 Natija:

```
34
```

👉 Annotation — majburiy emas, tavsiyaviy.

---

# 📌 3. Annotationlarni ko‘rish

Python annotationlarni saqlaydi.

```python
print(add.__annotations__)
```

📤 Natija:

```
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

👉 Bu metadata sifatida mavjud.

---

# 📌 4. Typing modulidan foydalanish

Murakkab tiplar uchun `typing` moduli ishlatiladi.

```python
from typing import List

def average(nums: List[int]) -> float:
    return sum(nums) / len(nums)
```

---

# 📌 5. Dict, Tuple, Optional

```python
from typing import Dict, Tuple, Optional

def process(data: Dict[str, int]) -> Tuple[str, int]:
    return max(data.items(), key=lambda x: x[1])

def find(name: str) -> Optional[str]:
    return name if name else None
```

👉 `Optional[str]` = `str | None`

---

# 📌 6. Python 3.10+ yangi sintaksis

Yangi usul 👇

```python
def greet(name: str | None) -> str:
    if name is None:
        return "Guest"
    return f"Hello {name}"
```

👉 Bu `Optional[str]` o‘rnini bosadi.

---

# 📌 7. Callable annotation

Funksiya parametr sifatida funksiya qabul qilsa:

```python
from typing import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)
```

👉 Bu functional programmingda juda muhim.

---

# 📌 8. Annotatsiyalarni real ishlatish

IDElar:

* PyCharm
* VS Code
* MyPy

annotatsiyalar asosida:

✅ xatolarni oldindan ko‘rsatadi
✅ autocomplete beradi
✅ refactoringni osonlashtiradi

---

# 📌 9. MyPy statik tekshiruv

Agar `mypy` ishlatsangiz:

```bash
mypy script.py
```

👉 noto‘g‘ri tiplar topiladi.

Bu enterprise Python’da standart hisoblanadi.

---

# 📌 10. Docstring vs Annotation

### Docstring

```python
def add(a, b):
    """Add two integers"""
```

### Annotation

```python
def add(a: int, b: int) -> int:
```

👉 Annotation ancha kuchli.

---

# 📌 11. Custom annotation yozish

Annotation faqat tip emas, istalgan qiymat bo‘lishi mumkin.

```python
def func(x: "must be positive"):
    ...
```

👉 Frameworklar bundan foydalanadi.

Masalan:

* FastAPI
* Pydantic
* dataclasses

---

# 📌 12. Real hayotiy misol (API function)

```python
from typing import List

def get_users(limit: int = 10) -> List[dict]:
    return [{"id": 1}, {"id": 2}]
```

👉 Bu professional API kodga o‘xshaydi.

---

# 📌 13. Nega annotation muhim?

Annotation:

✅ documentationni avtomatlashtiradi

✅ type safety beradi

✅ IDE yordam beradi

✅ static analiz imkonini beradi

✅ katta jamoalarda zarur

---