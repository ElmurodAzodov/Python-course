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

# ⚡ `functools.partial` — Fix Arguments (Partial Function Application)

Python’da `functools.partial` **mavjud funksiyaning ayrim argumentlarini oldindan belgilab qo‘yib yangi funksiya yaratish** uchun ishlatiladi.

Bu konsepsiya **Partial Function Application** deb ataladi.

Ya'ni:

```
original function + fixed arguments → new function
```

---

# 📌 1. `partial` qayerda joylashgan

`partial` funksiyasi **`functools` modulida** joylashgan.

### Import qilish

```python
from functools import partial
```

---

# 📌 2. `partial` sintaksisi

```python
partial(function, *args, **kwargs)
```

| Qism       | Ma'nosi                                  |
| ---------- | ---------------------------------------- |
| `function` | asl funksiya                             |
| `*args`    | oldindan berilgan positional argumentlar |
| `**kwargs` | oldindan berilgan keyword argumentlar    |

Natija: **yangi funksiya object**

---

# 📌 3. Oddiy misol

### 💻 Asl funksiya

```python
def power(base, exponent):
    return base ** exponent
```

### 💻 `partial` bilan

```python
from functools import partial

square = partial(power, exponent=2)

print(square(5))
print(square(10))
```

### 📤 Output

```
25
100
```

### 🔍 Tushuntirish

```
square(5)
```

aslida:

```
power(5, 2)
```

---

# 📌 4. Positional argument fix qilish

```python
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

print(double(5))
print(double(10))
```

### 📤 Output

```
10
20
```

### Tushuntirish

```
double(5) → multiply(2,5)
```

---

# 📌 5. Bir nechta argument fix qilish

```python
from functools import partial

def add(a, b, c):
    return a + b + c

add10 = partial(add, 10, 20)

print(add10(5))
```

### 📤 Output

```
35
```

Jarayon:

```
add(10,20,5)
```

---

# 📌 6. Keyword argument fix qilish

```python
from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}"

say_hello = partial(greet, greeting="Hello")

print(say_hello("Ali"))
print(say_hello("Vali"))
```

### 📤 Output

```
Hello, Ali
Hello, Vali
```

---

# 📌 7. `partial` va lambda farqi

Ko‘p hollarda `partial` o‘rniga **lambda** ishlatiladi.

### Lambda usuli

```python
square = lambda x: power(x, 2)
```

### Partial usuli

```python
square = partial(power, exponent=2)
```

### Farqi

| Usul      | Xususiyat                         |
| --------- | --------------------------------- |
| `lambda`  | yangi funksiya yoziladi           |
| `partial` | mavjud funksiyani qayta ishlatadi |

---

# 📌 8. `partial` bilan `map()`

### 💻 Misol

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)

numbers = [1,2,3,4]

result = list(map(square, numbers))

print(result)
```

### 📤 Output

```
[1, 4, 9, 16]
```

---

# 📌 9. Real Example — Logger

```python
from functools import partial

def log(level, message):
    return f"[{level}] {message}"

info = partial(log, "INFO")
error = partial(log, "ERROR")

print(info("Server started"))
print(error("Connection failed"))
```

### 📤 Output

```
[INFO] Server started
[ERROR] Connection failed
```

---

# 📌 10. `partial` object nima?

`partial()` **yangi funksiya object** qaytaradi.

### Misol

```python
from functools import partial

def add(a,b):
    return a+b

add5 = partial(add,5)

print(type(add5))
```

### 📤 Output

```
<class 'functools.partial'>
```

---

# 📌 11. `partial` ichidagi atributlar

`partial` object ichida asl funksiya va argumentlar saqlanadi.

```python
from functools import partial

def multiply(a,b):
    return a*b

double = partial(multiply,2)

print(double.func)
print(double.args)
```

### 📤 Output

```
<function multiply>
(2,)
```

---

# 📌 12. Real World Use Case — Sorting

```python
from functools import partial

