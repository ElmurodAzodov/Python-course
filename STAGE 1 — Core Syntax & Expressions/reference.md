
# **STAGE 1 — Core Syntax & Expressions**
---

# 📊 **Variables and Assignment in Python**

## 🎯 Asosiy g‘oya

**Variable (o‘zgaruvchi)** — bu **obyektga ishora qiluvchi nom**.
Python’da o‘zgaruvchi **obyektning qiymatini saqlamaydi**, balki **obyektga reference (ishora) qiladi**.

**Assignment (taqsimlash)** — bu **obyektni o‘zgaruvchiga biriktirish** jarayoni.

---

## 1️⃣ O‘zgaruvchi yaratish va qiymat berish

```python
x = 10          # int obyekt
name = "Alice"  # str obyekt
pi = 3.14       # float obyekt
```

* `x`, `name`, `pi` — o‘zgaruvchi nomlari
* `=` — assignment operator (biriktirish)

### 🔑 Qoidalar:

1. Nom harf yoki underscore (`_`) bilan boshlanishi kerak
2. Keyingi belgilar: harflar, raqamlar, `_`
3. Case-sensitive: `var` ≠ `Var`

---

## 2️⃣ Multiple assignment

### a) Bir xil qiymat

```python
a = b = c = 0
print(a, b, c)  # 0 0 0
```

### b) Har xil qiymatlar

```python
x, y, z = 1, 2, 3
print(x, y, z)
```

* Tuple unpacking ishlatiladi
* Qiymatlar soni o‘zgaruvchilar soniga teng bo‘lishi kerak

---

## 3️⃣ Dynamic Typing bilan assignment

Python’da o‘zgaruvchi turini oldindan belgilash shart emas:

```python
x = 10
print(x, type(x))  # 10 <class 'int'>

x = "Hello"
print(x, type(x))  # Hello <class 'str'>
```

* `x` hozir **string obyektga** ishora qiladi
* Oldingi int obyekt garbage collector tomonidan tozalanadi (agar boshqa reference bo‘lmasa)

---

## 4️⃣ Constants (o‘zgarmas qiymatlar)

Python’da `const` yo‘q, lekin **konvensiya bilan** belgilanadi:

```python
PI = 3.14159  # katta harflar → constant sifatida ishlatiladi
```

* Python buni o‘zgartirishga to‘sqinlik qilmaydi, lekin **pep8 konvensiyasi** buni “o‘zgarmas” deb qabul qiladi

---

## 5️⃣ Assignment expressions (walrus operator `:=`) — Python 3.8+

```python
if (n := len("hello")) > 3:
    print(n)  # 5
```

* `:=` → obyektni bir vaqtning o‘zida **yaratish va qiymat berish**
* Ko‘p hollarda `while` yoki `if` statement’larda qulay

---

## 6️⃣ Common pitfalls

❌ Noto‘g‘ri nomlar:

```python
2var = 10       # Xato, raqam bilan boshlanishi mumkin emas
my-var = 5      # Xato, `-` ruxsat etilmagan
```

✅ To‘g‘ri:

```python
var2 = 10
my_var = 5
```

❌ Assignment o‘rniga `==` ishlatish:

```python
x == 5  # Xato, bu comparison
```

---

## 7️⃣ Reference vs Copy

```python
a = [1, 2, 3]
b = a  # b → a bilan bir xil list obyektga reference qiladi

b.append(4)
print(a)  # [1, 2, 3, 4]
```

* Mutable obyektlar assignment → **reference copy**
* Immutable obyektlar assignment → **obyektni almashtirish**

```python
x = 10
y = x
y += 5
print(x, y)  # 10 15
```

* `int` immutable → yangi obyekt yaratiladi

---

## 8️⃣ Best practices

* O‘zgaruvchi nomi **ma’noli** bo‘lsin: `age`, `name`, `total_sum`
* Konvensiya: **snake_case** (`my_variable`)
* Constantlar: **UPPER_CASE** (`PI`)
* Assignment expressions faqat Python ≥ 3.8

---
# 🏷️ **Identifiers and Keywords in Python**

## 🎯 Asosiy g‘oya

1. **Identifier** — Python’da **o‘zgaruvchi, funksiya, class, modul yoki obyekt nomi**.
2. **Keyword** — Python’da **maxsus ma’noga ega bo‘lgan oldindan belgilangan so‘zlar**, ular nom sifatida ishlatilmaydi.

---

## 1️⃣ Identifiers (nomlar)

### ✅ Qoidalari:

