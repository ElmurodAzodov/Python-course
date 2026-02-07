
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
# **Python’da String Formatting**

String Formatting — bu matnga **o‘zgaruvchilar yoki qiymatlarni joylashtirish** usulidir.
Python’da eng ko‘p ishlatiladigan ikki usul mavjud:

1. **f-string (Python 3.6+)**
2. **`format()` metodi**

---

## **1. f-string (Formated String Literals)**

* Sintaksis: `f"matn {o'zgaruvchi} matn"`
* Python 3.6+ versiyalarda ishlaydi.
* **Imkoniyatlari:**

  * O‘zgaruvchilarni bevosita qo‘shish
  * Ifodalardan foydalanish
  * Formatlash: raqamlar, o‘nlik, foiz va hokazo

---

### **1.1. Oddiy f-string**

```python
name = "Python"
version = 3.11
print(f"Hello {name}, version {version}")
```

**Natija:**

```
Hello Python, version 3.11
```

---

### **1.2. Ifodalarni ishlatish**

```python
a = 5
b = 3
print(f"{a} + {b} = {a+b}")
```

**Natija:**

```
5 + 3 = 8
```

---

### **1.3. Formatlash**

* **O‘nliklar bilan:** `{:.2f}` — 2 ta o‘nlik
* **Raqamlar joylashuvi:** `{num:10}` — 10 belgili joy

```python
pi = 3.1415926
print(f"Pi: {pi:.2f}")       # 2 o'nlik
print(f"Number: {42:10}")    # 10 belgi kengligi
```

**Natija:**

```
Pi: 3.14
Number:         42
```

---

### **1.4. Foydali misol**

```python
name = "Alice"
score = 92.4567
print(f"{name} scored {score:.1f} points in the exam")
```

**Natija:**

```
Alice scored 92.5 points in the exam
```

---

## **2. `format()` metodi**

* Sintaksis: `"matn {}".format(qiymat)`
* Python 2.7+ va 3.x versiyalarda ishlaydi.

---

### **2.1. Oddiy format()**

```python
name = "Python"
version = 3.11
print("Hello {}, version {}".format(name, version))
```

**Natija:**

```
Hello Python, version 3.11
```

---

### **2.2. Indeks bilan**

```python
print("{1} is better than {0}".format("Java", "Python"))
```

**Natija:**

```
Python is better than Java
```

---

### **2.3. Kalit so‘zlar bilan**

```python
print("Hello {n}, version {v}".format(n="Python", v=3.11))
```

**Natija:**

```
Hello Python, version 3.11
```

---

### **2.4. Formatlash**

```python
pi = 3.1415926
print("Pi: {:.2f}".format(pi))   # 2 ta o'nlik
print("Number: {:10}".format(42)) # 10 belgili kenglik
```

**Natija:**

```
Pi: 3.14
Number:         42
```

---

### **2.5. Foydali misol**

```python
name = "Bob"
score = 87.654
print("{n} scored {s:.1f} points".format(n=name, s=score))
```

**Natija:**

```
Bob scored 87.7 points
```

---

## **3. f-string vs format()**

| Xususiyat            | f-string                | format()           |
| -------------------- | ----------------------- | ------------------ |
| Sintaksis            | `f"{var}"`              | `"{}".format(var)` |
| Ifodalarni ishlatish | Ha                      | Cheklangan         |
| Python versiyasi     | 3.6+                    | 2.7+ va 3.x        |
| Qulaylik             | Ko‘proq o‘qishli va tez | Biroz uzunroq      |

---

## **4. Amaliy misol: Hisob-kitob + Formatlash**

```python
product = "Apple"
price = 4.567
quantity = 3

# f-string
print(f"{quantity} {product}s cost ${price*quantity:.2f}")

# format()
print("{} {}s cost ${:.2f}".format(quantity, product, price*quantity))
```

**Natija:**

```
3 Apples cost $13.70
3 Apples cost $13.70
```

---
# **Python’da Escape Characters (Qochirish belgilar)**

## **1. Escape character nima?**

