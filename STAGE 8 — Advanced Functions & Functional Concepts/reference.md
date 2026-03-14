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

# λ Lambda Functions (Anonymous, Single Expression)

Python’da **lambda function** — bu **nomi bo‘lmagan (anonymous)** kichik funksiya bo‘lib, **faqat bitta expression** dan iborat bo‘ladi.

Oddiy `def` bilan yoziladigan funksiyalarning **ixcham (short)** varianti sifatida ishlatiladi.

---

# 📌 1. Lambda Function Sintaksisi

### 🧠 Umumiy sintaksis

```python
lambda arguments: expression
```

| Qism         | Ma'nosi                         |
| ------------ | ------------------------------- |
| `lambda`     | lambda funksiya boshlanishi     |
| `arguments`  | parametrlar                     |
| `:`          | parametr va expression ajratadi |
| `expression` | hisoblanadigan qiymat           |

⚠️ Lambda funksiyada **faqat bitta expression bo‘lishi mumkin**.

---

# 📌 2. Oddiy funksiya vs Lambda

### 💻 Oddiy funksiya

```python
def add(a, b):
    return a + b

print(add(3, 5))
```

### 📤 Output

```
8
```

---

### 💻 Lambda varianti

```python
add = lambda a, b: a + b

print(add(3, 5))
```

### 📤 Output

```
8
```

### 🔍 Tushuntirish

| Kod           | Ma'nosi                |
| ------------- | ---------------------- |
| `lambda a, b` | parametrlar            |
| `:`           | expression boshlanishi |
| `a + b`       | natija                 |

Bu aslida quyidagiga teng:

```python
def add(a, b):
    return a + b
```

---

# 📌 3. Lambda funksiyani to‘g‘ridan-to‘g‘ri chaqirish

Lambda funksiyani **o‘zgaruvchiga saqlamasdan ham chaqirish mumkin**.

### 💻 Misol

```python
print((lambda a, b: a * b)(4, 6))
```

### 📤 Output

```
24
```

### 🔍 Tushuntirish

| Qism                | Ma'nosi             |
| ------------------- | ------------------- |
| `(lambda a,b: a*b)` | lambda funksiya     |
| `(4,6)`             | funksiya chaqirildi |

---

# 📌 4. Bitta parametrli lambda

```python
square = lambda x: x ** 2

print(square(5))
```

### 📤 Output

```
25
```

---

# 📌 5. Parametrsiz lambda

Lambda funksiyada **parametr bo‘lmasligi ham mumkin**.

```python
hello = lambda: "Hello Python"

print(hello())
```

### 📤 Output

```
Hello Python
```

---

# 📌 6. Lambda ichida shart (if expression)

Lambda funksiyada **if-else expression** ishlatish mumkin.

### 💻 Misol

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))
```

### 📤 Output

```
Even
Odd
```

---

# 📌 7. Lambda bilan sorting

Lambda ko‘pincha **sorting key** sifatida ishlatiladi.

### 💻 Misol

```python
students = [
    ("Ali", 85),
    ("Vali", 92),
    ("Hasan", 78)
]

students.sort(key=lambda x: x[1])

print(students)
```

### 📤 Output

```
[('Hasan', 78), ('Ali', 85), ('Vali', 92)]
```

### 🔍 Tushuntirish

| Qism            | Ma'nosi                       |
| --------------- | ----------------------------- |
| `x`             | tuple                         |
| `x[1]`          | baho                          |
| `sort(key=...)` | shu qiymat bo‘yicha saralaydi |

---

# 📌 8. Lambda bilan list transformatsiya

Lambda funksiyalar **data transformation** uchun juda qulay.

### 💻 Misol

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))

print(squares)
```

### 📤 Output

```
[1, 4, 9, 16, 25]
```

---

# 📌 9. Lambda bilan filter

### 💻 Misol

```python
numbers = [1,2,3,4,5,6,7,8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

### 📤 Output

```
[2, 4, 6, 8]
```

---

# 📌 10. Lambda bilan dictionary

```python
users = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 19},
    {"name": "Hasan", "age": 30}
]

users.sort(key=lambda user: user["age"])