1. Harflar (a-z, A-Z) yoki underscore (`_`) bilan boshlanishi kerak
2. Keyingi belgilar: harflar, raqamlar yoki underscore
3. Case-sensitive (`var` ≠ `Var`)
4. Python keywords bo‘lgan so‘zlardan foydalanish mumkin emas
5. Bo‘sh joy va maxsus belgilar (`!`, `@`, `#`) ishlatilmaydi

---

### Misol — to‘g‘ri identifiers

```python
name = "Alice"
_age = 25
total2 = 100
my_variable = 10
```

### Misol — noto‘g‘ri identifiers

```python
2name = "Bob"    # raqam bilan boshlanishi mumkin emas
my-var = 5       # `-` ishlatilmaydi
class = "X"      # keyword ishlatilgan
```

---

## 2️⃣ Keywords

Python keywords — bu **oldindan belgilangan so‘zlar**, ular **maxsus sintaksis** uchun ishlatiladi.

```python
import keyword
print(keyword.kwlist)
```

Natija (misol):

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### ❌ Keyword bilan identifier yaratish

```python
if = 5  # Xato
```

* Python **keyword** bo‘lgan so‘zni identifier sifatida qabul qilmaydi

---

## 3️⃣ Identifier naming conventions

| Type             | Convention | Misol            |
| ---------------- | ---------- | ---------------- |
| Variable         | snake_case | my_variable      |
| Constant         | UPPER_CASE | PI, MAX_SPEED    |
| Class            | PascalCase | MyClass, Student |
| Private          | _prefix    | _hidden_var      |
| Strongly private | __prefix   | __very_hidden    |

---

## 4️⃣ Dynamic typing va identifiers

Identifier o‘zgaruvchi turini belgilamaydi, **tur runtime’da aniqlanadi**:

```python
x = 10       # int
x = "Hello"  # str
```

* `x` hozir **string obyektga** ishora qiladi

---

## 5️⃣ Best practices

* Nom ma’noli bo‘lsin: `age`, `student_name`, `total_sum`
* Underscore bilan private maqsadda belgilash: `_hidden_var`
* Keyword va built-in nomlardan saqlaning: `list`, `str`, `id` ishlatish xavfli
* CamelCase faqat **class** nomlari uchun
* Snake_case → variables va functions

---

## 6️⃣ Common pitfalls

❌ Built-in function nomi bilan o‘zgaruvchi yaratish

```python
list = [1, 2, 3]  # Python built-in list’ni shadow qiladi
```

* To‘g‘ri: `my_list = [1,2,3]`

❌ Keyword bilan identifier

```python
for = 10  # Xato
```

---
# 🔤 **Built-in Data Types in Python**

Python’da bir nechta **asosiy built-in data types** mavjud. Ular **mutable** va **immutable** ga bo‘linadi.

---

## 1️⃣ Numeric Types

### a) Integers (`int`) — butun sonlar

```python
x = 10
y = -5
```

* Immutable
* Arbitrary precision (cheksiz aniqlik)

### b) Floating-point (`float`) — suzuvchi nuqtali sonlar

```python
pi = 3.14159
a = 0.1
```

* Immutable
* 64-bit IEEE 754
* Round-off errors mumkin

### c) Complex (`complex`) — kompleks sonlar

```python
z = 2 + 3j
print(z.real, z.imag)  # 2.0 3.0
```

* Immutable
* Real va imaginary qismlar float

---

## 2️⃣ Sequence Types

### a) String (`str`)

```python
s = "Hello, World!"
```

* Immutable
* Text data saqlash
* Indexing, slicing, concatenation mavjud

### b) List (`list`)

```python
lst = [1, 2, 3]
lst.append(4)  # mutable
```

* Mutable
* Har xil data type saqlashi mumkin
* Indexing, slicing, append, pop, extend

### c) Tuple (`tuple`)

```python
t = (1, 2, 3)
```

* Immutable
* Indexing, slicing mavjud
* Ichidagi element mutable bo‘lsa, u o‘zgaradi

### d) Range (`range`)

```python
r = range(5)  # 0,1,2,3,4
```

* Immutable
* Looplarda ishlatiladi

---

## 3️⃣ Set Types

### a) Set (`set`)

```python
s = {1, 2, 3}
s.add(4)
```

* Mutable
* Unikal elementlar
* Unordered

### b) Frozen set (`frozenset`)

```python
fs = frozenset([1, 2, 3])
```

* Immutable
* Hashable → dict key bo‘lishi mumkin

---

## 4️⃣ Mapping Type

### Dictionary (`dict`)

```python
d = {"name": "Alice", "age": 25}
d["city"] = "Tashkent"  # mutable
```

* Mutable
* Key-value pairs
* Key immutable bo‘lishi kerak

---

