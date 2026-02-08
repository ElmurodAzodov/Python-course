
# **STAGE 0 — Programming & Python Foundations**
---
# ⚙️ **What Programming Is**

## 🎯 Asosiy g‘oya

**Programming (dasturlash)** — bu **kompyuterga nima qilish kerakligini aytish jarayoni**.

* Siz **algoritm** yaratib, uni **kompyuterga tushunarli tarzda** yozasiz
* Kompyuter **o‘z-o‘zidan fikrlay olmaydi**, faqat koddagi ko‘rsatmalarni bajaradi

---

## 1️⃣ Dasturlashning vazifalari

1. **Muammoni hal qilish** → masalan, foydalanuvchi yoshini tekshash
2. **Ma’lumotlarni qayta ishlash** → arifmetik, matn, fayllar
3. **Takrorlanuvchi jarayonlarni avtomatlashtirish** → loops, functions
4. **Interaktiv tizimlar yaratish** → input/output

---

## 2️⃣ Programming vs Algorithm

* **Algorithm** → muammoni hal qilishning **ketma-ket qoidalari**
* **Program** → algorithmni **kompyuter tushunadigan kodga** aylantirish

**Misol: Odd or Even**

1. Algorithm:

```
Step 1: Input a number
Step 2: Divide number by 2
Step 3: If remainder is 0 → Even
Step 4: Else → Odd
```

2. Program (Python):

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

* Algorithm → fikrlash qismi
* Program → kodlash qismi

---

## 3️⃣ Programming is about **instructions**

Kompyuter **har bir instruction**ni ketma-ket bajaradi:

| Instruction | Example             | Description                     |
| ----------- | ------------------- | ------------------------------- |
| Input       | `input()`           | Foydalanuvchidan ma’lumot olish |
| Process     | `x + y`             | Ma’lumotlarni hisoblash         |
| Decision    | `if ... else`       | Shart bo‘yicha tanlash          |
| Loop        | `for i in range(5)` | Takrorlash                      |
| Output      | `print()`           | Natijani chiqarish              |

---

## 4️⃣ High-level vs Low-level programming

* **High-level language** → odam uchun tushunarli (Python, C++, Java)
* **Low-level language** → kompyuterga yaqin (Assembly, Machine code)

**Python → High-level → tez yozish, oson tushunish, portable**

---

## 5️⃣ Key concepts in programming

1. **Variables (o‘zgaruvchilar)** → ma’lumot saqlash
2. **Data types** → int, float, str, bool
3. **Operators** → arifmetik va mantiqiy amallar
4. **Control flow** → if, else, loops
5. **Functions / Modules** → kodni qayta ishlatish
6. **Input/Output** → interaktivlik
7. **Comments / Documentation** → kodni tushunish osonligi

---

## 6️⃣ Practical example

**Masala:** Foydalanuvchi yoshini tekshirish va kattalar yoki bolalar deb chiqarish

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Child")
```

* **Step 1:** Input → `age = int(input(...))`
* **Step 2:** Decision → `if age >= 18:`
* **Step 3:** Output → `print()`

---

## 7️⃣ Why learn programming?

* Muammolarni **algoritmik fikrlash** bilan hal qilish
* Takrorlanuvchi ishlarni **avtomatlashtirish**
* Katta ma’lumotlarni **tez va ishonchli** ishlash
* Interaktiv va veb tizimlar, AI, data science, o‘yinlar yaratish
---
# 🐍 **What Python Is (Language vs Implementation)**

## 🎯 Asosiy g‘oya

Python — bu **yuqori darajadagi, interpreted, dynamically typed programming language**.

Python haqida tushunish uchun ikki jihat mavjud:

1. **Python as a Language (Til)**
2. **Python as an Implementation (Amalga oshirish)**

---

## 1️⃣ Python as a Language

* **Syntax & semantics** → kodni qanday yozish va nimani anglatishi
* **Features**:

| Feature           | Description                                    |
| ----------------- | ---------------------------------------------- |
| High-level        | Odam uchun tushunarli, abstrakt                |
| Interpreted       | Kodni qatorma-qator bajaradi                   |
| Dynamically typed | Variable turini belgilash shart emas           |
| Object-oriented   | Class, object, inheritance mavjud              |
| Multi-paradigm    | Procedural, functional, object-oriented coding |

**Example: Python syntax**

```python
name = "Alice"  # variable assignment
age = 25
print(f"{name} is {age} years old")
```

* Shu syntax boshqa Python implementatsiyalarida ham ishlaydi
* Tilning **standard specification** → Python Language Reference

---

## 2️⃣ Python as an Implementation

Python tilini **kompyuter bajaradigan shaklga aylantiradigan dastur**:

| Implementation  | Description                                         |
| --------------- | --------------------------------------------------- |
| **CPython**     | Default, C’da yozilgan, standard Python interpreter |
| **PyPy**        | JIT compiler, tez ishlashga mo‘ljallangan           |
| **Jython**      | Java platformasida ishlaydi                         |
| **IronPython**  | .NET platformasida ishlaydi                         |
| **MicroPython** | Embedded devices, microcontrollers                  |

* **Implementation** → tilning amalda ishlash shakli
* Syntax → bir xil, lekin **performance, libraries, platform compatibility** farq qiladi

---

## 3️⃣ CPython Overview (bir oz ko‘rib chiqamiz)

* **CPython** — default Python interpreter
* Kodni **bytecode** ga o‘girish → virtual machine bajaradi

```python
x = 10
print(x)
```

* `x = 10` → Python bytecode → CPython VM bajaradi
* Shu sababli Python interpreted, lekin **JIT** orqali tezlashtirish mumkin (PyPy)

---

## 4️⃣ Practical distinction

```python
# Python as a language
a = [1, 2, 3]  # list, syntax is same