print(users)
```

### 📤 Output

```
[
 {'name': 'Vali', 'age': 19},
 {'name': 'Ali', 'age': 25},
 {'name': 'Hasan', 'age': 30}
]
```

---

# 📌 11. Lambda ichida bir nechta parametr

```python
multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))
```

### 📤 Output

```
24
```

---

# 📌 12. Lambda limitationlari

Lambda funksiyalar **faqat bitta expression** qabul qiladi.

❌ Noto‘g‘ri:

```python
lambda x:
    y = x + 2
    return y
```

Sababi:

* assignment
* multiple statements
* loops
* return

lambda ichida ishlamaydi.

---

# 📌 13. Qachon lambda ishlatish kerak

Lambda **kichik va bir martalik funksiyalar** uchun ishlatiladi.

Masalan:

* `map()`
* `filter()`
* `sorted()`
* `min()`
* `max()`

---

# 📌 14. Qachon lambda ishlatmaslik kerak

Agar funksiya:

* katta bo‘lsa
* ko‘p qatorli bo‘lsa
* murakkab logika bo‘lsa

unda **def ishlatish tavsiya qilinadi**.

❌ Yomon kod

```python
result = lambda x: (x*2 + 5) / 3 if x > 10 else (x+7) * 4
```

✔️ Yaxshi kod

```python
def calculate(x):
    if x > 10:
        return (x*2 + 5) / 3
    else:
        return (x+7) * 4
```

---

# 📌 15. Lambda va Higher-Order Functions

Lambda ko‘pincha **higher-order functions** bilan ishlaydi.

Masalan:

```python
map()
filter()
reduce()
sorted()
min()
max()
```

Sababi:

bu funksiyalar **funksiyani argument sifatida qabul qiladi**.

---

<br>
<br>
<br>
<br>
<br>

# 🗺️ `map()` — Transform Iterable

Python’da `map()` funksiyasi **iterable ichidagi har bir elementga bir xil funksiyani qo‘llash** uchun ishlatiladi.

Bu jarayon **transformatsiya (transform)** deb ataladi.

Ya'ni:

```
input iterable  →  function apply  →  transformed iterable
```

---

# 📌 1. `map()` sintaksisi

```python
map(function, iterable)
```

| Qism       | Ma'nosi                                  |
| ---------- | ---------------------------------------- |
| `function` | har bir elementga qo‘llanadigan funksiya |
| `iterable` | list, tuple, set yoki boshqa iterable    |

Natija: **map object** qaytaradi.

Shuning uchun ko‘pincha:

```python
list(map(...))
```

ishlatiladi.

---

# 📌 2. Oddiy misol

### 💻 Masala

List ichidagi barcha sonlarni **kvadratga oshirish**.

---

### 🧠 Oddiy usul

```python
numbers = [1, 2, 3, 4, 5]

result = []

for n in numbers:
    result.append(n ** 2)

print(result)
```

### 📤 Output

```
[1, 4, 9, 16, 25]
```

---

### 💻 `map()` bilan

```python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

result = list(map(square, numbers))

print(result)
```

### 📤 Output

```
[1, 4, 9, 16, 25]
```

### 🔍 Tushuntirish

`map()` quyidagi ishni bajaradi:

```
square(1)
square(2)
square(3)
square(4)
square(5)
```

Natijalarni iterable ko‘rinishida qaytaradi.

---

# 📌 3. Lambda bilan `map()`

Ko‘pincha `map()` **lambda funksiyalar bilan ishlatiladi**.

### 💻 Misol

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)
```

### 📤 Output

```
[1, 4, 9, 16, 25]
```

Bu eng ko‘p ishlatiladigan `map()` patternlaridan biri.

---

# 📌 4. String transformatsiya

### 💻 Misol

List ichidagi barcha so‘zlarni **katta harfga o‘tkazish**.

```python
names = ["ali", "vali", "hasan"]

result = list(map(str.upper, names))

print(result)
```

### 📤 Output

```
['ALI', 'VALI', 'HASAN']
```

### 🔍 Tushuntirish

Bu yerda:

```
str.upper
```

funksiya sifatida uzatildi.

---

# 📌 5. Bir nechta iterable bilan `map()`

`map()` bir nechta iterable bilan ham ishlay oladi.

Bu holda funksiyaga **har bir iterable dan bittadan element beriladi**.

---

### 💻 Misol

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))

