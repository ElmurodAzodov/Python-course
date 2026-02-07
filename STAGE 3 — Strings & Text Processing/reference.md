
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

# **Python’da String Immutability (O‘zgarmasligi)**

## **1. String immutable nima?**

Python’da **stringlar immutable** turga ega, ya’ni:

* **Yaratilgan stringni bevosita o‘zgartirish mumkin emas.**
* Agar stringni “o‘zgartirmoqchi” bo‘lsak, aslida **yangi string** yaratiladi.

---

## **2. Misol**

```python
text = "Python"

# text[0] = "p"  # Xato! TypeError
```

**Natija:**

```
TypeError: 'str' object does not support item assignment
```

> 🔑 Eslatma: Python bu xatoni beradi, chunki stringlar o‘zgarmas.

---

## **3. Stringni o‘zgartirish usullari**

Immutable bo‘lsa-da, stringni “o‘zgartirish” uchun quyidagi usullar ishlatiladi:

### **3.1. Slicing bilan yangi string yaratish**

```python
text = "Python"
new_text = "p" + text[1:]
print(new_text)
```

**Natija:**

```
python
```

> Izoh: asl `text` o‘zgarmadi, yangi `new_text` yaratildi.

---

### **3.2. String Methods bilan yangi string yaratish**

Ko‘p string metodlari **asl stringni o‘zgartirmaydi**, balki **yangi string qaytaradi**:

```python
text = "python"
upper_text = text.upper()  # yangi string
print(text)        # python
print(upper_text)  # PYTHON
```

**Natija:**

```
python
PYTHON
```

---

### **3.3. Concatenation bilan yangi string**

```python
text = "Hello"
text = text + " World"
print(text)
```

**Natija:**

```
Hello World
```

> Izoh: asl “Hello” stringi o‘chmaydi, Python yangi string yaratadi va `text`ga beradi.

---

### **3.4. Repetition bilan yangi string**

```python
text = "Ha! "
text = text * 3
print(text)
```

**Natija:**

```
Ha! Ha! Ha! 
```

---

## **4. Nega string immutable?**

1. **Xotira samaradorligi** – bir xil stringlar bir nechta o‘zgaruvchilarda ishlatilsa, Python ularni qayta ishlatadi.
2. **Xatolikdan himoya** – stringlarni noto‘g‘ri o‘zgartirishdan saqlaydi.
3. **Thread-safe** – bir vaqtning o‘zida bir nechta jarayonlar stringni xavfsiz ishlata oladi.

---

## **5. Amaliy misol: Immutable vs Mutable**

```python
# Immutable string
text = "Hello"
new_text = text.replace("H", "h")
print(text)      # Hello
print(new_text)  # hello

# Mutable list
lst = [1, 2, 3]
lst[0] = 9
print(lst)  # [9, 2, 3]
```

> Izoh: `text.replace()` asl stringni o‘zgartirmadi, `new_text` yaratildi.
> `list` esa mutable bo‘lgani uchun bevosita o‘zgardi.

---

## **6. Xulosa**

1. Python stringlari **immutable** — bevosita o‘zgartirib bo‘lmaydi.
2. O‘zgartirish kerak bo‘lsa, **yangi string** yaratish kerak:

   * **Slicing + concatenation**
   * **String metodlari** (`upper()`, `replace()`, `strip()` va hokazo)
3. Immutable bo‘lishi **xotira samaradorligi va xavfsizlik** uchun foydalidir.

---
# **Python’da Common String Methods**

Python stringlari **immutable**, shuning uchun ko‘plab metodlar asl stringni o‘zgartirmaydi, balki **yangi string** qaytaradi.

---

## **1. Case-related methods (Kichik/katta harflar bilan ishlash)**

| Method         | Ta’rif                                | Misol                                     |
| -------------- | ------------------------------------- | ----------------------------------------- |
| `upper()`      | Hamma harflarni katta qiladi          | `"python".upper()` → `"PYTHON"`           |
| `lower()`      | Hamma harflarni kichik qiladi         | `"PYTHON".lower()` → `"python"`           |
| `capitalize()` | Faqat birinchi harfni katta qiladi    | `"python".capitalize()` → `"Python"`      |
| `title()`      | Har bir so‘zni katta qiladi           | `"hello world".title()` → `"Hello World"` |
| `swapcase()`   | Katta ↔ kichik harflarni almashtiradi | `"PyThOn".swapcase()` → `"pYtHoN"`        |