# Python implementation effect
# CPython → standart interpreter
# PyPy → tezroq execution
# Jython → JVM da ishlaydi
```

* Kod **bir xil**, lekin **platform, speed, memory usage** turlicha

---

## 5️⃣ Key points

* Python **Language** → **syntax, semantics, features**
* Python **Implementation** → **kompyuterga qanday bajarish**, interpreter / compiler
* Masalan:

```python
print("Hello, World!")
```

* Bu Python tilining **syntax** qismi
* Siz **CPython** yoki **PyPy** ishlatsangiz ham, natija **Hello, World!**

---

## 6️⃣ Why this distinction matters

* Performance optimizations → PyPy vs CPython
* Platform compatibility → Jython, IronPython
* Embedded systems → MicroPython
* Standard library → language specification bilan bir xil

---

# 🔧 **CPython Overview**

## 🎯 Asosiy g‘oya

**CPython** — bu Python’ning **standard va default implementatsiyasi** bo‘lib, **C dasturlash tilida yozilgan interpreter** hisoblanadi.

* Python tilidagi kodni **kompyuter tushunadigan bytecode** ga aylantiradi
* Bytecode → Python Virtual Machine (PVM) tomonidan bajariladi

---

## 1️⃣ CPython qanday ishlaydi?

1. **Source Code** → Python tilida yozilgan fayl (`.py`)
2. **Parsing** → Syntax tekshiriladi, AST (Abstract Syntax Tree) hosil qilinadi
3. **Compilation** → Bytecode (`.pyc`) ga aylantiriladi
4. **Execution** → Python Virtual Machine bajaradi

**Diagramma (soddalashtirilgan):**

```
Python code (.py) 
       ↓
   Parser → AST
       ↓
Compilation → Bytecode (.pyc)
       ↓
Python Virtual Machine → Execution
```

---

## 2️⃣ Bytecode nima?

* **Bytecode** — Python interpreter tushunadigan **o‘rta kod**
* Platformdan mustaqil
* `.pyc` fayllarda saqlanishi mumkin → keyingi ishga tushirish tezroq

```python
# Misol
x = 5 + 3
```

* CPython → `x = 5 + 3` kodini bytecode’ga o‘girish
* Keyin PVM uni bajaradi → `x = 8`

---

## 3️⃣ Features of CPython

* **Default Python interpreter** → o‘rnatilgan bo‘ladi
* **C API** → Python kodini C extension’lar bilan integratsiya qilish
* **Garbage Collector** → Automatic memory management
* **Dynamic typing & high-level abstractions**
* **Cross-platform** → Windows, Linux, macOS

---

## 4️⃣ Practical example

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

* CPython ishlashi jarayoni:

1. Parser → kod sintaksis tekshiriladi
2. Compilation → `add` function bytecode’ga aylantiriladi
3. Execution → PVM `5 + 3` ni hisoblaydi va `8` natija beradi

* Siz **interpreterni ochganingizda**, CPython shu jarayonni bajaradi

---

## 5️⃣ `.pyc` files

* Python kodini birinchi marta bajarishda **bytecode** kompilyatsiya qilinadi
* `.pyc` fayl → keyingi ishga tushirishni tezlashtiradi

```bash
__pycache__/example.cpython-310.pyc
```

* Platform va Python version bilan bog‘liq
* Foydalanuvchi ko‘pincha bu bilan ishlamaydi, CPython avtomatik boshqaradi

---

## 6️⃣ Advantages of CPython

* Standard va eng keng tarqalgan
* C extension’lari bilan integratsiya
* Cross-platform, stable, well-documented
* Ideal for beginners va production

---

## 7️⃣ Limitations

* **Speed** → interpreted bo‘lgani uchun boshqa JIT interpreters (PyPy) dan sekinroq
* **Global Interpreter Lock (GIL)** → parallel CPU-bound threads’larda cheklov
* Memory footprint → ba’zan yuqori

---
## **.pyc va PVM haqida qisqacha**
---

### 1️⃣ `.pyc` fayllar

* `.pyc` — bu **Python kompilyatsiyasi natijasi** (compiled file).
* Python kodi (`.py` fayl) **to‘g‘ridan-to‘g‘ri mashina kodi** emas, balki **bytecode** ga aylanadi.
* Bytecode — bu **Python Virtual Machine (PVM)** tomonidan ishlatiladigan o‘rta darajadagi ko‘rsatmalar.

**Jarayoni:**

1. Siz `script.py` yozasiz.
2. Python ishga tushganda:

   * Kodni tekshiradi.
   * Uni **bytecode** ga kompilyatsiya qiladi.
   * Natijani `__pycache__/script.cpython-3x.pyc` ga saqlaydi.
3. Keyingi ishga tushirishda, `.pyc` mavjud bo‘lsa, PVM **tezroq ishlaydi**, chunki kompilyatsiya qilish kerak emas.

Misol:

```bash
python example.py
# __pycache__/example.cpython-310.pyc yaratiladi
```

> **Eslatma:** `.pyc` faylni o‘zgartirmasangiz, Python kodi xuddi `.py` fayl bilan bir xil ishlaydi.

---

### 2️⃣ PVM (Python Virtual Machine)

* **PVM** — Python interpretatori ichida ishlaydigan **virtual mashina**.
* U `bytecode` ni qabul qiladi va **kompyuterning haqiqiy mashina kodiga aylantirib bajaradi**.
* PVM bo‘lmasa, Python kodi ishlamaydi.

**Jarayonni tushuntirish (soddalashtirilgan):**

```
.py fayl  → (Python interpretatori) → bytecode (.pyc) → (PVM) → natija ekranda
```

**Misol bilan:**

```python
print("Salom!")
```

1. Python `print("Salom!")` ni bytecode ga aylantiradi.
2. PVM bytecode ni o‘qiydi va ekranga `Salom!` chiqaradi.

---
# 🔄 **Interpreter vs Compiler**

## 🎯 Asosiy g‘oya

Dastur kodini kompyuter tushunadigan shaklga aylantirish uchun **ikkita yondashuv** mavjud:

1. **Compiler (kompilyator)**
2. **Interpreter (tarjimon)**

Python — **interpreted language**, lekin bu tushuncha yanada aniqlik talab qiladi.

---

## 1️⃣ Compiler nima?

* **Whole program**ni bir martada machine code’ga (binary) o‘giradi
* Natijada **standalone executable** hosil bo‘ladi
* **Bajarilish** → kompilatsiyadan keyin

| Feature           | Description                                 |
| ----------------- | ------------------------------------------- |
| Example languages | C, C++, Rust                                |
| Compilation time  | Oldindan, kod bajarilishidan oldin          |
| Execution         | Tez (direct machine code)                   |
| Errors            | Butun kod tekshiriladi, compile-time errors |
| Debugging         | Qiyinroq, chunki machine code ko‘rish qiyin |

**Misol: C dastur**

```c
#include <stdio.h>
int main() {
    int x = 5;
    printf("%d\n", x);
    return 0;
}
```

* `gcc program.c -o program` → executable hosil bo‘ladi
* Keyin `./program` → 5 natija beradi

---

## 2️⃣ Interpreter nima?

* Kodni **qatorma-qator o‘qiydi va bajaradi**
* **Runtime errors** → bajarish vaqtida paydo bo‘ladi
* Tezroq yozish va debugging uchun qulay

| Feature           | Description                 |
| ----------------- | --------------------------- |
| Example languages | Python, Ruby, JavaScript    |
| Compilation time  | Yo‘q (line by line)         |
| Execution         | Line by line                |
| Errors            | Runtime errors              |
| Debugging         | Oson, print yoki REPL bilan |

**Python misol**

```python
x = 5
print(x)
```

* `python script.py` → interpreter → qatorma-qator bajaradi

---

## 3️⃣ Key differences: Interpreter vs Compiler

| Feature         | Compiler              | Interpreter           |
| --------------- | --------------------- | --------------------- |
| Execution       | Whole program         | Line by line          |
| Error detection | Compile-time          | Runtime               |
| Speed           | Faster (machine code) | Slower (line by line) |
| Flexibility     | Less interactive      | Interactive (REPL)    |
| Examples        | C, C++, Rust          | Python, Ruby, JS      |

---

## 4️⃣ Python qanday ishlaydi?

* **CPython interpreter** → Python code → bytecode → PVM
* Shunday qilib, **Python interpreted**, lekin **bytecode compilation** orqali qisman kompilyatsiya qilinadi

```python
x = 10
y = 5
print(x + y)
```

1. CPython → parse & compile → bytecode
2. Python Virtual Machine → execute bytecode → 15

* Shuning uchun Python **line-by-line** ishlaydi, lekin **bytecode** yordamida tezroq

---

## 5️⃣ Practical analogy

* **Compiler** → kitobni **butunlay tarjima qilib keyin chiqaradi**
* **Interpreter** → kitobni **sahifa-sahifa tarjima qiladi**

---

## 6️⃣ Advantages of interpreter (Python)

* Tez prototyping → kodni darhol bajarish mumkin
* Interactive debugging → REPL bilan ishlash
* Platform-independent → bytecode PVM orqali ishlaydi

---
# 🏃 **Python Execution Model**

## 🎯 Asosiy g‘oya

**Python Execution Model** — bu Python dasturi:

> **yozilishidan → bajarilishigacha bo‘lgan barcha bosqichlar**

qanday ishlashini tushuntiradi.

Python’da kod **to‘g‘ridan-to‘g‘ri CPU tomonidan bajarilmaydi**.
U **bir necha oraliq bosqichlardan** o‘tadi.

---

## 1️⃣ Python dasturi ishga tushganda nima bo‘ladi?

Quyidagi oddiy kodni olaylik:

```python
x = 10
y = 5
print(x + y)
```

Bu kod bajarilganda **quyidagi jarayonlar** sodir bo‘ladi:

```
Source Code (.py)
      ↓