## 5️⃣ Boolean Type (`bool`)

```python
x = True
y = False
```

* Immutable
* Subclass of int (`True == 1`, `False == 0`)
* Control flow uchun muhim

---

## 6️⃣ NoneType (`None`)

```python
x = None
```

* Singleton
* Immutable
* Falsy value

---

## 7️⃣ Bytes and Bytearray

### a) Bytes (`bytes`) — immutable

```python
b = b"hello"
```

### b) Bytearray (`bytearray`) — mutable

```python
ba = bytearray(b"hello")
ba[0] = 72  # H
```

---

## 8️⃣ Summary Table

| Type      | Mutable? | Example          | Notes               |
| --------- | -------- | ---------------- | ------------------- |
| int       | ❌        | 10               | Arbitrary precision |
| float     | ❌        | 3.14             | IEEE 754            |
| complex   | ❌        | 2+3j             | Real + Imag         |
| bool      | ❌        | True/False       | Subclass of int     |
| str       | ❌        | "Hello"          | Immutable sequence  |
| tuple     | ❌        | (1,2)            | Immutable sequence  |
| frozenset | ❌        | frozenset({1,2}) | Hashable set        |
| list      | ✅        | [1,2,3]          | Mutable sequence    |
| dict      | ✅        | {"a":1}          | Mutable mapping     |
| set       | ✅        | {1,2,3}          | Mutable unordered   |
| bytearray | ✅        | bytearray(b"hi") | Mutable bytes       |
| NoneType  | ❌        | None             | Singleton           |

---
# 🌀 **Dynamic Typing in Python**

## 🎯 Asosiy g‘oya

Python — **dynamically typed language**, ya’ni:

> O‘zgaruvchi yaratishda siz turini belgilashingiz shart emas, tur **runtime’da aniqlanadi**.

* Har bir obyekt **type** ga ega
* O‘zgaruvchi **obyektga ishora qiladi**, tur emas
* Shu sababli o‘zgaruvchining turini istalgan vaqtda o‘zgartirish mumkin

---

## 1️⃣ Misol — tur o‘zgarishi

```python
x = 10          # int
print(x, type(x))  # 10 <class 'int'>

x = "Hello"     # str
print(x, type(x))  # Hello <class 'str'>

x = 3.14        # float
print(x, type(x))  # 3.14 <class 'float'>
```

* `x` o‘zi hech qachon type’ni saqlamaydi, **obyektga reference qiladi**
* Python garbage collector orqali eski obyektlarni tozalaydi, agar boshqa reference bo‘lmasa

---

## 2️⃣ Immutable obyekt va dynamic typing

```python
a = 5
b = a

b += 1
print(a, b)  # 5 6
```

* `int` immutable → yangi obyekt yaratiladi
* Dynamic typing sababli `b` endi yangi `int` obyektga ishora qiladi

---

## 3️⃣ Mutable obyekt va dynamic typing

```python
lst = [1, 2, 3]
lst2 = lst

lst2.append(4)
print(lst)  # [1, 2, 3, 4]
```

* Mutable → assignment orqali **reference copy** bo‘ladi
* Dynamic typing ham shu jarayonni qo‘llab-quvvatlaydi

---

## 4️⃣ Function argumentlarida

```python
def func(x):
    print(x, type(x))

func(10)       # 10 <class 'int'>
func("Hi")     # Hi <class 'str'>
func([1,2])    # [1,2] <class 'list'>
```

* Python argument type’ini tekshirmaydi → dynamic typing

---

## 5️⃣ Dynamic typing afzalliklari

✔ Tez va flexible kod yozish imkoniyati
✔ Turga bog‘lanmagan algoritmlar
✔ Functional programming / generic coding oson

---

## 6️⃣ Dynamic typing kamchiliklari

❌ Type xatolari runtime’da paydo bo‘ladi

```python
x = 10
x + "5"   # TypeError
```

❌ IDE autocomplete yoki type hint qiyinroq

---

## 7️⃣ Type hints (optional)

Python 3.5+ bilan **type hint** orqali static-like typing qo‘shish mumkin:

```python
def add(a: int, b: int) -> int:
    return a + b

x: str = "Hello"
```

* Bu kodni ishlatishga to‘sqinlik qilmaydi
* Faqat **type checking tools** (mypy, PyCharm) ogohlantiradi

---

## 8️⃣ Type conversion (casting) bilan birga

Dynamic typing → turlarni o‘zgartirish oson:

```python
x = "123"
y = int(x) + 10
print(y, type(y))  # 133 <class 'int'>
```

* Automatic type promotion ham mavjud (int + float → float)

---
# ✅ **Type Checking in Python**