def power(base, exp):
    return base ** exp

cube = partial(power, exp=3)

numbers = [1,2,3,4]

result = list(map(cube, numbers))

print(result)
```

### 📤 Output

```
[1, 8, 27, 64]
```

---

# 📌 13. `partial` ishlash modeli

`partial` quyidagi konsepsiya asosida ishlaydi:

```
new_function(x) = original_function(fixed_args, x)
```

Masalan:

```
double = partial(multiply, 2)
```

aslida:

```
double(x) = multiply(2, x)
```

---

<br>
<br>
<br>
<br>
<br>

# ⚡ `functools.wraps` — Preserve Function Metadata

Python’da **decorator** ishlatilganda asl funksiya **metadata**si yo‘qolib ketishi mumkin.
`functools.wraps` bu muammoni hal qiladi.

`wraps` **asl funksiya haqidagi ma'lumotlarni saqlab qoladi**.

Saqlanadigan metadata:

* `__name__`
* `__doc__`
* `__module__`
* `__annotations__`
* `__qualname__`

---

# 📌 1. `wraps` qayerda joylashgan

`wraps` **`functools` modulida** joylashgan.

```python
from functools import wraps
```

---

# 📌 2. Muammo — decorator metadata ni yo‘qotadi

### 💻 Misol

```python
def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """This function greets the user"""
    print("Hello")


print(greet.__name__)
print(greet.__doc__)
```

### 📤 Output

```
wrapper
None
```

### 🔍 Muammo

| Asl qiymat                        | Decoratordan keyin |
| --------------------------------- | ------------------ |
| `greet`                           | `wrapper`          |
| `"This function greets the user"` | `None`             |

Sababi:

Decorator **asl funksiyani wrapper bilan almashtirdi**.

---

# 📌 3. `wraps` bilan muammoni hal qilish

### 💻 Misol

```python
from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """This function greets the user"""
    print("Hello")


print(greet.__name__)
print(greet.__doc__)
```

### 📤 Output

```
greet
This function greets the user
```

---

# 📌 4. `wraps` nima qiladi

`wraps(func)` quyidagi metadata ni **wrapper funksiyaga ko‘chiradi**.

| Metadata          | Tavsif               |
| ----------------- | -------------------- |
| `__name__`        | funksiya nomi        |
| `__doc__`         | docstring            |
| `__module__`      | modul nomi           |
| `__annotations__` | type hints           |
| `__qualname__`    | to‘liq funksiya nomi |

---

# 📌 5. `wraps` ishlash modeli

`wraps` aslida **`update_wrapper()`** funksiyasining qisqa varianti.

Ichki ishlash prinsipi:

```python
wrapper.__name__ = func.__name__
wrapper.__doc__ = func.__doc__
wrapper.__module__ = func.__module__
```

---

# 📌 6. Real Example — Logging Decorator

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    """Add two numbers"""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(3,4))
```

### 📤 Output

```
add
Add two numbers
Calling add
7
```

---

# 📌 7. Debugging uchun muhim

Ko‘p frameworklar **funksiya metadata** dan foydalanadi.

Masalan:

* testing tools
* documentation generators
* web frameworks
* introspection tools

Agar `wraps` ishlatilmasa:

* funksiya nomi noto‘g‘ri bo‘ladi
* docstring yo‘qoladi
* debugging qiyinlashadi

---

# 📌 8. `inspect` bilan farq

### 💻 wraps ishlatilmasa

```python
import inspect

print(inspect.getsource(greet))
```

`wrapper` ko‘rinadi.

---

### 💻 wraps ishlatilsa

`inspect` asl funksiya bilan ishlaydi.

---

# 📌 9. `wraps` qayerda ishlatiladi

`wraps` **deyarli har bir decorator ichida ishlatilishi kerak**.

Masalan:

* logging decorator
* caching decorator
* timing decorator
* authorization decorator

---