Lexing & Parsing
      ↓
AST (Abstract Syntax Tree)
      ↓
Bytecode Compilation
      ↓
Python Virtual Machine (PVM)
      ↓
Execution (Output)
```

---

## 2️⃣ Lexing va Parsing (Syntax tekshirish)

### 🔹 Lexing

* Kod **token**larga bo‘linadi
* Masalan:

```python
x = 10
```

Tokenlar:

* `x` → identifier
* `=` → assignment
* `10` → integer literal

### 🔹 Parsing

* Tokenlar asosida **syntax to‘g‘rimi yoki yo‘qmi** tekshiriladi

❌ Syntax error misol:

```python
if x > 5
    print(x)
```

* Bu bosqichda Python to‘xtaydi
* **Bajarilish bo‘lmaydi**

---

## 3️⃣ AST — Abstract Syntax Tree

* Kod **daraxt ko‘rinishida** ifodalanadi
* Python kodning **ma’nosini** tushunadi

```python
x = 10 + 5
```

AST taxminan shunday:

```
Assign
 ├── Name: x
 └── Add
     ├── Constant: 10
     └── Constant: 5
```

* AST → keyingi bosqichga tayyor holat

---

## 4️⃣ Bytecode Compilation

* AST → **bytecode** ga aylantiriladi
* Bytecode → Python’ning **o‘ziga xos instruktsiyalari**

```python
x = 10 + 5
```

Bytecode (soddalashtirilgan):

```
LOAD_CONST 10
LOAD_CONST 5
BINARY_ADD
STORE_NAME x
```

📌 Muhim:

* Bytecode **platformdan mustaqil**
* `.pyc` fayllarda saqlanishi mumkin

---

## 5️⃣ Python Virtual Machine (PVM)

* Bytecode’ni **qatorma-qator bajaradi**
* PVM → CPython ichidagi virtual processor

```python
print(x)
```

* PVM:

  1. `x` ni xotiradan oladi
  2. `print` funksiyasini chaqiradi
  3. Natijani chiqaradi

---

## 6️⃣ `.pyc` va `__pycache__`

* Python modul birinchi marta yuklanganda:

  * Bytecode yaratiladi
  * `__pycache__/module.cpython-310.pyc` saqlanadi

📌 Foyda:

* Keyingi ishga tushirish tezroq
* Agar `.py` o‘zgarsa → `.pyc` qayta yaratiladi

---

## 7️⃣ Runtime Execution

* Execution vaqtida:

  * Variables xotirada yaratiladi
  * Objects heap’da saqlanadi
  * Reference count va garbage collection ishlaydi

❌ Runtime error misol:

```python
x = 10
print(y)
```

* Syntax to‘g‘ri
* Lekin `y` yo‘q → **NameError (runtime error)**

---

## 8️⃣ Python Execution Model vs Compiler Model

| Python             | C / C++                 |
| ------------------ | ----------------------- |
| Bytecode + VM      | Machine code            |
| Runtime error ko‘p | Compile-time error ko‘p |
| Dynamic typing     | Static typing           |
| REPL mavjud        | REPL yo‘q               |

---

## 9️⃣ Nima uchun bu muhim?

* **Performance** tushunish
* **Debugging** osonlashadi
* `.pyc`, import, execution order tushuniladi
* Advanced mavzular (GIL, memory, optimization) uchun asos bo‘ladi

---
# 📄 **Python Source Files (.py)**

## 🎯 Asosiy g‘oya

**Python source file** — bu Python kod yozilgan **oddiy matnli fayl** bo‘lib, odatda **`.py`** kengaytmaga ega bo‘ladi.

* Python interpreter aynan shu fayllarni o‘qiydi va bajaradi
* Bu fayllar **Python Execution Model** dagi birinchi bosqich hisoblanadi

---

## 1️⃣ Python source file nima?

* Oddiy **text file**
* Ichida:

  * Python statements
  * expressions
  * functions
  * classes
  * comments
  * docstrings bo‘lishi mumkin

📌 Misol: `hello.py`

```python
print("Hello, World!")
```

Ishga tushirish:

```bash
python hello.py
```

Natija:

```
Hello, World!
```

---

## 2️⃣ `.py` faylning asosiy tuzilishi

Python source file odatda quyidagi qismlardan iborat bo‘lishi mumkin:

```python
# 1. Comments
# 2. Imports
# 3. Constants / Variables
# 4. Functions
# 5. Classes
# 6. Main execution logic
```

### Amaliy misol:

```python
# comment
PI = 3.14

