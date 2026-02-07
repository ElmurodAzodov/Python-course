
# **STAGE 3 — Strings & Text Processing**
---

# **Python’da String Creation (Matn yaratish)**

## **1. String nima?**

Python’da **string** — bu belgilar ketma-ketligidir (text yoki matn).
Masalan: `"Hello"` yoki `'Python'`.

Python’da stringlarni yaratishning bir nechta usullari mavjud.

---

## **2. String yaratish usullari**

### **2.1. Single Quotes (Yagona tirnoq)**

```python
text1 = 'Hello'
print(text1)
```

**Natija:**

```
Hello
```

### **2.2. Double Quotes (Ikkita tirnoq)**

```python
text2 = "World"
print(text2)
```

**Natija:**

```
World
```

**Eslatma:** Single yoki double quotes o‘rtasida hech qanday farq yo‘q.
Single quotes ichida double quotes ishlatish mumkin va aksincha:

```python
text3 = "Python's awesome"
text4 = 'He said "Hello!"'
print(text3)
print(text4)
```

**Natija:**

```
Python's awesome
He said "Hello!"
```

---

### **2.3. Triple Quotes (Uch tirnoq)**

Triple quotes — `'''...'''` yoki `"""..."""` ko‘p qatorli matnlar uchun ishlatiladi.

```python
multi_line = """This is a
multi-line
string"""
print(multi_line)
```

**Natija:**

```
This is a
multi-line
string
```

---

### **2.4. String concatenation (Matnlarni birlashtirish)**

`+` operatori yordamida bir nechta stringlarni birlashtirish mumkin:

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```

**Natija:**

```
Hello World
```

---

### **2.5. String repetition (Takrorlash)**

`*` operatori yordamida stringni takrorlash mumkin:

```python
text = "Ha! " * 3
print(text)
```

**Natija:**

```
Ha! Ha! Ha! 
```

---

### **2.6. Casting to string (Stringga o‘zgartirish)**

Boshqa turdagi ma’lumotlarni stringga aylantirish uchun `str()` funksiyasidan foydalaniladi:

```python
num = 123
float_num = 45.67
flag = True

print(str(num))        # "123"
print(str(float_num))  # "45.67"
print(str(flag))       # "True"
```

---

### **2.7. Raw Strings (r"" yoki r'')**

Backslash `\` bilan maxsus belgilarni qochirishni xohlashsiz ishlatish uchun **raw strings** ishlatiladi:

```python
path = r"C:\Users\Name\Documents"
print(path)
```

**Natija:**

```
C:\Users\Name\Documents
```

Agar `r` ishlatilmasa, `\n` yoki `\t` kabi maxsus belgilar bajariladi.

---

### **2.8. Empty string (Bo‘sh string)**

Bo‘sh string yaratish mumkin:

```python
empty = ""
print(empty)
print(len(empty))  # uzunligi 0
```

---

## **3. String Immutability (O‘zgarmasligi)**

Python’da stringlar **immutable** (o‘zgarmas) turga ega.
Ya’ni, string yaratilgandan keyin, uni bevosita o‘zgartirish mumkin emas.

```python
text = "Hello"
# text[0] = "h"   # Xato! string o'zgartirilmaydi
text = "h" + text[1:]  # To'g'ri: yangi string yaratamiz
print(text)
```

**Natija:**

```
hello
```

---

## **4. Misol: turli string yaratish usullari**

```python
# Single quotes
s1 = 'Python'

# Double quotes
s2 = "Programming"

# Triple quotes
s3 = """This is
a multi-line
string"""

# Concatenation
s4 = s1 + " " + s2

# Repetition
s5 = "Ha! " * 5

# Casting
s6 = str(2026)

# Raw string
s7 = r"C:\Users\Python"

# Empty string
s8 = ""