# 📌 10. Timing Decorator Example

```python
import time
from functools import wraps

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Execution time: {end-start}")

        return result

    return wrapper


@timer
def slow_function():
    time.sleep(1)
    print("Finished")


slow_function()
```

### 📤 Output

```
Finished
Execution time: 1.0
```

---

# 📌 11. Type hints bilan ishlash

`wraps` **type annotations** ni ham saqlab qoladi.

### 💻 Misol

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator
def add(a: int, b: int) -> int:
    return a + b


print(add.__annotations__)
```

### 📤 Output

```
{'a': int, 'b': int, 'return': int}
```

---

# 📌 12. `wraps` ishlash formulasi

Decorator ichida har doim quyidagi pattern ishlatiladi:

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

Bu **Python decorator writing standard pattern** hisoblanadi.

---

<br>
<br>
<br>
<br>
<br>

# ⚡ `functools.singledispatch` — Generic Functions

Python’da **`singledispatch`** yordamida **bir funksiya turli tipdagi argumentlarga mos ishlaydigan generic function** sifatida yoziladi.

Ya’ni: **bir nomli funksiya, turli tipdagi argumentlarga turlicha javob beradi**.

---

# 📌 1. `singledispatch` qayerda joylashgan

`singledispatch` **`functools` modulida** joylashgan.

```python
from functools import singledispatch
```

---

# 📌 2. Asosiy sintaksis

```python
@singledispatch
def func(arg):
    """Default implementation"""
    ...
    
@func.register(int)
def _(arg: int):
    """Integer-specific implementation"""
    ...
    
@func.register(list)
def _(arg: list):
    """List-specific implementation"""
    ...
```

> Aslida default funksiya barcha tiplar uchun fallback sifatida ishlaydi.
> `@func.register(type)` bilan turli tiplar uchun maxsus implementatsiya yoziladi.

---

# 📌 3. Oddiy misol

```python
from functools import singledispatch

@singledispatch
def show(value):
    print(f"Default: {value}")

@show.register(int)
def _(value):
    print(f"Integer: {value}")

@show.register(str)
def _(value):
    print(f"String: {value}")

@show.register(list)
def _(value):
    print(f"List of length {len(value)}")
```

### 💻 Test

```python
show(10)
show("Hello")
show([1,2,3])
show(3.14)
```

### 📤 Output

```
Integer: 10
String: Hello
List of length 3
Default: 3.14
```

---

# 📌 4. Tushuntirish

| Qism                   | Tavsif                               |
| ---------------------- | ------------------------------------ |
| `@singledispatch`      | default/fallback funksiya            |
| `@func.register(type)` | tipga mos maxsus funksiya            |
| `_`                    | funksiya nomi anonim bo‘lishi mumkin |
| Default                | barcha boshqa tiplar uchun ishlaydi  |

---

# 📌 5. Argument tiplarini qo‘llash

```python
@show.register(float)
def _(value: float):
    print(f"Float: {value}")
```

```python
show(3.14)
```

### 📤 Output

```
Float: 3.14
```

---

# 📌 6. `singledispatch` bilan generic printing

```python
from functools import singledispatch

@singledispatch
def printer(data):
    print(f"Unknown type: {data}")

@printer.register(int)
def _(data):
    print(f"Integer: {data}")

@printer.register(str)
def _(data):
    print(f"String: {data}")

@printer.register(list)
def _(data):
    print(f"List: {', '.join(str(x) for x in data)}")
```

### 💻 Test

```python
printer(5)
printer("Python")
printer([1,2,3])
printer({1: 'a'})
```

### 📤 Output

```
Integer: 5
String: Python
List: 1, 2, 3
Unknown type: {1: 'a'}
```

---

# 📌 7. `singledispatch` vs `if-elif` chain

```python
def show(value):
    if isinstance(value, int):
        print(f"Integer: {value}")
    elif isinstance(value, str):
        print(f"String: {value}")
    elif isinstance(value, list):
        print(f"List of length {len(value)}")
    else:
        print(f"Default: {value}")