def area(radius):
    return PI * radius ** 2

print(area(5))
```

---

## 3️⃣ Encoding (fayl kodlash)

Python 3’da default encoding → **UTF-8**

* Unicode belgilarni bemalol ishlatish mumkin:

```python
name = "O‘zbekcha matn"
print(name)
```

Agar kerak bo‘lsa, encoding ko‘rsatish mumkin:

```python
# -*- coding: utf-8 -*-
```

📌 Odatda bu **kerak emas**, Python 3’da UTF-8 default.

---

## 4️⃣ Python source file va execution

Python `.py` faylni ishga tushirganda:

1. Fayl o‘qiladi
2. Syntax tekshiriladi
3. Bytecode’ga kompilyatsiya qilinadi
4. Python Virtual Machine bajaradi

Agar syntax xato bo‘lsa:

```python
if True
    print("Hello")
```

Natija:

```
SyntaxError
```

---

## 5️⃣ `__name__ == "__main__"` tushunchasi

Python source file:

```python
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()
```

### Nima uchun kerak?

* Agar fayl **to‘g‘ridan-to‘g‘ri ishga tushirilsa** → kod bajariladi
* Agar fayl **import qilinsa** → main block bajarilmaydi

📌 Bu professional Python’da **juda muhim tushuncha**

---

## 6️⃣ Import va source files

Python source file → **module** bo‘lishi mumkin

```python
# math_utils.py
def add(a, b):
    return a + b
```

```python
# main.py
import math_utils
print(math_utils.add(3, 4))
```

* Har bir `.py` fayl → modul
* Import qilinganda:

  * Kod **bir marta** bajariladi
  * Bytecode cache yaratiladi

---

## 7️⃣ Fayl nomlash qoidalari

✅ To‘g‘ri:

```text
main.py
math_utils.py
user_profile.py
```

❌ Noto‘g‘ri:

```text
my file.py       # bo‘sh joy
123.py           # raqam bilan boshlanish
class.py         # keyword
```

📌 Snake_case tavsiya etiladi.

---

## 8️⃣ Python source file vs Script vs Module

| Tushuncha   | Tavsif                              |
| ----------- | ----------------------------------- |
| Source file | `.py` fayl                          |
| Script      | Bevosita ishga tushiriladigan `.py` |
| Module      | Import qilinadigan `.py`            |
| Package     | Bir nechta modullar papkasi         |

---

## 9️⃣ Common mistakes

❌ `.py.txt` qilib saqlash

❌ Noto‘g‘ri indentation

❌ Fayl nomini keyword bilan nomlash

❌ Encoding muammolari (Python 2’da ko‘p bo‘lgan)

---
# 📊 **Python Versions and Release Cycle**

## 🎯 Asosiy g‘oya

Python — **doimiy rivojlanib boradigan til**.
Shu sababli:

* Python’ning **turli versiyalari** mavjud
* Har bir versiyaning **qo‘llab-quvvatlash muddati** bor
* Har bir yangi versiya **yangi imkoniyatlar**, **bug fixlar** va ba’zan **breaking changes** olib keladi

---

## 1️⃣ Python version nima?

Python version quyidagi ko‘rinishda bo‘ladi:

```
MAJOR.MINOR.MICRO
```

Masalan:

```
Python 3.11.2
```

| Qism  | Ma’nosi                    |
| ----- | -------------------------- |
| MAJOR | Katta o‘zgarishlar (2 → 3) |
| MINOR | Yangi feature’lar          |
| MICRO | Bug fix, xavfsizlik        |

---

## 2️⃣ Python 2 vs Python 3

### 🛑 Python 2 (END OF LIFE)

* Python 2.7 → **2020-yil 1-yanvar** da rasman to‘xtatilgan
* Endi **ishlatilmaydi va tavsiya etilmaydi**

Misol farqi:

```python
# Python 2
print "Hello"