# Output
print(s1, s2, s3, s4, s5, s6, s7, s8, sep="\n---\n")
```

**Natija:**

```
Python
---
Programming
---
This is
a multi-line
string
---
Python Programming
---
Ha! Ha! Ha! Ha! Ha! 
---
2026
---
C:\Users\Python
---
```

---
# **Python’da String Indexing (Indekslash)**

## **1. Indexing nima?**

**Indexing** — bu string ichidagi har bir belgiga **raqamli indeks** orqali murojaat qilish.
Python’da **string belgilar ketma-ketligi** sifatida saqlanadi va har bir belgiga **0’dan boshlab raqam beriladi**.

---

## **2. Ijobiy indekslar (Positive Indexing)**

* Birinchi belgi: 0
* Ikkinchi belgi: 1
* Uchinchisi: 2 … va hokazo

```python
text = "Python"
print(text[0])  # P
print(text[1])  # y
print(text[5])  # n
```

**Natija:**

```
P
y
n
```

---

## **3. Salbiy indekslar (Negative Indexing)**

* So‘nggi belgidan boshlab hisoblanadi: -1
* So‘nggi oldingi: -2 … va hokazo

```python
text = "Python"
print(text[-1])  # n
print(text[-2])  # o
print(text[-6])  # P
```

**Natija:**

```
n
o
P
```

> 🔑 Foydali qoidalar:
>
> * `text[0]` va `text[-len(text)]` bir xil belgi.
> * `text[-1]` — bu **oxirgi belgi**.

---

## **4. IndexError (Xato indeks)**

Agar string uzunligidan oshiq indeks berilsa, Python **IndexError** beradi:

```python
text = "Python"
# print(text[6])  # IndexError: string index out of range
```

---

## **5. Amaliy misollar**

```python
word = "Programming"

# 1. Birinchi va oxirgi belgini chiqarish
first = word[0]
last = word[-1]

# 2. O‘rta belgini chiqarish
middle_index = len(word)//2
middle = word[middle_index]

# 3. Belgilarning pozitsiyasi bilan chiqarish
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")

print("First:", first)
print("Middle:", middle)
print("Last:", last)
```

**Natija:**

```
Index 0: P
Index 1: r
Index 2: o
Index 3: g
Index 4: r
Index 5: a
Index 6: m
Index 7: m
Index 8: i
Index 9: n
Index 10: g
First: P
Middle: a
Last: g
```

---
# **Python’da String Slicing (Kesish)**

## **1. Slicing nima?**

**Slicing** — bu stringning bir qismini ajratib olish usuli.
Sintaksisi:

```python
string[start:stop:step]
```

* **start** — boshlanish indeksi (shu belgidan boshlab)
* **stop** — tugash indeksi (shu belgigacha, ammo uni o‘z ichiga olmaydi)
* **step** — qadam (har nechanchi belgini olamiz)

> `step` default qiymati 1

---

## **2. Oddiy slicing**

```python
text = "Python"
print(text[0:4])  # 0,1,2,3 indeksdagi belgilar
```

**Natija:**

```
Pyth
```

> 🔑 Eslatma: `stop` indeksi **o‘z ichiga olmaydi**.

---

## **3. Boshlang‘ich yoki tugash indeksini bo‘sh qoldirish**

```python
text = "Python"

print(text[:4])  # 0 dan 3 gacha
print(text[2:])  # 2-indeksdan oxirigacha
print(text[:])   # hamma string
```

**Natija:**

```
Pyth
thon
Python
```

---

## **4. Step bilan slicing**

```python
text = "Python"
print(text[::2])  # har 2-belgini olish
print(text[1::2]) # 1-indeksdan boshlab har 2-belgi
```

**Natija:**

```
Pto
yhn
```

---

## **5. Salbiy step (teskari tartibda)**

```python
text = "Python"
print(text[::-1])  # stringni teskariga o‘girish
print(text[5:0:-1]) # indeks 5 dan 1 gacha (0 kirmaydi)
```

**Natija:**

```
nohtyP
nohty
```

> 🔑 Eslatma: `[::-1]` — **stringni teskari o‘girishning tez usuli**.

---

## **6. Amaliy misollar**

```python
word = "Programming"

# 1. Dastlabki 6 belgini ajratish
print(word[:6])  # Progra

# 2. Oxirgi 3 belgini ajratish
print(word[-3:]) # ing

# 3. Har 2-belgini ajratish
print(word[::2]) # Pormig

# 4. Stringni teskari chiqarish
print(word[::-1]) # gnimmargorP

# 5. Belgilarni qisman teskari olish
print(word[5:0:-1]) # argorP
```

---