```

`singledispatch` bu ishni **clean, scalable va maintainable** qiladi.

---

# 📌 8. Real Example — Type-specific calculation

```python
from functools import singledispatch

@singledispatch
def process(data):
    return f"Unknown type: {data}"

@process.register(int)
def _(data):
    return data ** 2

@process.register(str)
def _(data):
    return data.upper()

@process.register(list)
def _(data):
    return [x*2 for x in data]
```

### 💻 Test

```python
print(process(5))
print(process("hello"))
print(process([1,2,3]))
```

### 📤 Output

```
25
HELLO
[2, 4, 6]
```

---

# 📌 9. Foydalari

* **Single function name** turli tiplar uchun ishlatiladi
* **Maintainable code**: yangi tip qo‘shish oson
* **Decorator based**: Pythonic
* **Default implementation**: boshqa tiplar uchun fallback

---

# 📌 10. Cheklovlar

* Faqat **birinchi argument bo‘yicha dispatch** ishlaydi
* Ko‘p argumentli dispatch qilolmaysiz
* Typing bilan ishlashda `@register` kerak bo‘ladi

---

<br>
<br>
<br>
<br>
<br>

# ⚡ `functools.lru_cache / @cache` — Memoization

Python’da `functools.lru_cache` yoki Python 3.9+ da `@cache` yordamida **funksiya natijalarini saqlab, takroriy chaqirishlarni tezlashtirish** mumkin.
Bu **memoization** deb ataladi.

---

# 📌 1. `lru_cache` qayerda joylashgan

`lru_cache` **`functools` modulida** joylashgan.

```python id="2yh3qf"
from functools import lru_cache
```

---

# 📌 2. `lru_cache` sintaksisi

```python id="q6v1ga"
@lru_cache(maxsize=128)
def func(args):
    ...
```

| Parametr  | Tavsif                                              |
| --------- | --------------------------------------------------- |
| `maxsize` | Cache da saqlanadigan elementlar soni (default 128) |
| `None`    | Cheksiz cache                                       |
| `typed`   | True bo‘lsa, turga qarab alohida cache saqlaydi     |

---

# 📌 3. Oddiy misol — Fibonacci

```python id="kztf9p"
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
```

### 📤 Output

```
55
```

### 🔍 Tushuntirish

* Recursive Fibonacci tez ishlaydi, chunki `fib(x)` natijasi **cache** da saqlanadi
* Takroriy hisoblashlar yo‘qoladi

---

# 📌 4. `@cache` (Python 3.9+)

`@cache` — `lru_cache(maxsize=None)` qisqa varianti.

```python id="2a7glf"
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

Natija va ishlash **lru_cache(maxsize=None)** bilan bir xil.

---

# 📌 5. Cache statistikasi

`lru_cache` **statistik metodlar** bilan ishlaydi:

```python id="rfhn1k"
fib.cache_info()
fib.cache_clear()
```

### 💻 Misol

```python id="v0j7p7"
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
print(fib.cache_info())
```

### 📤 Output

```
55
CacheInfo(hits=8, misses=11, maxsize=None, currsize=11)
```

* **hits** — cache dan foydalangan chaqirishlar
* **misses** — original hisoblangan chaqirishlar
* **currsize** — hozirgi cache hajmi

---

# 📌 6. Real Example — Factorial

```python id="6okzj9"
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

### 📤 Output

```
120
```

---

# 📌 7. Type-specific caching (`typed=True`)

```python id="t3xwlf"
@lru_cache(maxsize=None, typed=True)
def add(x):
    return x + 1