# Python 3
print("Hello")
```

📌 **Hozir faqat Python 3 ishlatiladi**

---

## 3️⃣ Python 3 versionlar evolyutsiyasi

Ba’zi muhim versiyalar:

| Version | Muhim yangilik                        |
| ------- | ------------------------------------- |
| 3.6     | f-strings                             |
| 3.7     | dict order guaranteed                 |
| 3.8     | Walrus operator `:=`                  |
| 3.9     | Type hint improvements                |
| 3.10    | `match / case`                        |
| 3.11    | Katta performance yaxshilanishi       |
| 3.12    | Cleaner internals, deprecated removal |

📌 Python 3 → **orqaga moslikka jiddiy e’tibor beradi**

---

## 4️⃣ Python Release Cycle (hayot aylanishi)

Har bir Python versiya quyidagi bosqichlardan o‘tadi:

```
Alpha → Beta → Release Candidate → Final
```

### Keyin:

```
Bugfix Support → Security Support → End of Life
```

### Odatda:

* **Yangi MAJOR.MINOR** → har yil
* **Bugfix** → ~18 oy
* **Security updates** → ~5 yil

---

## 5️⃣ Release Cycle misoli

Masalan: **Python 3.10**

* 2021 → chiqarilgan
* 2021–2023 → bugfix updates
* 2023–2026 → security updates
* 2026 → End of Life

📌 EOL’dan keyin:

* Xavfsizlik patch yo‘q
* Tavsiya etilmaydi

---

## 6️⃣ Python version qanday tekshiriladi?

### Terminalda:

```bash
python --version
```

yoki:

```bash
python3 --version
```

### Python ichida:

```python
import sys
print(sys.version)
```

---

## 7️⃣ Nima uchun version muhim?

### ❗ Feature availability

```python
match x:
    case 1:
        print("One")
```

* Bu faqat **Python 3.10+** da ishlaydi

---

### ❗ Library compatibility

* Ba’zi kutubxonalar faqat ma’lum versiyalarni qo‘llaydi
* Masalan:

  * NumPy → Python 3.9+
  * Django → ma’lum versiyalar

---

### ❗ Production muhit

* Serverda boshqa version bo‘lishi mumkin
* Virtual environment va version pinning muhim

---

## 8️⃣ Best practices

✅ Python 3 ning **eng so‘nggi stable** versiyasini ishlatish

✅ Virtual environment (`venv`) ishlatish

✅ `requirements.txt` yoki `pyproject.toml` bilan versionlarni belgilash

✅ EOL versiyalarni ishlatmaslik

---
# 📥 **Installing Python Correctly**

## 🎯 Asosiy g‘oya

Python’ni **to‘g‘ri o‘rnatish** degani:

* To‘g‘ri **versiyani tanlash**
* To‘g‘ri **yo‘l (PATH)** sozlash
* To‘g‘ri **bir nechta Python versiyalarni boshqarish**
* **Virtual environment** ishlata olish

---

## 1️⃣ Qaysi Python versiyani o‘rnatish kerak?

✅ Tavsiya:

* **Python 3.x** (eng so‘nggi stable versiya)
* Yangi boshlovchilar uchun: **Python 3.11 yoki 3.12**

❌ O‘rnatmang:

* Python 2.x (EOL)
* Juda eski Python 3 versiyalar

---

## 2️⃣ Windows’da Python o‘rnatish

### 🔹 1-qadam: Rasmiy sayt

👉 [https://www.python.org](https://www.python.org)

* **Downloads → Windows**
* “Download Python 3.x.x”

---

### 🔹 2-qadam: Installer sozlamalari (MUHIM!)

Installer ishga tushganda:

☑️ **Add Python to PATH** (ENG MUHIM)
☑️ **Install launcher for all users**

Keyin:
👉 **Install Now**

📌 Agar PATH belgilanmasa:

```bash
'python' is not recognized as an internal or external command
```

---

### 🔹 3-qadam: Tekshirish

Command Prompt yoki PowerShell’da:

```bash
python --version
```

yoki:

```bash
py --version
```

---

## 3️⃣ macOS’da Python o‘rnatish

### ⚠️ Ogohlantirish

* macOS’da keladigan Python → **system Python**
* Uni o‘zgartirmang ❌

---

### 🔹 Variant 1: Homebrew (Tavsiya)

```bash
brew install python
```

Tekshirish:

```bash
python3 --version
```

---

### 🔹 Variant 2: python.org

* macOS installer yuklab oling
* `.pkg` fayl orqali o‘rnating

---

## 4️⃣ Linux’da Python o‘rnatish

Ko‘p Linux distro’larda Python oldindan bor.

### Tekshirish:

```bash
python3 --version
```

### Agar yo‘q bo‘lsa:

**Ubuntu / Debian:**

```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**

```bash
sudo dnf install python3
```

---

## 5️⃣ Python Launcher (Windows)

Windows’da `py` komandasi mavjud:

```bash
py
py -3.11
py -3.12
```

Bu:

* Bir nechta Python versiyani boshqaradi
* Juda qulay va xavfsiz

---

## 6️⃣ PATH nima va nega muhim?

PATH — bu OS’ga:

> `python` buyrug‘i qayerdan topilishini aytadi

Agar noto‘g‘ri bo‘lsa:

```bash
python: command not found
```

PATH to‘g‘ri bo‘lsa:

```bash
python --version
```

ishlaydi ✅

---

## 7️⃣ Virtual Environment (juda muhim!)

Virtual environment:

* Har bir loyiha uchun alohida Python muhit

Yaratish:

```bash
python -m venv venv
```

Faollashtirish:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

📌 Professional development’da **majburiy**

---

## 8️⃣ pip tekshirish

```bash
pip --version
```

Agar yo‘q bo‘lsa:

```bash
python -m ensurepip --upgrade
```

---

## 9️⃣ Common xatolar

❌ Python’ni bir nechta joydan o‘rnatish

❌ PATH belgilanmasligi

❌ System Python’ni o‘zgartirish

❌ Virtual environment ishlatmaslik

❌ Eski versiyada ishlash

---
# 💻 **Python REPL (Read–Eval–Print Loop)**

## 🎯 Asosiy g‘oya

**Python REPL** — bu Python’ning **interaktiv muhiti** bo‘lib, u yerda:

> kod yoziladi → darhol bajariladi → natija chiqariladi → yana davom etiladi

REPL — **o‘rganish, sinash va tezkor tekshiruvlar** uchun juda qulay.

---

## 1️⃣ REPL nimani anglatadi?

REPL qisqartmasi:

| Harf | Ma’nosi                     |
| ---- | --------------------------- |
| R    | Read – kodni o‘qiydi        |
| E    | Eval – baholaydi (bajaradi) |
| P    | Print – natijani chiqaradi  |
| L    | Loop – yana davom etadi     |

---

## 2️⃣ Python REPL qanday ishga tushiriladi?

### 🔹 Terminalda:

```bash
python
```

yoki:

```bash
python3
```

Natija:

```text
Python 3.11.2 (main, ...)
>>>
```