print(result)
```

### 📤 Output

```
[5, 7, 9]
```

### 🔍 Tushuntirish

`map()` quyidagicha ishlaydi:

```
1 + 4
2 + 5
3 + 6
```

---

# 📌 6. String → Integer konvertatsiya

Ko‘pincha `map()` **type conversion** uchun ishlatiladi.

### 💻 Misol

```python
numbers = ["1", "2", "3", "4"]

result = list(map(int, numbers))

print(result)
```

### 📤 Output

```
[1, 2, 3, 4]
```

Bu juda keng tarqalgan pattern.

---

# 📌 7. Input bilan ishlash

### 💻 Misol

```python
numbers = list(map(int, input().split()))

print(numbers)
```

### Tushuntirish

```
input() → string
split() → list[str]
map(int, ...) → list[int]
```

Masalan:

```
Input:
10 20 30
```

```
Output:
[10, 20, 30]
```

---

# 📌 8. `map` object nima?

`map()` darhol list qaytarmaydi.

U **lazy iterator** qaytaradi.

### 💻 Misol

```python
numbers = [1,2,3]

result = map(lambda x: x*2, numbers)

print(result)
```

### 📤 Output

```
<map object at 0x...>
```

Shuning uchun ko‘pincha:

```python
list(map(...))
```

ishlatiladi.

---

# 📌 9. `map()` va list comprehension

Ko‘pincha `map()` o‘rniga **list comprehension** ishlatiladi.

---

### 💻 map()

```python
numbers = [1,2,3,4]

result = list(map(lambda x: x**2, numbers))
```

---

### 💻 list comprehension

```python
numbers = [1,2,3,4]

result = [x**2 for x in numbers]
```

Natija bir xil:

```
[1,4,9,16]
```

---

### Qaysi biri yaxshi?

| Usul          | Qachon ishlatish       |
| ------------- | ---------------------- |
| `map()`       | funksiya tayyor bo‘lsa |
| comprehension | ko‘proq pythonic       |

---

# 📌 10. Real Example — Data Processing

### 💻 Misol

```python
prices = [100, 200, 300]

taxed_prices = list(map(lambda p: p * 1.12, prices))

print(taxed_prices)
```

### 📤 Output

```
[112.0, 224.0, 336.0]
```

---

# 📌 11. `map()` bilan tuple ishlatish

```python
numbers = (1, 2, 3)

result = list(map(lambda x: x + 10, numbers))

print(result)
```

### 📤 Output

```
[11, 12, 13]
```

---

# 📌 12. `map()` bilan bir nechta operatsiya

### 💻 Misol

```python
data = [1, 2, 3, 4]

result = list(map(lambda x: (x, x**2, x**3), data))

print(result)
```

### 📤 Output

```
[(1,1,1), (2,4,8), (3,9,27), (4,16,64)]
```

---

# 📌 13. `map()` ning ishlash modeli

`map()` quyidagi prinsip asosida ishlaydi:

```
for element in iterable:
    function(element)
```

ya'ni:

```
map(f, [a,b,c])
```

aslida:

```
[f(a), f(b), f(c)]
```

---

<br>
<br>
<br>
<br>
<br>

# 🔍 `filter()` — Select Items from Iterable

Python’da `filter()` funksiyasi **iterable ichidan ma'lum shartga mos keladigan elementlarni tanlab olish** uchun ishlatiladi.

Agar `map()` **transform** qilsa,
`filter()` esa **elementlarni saralab (select)** beradi.

```
iterable → condition check → filtered iterable
```

---

# 📌 1. `filter()` sintaksisi

```python
filter(function, iterable)
```

| Qism       | Ma'nosi                             |
| ---------- | ----------------------------------- |
| `function` | har element uchun shart             |
| `iterable` | list, tuple, set va boshqa iterable |

Funksiya **True yoki False** qaytarishi kerak.

```
True  → element saqlanadi
False → element chiqarib tashlanadi
```

Natija: **filter object (iterator)** qaytaradi.

Shuning uchun ko‘pincha:

```python
list(filter(...))
```

ishlatiladi.

---

# 📌 2. Oddiy misol — Juft sonlarni tanlash

### 💻 Oddiy usul

```python
numbers = [1,2,3,4,5,6]

result = []

for n in numbers:
    if n % 2 == 0:
        result.append(n)

print(result)
```

### 📤 Output

```
[2, 4, 6]
```

---

### 💻 `filter()` bilan

```python
numbers = [1,2,3,4,5,6]