print(add(1))
print(add(1.0))  # alohida cache
```

---

# 📌 8. Cache clear qilish

```python id="4n9hgs"
fib.cache_clear()
```

* Cache tozalanadi
* Keyingi chaqirishlar **miss** bo‘ladi

---

# 📌 9. `lru_cache` bilan recursive optimization

### 💻 Oddiy Fibonacci (slow)

```python id="eyx0ev"
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # juda sekin
```

---

### 💻 `lru_cache` bilan (fast)

```python id="yrq5zi"
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # juda tez
```

---

# 📌 10. `lru_cache` vs `@cache`

| Funksiya                   | Tavsif                                         |
| -------------------------- | ---------------------------------------------- |
| `@lru_cache(maxsize=None)` | cheksiz cache, recursive optimization          |
| `@cache`                   | qisqa syntax, Python 3.9+                      |
| `maxsize`                  | cheklangan cache bo‘lsa, LRU eviction ishlaydi |

---

# 📌 11. Foydali pattern

* Recursive algorithms (`fib`, `factorial`, `combination`)
* Expensive computations
* Web requests / API results caching

---

# 📌 12. Misol — Expensive Computation

```python id="2qk17z"
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def slow_square(n):
    time.sleep(1)
    return n*n

print(slow_square(5))  # 1 sec
print(slow_square(5))  # instant, cached
```

### 📤 Output

```
25
25
```

---

<br>
<br>
<br>
<br>
<br>

# 🔁 Recursion — Base Case & Recursion Limit

Python’da **recursion** — bu funksiya o‘zini **o‘z ichida chaqirishi**dir.
Recursive funksiyalar **muayyan shart asosida to‘xtashi** kerak, aks holda **infinite recursion → crash** bo‘ladi.

---

# 📌 1. Recursion elementlari

1. **Base case (bazaviy holat)**

   * Rekursiyani to‘xtatadigan shart
   * Har doim **oldin tekshiriladi**
2. **Recursive case**

   * Funksiya o‘zini chaqiradi
   * Base case tomon yetishi kerak

---

# 📌 2. Oddiy misol — Factorial

```python id="h7v5zw"
def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n-1)  # Recursive case

print(factorial(5))
```

### 📤 Output

```id="s3q2y1"
120
```

Jarayon:

```
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)
= 120
```

---

# 📌 3. Oddiy misol — Fibonacci

```python id="g7t2jp"
def fib(n):
    if n < 2:  # Base case
        return n
    return fib(n-1) + fib(n-2)  # Recursive case

print(fib(10))
```

### 📤 Output

```id="v9k8nb"
55
```

---

# 📌 4. Recursion limit

Python’da **rekursiya chuqurligi cheklangan**:

```python id="p4k9sh"
import sys
print(sys.getrecursionlimit())
```

* Default: 1000
* O‘zgartirish mumkin:

```python id="m3l4yt"
sys.setrecursionlimit(2000)
```

⚠️ Diqqat: Haddan oshirish **stack overflow** ga olib kelishi mumkin.

---

# 📌 5. Base case muhimligi

Base case bo‘lmasa **RecursionError: maximum recursion depth exceeded** yuz beradi.

```python id="x5v1ku"
def infinite_recursion():
    return infinite_recursion()

infinite_recursion()
```

### 📤 Output

```id="c8y2fh"
RecursionError: maximum recursion depth exceeded
```

---

# 📌 6. Reverse list misol

```python id="y7q3zt"
def reverse_list(lst):
    if not lst:  # Base case: bo‘sh list
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

print(reverse_list([1,2,3,4]))
```

### 📤 Output

```id="d4k6fr"
[4, 3, 2, 1]
```

---

# 📌 7. Sum of list misol

```python id="r9t5hn"
def sum_list(lst):
    if not lst:  # Base case
        return 0
    return lst[0] + sum_list(lst[1:])  # Recursive call

print(sum_list([1,2,3,4]))
```

### 📤 Output

```id="k3v7lt"
10
```

---

# 📌 8. Tail recursion

Python **tail recursion optimization** qilmaydi.
Shuning uchun **chuqur recursion** uchun `lru_cache` yoki loop ishlatish yaxshiroq.

Tail recursion misol (Python-da oson emas):

```python id="f8q4yz"
def fact_tail(n, acc=1):
    if n == 0:
        return acc
    return fact_tail(n-1, n*acc)