Bu `>>>` — **REPL prompt**

---

## 3️⃣ REPL’da birinchi buyruq

```python
>>> 2 + 3
5
```

* Siz `print()` yozmadingiz
* REPL natijani avtomatik chiqaradi

📌 Script’da esa:

```python
print(2 + 3)
```

---

## 4️⃣ Variables REPL’da

```python
>>> x = 10
>>> x * 2
20
```

* Variable saqlanadi
* REPL sessiya davomida mavjud

---

## 5️⃣ Funksiya aniqlash REPL’da

```python
>>> def square(x):
...     return x * x
...
>>> square(5)
25
```

📌 `...` → ko‘p qatorli kod belgisi

---

## 6️⃣ REPL vs Script farqi

| REPL          | Script            |
| ------------- | ----------------- |
| Interaktiv    | Oldindan yoziladi |
| Tezkor test   | To‘liq dastur     |
| Natija darhol | `print()` kerak   |
| Vaqtinchalik  | Doimiy fayl       |

---

## 7️⃣ REPL’da xatolar

### Syntax error:

```python
>>> if True
...
SyntaxError
```

### Runtime error:

```python
>>> 10 / 0
ZeroDivisionError
```

📌 Xatolarni **darhol ko‘rasiz**

---

## 8️⃣ REPL’dan chiqish

```python
>>> exit()
```

yoki:

```python
>>> quit()
```

yoki:

**Ctrl + D** (Linux/macOS)
**Ctrl + Z + Enter** (Windows)

---

## 9️⃣ Advanced REPL features

### 🔹 `_` — oxirgi natija

```python
>>> 5 + 5
10
>>> _ * 2
20
```

---

### 🔹 help()

```python
>>> help(str)
```

---

### 🔹 dir()

```python
>>> dir(list)
```

---

## 🔟 IPython va IDLE

* **IDLE** → Python bilan birga keladi
* **IPython** → kuchliroq interaktiv muhit

```bash
pip install ipython
ipython
```

Afzalliklari:

* Syntax highlighting
* Autocomplete
* History

---

## 1️⃣1️⃣ REPL qachon ishlatiladi?

✅ Yangi tushuncha sinash

✅ Funksiya tekshirish

✅ Kutubxona o‘rganish

✅ Debug qilish

✅ Matematik hisob-kitob

❌ Katta loyiha uchun emas
---

# 🚀 **Running Python Scripts**

## 🎯 Asosiy g‘oya

**Python script** — bu `.py` fayl bo‘lib, u **Python interpreter tomonidan yuqoridan pastga qarab** bajariladi.

Scriptni ishga tushirish — Python bilan ishlashning **eng asosiy amaliy ko‘nikmasi**.

---

## 1️⃣ Eng oddiy script

### `hello.py`

```python
print("Hello, World!")
```

Terminalda:

```bash
python hello.py
```

Natija:

```
Hello, World!
```

---

## 2️⃣ Script qayerdan ishga tushiriladi?

### 🔹 1. To‘g‘ri papkada bo‘lish

```bash
cd path/to/your/project
python main.py
```

### 🔹 2. To‘liq yo‘l bilan

```bash
python C:\Users\User\project\main.py
```

(macOS/Linux)

```bash
python3 /home/user/project/main.py
```

---

## 3️⃣ Windows vs macOS/Linux farqlari

### Windows:

```bash
python script.py
```

yoki:

```bash
py script.py
```

### macOS / Linux:

```bash
python3 script.py
```

📌 Sababi: system Python versiyalari farqli bo‘lishi mumkin.

---

## 4️⃣ Virtual environment bilan script ishga tushirish

```bash
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

python app.py
```

📌 Bu professional development uchun **juda muhim**

---

## 5️⃣ `__name__ == "__main__"` bilan ishlash

```python
def main():
    print("Script running")

if __name__ == "__main__":
    main()
```

* Fayl **to‘g‘ridan-to‘g‘ri ishga tushsa** → bajariladi
* Fayl **import qilinsa** → bajarilmaydi

---

## 6️⃣ Script’ga argument berish

```bash
python greet.py Ali
```

```python
# greet.py
import sys
print("Hello", sys.argv[1])
```

Natija:

```
Hello Ali
```

---

## 7️⃣ Script ishga tushirishda xatolar

### ❌ File not found

```bash
python app.py
```

Agar fayl yo‘q bo‘lsa:

```
can't open file
```

---

### ❌ Python topilmadi

```
'python' is not recognized
```

➡ PATH muammosi

---

### ❌ Syntax error

```python
if True
    print("Hi")
```

---

## 8️⃣ Shebang (macOS / Linux)

```python
#!/usr/bin/env python3
print("Hello")
```

Keyin:

```bash
chmod +x script.py
./script.py
```

📌 Windows’da ishlamaydi

---

## 9️⃣ Script vs Module vs Package

| Turi    | Tavsif                 |
| ------- | ---------------------- |
| Script  | Bevosita ishga tushadi |
| Module  | Import qilinadi        |
| Package | Modullar papkasi       |

---

## 🔟 IDE orqali ishga tushirish

* VS Code → Run ▶️
* PyCharm → Run Configuration
* IDLE → Run Module (F5)

📌 IDE aslida terminalda `python script.py` bajaradi

---
# ✏️ **Code Editors and IDEs**

## 🎯 Asosiy g‘oya

Python kodini yozish uchun:

* **Oddiy text editor** yetarli emas ❌
* **Code editor yoki IDE** kerak bo‘ladi ✅

Ular:

* Xatolarni tez topishga
* Kodni chiroyli yozishga
* Ish unumdorligini oshirishga yordam beradi

---

## 1️⃣ Code Editor vs IDE farqi

| Code Editor            | IDE               |
| ---------------------- | ----------------- |
| Yengil                 | Og‘irroq          |
| Tez ochiladi           | Ko‘proq imkoniyat |
| Plugin bilan kengayadi | Hammasi ichida    |
| Masalan: VS Code       | Masalan: PyCharm  |

---

## 2️⃣ Eng mashhur Code Editors

### 🟦 VS Code (ENG TAVSIYA ETILADI)

**Nega?**

* Bepul
* Tez
* Kuchli Python qo‘llab-quvvatlash
* Professional daraja