## 🎯 Asosiy g‘oya

Python’da **har bir obyekt** o‘z **type** ga ega.
**Type checking** — bu obyekt turini aniqlash va shartli yoki debugging holatlarida tekshirish jarayoni.

---

## 1️⃣ `type()` funksiyasi

```python
x = 10
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

z = "Hello"
print(type(z))  # <class 'str'>
```

* `type()` har doim **obyekt turini** qaytaradi
* Immutable va mutable obyektlar uchun ishlaydi

---

## 2️⃣ `isinstance()` funksiyasi

```python
x = 10
print(isinstance(x, int))    # True
print(isinstance(x, float))  # False
```

### a) Multiple types tekshirish

```python
y = 3.14
print(isinstance(y, (int, float)))  # True
```

* Tuple orqali bir nechta type tekshirish mumkin

### b) Subclass tekshirish

```python
print(isinstance(True, int))  # True, bool → int subclass
```

---

## 3️⃣ Type checking vs Comparison

❌ Noto‘g‘ri:

```python
x = 10
if type(x) == int:
    print("int")  # ishlaydi, lekin subclass e’tibor bermaydi
```

✅ Tavsiya etiladi:

```python
if isinstance(x, int):
    print("int or subclass")
```

---

## 4️⃣ Mutable vs Immutable obyektlarda type check

```python
lst = [1, 2, 3]
tpl = (1, 2, 3)

print(isinstance(lst, list))  # True
print(isinstance(tpl, tuple)) # True
```

* `type()` va `isinstance()` ikkalasi ham ishlaydi
* `isinstance()` **subclass’larni ham tekshiradi**

---

## 5️⃣ Type hints bilan type checking

```python
def add(a: int, b: int) -> int:
    return a + b

x: str = "Hello"
```

* Python interpreter ishlashga to‘sqinlik qilmaydi
* Lekin `mypy` yoki IDE type xatolarni ko‘rsatadi

---

## 6️⃣ Common pitfalls

❌ `is` bilan type tekshirish

```python
x = 10
print(type(x) is int)  # True, lekin subclass bilan mos kelmaydi
```

* Tavsiya: **isinstance()** ishlatish

❌ Dynamic typingda noto‘g‘ri type:

```python
x = 10
x = "Hello"
print(isinstance(x, int))  # False
```

* Har doim runtime’da tekshirish kerak

---

## 7️⃣ Practical example

```python
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    if b == 0:
        return None
    return a / b

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, "2"))  # None
```

* Type checking → xatolardan saqlaydi

---
# 🔄 **Type Conversion in Python**

## 🎯 Asosiy g‘oya

**Type conversion** — bu **bir turdagi obyektni boshqa turga o‘zgartirish** jarayoni.

* **Implicit (automatic)** → Python avtomatik bajaradi
* **Explicit (manual / casting)** → dasturchi bajaradi

---

## 1️⃣ Implicit Type Conversion (Type Promotion)

* Python arifmetik operatsiyada **turini avtomatik o‘zgartiradi**
* Ko‘pincha **int → float**

```python
x = 5       # int
y = 2.5     # float

z = x + y
print(z, type(z))  # 7.5 <class 'float'>
```

* `int + float` → float natija

---

## 2️⃣ Explicit Type Conversion (Casting)

Python’da **built-in functions** orqali:

| Function                               | Maqsad                    |
| -------------------------------------- | ------------------------- |
| `int()`                                | float, str → int          |
| `float()`                              | int, str → float          |
| `str()`                                | int, float, bool → str    |
| `bool()`                               | int, float, str → bool    |
| `complex()`                            | int, float, str → complex |
| `list()`, `tuple()`, `set()`, `dict()` | sequence conversion       |

---

### a) int()

```python
x = int(3.9)
y = int("10")
print(x, y)  # 3 10
```

❌ Xato:

```python
int("abc")  # ValueError
```

---

### b) float()

```python
x = float(5)
y = float("3.14")
print(x, y)  # 5.0 3.14
```

---

### c) str()

```python
x = str(10)
y = str(3.14)
z = str(True)
print(x, y, z)  # '10' '3.14' 'True'
```

---

### d) bool()

```python
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("Hello")) # True
print(bool([]))      # False
print(bool([1,2]))   # True
```

---

### e) complex()

```python
z1 = complex(2)
z2 = complex(3.5, 1)
z3 = complex("2+3j")
print(z1, z2, z3)  # (2+0j) (3.5+1j) (2+3j)
```

---

## 3️⃣ Sequence Conversion

```python
lst = list((1, 2, 3))
tpl = tuple([1, 2, 3])
st = set([1, 2, 2, 3])
print(lst, tpl, st)  # [1,2,3] (1,2,3) {1,2,3}
```