```

---

# 📌 9. Recursion vs Iteration

| Recursion             | Iteration              |
| --------------------- | ---------------------- |
| Elegant, concise      | Loop orqali bajariladi |
| Stack ishlatiladi     | Stack ishlatilmaydi    |
| Stack overflow xavfi  | Yo‘q                   |
| Memoization bilan tez | Tez va xavfsiz         |

---

# 📌 10. Real example — GCD

```python id="p7v3js"
def gcd(a, b):
    if b == 0:  # Base case
        return a
    return gcd(b, a % b)  # Recursive call

print(gcd(48, 18))
```

### 📤 Output

```id="k4t9lx"
6
```

---

# 📌 11. Tips for recursion

1. Har doim **base case** bo‘lishi kerak
2. Recursive call **base case tomon** yetishi lozim
3. Chuqur recursion → `RecursionError`
4. Stack-heavy tasks → iteration yoki `lru_cache` bilan optimizatsiya

---

<br>
<br>
<br>
<br>
<br>

# 🔒 Closures — Functions with Captured State

Python’da **closure** — bu **bir funksiyaning ichida yaratilgan va o‘zining tashqi scope’dagi o‘zgaruvchilarni eslab qoladigan funksiya**.

Ya’ni, ichki funksiya **tashqi funksiyaning o‘zgaruvchilarini “yodda saqlaydi”** va ular bilan ishlash imkoniga ega.

---

# 📌 1. Closure qanday ishlaydi

1. Tashqi funksiya (`outer`) chaqiriladi
2. Ichki funksiya (`inner`) yaratiladi
3. Ichki funksiya **tashqi scope’dagi o‘zgaruvchilarni saqlaydi**
4. Tashqi funksiya return qilinadi — ichki funksiya bilan birga

---

# 📌 2. Oddiy misol

```python id="z8v9a1"
def outer(x):
    def inner(y):
        return x + y  # x tashqi scope’dan olinadi
    return inner

add5 = outer(5)
print(add5(10))
print(add5(3))
```

### 📤 Output

```id="t7x4b9"
15
8
```

Tushuntirish:

* `add5 = outer(5)` → `x = 5` eslab qolindi
* `add5(10)` → `10 + 5 = 15`

---

# 📌 3. Ichki funksiya “captured state” bilan

```python id="k3v1d8"
def counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter(5)
print(c())  # 6
print(c())  # 7
print(c())  # 8
```

* `nonlocal` tashqi o‘zgaruvchini yangilashga yordam beradi
* `count` closure ichida saqlanadi

---

# 📌 4. Multiple closures

```python id="v9w2j5"
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))
```

### 📤 Output

```id="y4m8r2"
10
15
```

* Har bir closure o‘z `factor` qiymatini eslab qoladi

---

# 📌 5. Closures vs Global variables

Closures **local state** saqlaydi, global o‘zgaruvchilardan farqli:

```python id="h2r5xq"
def make_adder(x):
    return lambda y: x + y  # closure

f = make_adder(10)
print(f(5))  # 15
```

* `x` global emas, faqat closure ichida mavjud

---

# 📌 6. Decoratorlar aslida closures

```python id="d5p8mk"
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello {name}")

greet("Ali")
```

* `wrapper` closure bo‘lib, `func` ni eslab qoladi

---

# 📌 7. Advantages of Closures

1. **Data hiding** — private variable yaratish
2. **Maintaining state** — funksiyalar o‘z holatini saqlaydi
3. **Functional programming** — yuqori tartibli funksiya yaratish
4. **Reusable code** — parametrizatsiyalangan funksiyalar

---

# 📌 8. Real Example — Counter Factory

```python id="u8n5fp"
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = make_counter()
c2 = make_counter()