def is_even(x):
    return x % 2 == 0

result = list(filter(is_even, numbers))

print(result)
```

### 📤 Output

```
[2, 4, 6]
```

---

# 📌 3. Lambda bilan `filter()`

Ko‘pincha `filter()` **lambda bilan ishlatiladi**.

### 💻 Misol

```python
numbers = [1,2,3,4,5,6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

### 📤 Output

```
[2, 4, 6]
```

---

# 📌 4. Musbat sonlarni tanlash

```python
numbers = [-5, -2, 0, 3, 8, -1]

result = list(filter(lambda x: x > 0, numbers))

print(result)
```

### 📤 Output

```
[3, 8]
```

---

# 📌 5. String uzunligi bo‘yicha filter

### 💻 Misol

```python
words = ["apple", "hi", "banana", "ok"]

result = list(filter(lambda w: len(w) > 3, words))

print(result)
```

### 📤 Output

```
['apple', 'banana']
```

---

# 📌 6. Dictionary list bilan ishlash

### 💻 Misol

```python
users = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 17},
    {"name": "Hasan", "age": 30}
]

adults = list(filter(lambda u: u["age"] >= 18, users))

print(adults)
```

### 📤 Output

```
[
 {'name': 'Ali', 'age': 25},
 {'name': 'Hasan', 'age': 30}
]
```

---

# 📌 7. `None` bilan ishlatish

`filter(None, iterable)` **False qiymatlarni olib tashlaydi**.

False qiymatlar:

```
0
None
''
False
[]
{}
```

---

### 💻 Misol

```python
data = [0, 1, "", "hello", None, 5]

result = list(filter(None, data))

print(result)
```

### 📤 Output

```
[1, 'hello', 5]
```

---

# 📌 8. `filter()` iterator qaytaradi

### 💻 Misol

```python
numbers = [1,2,3,4]

result = filter(lambda x: x > 2, numbers)

print(result)
```

### 📤 Output

```
<filter object at 0x...>
```

Shuning uchun ko‘pincha:

```python
list(filter(...))
```

ishlatiladi.

---

# 📌 9. `filter()` ishlash modeli

`filter()` quyidagi prinsip asosida ishlaydi:

```
for element in iterable:
    if function(element):
        yield element
```

Masalan:

```
filter(f, [a,b,c])
```

aslida:

```
[a if f(a), b if f(b), c if f(c)]
```

---

# 📌 10. `filter()` va list comprehension

Ko‘pincha `filter()` o‘rniga **list comprehension** ishlatiladi.

---

### 💻 `filter()`

```python
numbers = [1,2,3,4,5,6]

result = list(filter(lambda x: x % 2 == 0, numbers))
```

---

### 💻 List comprehension

```python
numbers = [1,2,3,4,5,6]

result = [x for x in numbers if x % 2 == 0]
```

Natija:

```
[2, 4, 6]
```

---

### Qaysi biri yaxshi?

| Usul          | Qachon ishlatiladi     |
| ------------- | ---------------------- |
| `filter()`    | functional programming |
| comprehension | pythonic style         |

---

# 📌 11. Real Example — Email filter

### 💻 Misol

```python
emails = [
    "user@gmail.com",
    "test@yahoo.com",
    "admin@gmail.com"
]

gmail_users = list(filter(lambda e: "gmail" in e, emails))

print(gmail_users)
```

### 📤 Output

```
['user@gmail.com', 'admin@gmail.com']
```

---

# 📌 12. `map()` va `filter()` kombinatsiyasi

### 💻 Misol

```python
numbers = [1,2,3,4,5,6]

result = list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)
```

### 📤 Output

```
[4, 16, 36]
```

Jarayon:

```
filter → [2,4,6]
map → [4,16,36]
```

---

<br>
<br>
<br>
<br>
<br>

# 📊 `reduce()` — Accumulate Values (from `functools`)

Python’da `reduce()` funksiyasi **iterable ichidagi elementlarni ketma-ket birlashtirib bitta natija hosil qilish** uchun ishlatiladi.

Bu jarayon **accumulate (yig‘ish)** deb ataladi.

Masalan:

```
[1,2,3,4] → 1+2+3+4 → 10
```

`reduce()` **functional programming** konsepsiyasiga kiradi.

---

# 📌 1. `reduce()` qayerda joylashgan

`reduce()` Python built-in emas.
U **`functools` modulida** joylashgan.

### Import qilish

```python
from functools import reduce
```

---

# 📌 2. `reduce()` sintaksisi

```python
reduce(function, iterable)
```

yoki

```python
reduce(function, iterable, initializer)
```

| Qism          | Ma'nosi                                |
| ------------- | -------------------------------------- |
| `function`    | ikki argument qabul qiladigan funksiya |
| `iterable`    | list, tuple va boshqa iterable         |
| `initializer` | boshlang‘ich qiymat (ixtiyoriy)        |

---

# 📌 3. `reduce()` qanday ishlaydi

Misol:

```python
reduce(lambda a, b: a + b, [1,2,3,4])
```

Jarayon:

```
1 + 2 → 3
3 + 3 → 6
6 + 4 → 10
```

Natija:

```
10
```

---

# 📌 4. Oddiy misol — yig‘indi

### 💻 Kod

```python
from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

### 📤 Output

```
10
```

---

# 📌 5. Ko‘paytma hisoblash

### 💻 Misol

```python
from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda a, b: a * b, numbers)