**Escape character** — bu **maxsus belgi** bo‘lib, string ichida o‘ziga xos vazifani bajaradi.
Python’da escape character **`\` (backslash)** bilan boshlanadi.

---

## **2. Eng ko‘p ishlatiladigan escape characters**

| Escape | Ta’rif                                  | Misol                 |
| ------ | --------------------------------------- | --------------------- |
| `\n`   | Yangi qatordan boshlash                 | `"Hello\nWorld"`      |
| `\t`   | Tab (4 yoki 8 bo‘shliq)                 | `"Hello\tWorld"`      |
| `\\`   | Backslash (`\`)                         | `"C:\\Users\\Name"`   |
| `\'`   | Single quote (`'`)                      | `'It\'s Python'`      |
| `\"`   | Double quote (`"`)                      | `"He said \"Hello\""` |
| `\r`   | Carriage return (qator boshiga qaytish) | `"123\rABC"`          |
| `\b`   | Backspace (oxirgi belgini o‘chiradi)    | `"Hello\bWorld"`      |
| `\f`   | Form feed                               | `"Hello\fWorld"`      |
| `\v`   | Vertical tab                            | `"Hello\vWorld"`      |
| `\ooo` | Oktal kod                               | `\101` → `A`          |
| `\xhh` | Hex kod                                 | `\x41` → `A`          |

---

## **3. Misollar bilan tushuntirish**

### **3.1. Yangi qator va tab**

```python
print("Hello\nWorld")
print("Name:\tAlice")
```

**Natija:**

```
Hello
World
Name:   Alice
```

---

### **3.2. Qavs ichida tirnoq ishlatish**

```python
print('It\'s Python')
print("He said \"Hello\"")
```

**Natija:**

```
It's Python
He said "Hello"
```

---

### **3.3. Backslash ishlatish**

```python
print("C:\\Users\\Name\\Documents")
```

**Natija:**

```
C:\Users\Name\Documents
```

---

### **3.4. Carriage return va backspace**

```python
print("12345\rABC")   # Carriage return
print("Hello\bWorld") # Backspace
```

**Natija:**

```
ABC45
HellWorld
```

> 🔑 `\r` — qator boshiga qaytaradi, eski belgilar ustiga yozadi.
> 🔑 `\b` — oxirgi belgini o‘chiradi.

---

### **3.5. Raw strings bilan escape characterdan qochish**

* `r""` yoki `r''` ishlatilsagina `\` maxsus belgini bajarishdan saqlanadi.

```python
path = r"C:\Users\Alice\Documents"
print(path)
```

**Natija:**

```
C:\Users\Alice\Documents
```

---

## **4. Amaliy misol: matnni formatlash**

```python
text = "Hello\tWorld!\nWelcome to Python.\nPath: C:\\Users\\Alice"
print(text)
```

**Natija:**

```
Hello   World!
Welcome to Python.
Path: C:\Users\Alice
```

---
# **Python’da Unicode**

## **1. Unicode nima?**

**Unicode** — bu **har bir belgiga unikal raqamli kod** beruvchi standart.

* Maqsadi: **barcha tillardagi belgilarni bir xil usulda saqlash va ishlatish**.
* Python 3-da **stringlar (`str`) Unicode bo‘ladi**, ya’ni ular **global belgilarni** qo‘llab-quvvatlaydi.

```python
text = "Привет, 你好, Hello"
print(text)
```

**Natija:**

```
Привет, 你好, Hello
```

> 🔑 Python 3’da `str` har doim Unicode, `bytes` esa raw byte ma’lumot.

---

## **2. Unicode kodlarini olish va ishlatish**

### **2.1. `ord()` — belgini Unicode kodiga o‘zgartirish**

```python
print(ord("A"))  # 65
print(ord("Ж"))  # 1046
print(ord("你"))  # 20320
```

---

### **2.2. `chr()` — Unicode kodidan belgi yaratish**

```python
print(chr(65))     # A
print(chr(1046))   # Ж
print(chr(20320))  # 你
```

---

### **2.3. Unicode escape bilan yozish**

```python
print("\u0416")   # Ж
print("\u4F60")   # 你
```

* `\uXXXX` — 4-hex belgili Unicode
* `\UXXXXXXXX` — 8-hex belgili Unicode

```python
print("\U0001F600")  # 😀 (emoji)
```

---

## **3. Stringlarni kodlash va dekodlash (Encoding / Decoding)**

### **3.1. `encode()`**

* Stringni `bytes` turiga o‘zgartiradi.
* Encoding misol: `utf-8`, `utf-16`, `ascii`

```python
text = "Hello, Привет, 你好"
encoded = text.encode("utf-8")
print(encoded)
```

**Natija (UTF-8 byte ko‘rinishi):**

```
b'Hello, \xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xe4\xbd\xa0\xe5\xa5\xbd'
```

---

### **3.2. `decode()`**

* Bytesni stringga qaytaradi.

```python
decoded = encoded.decode("utf-8")
print(decoded)
```

**Natija:**

```
Hello, Привет, 你好
```

---

### **3.3. ASCII bilan ehtiyot bo‘lish**

* `ascii` encoding faqat **ingliz alifbosi va raqamlar** bilan ishlaydi.

```python
text = "Привет"
# text.encode("ascii")  # UnicodeEncodeError
```

> 🔑 Xalqaro matnlar bilan ishlashda **UTF-8** standart hisoblanadi.

---

## **4. Emoji va maxsus belgilar bilan ishlash**

```python
smile = "😀"
print(ord(smile))      # 128512
print(chr(128512))     # 😀
```

* Python 3 Unicode yordamida **emoji, maxsus belgilar va boshqa tillar bilan bemalol ishlaydi**.

---

## **5. Amaliy misol: Unicode va encoding**

```python
text = "Привет, Python! 👋"