print(c1())  # 1
print(c1())  # 2
print(c2())  # 1
print(c2())  # 2
```

* Har bir closure **alohida state** saqlaydi

---

# 📌 9. Real Example — Greeting Factory

```python id="t3m9qv"
def greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = greeter("Hello")
hi = greeter("Hi")

print(hello("Ali"))
print(hi("Vali"))
```

### 📤 Output

```id="r8v4bz"
Hello, Ali!
Hi, Vali!
```

* `greeting` har bir closure uchun saqlanadi

---

<br>
<br>
<br>
<br>
<br>

# 🎨 Decorators — `@` Syntax & Wrapping Functions

Python’da **decorator** — bu funksiya yoki klassni **o‘zgartiruvchi funksiya**.
Asosan, u **boshqa funksiyani qabul qilib, yangi funksiya qaytaradi**.

* Sintaksisda: `@decorator_name`
* Ichida: **wrapping** orqali asl funksiya qo‘shimcha xatti-harakat bilan qayta ishlanadi

---

# 📌 1. Oddiy decorator sintaksisi

```python id="a1x9v2"
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
```

---

# 📌 2. Decorator qo‘llash

```python id="b2y0q3"
@my_decorator
def greet():
    print("Hello!")

greet()
```

### 📤 Output

```id="c3z1r4"
Before function call
Hello!
After function call
```

* `@my_decorator` → `greet = my_decorator(greet)`

---

# 📌 3. Arguments bilan decorator

```python id="d4a2s5"
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(5, 7))
```

### 📤 Output

```id="e5b3t6"
Before call
After call
12
```

* `*args, **kwargs` → barcha argumentlarni wrapper ga uzatadi

---

# 📌 4. Multiple decorators

```python id="f6c4u7"
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator1 Before")
        result = func(*args, **kwargs)
        print("Decorator1 After")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator2 Before")
        result = func(*args, **kwargs)
        print("Decorator2 After")
        return result
    return wrapper

@decorator1
@decorator2
def greet(name):
    print(f"Hello {name}")

greet("Ali")
```

### 📤 Output

```id="g7d5v8"
Decorator1 Before
Decorator2 Before
Hello Ali
Decorator2 After
Decorator1 After
```

* **Decorator chaining**: yuqoridagi decorator birinchi chaqiriladi, keyingi esa ichki wrapper

---

# 📌 5. Decorator va functools.wraps

```python id="h8e6w9"
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before call")
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    """Say hello"""
    print("Hello")

print(greet.__name__)  # greet
print(greet.__doc__)   # Say hello
```

* `@wraps` → asl metadata saqlanadi (`__name__`, `__doc__`)

---

# 📌 6. Parameterized decorators

Decoratorga **o‘z parametrini berish** mumkin:

```python id="i9f7x0"
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Ali")
```

### 📤 Output

```id="j0g8y1"
Hello Ali
Hello Ali
Hello Ali
```

---

# 📌 7. Decorator pattern summary

```python id="k1h9z2"
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before
        result = func(*args, **kwargs)
        # After
        return result
    return wrapper
```

1. **Outer function** — decorator
2. **Inner function** — wrapper
3. **Return wrapper** — asl funksiya o‘rnini egallaydi

---

# 📌 8. Real Example — Logging Decorator

```python id="l2i0a3"
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 7))
```

### 📤 Output

```id="m3j1b4"
Calling add with (5, 7) {}
12
```

---

# 📌 9. Real Example — Timing Decorator

```python id="n4k2c5"
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end-start:.4f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(1)
    return a + b