print(result)
```

### 📤 Output

```
24
```

Jarayon:

```
1*2 = 2
2*3 = 6
6*4 = 24
```

---

# 📌 6. Maksimum qiymat topish

```python
from functools import reduce

numbers = [3,7,2,9,5]

result = reduce(lambda a, b: a if a > b else b, numbers)

print(result)
```

### 📤 Output

```
9
```

---

# 📌 7. Stringlarni birlashtirish

### 💻 Misol

```python
from functools import reduce

words = ["Python", "is", "awesome"]

sentence = reduce(lambda a, b: a + " " + b, words)

print(sentence)
```

### 📤 Output

```
Python is awesome
```

---

# 📌 8. Initializer bilan ishlash

`initializer` boshlang‘ich qiymat beradi.

### 💻 Misol

```python
from functools import reduce

numbers = [1,2,3]

result = reduce(lambda a, b: a + b, numbers, 10)

print(result)
```

### 📤 Output

```
16
```

Jarayon:

```
10 + 1 = 11
11 + 2 = 13
13 + 3 = 16
```

---

# 📌 9. List elementlarini ko‘paytirish (Real Example)

### 💻 Misol

```python
from functools import reduce

prices = [100, 200, 300]

total = reduce(lambda a, b: a + b, prices)

print(total)
```

### 📤 Output

```
600
```

---

# 📌 10. `reduce()` ishlash modeli

`reduce()` quyidagi algoritm asosida ishlaydi:

```python
result = iterable[0]

for element in iterable[1:]:
    result = function(result, element)
```

Masalan:

```
reduce(f, [a,b,c,d])
```

aslida:

```
f(f(f(a,b),c),d)
```

---

# 📌 11. `map`, `filter`, `reduce` farqi

| Funksiya   | Vazifasi   |
| ---------- | ---------- |
| `map()`    | transform  |
| `filter()` | select     |
| `reduce()` | accumulate |

Misol:

```
map → har elementni o‘zgartiradi
filter → elementlarni saralaydi
reduce → bitta natija chiqaradi
```

---

# 📌 12. `reduce()` vs built-in funksiyalar

Ko‘pincha `reduce()` o‘rniga Python built-in funksiyalari ishlatiladi.

### ❌ reduce

```python
reduce(lambda a,b: a+b, numbers)
```

### ✔️ yaxshiroq

```python
sum(numbers)
```

---

### ❌ reduce

```python
reduce(lambda a,b: a if a>b else b, numbers)
```

### ✔️ yaxshiroq

```python
max(numbers)
```

---

# 📌 13. Qachon `reduce()` ishlatish kerak

`reduce()` foydali bo‘ladi agar:

* custom aggregation kerak bo‘lsa
* murakkab accumulation bo‘lsa
* functional programming yozilayotgan bo‘lsa

---

# 📌 14. Real Functional Pipeline

```python
from functools import reduce

numbers = [1,2,3,4,5]

result = reduce(
    lambda a,b: a+b,
    map(lambda x: x*2, numbers)
)

print(result)
```

Jarayon:

```
numbers → [1,2,3,4,5]
map → [2,4,6,8,10]
reduce → 30
```

---

<br>
<br>
<br>
<br>
<br>