**Misol:**

```python
text = "python programming"
print(text.upper())
print(text.title())
print(text.capitalize())
print(text.swapcase())
```

**Natija:**

```
PYTHON PROGRAMMING
Python Programming
Python programming
PYTHON PROGRAMMING
```

---

## **2. Search / Replace methods (Qidirish va o‘zgartirish)**

| Method              | Ta’rif                                                            | Misol                                       |
| ------------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| `find(sub)`         | `sub` substring qayerda ekanini qaytaradi (-1 agar yo‘q bo‘lsa)   | `"Python".find("t")` → 2                    |
| `index(sub)`        | `sub` substring qayerda ekanini qaytaradi (xato agar yo‘q bo‘lsa) | `"Python".index("t")` → 2                   |
| `replace(old, new)` | `old` substringni `new` bilan almashtiradi                        | `"Python".replace("Py", "Ja")` → `"Jathon"` |

**Misol:**

```python
text = "I love Python"
print(text.find("Python"))
print(text.replace("Python", "Java"))
```

**Natija:**

```
7
I love Java
```

---

## **3. Strip / Split / Join methods (Bo‘shliq va bo‘lish)**

| Method           | Ta’rif                                     | Misol                                  |
| ---------------- | ------------------------------------------ | -------------------------------------- |
| `strip()`        | Boshi va oxiridagi bo‘shliqlarni o‘chiradi | `"  hello  ".strip()` → `"hello"`      |
| `lstrip()`       | Boshi bo‘shliqni o‘chiradi                 | `"  hello".lstrip()` → `"hello"`       |
| `rstrip()`       | Oxiri bo‘shliqni o‘chiradi                 | `"hello  ".rstrip()` → `"hello"`       |
| `split(sep)`     | Stringni `sep` bo‘yicha bo‘ladi            | `"a,b,c".split(",")` → `['a','b','c']` |
| `join(iterable)` | Ro‘yxatni stringga birlashtiradi           | `"-".join(["a","b","c"])` → `"a-b-c"`  |

**Misol:**

```python
text = "   Python   "
print(text.strip())
words = "I,love,Python".split(",")
print(words)
joined = " ".join(words)
print(joined)
```

**Natija:**

```
Python
['I', 'love', 'Python']
I love Python
```

---

## **4. Check Methods (Tekshirish)**

| Method            | Ta’rif                               | Misol                              |
| ----------------- | ------------------------------------ | ---------------------------------- |
| `isalpha()`       | Faqat harflardan iborat bo‘lsa True  | `"Python".isalpha()` → True        |
| `isdigit()`       | Faqat raqamlardan iborat bo‘lsa True | `"123".isdigit()` → True           |
| `isalnum()`       | Harf yoki raqam bo‘lsa True          | `"Python123".isalnum()` → True     |
| `isspace()`       | Faqat bo‘shliq bo‘lsa True           | `"   ".isspace()` → True           |
| `startswith(sub)` | Substring bilan boshlansa True       | `"Python".startswith("Py")` → True |
| `endswith(sub)`   | Substring bilan tugasa True          | `"Python".endswith("on")` → True   |

**Misol:**

```python
print("Python".isalpha())
print("123".isdigit())
print("Python123".isalnum())
print("   ".isspace())
print("Python".startswith("Py"))
print("Python".endswith("on"))
```

**Natija:**

```
True
True
True
True
True
True
```

---

## **5. Formatting Methods (Matnni shakllantirish)**

| Method     | Ta’rif                        | Misol                                               |
| ---------- | ----------------------------- | --------------------------------------------------- |
| `format()` | String ichiga qiymat kiritish | `"Hello {}".format("Python")` → `"Hello Python"`    |
| f-string   | `f""` bilan formatlash        | `name="Python"; f"Hello {name}"` → `"Hello Python"` |

**Misol:**

```python
name = "Python"
version = 3.11
print("Hello {} version {}".format(name, version))
print(f"Hello {name} version {version}")
```

**Natija:**

```
Hello Python version 3.11
Hello Python version 3.11
```

---

## **6. Amaliy misol: String methodsni birlashtirish**