📌 Kerakli extensionlar:

* Python (Microsoft)
* Pylance
* Black Formatter
* Jupyter

🔹 Afzalliklari:

* Debugger
* Git integratsiya
* Virtual env tanlash
* IntelliSense

---

### 🟨 Sublime Text

* Juda tez
* Minimalist
* Pullik (trial bor)

Kamchiligi:

* Python uchun kamroq “out of the box” imkoniyat

---

### 🟥 Notepad++ (Windows)

* Yengil
* Boshlovchilar uchun

Kamchiligi:

* Katta loyihalar uchun emas

---

## 3️⃣ Eng mashhur Python IDE’lar

### 🟩 PyCharm (Professional Python IDE)

**Ikki turi:**

* Community (bepul)
* Professional (pullik)

Afzalliklari:

* Kuchli debugger
* Refactoring
* Virtual env avtomatik
* Django/Flask support

Kamchiligi:

* Og‘irroq
* Kompyuter resurs talab qiladi

---

### 🟪 IDLE (Python bilan birga keladi)

* Boshlovchilar uchun
* Juda oddiy

Kamchiligi:

* Professional loyiha uchun yetarli emas

---

## 4️⃣ Qaysi birini tanlash kerak?

### 🔰 Boshlovchi:

👉 **VS Code** yoki **IDLE**

### 👨‍💻 O‘rta daraja:

👉 **VS Code + extensions**

### 🧠 Professional:

👉 **VS Code** yoki **PyCharm**

📌 Hozirgi industry standarti: **VS Code**

---

## 5️⃣ Muhim funksiyalar (bo‘lishi shart)

✅ Syntax highlighting
✅ Auto-complete
✅ Linting
✅ Debugger
✅ Git integratsiya
✅ Virtual environment support

---

## 6️⃣ IDE qanday qilib ishni osonlashtiradi?

Misol:

```python
def add(a, b):
    return a + b
```

IDE:

* Typo’ni ko‘rsatadi
* Parametrlarni tavsiya qiladi
* Docstring’ni ko‘rsatadi

---

## 7️⃣ REPL + Editor kombinatsiyasi

* REPL → tez test
* Editor → real loyiha

Professional workflow:

```text
VS Code + Terminal + venv
```

---

## 8️⃣ Common mistakes

❌ Word yoki Google Docs’da kod yozish
❌ Syntax highlighting o‘chirilgan editor
❌ Virtual environment tanlanmagan
❌ Formatter ishlatmaslik

---
# ✏️ **Code Editors and IDEs**

## 🎯 Asosiy g‘oya

Python kodini yozish uchun:

* **Oddiy text editor** yetarli emas ❌
* **Code editor yoki IDE** kerak bo‘ladi ✅

Ular:

* Xatolarni tez topishga
* Kodni chiroyli yozishga
* Ish unumdorligini oshirishga yordam beradi

---

## 1️⃣ Code Editor vs IDE farqi

| Code Editor            | IDE               |
| ---------------------- | ----------------- |
| Yengil                 | Og‘irroq          |
| Tez ochiladi           | Ko‘proq imkoniyat |
| Plugin bilan kengayadi | Hammasi ichida    |
| Masalan: VS Code       | Masalan: PyCharm  |

---

## 2️⃣ Eng mashhur Code Editors

### 🟦 VS Code (ENG TAVSIYA ETILADI)

**Nega?**

* Bepul
* Tez
* Kuchli Python qo‘llab-quvvatlash
* Professional daraja

📌 Kerakli extensionlar:

* Python (Microsoft)
* Pylance
* Black Formatter
* Jupyter

🔹 Afzalliklari:

* Debugger
* Git integratsiya
* Virtual env tanlash
* IntelliSense

---

### 🟨 Sublime Text

* Juda tez
* Minimalist
* Pullik (trial bor)

Kamchiligi:

* Python uchun kamroq “out of the box” imkoniyat

---

### 🟥 Notepad++ (Windows)

* Yengil
* Boshlovchilar uchun

Kamchiligi:

* Katta loyihalar uchun emas

---

## 3️⃣ Eng mashhur Python IDE’lar

### 🟩 PyCharm (Professional Python IDE)

**Ikki turi:**

* Community (bepul)
* Professional (pullik)

Afzalliklari:

* Kuchli debugger
* Refactoring
* Virtual env avtomatik
* Django/Flask support

Kamchiligi:

* Og‘irroq
* Kompyuter resurs talab qiladi

---

### 🟪 IDLE (Python bilan birga keladi)

* Boshlovchilar uchun
* Juda oddiy

Kamchiligi:

* Professional loyiha uchun yetarli emas

---

## 4️⃣ Qaysi birini tanlash kerak?

### 🔰 Boshlovchi:

👉 **VS Code** yoki **IDLE**

### 👨‍💻 O‘rta daraja:

👉 **VS Code + extensions**

### 🧠 Professional:

👉 **VS Code** yoki **PyCharm**

📌 Hozirgi industry standarti: **VS Code**

---

## 5️⃣ Muhim funksiyalar (bo‘lishi shart)

✅ Syntax highlighting
✅ Auto-complete
✅ Linting
✅ Debugger
✅ Git integratsiya
✅ Virtual environment support

---

## 6️⃣ IDE qanday qilib ishni osonlashtiradi?

Misol:

```python
def add(a, b):
    return a + b
```

IDE:

* Typo’ni ko‘rsatadi
* Parametrlarni tavsiya qiladi
* Docstring’ni ko‘rsatadi

---

## 7️⃣ REPL + Editor kombinatsiyasi

* REPL → tez test
* Editor → real loyiha

Professional workflow:

```text
VS Code + Terminal + venv
```

---

## 8️⃣ Common mistakes

❌ Word yoki Google Docs’da kod yozish

❌ Syntax highlighting o‘chirilgan editor

❌ Virtual environment tanlanmagan

❌ Formatter ishlatmaslik

---
# ↪️ **Indentation and Code Blocks**

## 🎯 Asosiy g‘oya

Python’da:

* **{ } yo‘q**
* Kod bloklari **bo‘sh joy (indentation)** bilan belgilanadi
* Indentation → **logik tuzilma**

📌 Boshqa tillardan asosiy farq shu!