# 1. Unicode kodlarini ko‘rsatish
codes = [ord(c) for c in text]
print(codes)

# 2. UTF-8 ga encode qilish
encoded = text.encode("utf-8")
print(encoded)

# 3. UTF-8 dan decode qilish
decoded = encoded.decode("utf-8")
print(decoded)
```

**Natija:**

```
[1055, 1088, 1080, 1074, 1077, 1090, 44, 32, 80, 121, 116, 104, 111, 110, 33, 32, 128075]
b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, Python! \xf0\x9f\x91\x8b'
Привет, Python! 👋
```

---
# **Python’da Encoding va Decoding**

## **1. Encoding va Decoding nima?**

1. **Encoding** — string (`str`)ni **bytes**ga o‘zgartirish jarayoni.
2. **Decoding** — bytesni (`bytes`) **string**ga o‘zgartirish jarayoni.

> 🔑 Python 3-da **`str` = Unicode**, **`bytes` = raw byte ma’lumot**.

---

## **2. Syntax**

```python
# Encoding
bytes_data = text.encode(encoding="utf-8")  # str → bytes

# Decoding
decoded_text = bytes_data.decode(encoding="utf-8")  # bytes → str
```

* `encoding` parametri: `"utf-8"`, `"utf-16"`, `"ascii"`, `"latin1"` va boshqalar.
* Default encoding Python 3-da `"utf-8"` hisoblanadi.

---

## **3. Encoding misollari**

```python
text = "Hello, Привет, 你好"

# UTF-8 encoding
utf8_bytes = text.encode("utf-8")
print(utf8_bytes)

# UTF-16 encoding
utf16_bytes = text.encode("utf-16")
print(utf16_bytes)
```

**Natija (UTF-8 va UTF-16 bytes):**

```
b'Hello, \xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xe4\xbd\xa0\xe5\xa5\xbd'
b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x1f\x04@\x04B\x04B\x04E\x04\x12\x04, \x00\xa0Ni?'
```

> 🔑 UTF-16 har bir belgi uchun 2 yoki 4 bayt ishlatadi, UTF-8 esa o‘zgaruvchan uzunlikda.

---

## **4. Decoding misollari**

```python
# UTF-8 bytesni str ga o‘tkazish
decoded_text = utf8_bytes.decode("utf-8")
print(decoded_text)
```

**Natija:**

```
Hello, Привет, 你好
```

> 🔑 Encoding → bytes, Decoding → str

---

## **5. ASCII bilan ehtiyot bo‘lish**

```python
text = "Привет"

# text.encode("ascii")  # UnicodeEncodeError
```

* ASCII faqat **ingliz alifbosi va raqamlar** bilan ishlaydi.
* Global matnlar uchun **UTF-8** ishlatiladi.

---

## **6. Amaliy misol: faylga yozish va o‘qish**

```python
text = "Hello, Привет, 你好"

# 1. UTF-8 bilan faylga yozish
with open("example.txt", "w", encoding="utf-8") as f:
    f.write(text)

# 2. UTF-8 bilan fayldan o‘qish
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
```

**Natija:**

```
Hello, Привет, 你好
```

> 🔑 Encoding va decoding fayllarda yoki tarmoqqa uzatishda juda muhim.

---

## **7. Bytes va string bilan ishlash misoli**

```python
text = "Python 🐍"