* Duplicate values set’da yo‘qoladi

---

## 4️⃣ Practical examples

### a) User input conversion

```python
age = input("Enter your age: ")  # input → str
age = int(age)                    # convert to int

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### b) Mixed arithmetic

```python
a = "10"
b = 5
c = int(a) + b
print(c)  # 15
```

---

## 5️⃣ Common pitfalls

❌ Noto‘g‘ri conversion

```python
int("3.14")  # ValueError
```

* To‘g‘ri: `float("3.14")` → 3.14 → int(3.14) → 3

❌ Dynamic typingda arifmetik xatolar

```python
x = "10"
y = 5
print(x + y)  # TypeError
```

* To‘g‘ri: `int(x) + y`

---
# ⌨️ **Input Handling in Python**

## 🎯 Asosiy g‘oya

**Input handling** — bu dasturga **foydalanuvchi tomonidan kiritilgan qiymatni olish** jarayoni.

* Python 3-da bu uchun **`input()`** funksiyasi ishlatiladi
* Input har doim **string** tipida qaytariladi
* Agar boshqa tur kerak bo‘lsa → **type conversion** ishlatiladi

---

## 1️⃣ `input()` funksiyasi

```python
name = input("Enter your name: ")
print("Hello,", name)
```

* `"Enter your name: "` → foydalanuvchiga prompt sifatida ko‘rsatiladi
* Foydalanuvchi kiritgan qiymat **string** sifatida olinadi

---

## 2️⃣ Number input olish

```python
age = input("Enter your age: ")  # string
age = int(age)                    # convert to int
print("You are", age, "years old")
```

* Agar foydalanuvchi raqam kiritmasa → **ValueError**
* `float()` bilan float tip olish mumkin:

```python
price = float(input("Enter price: "))
```

---

## 3️⃣ One-liner conversion

```python
x = int(input("Enter a number: "))
y = float(input("Enter a float: "))
```

* Shu tarzda type conversion bilan birga olish mumkin

---

## 4️⃣ Multiple values input

```python
a, b = input("Enter two numbers separated by space: ").split()
a = int(a)
b = int(b)
print(a + b)
```

* `.split()` → inputni bo‘lib beradi
* `.split(',')` → vergul bilan bo‘lish mumkin

### a) List comprehension bilan

```python
nums = [int(x) for x in input("Enter numbers: ").split()]
print(nums)
```

* Foydalanuvchi `"1 2 3 4"` → `[1, 2, 3, 4]`

---

## 5️⃣ Input validation

```python
age = input("Enter age: ")
if not age.isdigit():
    print("Invalid input!")
else:
    age = int(age)
    print("Age:", age)