slow_add(5, 7)
```

### 📤 Output

```id="o5l3d6"
slow_add executed in 1.0002s
12
```

---

# 📌 10. Advantages of Decorators

1. **Code reuse** — logging, timing, authentication, memoization
2. **Separation of concerns** — asl funksiya logikasi va qo‘shimcha xatti-harakat alohida
3. **Pythonic** — `@` syntax oson va chiroyli
4. **Composable** — bir nechta decorator chaining mumkin

---

<br>
<br>
<br>
<br>
<br>

# 📝 Function Annotations — Type Hints

Python’da **function annotations** yordamida funksiya argumentlari va return qiymatlari uchun **tiplarni belgilash** mumkin.

* Bu kodni **o‘qish, dokumentatsiya va static type checking** uchun qulay qiladi.
* Python-da **optional**, runtime da majburiy emas.

---

# 📌 1. Sintaksis

```python id="a1x9t2"
def func(a: int, b: str) -> bool:
    ...
```

| Qism      | Tavsif                    |
| --------- | ------------------------- |
| `a: int`  | argument `a` tipi `int`   |
| `b: str`  | argument `b` tipi `str`   |
| `-> bool` | return qiymat tipi `bool` |

---

# 📌 2. Oddiy misol

```python id="b2y0u3"
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 7))
```

### 📤 Output

```id="c3z1v4"
12
```

* Type hints faqat **informatsion**
* Runtime da Python tekshirmaydi

---

# 📌 3. Multiple argument types

```python id="d4a2w5"
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

print(greet("Ali", 25))
```

### 📤 Output

```id="e5b3x6"
Hello Ali, you are 25 years old
```

---

# 📌 4. Default argument bilan

```python id="f6c4y7"
def increment(x: int, step: int = 1) -> int:
    return x + step

print(increment(5))
print(increment(5, 3))
```

### 📤 Output

```id="g7d5z8"
6
8
```

---

# 📌 5. Complex types (Python 3.9+)

```python id="h8e6a9"
def process(data: list[int]) -> dict[str, int]:
    return {str(i): i*2 for i in data}

print(process([1,2,3]))
```

### 📤 Output

```id="i9f7b0"
{'1': 2, '2': 4, '3': 6}
```

---

# 📌 6. Optional & Union types

```python id="j0g8c1"
from typing import Optional, Union

def square(x: Optional[int] = None) -> Union[int, None]:
    if x is None:
        return None
    return x**2

print(square(5))
print(square())
```

### 📤 Output

```id="k1h9d2"
25
None
```

---

# 📌 7. Callable & Any

```python id="l2i0e3"
from typing import Callable, Any

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

print(apply(lambda x: x*2, 5))
```

### 📤 Output

```id="m3j1f4"
10
```

---

# 📌 8. Accessing Annotations

```python id="n4k2g5"
def greet(name: str) -> str:
    return f"Hello {name}"

print(greet.__annotations__)
```

### 📤 Output

```id="o5l3h6"
{'name': <class 'str'>, 'return': <class 'str'>}
```

---

# 📌 9. Benefits

1. **Static type checking** (`mypy`, `pyright`)
2. **Code readability**
3. **Better IDE support** (auto-completion, hints)
4. **Documentation generation**

---

# 📌 10. Summary

| Feature              | Description                       |
| -------------------- | --------------------------------- |
| Argument annotations | `a: int`                          |
| Return annotation    | `-> str`                          |
| Optional & Union     | `Optional[int]`, `Union[str,int]` |
| Complex types        | `list[int]`, `dict[str,int]`      |
| Callable             | `Callable[[int], int]`            |
| Access               | `function.__annotations__`        |

---

# 📌 11. Example — Full

```python id="p6m4h7"
from typing import List, Dict, Callable

def process_data(data: List[int], transform: Callable[[int], int]) -> Dict[int, int]:
    return {x: transform(x) for x in data}

print(process_data([1,2,3], lambda x: x*10))
```

### 📤 Output

```id="q7n5i8"
{1: 10, 2: 20, 3: 30}
```

---

Function annotations — bu **kodni self-documenting va type-safe qilish vositasi**, runtime da Python majburiy emas, lekin IDE va type checkers yordamida katta foyda beradi.