# str → bytes
b = text.encode("utf-8")
print(b)  # b'Python \xf0\x9f\x90\x8d'

# bytes → str
s = b.decode("utf-8")
print(s)  # Python 🐍
```

---
# **Python’da Text Normalization**

## **1. Text Normalization nima?**

**Text Normalization** — bu matnni **standart, bir hil shaklga keltirish** jarayoni.

* Maqsad: turli variantdagi matnlarni **bir xil formatga keltirish**, masalan:

  * Katta/ kichik harflar farqini yo‘qotish
  * Diakritik belgilarni olib tashlash (`é → e`)
  * Bo‘shliqlar va maxsus belgilarni tozalash

* Bu **NLP (Natural Language Processing)**, matn qidirish, tahlil va mashina o‘rganish uchun zarur.

---

## **2. Katta/kichik harf bilan normalizatsiya**

```python
text = "PyTHon Is FuN"
normalized = text.lower()  # yoki .upper()
print(normalized)
```

**Natija:**

```
python is fun
```

> 🔑 `lower()` va `upper()` — eng oddiy normalizatsiya usuli.

---

## **3. Bo‘shliqlarni tozalash**

```python
text = "   Hello   World  "
normalized = text.strip()        # boshi va oxiridagi bo‘shliq
normalized2 = " ".join(text.split())  # ortiqcha bo‘shliqlarni olib tashlash
print(f"'{normalized}'")
print(f"'{normalized2}'")
```

**Natija:**

```
'Hello   World'
'Hello World'
```

> 🔑 `.split()` va `.join()` yordamida **ortiqcha bo‘shliqlarni** olib tashlash mumkin.

---

## **4. Diakritik belgilarni olib tashlash**

Masalan, `café → cafe`.
Buning uchun **`unicodedata`** modulidan foydalanamiz.

```python
import unicodedata

text = "Café naïve fiancé"
normalized = ''.join(
    c for c in unicodedata.normalize('NFD', text)
    if unicodedata.category(c) != 'Mn'
)
print(normalized)
```

**Natija:**

```
Cafe naive fiance
```

> 🔑 `NFD` — decomposed form, har bir diakritik belgini alohida ajratadi.
> `Mn` — diakritik belgilar (Nonspacing Mark).

---

## **5. Maxsus belgilar va belgilarni tozalash**

* Faqat **alifbo va raqamlarni qoldirish** uchun `re` modulidan foydalanish mumkin:

```python
import re

text = "Hello!!! Welcome to Python 3.11 😃"
normalized = re.sub(r'[^A-Za-z0-9 ]+', '', text)
print(normalized)
```

**Natija:**

```
Hello Welcome to Python 311
```

---

## **6. Unicode normalizatsiyasi (NFC, NFD, NFKC, NFKD)**

| Form | Ta’rif                                                                                          |
| ---- | ----------------------------------------------------------------------------------------------- |
| NFC  | Canonical Composition — belgilar birlashtiriladi                                                |
| NFD  | Canonical Decomposition — belgilar va diakritiklar ajratiladi                                   |
| NFKC | Compatibility Composition — belgilar birlashtiriladi va simvol variantlari standartlashtiriladi |
| NFKD | Compatibility Decomposition — diakritiklar va simvol variantlari ajratiladi                     |

```python
import unicodedata

text = "ﬁ"  # ligature fi
print(unicodedata.normalize('NFKC', text))  # fi
```

---

## **7. Amaliy misol: matnni normalizatsiya qilish**

```python
import unicodedata
import re

text = "  Héllò Wörld!!! Welcome to Café Python 3.11 😃  "

# 1. Katta/kichik harf
text = text.lower()

# 2. Bo‘shliqlarni tozalash
text = " ".join(text.split())

# 3. Diakritik belgilarni olib tashlash
text = ''.join(
    c for c in unicodedata.normalize('NFD', text)
    if unicodedata.category(c) != 'Mn'
)

# 4. Maxsus belgilarni olib tashlash
text = re.sub(r'[^a-z0-9 ]+', '', text)

print(text)
```

**Natija:**

```
hello world welcome to cafe python 311
```

> 🔑 Natija: **standart, bir hil, tozalangan matn**.

---