```python
text = "   hello python world   "
# 1. Boshi va oxiridagi bo‘shliqni olib tashlash
clean = text.strip()
# 2. Katta harflar
upper_text = clean.upper()
# 3. So‘zlarni ajratish
words = upper_text.split()
# 4. Birinchi so‘zni almashtirish
words[0] = "HI"
# 5. Ro‘yxatni stringga birlashtirish
final_text = " ".join(words)
print(final_text)
```

**Natija:**

```
HI PYTHON WORLD
```
---
# **Python’da Searching and Replacing**

Stringlarni qidirish va o‘zgartirish — text processingning eng asosiy vazifalaridan biridir. Pythonda bu **string metodlari** orqali amalga oshiriladi.

---

## **1. Searching (Qidirish)**

Python stringlarida substring yoki belgi qayerda joylashganini aniqlash uchun bir nechta metodlar mavjud:

### **1.1. `find()`**

* Qidirilgan substringning **birinchi uchrashgan indeksini** qaytaradi.
* Agar substring topilmasa, **-1** qaytaradi.

```python
text = "I love Python programming"
print(text.find("Python"))  # 7
print(text.find("Java"))    # -1
```

---

### **1.2. `rfind()`**

* **Oxirgi uchrashgan indeksni** qaytaradi.

```python
text = "I love Python and Python is fun"
print(text.rfind("Python"))  # 14
```

---

### **1.3. `index()`**

* `find()`ga o‘xshaydi, lekin substring topilmasa **ValueError** beradi.

```python
text = "I love Python"
print(text.index("Python"))  # 7
# print(text.index("Java"))  # ValueError
```

---

### **1.4. `rindex()`**

* `rfind()` kabi, oxirgi uchrashgan joyni beradi, topilmasa **ValueError**.

```python
text = "Python is fun. Python is powerful."
print(text.rindex("Python"))  # 17
```

---

### **1.5. `count()`**

* Substring nechta marta uchrashganini hisoblaydi.

```python
text = "Python is fun. Python is powerful."
print(text.count("Python"))  # 2
print(text.count("Java"))    # 0
```

---

## **2. Replacing (O‘zgartirish)**

Stringlarni o‘zgartirish uchun eng ko‘p ishlatiladigan metod — **`replace()`**.

### **2.1. `replace(old, new, count=-1)`**

* `old` substringni `new` bilan almashtiradi.
* `count` optional, nechta substringni almashtirishni belgilaydi (default -1, barcha substringlar).

```python
text = "I love Python. Python is powerful."
# Barcha "Python" so‘zlarini "Java" bilan almashtirish
new_text = text.replace("Python", "Java")
print(new_text)
```

**Natija:**

```
I love Java. Java is powerful.
```

```python
# Faqat birinchi uchrashuvni almashtirish
new_text = text.replace("Python", "Java", 1)
print(new_text)
```

**Natija:**

```
I love Java. Python is powerful.
```

---

## **3. Qidirish + almashtirish kombinatsiyasi**

Ko‘pincha dasturda qidirish va almashtirishni birlashtirib ishlatamiz:

```python
text = "Python is fun. Python is powerful."

if text.find("Python") != -1:
    new_text = text.replace("Python", "Java")
    print("Almashtirilgan matn:", new_text)
else:
    print("Python topilmadi.")
```

**Natija:**

```
Almashtirilgan matn: Java is fun. Java is powerful.
```

---

## **4. Case-insensitive qidirish va almashtirish**

Stringlarni katta/kichik harf farqini inobatga olmasdan qidirish uchun `.lower()` yoki `.upper()` bilan birga ishlatish mumkin:

```python
text = "Python is fun. python is powerful."
search_word = "python"

if search_word.lower() in text.lower():
    new_text = text.replace("Python", "Java").replace("python", "Java")
    print(new_text)
```

**Natija:**

```
Java is fun. Java is powerful.
```

---

## **5. Amaliy misol: matnni tozalash va o‘zgartirish**

```python
text = "  I love Python. Python is fun.  "
# 1. Bo‘shliqni olib tashlash
clean_text = text.strip()
# 2. "Python" ni "Java" bilan almashtirish
final_text = clean_text.replace("Python", "Java")
# 3. Natijani chiqarish
print(final_text)
```

**Natija:**

```
I love Java. Java is fun.
```

---