---

## 1️⃣ Code block nima?

**Code block** — bu birgalikda bajariladigan kodlar guruhi.

Misol:

```python
if x > 0:
    print("Musbat")
    print("Son")
```

* Bu yerda 2 qator → **bitta code block**

---

## 2️⃣ Indentation qoidalari

### 🔹 Asosiy qoidalar:

✅ Har bir yangi block:

* Oldingisidan **bir xil miqdorda ichkariga suriladi**

✅ Tavsiya:

* **4 ta bo‘sh joy (spaces)**

❌ Tab + space aralashmasi → xato

---

## 3️⃣ Indentation qanday ishlaydi?

Python:

* Qator boshidagi bo‘sh joylarni sanaydi
* Agar noto‘g‘ri bo‘lsa → **IndentationError**

### To‘g‘ri:

```python
if True:
    print("A")
    print("B")
```

### Noto‘g‘ri:

```python
if True:
    print("A")
      print("B")
```

Natija:

```
IndentationError
```

---

## 4️⃣ Qaysi joylarda indentation majburiy?

Indentation **faqat `:` dan keyin** ishlatiladi:

```python
if
elif
else
for
while
def
class
try
except
finally
with
match / case
```

Misol:

```python
for i in range(3):
    print(i)
```

---

## 5️⃣ Nested (ichma-ich) code blocks

```python
if x > 0:
    if x % 2 == 0:
        print("Musbat va juft")
    else:
        print("Musbat va toq")
```

Indentation darajasi:

* 1-daraja → `if x > 0`
* 2-daraja → `if x % 2 == 0`

---

## 6️⃣ else bloklarida indentation

```python
if x > 0:
    print("Musbat")
else:
    print("Manfiy yoki nol")
```

📌 `else` — **if bilan bir darajada** bo‘lishi shart

---

## 7️⃣ Function va class blocklari

### Function:

```python
def greet():
    print("Hello")
    print("World")
```

### Class:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Salom", self.name)
```

---

## 8️⃣ pass — bo‘sh block uchun

Agar block bo‘sh bo‘lsa:

```python
if x > 0:
    pass
```

❌ Bo‘sh qoldirish mumkin emas

---

## 9️⃣ Common indentation xatolar

### ❌ Tab va space aralashmasi

```
TabError: inconsistent use of tabs and spaces
```

### ❌ Block ichida bo‘sh qatorlar

```python
if x > 0:

    print(x)
```

---

## 🔟 IDE yordamida indentation

IDE:

* Avtomatik 4 space qo‘yadi
* Tab → space’ga aylantiradi
* Xatoni ko‘rsatadi

📌 VS Code → juda qulay

---

## 1️⃣1️⃣ Real hayot analogiyasi

Indentation → **ierarxiya**

```text
Uy
 ├── Xona
 │    ├── Stol
 │    └── Kursi
```

Python ham shunday o‘ylaydi 😉

---
# 💬 **Comments and Documentation Strings**

## 🎯 Asosiy g‘oya

Python’da:

* **Comments** → dasturchilar uchun izoh
* **Docstrings** → kodning rasmiy hujjati (documentation)

📌 Python interpreter:

* Comment’larni **e’tiborsiz qoldiradi**
* Docstring’larni esa **maxsus saqlaydi**

---

## 1️⃣ Comments nima?

**Comment** — bu Python tomonidan bajarilmaydigan izoh.

### 🔹 Bir qatorli comment

```python
# Bu comment
x = 10  # bu ham comment
```

📌 `#` dan keyingi hamma narsa comment

---

## 2️⃣ Comment qachon ishlatiladi?

✅ Kod nima qilayotganini tushuntirish
✅ Murakkab joylarni izohlash
✅ TODO / FIX belgilash

```python
# TODO: optimallashtirish kerak
# FIXME: bu yerda xato bor
```

---

## 3️⃣ Noto‘g‘ri comment yozish

❌ Keraksiz comment:

```python
x = x + 1  # x ga 1 qo‘shildi
```

✔ Yaxshi variant:

```python
retry_count += 1
```

📌 Kod o‘zi tushunarli bo‘lsin

---

## 4️⃣ Multi-line comment bormi?

Python’da **haqiqiy multi-line comment yo‘q**.

❌ Noto‘g‘ri tushuncha:

```python
"""
Bu comment
"""
```

Bu aslida **docstring** (agar joyida ishlatilsa)

---

## 5️⃣ Documentation String (Docstring) nima?

**Docstring** — bu:

* Funksiya
* Class
* Module

uchun yoziladigan **rasmiy hujjat**

### 🔹 Uchta qo‘shtirnoq ishlatiladi:

```python
"""
Bu modul haqida ma’lumot
"""
```

---

## 6️⃣ Function docstring

```python
def add(a, b):
    """
    Ikki sonni qo‘shadi.

    Parameters:
        a (int): birinchi son
        b (int): ikkinchi son

    Returns:
        int: natija
    """
    return a + b
```

Docstring’ni ko‘rish:

```python
help(add)
```

---

## 7️⃣ Class docstring

```python
class Person:
    """
    Bu class insonni ifodalaydi.
    """

    def __init__(self, name):
        """
        Person obyektini yaratadi.

        name (str): ism
        """
        self.name = name
```

---

## 8️⃣ Module docstring

```python
"""
math_utils.py

Bu modul matematik yordamchi funksiyalarni o‘z ichiga oladi.
"""
```

📌 Module docstring → fayl boshida yoziladi

---

## 9️⃣ Docstring vs Comment farqi

| Comment        | Docstring     |
| -------------- | ------------- |
| `#`            | `""" """`     |
| Bajarilmaydi   | Saqlanadi     |
| Izoh uchun     | Documentation |
| help() da yo‘q | help() da bor |

---

## 🔟 Docstring formatlari

### 🔹 Google style

### 🔹 NumPy style

### 🔹 reStructuredText

📌 Boshlovchilar uchun:
👉 **Google style** tavsiya etiladi

---

## 1️⃣1️⃣ Best practices

✅ Murakkab joylarni comment bilan tushuntiring
✅ Public function/class uchun docstring yozing
✅ Keraksiz comment yozmang
✅ Docstring’ni doim yangilab boring

---