```

* `.isdigit()` → faqat raqamlar tekshirish uchun
* `.isalpha()`, `.isalnum()` ham mavjud

---

## 6️⃣ Practical examples

### a) Odd or Even

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### b) Simple Calculator

```python
a, b = [float(x) for x in input("Enter two numbers: ").split()]
op = input("Enter operation (+,-,*,/): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
```

---

## 7️⃣ Common pitfalls

❌ Foydalanuvchi kiritgan qiymatni avtomatik number deb hisoblash:

```python
x = input("Enter number: ")
print(x + 5)  # TypeError, x str
```

✅ To‘g‘ri:

```python
x = int(input("Enter number: "))
print(x + 5)
```

❌ Multiple values split qilmaslik:

```python
a, b = input("Enter numbers: ")  # ValueError
```

* To‘g‘ri: `.split()` ishlatish

---
# 🖨️ **Output Formatting in Python**

## 🎯 Asosiy g‘oya

Python’da **natijalarni chiqarish** uchun bir nechta usullar mavjud:

1. **Basic `print()`**
2. **Old-style formatting (`%`)**
3. **`str.format()` method**
4. **f-strings (Python 3.6+)**

---

## 1️⃣ Basic `print()`

```python
name = "Alice"
age = 25

print(name, "is", age, "years old")  # Alice is 25 years old
```

* `,` → avtomatik space qo‘shadi
* Har xil type’lar bilan ishlaydi (int, str, float)

---

### a) Separator va End parametrlar

```python
print("Python", "Java", "C++", sep=", ")  # Python, Java, C++
print("Hello", end="!")                     # Hello!
```

* `sep` → elementlar orasidagi delimiter
* `end` → print oxirida nima chiqishini belgilaydi

---

## 2️⃣ Old-style formatting (`%`)

```python
name = "Alice"
age = 25
print("%s is %d years old" % (name, age))
```

* `%s` → string
* `%d` → integer
* `%f` → float

```python
pi = 3.14159
print("Pi = %.2f" % pi)  # Pi = 3.14
```

* `.2f` → 2 decimal places

---

## 3️⃣ `str.format()` method

```python
name = "Alice"
age = 25
print("{} is {} years old".format(name, age))
```

* Positional arguments:

```python
print("{1} is {0} years old".format(age, name))  # Alice is 25 years old
```

* Named arguments:

```python
print("{n} is {a} years old".format(n=name, a=age))  # Alice is 25 years old
```

* Float formatting:

```python
pi = 3.14159
print("{:.2f}".format(pi))  # 3.14
```

---

## 4️⃣ f-strings (Python 3.6+)

```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")  # Alice is 25 years old
```

* `{}` ichida **har qanday expression** ishlaydi:

```python
a = 5
b = 10
print(f"{a} + {b} = {a+b}")  # 5 + 10 = 15
```

* Float formatting:

```python
pi = 3.14159
print(f"Pi = {pi:.3f}")  # Pi = 3.142
```

* Alignment:

```python
name = "Alice"
print(f"{name:<10}Hello")  # Alice     Hello (left-align)
print(f"{name:>10}Hello")  #      AliceHello (right-align)
print(f"{name:^10}Hello")  #   Alice   Hello (center-align)
```

---

## 5️⃣ Multiple line output

```python
print("Line1\nLine2\nLine3")
```

* `\n` → new line
* `\t` → tab

---

## 6️⃣ Practical example

```python
items = ["Apple", "Banana", "Cherry"]
prices = [100, 50, 75]

print("Item      Price")
print("-------------")
for item, price in zip(items, prices):
    print(f"{item:<10} {price:>5}")
```

Natija:

```
Item      Price
-------------
Apple       100
Banana       50
Cherry       75
```

* `:<10` → left align 10 spaces
* `:>5` → right align 5 spaces

---

## 7️⃣ Common pitfalls

❌ Concatenation bilan xatolik

```python
age = 25
print("Age: " + age)  # TypeError
```

✅ To‘g‘ri:

```python
print("Age:", age)           # 25
print("Age: " + str(age))    # Age: 25
print(f"Age: {age}")         # Age: 25
```

---
# 🔧 **Operators in Python**

Python’da operatorlar yordamida **arifmetik, mantiqiy va bit-level amallar** bajariladi.

Ularni **7 guruhga** bo‘lish mumkin:

---

## 1️⃣ Arithmetic Operators (➕➖*➗)

| Operator | Maqsad        | Misol    | Natija      |
| -------- | ------------- | -------- | ----------- |
| `+`      | Qo‘shish      | `5 + 3`  | 8           |
| `-`      | Ayirish       | `5 - 3`  | 2           |
| `*`      | Ko‘paytirish  | `5 * 3`  | 15          |
| `/`      | Bo‘lish       | `5 / 2`  | 2.5 (float) |
| `//`     | Butun bo‘lish | `5 // 2` | 2           |
| `%`      | Qoldiq        | `5 % 2`  | 1           |
| `**`     | Daraja        | `2 ** 3` | 8           |

**Amaliy misol:**

```python
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
# 13 7 30 3.3333333333333335 3 1 1000
```

---

## 2️⃣ Comparison Operators (⚖️)

| Operator | Maqsad           | Misol    | Natija |
| -------- | ---------------- | -------- | ------ |
| `==`     | Teng             | `5 == 5` | True   |
| `!=`     | Teng emas        | `5 != 3` | True   |
| `>`      | Katta            | `5 > 3`  | True   |
| `<`      | Kichik           | `5 < 3`  | False  |
| `>=`     | Katta yoki teng  | `5 >= 5` | True   |
| `<=`     | Kichik yoki teng | `5 <= 3` | False  |

**Amaliy misol:**

```python
x = 10
y = 20
print(x == y, x != y, x > y, x < y, x >= 10, y <= 20)
# False True False True True True
```

---

## 3️⃣ Logical Operators (🔗)

| Operator | Maqsad                       | Misol            | Natija |
| -------- | ---------------------------- | ---------------- | ------ |
| `and`    | Hammasi True bo‘lsa True     | `True and False` | False  |
| `or`     | Kamida biri True bo‘lsa True | `True or False`  | True   |
| `not`    | Mantiqiy inkor               | `not True`       | False  |

**Amaliy misol:**

```python
x = 10
y = 5
print(x > 5 and y < 10)  # True
print(x < 5 or y < 10)   # True
print(not x == 10)       # False
```

---

## 4️⃣ Assignment Operators (📝)

| Operator | Maqsad                 | Misol                  |
| -------- | ---------------------- | ---------------------- |
| `=`      | Oddiy taqsimlash       | `x = 5`                |
| `+=`     | Qo‘shib tayinlash      | `x += 3` → `x = x + 3` |
| `-=`     | Ayirib tayinlash       | `x -= 2`               |
| `*=`     | Ko‘paytirib tayinlash  | `x *= 4`               |
| `/=`     | Bo‘lib tayinlash       | `x /= 2`               |
| `//=`    | Butun bo‘lib tayinlash | `x //= 3`              |
| `%=`     | Qoldiq bilan tayinlash | `x %= 3`               |
| `**=`    | Daraja bilan tayinlash | `x **= 2`              |

**Amaliy misol:**

```python
x = 10
x += 5  # x = 15
x *= 2  # x = 30
x %= 7  # x = 2
print(x)
```

---

## 5️⃣ Bitwise Operators (🔢)

| Operator | Maqsad      | Misol    | Natija |    |   |
| -------- | ----------- | -------- | ------ | -- | - |
| `&`      | AND         | `5 & 3`  | 1      |    |   |
| `        | `           | OR       | `5     | 3` | 7 |
| `^`      | XOR         | `5 ^ 3`  | 6      |    |   |
| `~`      | NOT         | `~5`     | -6     |    |   |
| `<<`     | Left shift  | `5 << 1` | 10     |    |   |
| `>>`     | Right shift | `5 >> 1` | 2      |    |   |

**Amaliy misol:**

```python
a = 5      # 0b0101
b = 3      # 0b0011
print(a & b)  # 1 (0b0001)
print(a | b)  # 7 (0b0111)
print(a ^ b)  # 6 (0b0110)
print(~a)     # -6
print(a << 1) # 10
print(a >> 1) # 2
```

---

## 6️⃣ Membership Operators (👥)

| Operator | Maqsad             | Misol              | Natija |
| -------- | ------------------ | ------------------ | ------ |
| `in`     | Ichida mavjud      | `'a' in 'cat'`     | True   |
| `not in` | Ichida mavjud emas | `'x' not in 'cat'` | True   |

**Amaliy misol:**

```python
lst = [1,2,3]
print(2 in lst)       # True
print(5 not in lst)   # True
```

---

## 7️⃣ Identity Operators (🆔)

| Operator | Maqsad                        | Misol        | Natija     |
| -------- | ----------------------------- | ------------ | ---------- |
| `is`     | Object identity (same object) | `a is b`     | True/False |
| `is not` | Object identity emas          | `a is not b` | True/False |

**Amaliy misol:**

```python
a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)      # True (same object)
print(a is c)      # False (different object, even if values same)
print(a == c)      # True (values equal)
```

---
# 📝 **Expressions in Python**

## 🎯 Asosiy g‘oya

**Expression** — bu **Python’da qiymatni hisoblaydigan kod qismi**.

* Har bir expression **value** (qiymat) beradi
* Oddiy son, string, yoki murakkab arifmetik, mantiqiy, yoki function chaqiruvlar expression bo‘lishi mumkin

---

## 1️⃣ Simple expressions

```python
x = 5 + 3     # 8
y = x * 2     # 16
name = "Alice" + " " + "Bob"  # "Alice Bob"
```

* `5 + 3` → int expression
* `"Alice" + " " + "Bob"` → str expression

---

## 2️⃣ Comparison expressions

```python
a = 10
b = 20
print(a > b)   # False
print(a == 10) # True
print(a != b)  # True
```

* Har bir comparison expression → **bool** qiymat beradi

---

## 3️⃣ Logical expressions

```python
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

* `and`, `or`, `not` → **bool** expression

---

## 4️⃣ Assignment as an expression?

```python
x = 5  # assignment statement
```

* **Assignment** → statement, expression emas
* Lekin Python 3.8+ da **walrus operator `:=`** expression sifatida ishlaydi:

```python
if (n := len("Hello")) > 3:
    print(n)  # 5
```

* `n := len("Hello")` → **expression**, qiymat qaytaradi

---

## 5️⃣ Function calls as expressions

```python
def add(a, b):
    return a + b

result = add(10, 5)  # function call → expression
print(result)         # 15
```

* Har bir function chaqiruvi → value qaytaradi
* Shu sababli assignment yoki boshqa expressions ichida ishlatilishi mumkin

---

## 6️⃣ Chained expressions

```python
x = (5 + 3) * 2 - 4 / 2
print(x)  # 14.0
```

* Arifmetik expressions birlashtiriladi
* Operator precedence → qiymatni aniqlaydi

```python
y = 10 > 5 and 3 < 2 or not False
print(y)  # True
```

* Logical expressions ham chaining mumkin

---

## 7️⃣ Expressions with data structures

```python
lst = [1,2,3]
total = sum(lst) + len(lst)  # sum(lst) → 6, len(lst) → 3 → total = 9
print(total)
```

* Har bir function call, arithmetic, indexing → **expression**

```python
print(lst[0] + lst[-1])  # 1 + 3 = 4
```

---

## 8️⃣ Expressions vs Statements

| Feature                           | Expression | Statement   |
| --------------------------------- | ---------- | ----------- |
| Returns value?                    | ✅ Yes      | ❌ No        |
| Can be part of larger expression? | ✅ Yes      | ❌ No        |
| Example                           | `5 + 3`    | `x = 5 + 3` |

* **Assignment** → statement
* **Function call, arithmetic, logical operations** → expression

---
# 📊 **Operator Precedence in Python**

## 🎯 Asosiy g‘oya

**Operator precedence** — bu **Python expression ichidagi operatorlarning bajarilish tartibi**.

* Yuqori precedence → oldin bajariladi
* Past precedence → keyin bajariladi
* Parentheses `( )` → **eng yuqori ustuvorlik**, har doim birinchi bajariladi

---

## 1️⃣ Python operator precedence hierarchy (asosiy)

| Precedence  | Operators                                                 | Example                             |    |    |
| ----------- | --------------------------------------------------------- | ----------------------------------- | -- | -- |
| 1 (highest) | `()`                                                      | `(2 + 3) * 4`                       |    |    |
| 2           | `**`                                                      | `2 ** 3 ** 2`                       |    |    |
| 3           | `+x, -x, ~x` (unary plus, minus, bitwise NOT)             | `-5`, `+3`, `~2`                    |    |    |
| 4           | `*, /, //, %`                                             | `2 * 3`, `5 / 2`, `5 // 2`, `5 % 2` |    |    |
| 5           | `+, -`                                                    | `2 + 3 - 1`                         |    |    |
| 6           | `<<, >>` (bitwise shift)                                  | `2 << 1`                            |    |    |
| 7           | `&` (bitwise AND)                                         | `5 & 3`                             |    |    |
| 8           | `^` (bitwise XOR)                                         | `5 ^ 3`                             |    |    |
| 9           | `                                                         | ` (bitwise OR)                      | `5 | 3` |
| 10          | Comparison `==, !=, >, <, >=, <=, is, is not, in, not in` | `5 > 3`                             |    |    |
| 11          | `not` (logical NOT)                                       | `not True`                          |    |    |
| 12          | `and` (logical AND)                                       | `True and False`                    |    |    |
| 13 (lowest) | `or` (logical OR)                                         | `True or False`                     |    |    |

* **Left-to-right** yoki **Right-to-left** — operator turiga qarab
* Example: exponentiation (`**`) → **right-to-left**

---

## 2️⃣ Practical examples

### a) Arithmetic

```python
x = 2 + 3 * 4
print(x)  # 14, * oldin bajarildi

y = (2 + 3) * 4
print(y)  # 20, parentheses oldin bajarildi
```

### b) Exponentiation

```python
z = 2 ** 3 ** 2  # 2 ** (3 ** 2) → 2 ** 9
print(z)  # 512
```

### c) Unary vs Binary

```python
x = -3 ** 2  # -(3**2)
print(x)  # -9

y = (-3) ** 2
print(y)  # 9
```

---

### d) Logical

```python
a = True or False and False
# and → oldin bajariladi: False and False → False
# or → keyin: True or False → True
print(a)  # True
```

### e) Comparison chaining

```python
x = 5
print(1 < x < 10)  # True
```

* Python allows **chained comparisons**
* Equivalent: `(1 < x) and (x < 10)`

---

### f) Bitwise

```python
x = 5 & 3 | 2
# & → oldin bajariladi: 5 & 3 = 1
# | → keyin: 1 | 2 = 3
print(x)  # 3
```

---

## 3️⃣ Parentheses as a tool

* Murakkab expressions → **har doim** parentheses bilan tartibni aniqlash tavsiya etiladi

```python
result = (2 + 3) * (4 - 1) ** 2
print(result)  # 45
```

* O‘qish oson va xatolar kamayadi

---

## 4️⃣ Summary Rules

1. Parentheses `( )` → eng yuqori ustuvorlik
2. Exponentiation `**` → right-to-left
3. Unary operators `+,-,~` → next
4. Multiplication, division, modulo, floor → left-to-right
5. Addition, subtraction → left-to-right
6. Bitwise → shift → AND → XOR → OR
7. Comparison → logical NOT → logical AND → logical OR → lowest

---