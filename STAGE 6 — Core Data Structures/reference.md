
# **STAGE 6 — Core Data Structures**
---
# **Python Lists: Creation (Roʻyxat yaratish)**

## 1️⃣ **List nima?**

Python-da **list** — bu bir nechta elementlarni tartiblangan holda saqlaydigan ma’lumotlar tuzilmasi.
**Xususiyatlari:**

* Tartiblangan (`ordered`) ✅
* Elementlar bir xil yoki turli turdagi bo‘lishi mumkin (`heterogeneous`) ✅
* O‘zgartirilishi mumkin (`mutable`) ✅
* Index yordamida elementlarga murojaat qilish mumkin (`0`-dan boshlanadi)

---

## 2️⃣ **List yaratish usullari**

Python-da list yaratishning bir nechta asosiy usullari mavjud:

### **2.1 Oddiy qavslar bilan yaratish**

```python
# Bo'sh list
my_list = []

# Elementlar bilan list
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", 3.14, True]

print(numbers)   # [1, 2, 3, 4, 5]
print(mixed)     # [1, 'apple', 3.14, True]
```

✅ Bu usul eng asosiy va keng qo‘llaniladi.

---

### **2.2 `list()` funksiyasi bilan**

`list()` funksiyasi iterable obyektni listga aylantiradi.

```python
# Stringni listga aylantirish
letters = list("hello")
print(letters)  # ['h', 'e', 'l', 'l', 'o']

# Tupleni listga aylantirish
tup = (1, 2, 3)
numbers = list(tup)
print(numbers)  # [1, 2, 3]

# Setni listga aylantirish
s = {10, 20, 30}
nums = list(s)
print(nums)  # [10, 20, 30] (set tartiblangan emas)
```

---

### **2.3 List comprehension (ro‘yxat tushunchasi orqali)**

Python-da list yaratishning qulay va zamonaviy usuli — **list comprehension**.
Bu orqali shartli yoki matematik transformatsiyalar bilan list yaratish mumkin.

```python
# 0 dan 9 gacha sonlar ro'yxati
numbers = [i for i in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Faqat juft sonlar
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Har bir elementni kvadratga ko‘tarish
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# String elementlardan katta harfni olish
words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
print(upper_words)  # ['APPLE', 'BANANA', 'CHERRY']
```

---

### **2.4 Multiplikatsiya operatori bilan**

Listni qayta takrorlash orqali ham yaratish mumkin.

```python
# Bo'sh ro'yxatni 5 marta takrorlash
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

# String elementini takrorlash
letters = ["A"] * 3
print(letters)  # ['A', 'A', 'A']

# Ichki listni takrorlash (ehtiyot bo‘lish kerak!)
nested = [[1, 2]] * 3
print(nested)  # [[1, 2], [1, 2], [1, 2]]

# Muammo: nested[0][0] = 9
nested[0][0] = 9
print(nested)  # [[9, 2], [9, 2], [9, 2]]  # barcha ichki listlar bir xil objectga ulangan!
```

---

## 3️⃣ **Bo‘sh list yaratish**

Bo‘sh list yaratishning ikki usuli mavjud:

```python
a = []        # tavsiya etilgan
b = list()    # ham ishlaydi

print(a, b)   # [], []
```

---

## 4️⃣ **List elementlarini turli turlarda yaratish**

List ichida **int, float, string, bool, list, tuple, set, dict** kabi elementlarni aralashtirish mumkin.

```python
my_list = [1, 3.14, "Python", True, [1, 2], (3, 4), {5, 6}, {"key": "value"}]
print(my_list)
```

---

## 5️⃣ **List yaratishda e’tibor beriladigan nuqtalar**

1. List tartiblangan (`ordered`) → index orqali murojaat qilsa bo‘ladi.
2. List mutable (`o‘zgartirilishi mumkin`) → element qo‘shish, o‘chirish, o‘zgartirish mumkin.
3. List ichidagi elementlar turli turlarda bo‘lishi mumkin.
4. Bo‘sh listni yaratish va keyin element qo‘shish qulay usuldir (`append()` metodidan foydalaniladi).

---

## 6️⃣ **Amaliy misollar**

```python
# 1. Bo'sh list yaratish va element qo'shish
fruits = []
fruits.append("apple")
fruits.append("banana")
print(fruits)  # ['apple', 'banana']

# 2. Stringdan list yaratish
word = "Python"
letters = list(word)
print(letters)  # ['P', 'y', 't', 'h', 'o', 'n']

# 3. List comprehension bilan list yaratish
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 4. Ichki list yaratish
matrix = [[0]*3 for _ in range(3)]
print(matrix)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---
# **Python Lists: Indexing (Indekslar orqali murojaat qilish)**

## 1️⃣ **Indexing nima?**

Listning har bir elementi **tartiblangan tartib raqamiga** ega, bu raqamga **index** deyiladi.

* Python-da indexlar **0** dan boshlanadi.
* List uzunligi `n` bo‘lsa, so‘nggi element indeksi `n-1` bo‘ladi.

---

## 2️⃣ **Oddiy (pozitiv) indexlar**

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  # 'apple'   -> birinchi element
print(fruits[1])  # 'banana'
print(fruits[3])  # 'date'    -> oxirgi element
```

**Eslatma:** Agar mavjud bo‘lmagan indeksga murojaat qilinsa, **IndexError** chiqadi:

```python
print(fruits[4])  # IndexError: list index out of range
```

---

## 3️⃣ **Salbiy (negative) indexlar**

Python-da **-1** indeksi listning oxirgi elementini bildiradi.
Shu tarzda, -2, -3, ... indekslari orqadan sanash imkonini beradi.

```python
print(fruits[-1])  # 'date'      -> oxirgi element
print(fruits[-2])  # 'cherry'    -> oxirdan ikkinchi
print(fruits[-4])  # 'apple'     -> oxirdan to‘rtinchi
```

---

## 4️⃣ **Indexing bilan elementlarni o‘zgartirish**

List **mutable** ekanligi sababli index orqali elementni o‘zgartirish mumkin:

```python
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

fruits[-1] = "dragonfruit"
print(fruits)  # ['apple', 'blueberry', 'cherry', 'dragonfruit']
```

---

## 5️⃣ **Index orqali nested list elementiga murojaat**

List ichida list bo‘lsa, **ikki yoki undan ko‘p indekslar** ishlatiladi:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1   -> birinchi qator, birinchi element
print(matrix[1][2])  # 6   -> ikkinchi qator, uchinchi element
print(matrix[-1][-1]) # 9   -> oxirgi qator, oxirgi element
```

---

## 6️⃣ **Indexing bilan string elementlarga murojaat**

Agar list ichida string bo‘lsa, stringning har bir harfiga index orqali murojaat qilish mumkin:

```python
words = ["hello", "world"]
print(words[0][1])  # 'e'  -> "hello" so'zining ikkinchi harfi
print(words[1][-1]) # 'd'  -> "world" so'zining oxirgi harfi
```

---

## 7️⃣ **Indexing bilan ehtiyot bo‘lish kerak**

1. **IndexError** – mavjud bo‘lmagan indeksga murojaat qilinsa.
2. **Mutable listlar** – indeks orqali elementni o‘zgartirish mumkin, immutable tiplarda (`tuple`) bu mumkin emas.

```python
numbers = [10, 20, 30]
numbers[1] = 99
print(numbers)  # [10, 99, 30]

t = (10, 20, 30)
# t[1] = 99  -> TypeError: 'tuple' object does not support item assignment
```

---

## 8️⃣ **Amaliy misollar**

```python
# 1. Oddiy list indexing
colors = ["red", "green", "blue", "yellow"]
print(colors[0])   # red
print(colors[-1])  # yellow

# 2. Nested list
grid = [[1,2],[3,4],[5,6]]
print(grid[2][0])  # 5

# 3. String ichidagi harf
words = ["Python", "Java"]
print(words[0][3])  # h

# 4. Index yordamida o'zgartirish
numbers = [1,2,3,4,5]
numbers[2] = 99
print(numbers)  # [1, 2, 99, 4, 5]
```

---
# **Python Lists: Slicing (Listni kesish)**

## 1️⃣ **Slicing nima?**

**Slicing** — listning **bir qism elementlarini ajratib olish** usuli.

* Natija **yangi list** bo‘ladi.
* Asl list o‘zgarmaydi (agar bevosita index orqali o‘zgartirmasak).

Sintaksis:

```python
list_name[start:stop:step]
```

* **start** – qayerdan boshlash (shu index kiradi)
* **stop** – qayergacha (shu index **kirmaydi**)
* **step** – qadam (elementlar orasidagi interval)

---

## 2️⃣ **Asosiy slicing**

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

print(fruits[1:4])  # ['banana', 'cherry', 'date']
```

* 1-indekstdan boshlanadi, 4-indeks kirmaydi.
* Natija yangi list: `['banana', 'cherry', 'date']`

---

## 3️⃣ **Start yoki Stop ni tashlab qo‘yish**

```python
# Boshi: start=0
print(fruits[:3])  # ['apple', 'banana', 'cherry']

# Oxiri: stop=len(list)
print(fruits[2:])  # ['cherry', 'date', 'fig']

# Hammasi
print(fruits[:])   # ['apple', 'banana', 'cherry', 'date', 'fig']
```

---

## 4️⃣ **Step (qadam) bilan slicing**

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Har 2-elementni olish
print(numbers[::2])  # [0, 2, 4, 6, 8]

# Har 3-elementni olish
print(numbers[::3])  # [0, 3, 6, 9]

# Teskari tartibda olish
print(numbers[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

## 5️⃣ **Salbiy indexlar bilan slicing**

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

# Oxirdan kesish
print(fruits[-4:-1])  # ['banana', 'cherry', 'date']

# Teskari kesish
print(fruits[-1:-4:-1])  # ['fig', 'date', 'cherry']
```

✅ Eslatma: **step < 0** bo‘lsa, start > stop bo‘lishi kerak.

---

## 6️⃣ **Nested list slicing**

List ichida list bo‘lsa ham slicing ishlaydi:

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# 1-qator va 2-qatorni olish
print(matrix[0:2])  # [[1,2,3],[4,5,6]]

# 1-qatorning 1 va 2-elementini olish
print(matrix[0][0:2])  # [1, 2]
```

---

## 7️⃣ **Slicing yordamida elementni o‘zgartirish**

List mutable bo‘lgani uchun, slicing yordamida bir nechta elementni o‘zgartirish mumkin:

```python
numbers = [0,1,2,3,4,5]

# 1-3 indeksdagi elementlarni o'zgartirish
numbers[1:4] = [10, 20, 30]
print(numbers)  # [0, 10, 20, 30, 4, 5]

# Slicing bilan elementlarni o'chirish
numbers[1:4] = []
print(numbers)  # [0, 4, 5]
```

---

## 8️⃣ **Amaliy misollar**

```python
# 1. Oddiy slicing
letters = ['a','b','c','d','e','f']
print(letters[2:5])  # ['c','d','e']

# 2. Step bilan slicing
print(letters[1:6:2]) # ['b','d','f']

# 3. Teskari tartibda slicing
print(letters[::-1])   # ['f','e','d','c','b','a']

# 4. Slicing bilan o‘zgartirish
letters[1:4] = ['x','y','z']
print(letters)         # ['a','x','y','z','e','f']

# 5. Nested list slicing
matrix = [[1,2],[3,4],[5,6]]
print(matrix[1:])      # [[3,4],[5,6]]
print(matrix[0][1:])   # [2]
```

---
# **Python Lists: Methods (Metodlar)**

List metodlari — bu list bilan ishlash, element qo‘shish, o‘chirish, tartiblash va boshqa amallarni bajarish uchun Python tomonidan berilgan funksiyalar.

---

## 1️⃣ **`append()` — Oxiriga element qo‘shish**

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']
```

* Faqat **bitta element** qo‘shadi.
* List **mutable**, shuning uchun asl list o‘zgardi.

---

## 2️⃣ **`extend()` — Bir nechta element qo‘shish**

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # ['apple', 'banana', 'cherry', 'date']
```

* **Iterable** (list, tuple, set) qabul qiladi.
* Farqi: `append()` iterableni bitta element sifatida qo‘shadi, `extend()` esa **alohida elementlar** sifatida qo‘shadi.

```python
fruits = ["apple", "banana"]
fruits.append(["cherry", "date"])
print(fruits)  # ['apple', 'banana', ['cherry', 'date']]
```

---

## 3️⃣ **`insert()` — Ko‘rsatilgan indexga element qo‘shish**

```python
fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # ['apple', 'cherry', 'banana']
```

* Sintaksis: `list.insert(index, element)`
* Element shu indexga joylanadi, keyingilari orqaga suriladi.

---

## 4️⃣ **`remove()` — Elementni qiymat bo‘yicha o‘chirish**

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana']
```

* Faqat **birinchi topilgan** qiymatni o‘chiradi.
* Agar qiymat mavjud bo‘lmasa → `ValueError`.

---

## 5️⃣ **`pop()` — Oxirgi yoki ko‘rsatilgan indexdagi elementni o‘chirish va qaytarish**

```python
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()
print(last)   # 'cherry'
print(fruits) # ['apple', 'banana']

second = fruits.pop(1)
print(second) # 'banana'
print(fruits) # ['apple']
```

* `pop()` **index** oladi, default = -1 (oxirgi element).

---

## 6️⃣ **`clear()` — Listni bo‘shatish**

```python
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # []
```

* Listni bo‘sh qiladi, yangi list yaratmaydi.

---

## 7️⃣ **`index()` — Elementning indexini topish**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # 1
```

* Agar element bir nechta bo‘lsa, **birinchi topilgan index** qaytariladi.
* Element bo‘lmasa → `ValueError`.

---

## 8️⃣ **`count()` — Element nechta borligini hisoblash**

```python
fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # 2
```

* Qiymat necha marta uchraganini qaytaradi.

---

## 9️⃣ **`sort()` — Listni tartiblash**

```python
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # [1, 2, 5, 9]

# Teskari tartib
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 2, 1]
```

* Asl list **o‘zgartiriladi**.
* `sorted()` funksiyasi esa **yangi tartiblangan list** beradi, aslini o‘zgartirmaydi.

```python
numbers = [5, 2, 9, 1]
new_list = sorted(numbers)
print(new_list)  # [1, 2, 5, 9]
print(numbers)   # [5, 2, 9, 1]
```

---

## 🔟 **`reverse()` — Listni teskari qilish**

```python
numbers = [1,2,3,4]
numbers.reverse()
print(numbers)  # [4,3,2,1]
```

* Faqat **listni o‘zgartiradi**, yangi list qaytarmaydi.

---

## 1️⃣1️⃣ **`copy()` — Listning nusxasini olish**

```python
numbers = [1,2,3]
new_list = numbers.copy()
print(new_list)  # [1, 2, 3]

# Tasodifiy o'zgartirish asl listga ta'sir qilmaydi
new_list.append(4)
print(numbers)   # [1, 2, 3]
print(new_list)  # [1, 2, 3, 4]
```

---

## 1️⃣2️⃣ **Amaliy misollar**

```python
# 1. append va extend
a = [1,2]
a.append([3,4])
print(a)   # [1, 2, [3, 4]]

b = [1,2]
b.extend([3,4])
print(b)   # [1, 2, 3, 4]

# 2. insert
a = [10,20,30]
a.insert(1,15)
print(a)   # [10, 15, 20, 30]

# 3. remove va pop
a.remove(20)
print(a)   # [10, 15, 30]

x = a.pop()
print(x)   # 30
print(a)   # [10, 15]

# 4. count va index
a = [1,2,1,3,1]
print(a.count(1))   # 3
print(a.index(3))   # 3

# 5. sort va reverse
a = [5,2,4,1]
a.sort()
print(a)            # [1,2,4,5]
a.reverse()
print(a)            # [5,4,2,1]

# 6. copy va clear
b = a.copy()
b.clear()
print(b)            # []
print(a)            # [5,4,2,1]
```

---

### ✅ **Xulosa**

* List metodlari list bilan ishlashni qulay qiladi:

  * Qo‘shish: `append()`, `extend()`, `insert()`
  * O‘chirish: `remove()`, `pop()`, `clear()`
  * Qidirish: `index()`, `count()`
  * Tartiblash: `sort()`, `reverse()`
  * Nusxalash: `copy()`
* **Mutable list** bo‘lganligi uchun metodlar ko‘p hollarda asl listni o‘zgartiradi.

---
# **Python Lists: Mutability (O‘zgartiriluvchanlik)**

## 1️⃣ **Mutability nima?**

**Mutability** — obyektni yaratilgandan keyin **ichki qiymatlarini o‘zgartirish imkoniyati**.

* **Mutable**: qiymatlarini o‘zgartirish mumkin → `list`, `dict`, `set`
* **Immutable**: qiymatlarini o‘zgartirish mumkin emas → `tuple`, `str`, `int`, `float`

---

## 2️⃣ **List mutable ekanligi**

Python-da **list mutable**, ya’ni list yaratganingizdan keyin uning elementlarini:

* qo‘shish
* o‘chirish
* o‘zgartirish

mumkin.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']

# Elementni o'zgartirish
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Element qo'shish
fruits.append("date")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

# Element o'chirish
fruits.pop(0)
print(fruits)  # ['blueberry', 'cherry', 'date']
```

✅ List yaratganingizdan keyin uning **asl obyektini o‘zgartirish mumkin**.

---

## 3️⃣ **Immutable object bilan solishtirish**

**Tuple** immutable misol:

```python
t = (1, 2, 3)
# t[1] = 99  -> TypeError: 'tuple' object does not support item assignment
```

* Tuple yaratgandan keyin elementlarini **o‘zgartirib bo‘lmaydi**.
* List bilan farqi shunda.

---

## 4️⃣ **Mutability va referenslar (IDs)**

List mutable bo‘lgani uchun, bir listni boshqa o‘zgaruvchiga tenglashtirsangiz, ular **bir xil obyektni** bildiradi.

```python
a = [1, 2, 3]
b = a  # b ham a bilan bir xil obyektga bog‘landi

b.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

# ID larini tekshirish
print(id(a))  # 140291241234560 (misol)
print(id(b))  # 140291241234560 (bir xil)
```

* Agar asl listni o‘zgartirmasdan nusxa olish kerak bo‘lsa, `.copy()` ishlatiladi:

```python
a = [1,2,3]
b = a.copy()
b.append(4)
print(a)  # [1,2,3]
print(b)  # [1,2,3,4]
```

---

## 5️⃣ **Nested listlarda mutability**

List ichida list bo‘lsa, **ichki list ham mutable**:

```python
matrix = [[1,2],[3,4]]
matrix[0][0] = 99
print(matrix)  # [[99,2],[3,4]]
```

* Ichki listni o‘zgartirish asl listga ta’sir qiladi.
* Shu sabab, ko‘p hollarda **deep copy** kerak bo‘ladi (`copy.deepcopy()`).

```python
import copy
matrix2 = copy.deepcopy(matrix)
matrix2[0][0] = 0
print(matrix)   # [[99, 2], [3, 4]]  -> asl list o'zgarmadi
print(matrix2)  # [[0, 2], [3, 4]]  -> yangi list
```

---

## 6️⃣ **Mutability bilan slicing**

Slicing orqali **yangi list** hosil bo‘ladi, shuning uchun slicing bilan ishlaganda asl list o‘zgarmaydi:

```python
numbers = [1,2,3,4,5]
subset = numbers[1:4]
subset[0] = 99
print(numbers)  # [1,2,3,4,5]  -> asl list o'zgarmadi
print(subset)   # [99,3,4]
```

* **Exception:** nested listlarda slicing **faqat yuqori darajadagi listni nusxalaydi**, ichki listlar **original obyektga ulangan**.

```python
nested = [[1,2],[3,4]]
slice_nested = nested[:]
slice_nested[0][0] = 99
print(nested)       # [[99,2],[3,4]] -> ichki list asl listga ta'sir qildi
```

---

## 7️⃣ **Amaliy misollar**

```python
# 1. Oddiy mutable list
a = [1,2,3]
a[0] = 10
a.append(4)
a.pop()
print(a)  # [10,2,3]

# 2. Immutable tuple bilan solishtirish
t = (1,2,3)
# t[0] = 99 -> TypeError

# 3. Copy bilan mutability
b = a.copy()
b[1] = 99
print(a)  # [10,2,3]
print(b)  # [10,99,3]

# 4. Nested list mutability
matrix = [[1,2],[3,4]]
matrix[0][1] = 99
print(matrix)  # [[1,99],[3,4]]
```

---
# **Python Tuples: Packing (Tuple yaratish)**

## 1️⃣ **Tuple nima?**

**Tuple** — bu **tartiblangan** va **immutable** (o‘zgartirib bo‘lmaydigan) ma’lumotlar to‘plami.

* Elementlar bir xil yoki turli turdagi bo‘lishi mumkin.
* Listdan farqi: **tuple immutable**, ya’ni yaratgandan keyin elementlarni o‘zgartirish mumkin emas.
* Tuple ko‘pincha **ma’lumotlarni o‘zgarmas sifatida saqlash** uchun ishlatiladi.

---

## 2️⃣ **Tuple Packing nima?**

**Packing** — bir nechta qiymatlarni **bitta tuple**ga joylash jarayoni.

```python
# Oddiy tuple yaratish (packing)
my_tuple = 1, 2, 3, 4
print(my_tuple)       # (1, 2, 3, 4)
print(type(my_tuple)) # <class 'tuple'>
```

✅ Eslatma: **qavslar ixtiyoriy**, lekin odatda aniqlik uchun ishlatiladi:

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # (1, 2, 3, 4)
```

---

## 3️⃣ **Tuple yaratish turli qiymatlar bilan**

Tuple elementlari **har qanday turda** bo‘lishi mumkin:

```python
mixed_tuple = (1, 3.14, "Python", True)
print(mixed_tuple)  # (1, 3.14, 'Python', True)
```

* Tuple ichida list, tuple, dict ham bo‘lishi mumkin:

```python
nested_tuple = (1, [2,3], (4,5), {"a":10})
print(nested_tuple)
```

---

## 4️⃣ **Bitta elementli tuple**

Bitta elementli tuple yaratish uchun **vergul** ishlatiladi:

```python
single = (5,)
print(single)       # (5,)
print(type(single)) # <class 'tuple'>

not_a_tuple = (5)
print(type(not_a_tuple)) # <class 'int'>  -> bitta elementli tuple emas!
```

* **Muhim:** bitta elementda vergul bo‘lmasa, u **tuple** hisoblanmaydi.

---

## 5️⃣ **Tuple Packing misollari**

```python
# 1. Oddiy packing
a = 10
b = 20
c = 30
my_tuple = a, b, c
print(my_tuple)  # (10, 20, 30)

# 2. String va float bilan
info = "Alice", 25, 3.14
print(info)      # ('Alice', 25, 3.14)

# 3. List va tuple aralash
data = [1,2], (3,4), 5
print(data)      # ([1,2], (3,4), 5)
```

---

## 6️⃣ **Packingning afzalliklari**

1. Qisqa va oson sintaksis.
2. Bir nechta qiymatlarni **bir joyda saqlash**.
3. **Immutable** → xavfsiz saqlash (elementlar tasodifiy o‘zgarmaydi).
4. Keyinchalik **unpacking** yordamida elementlarga osongina murojaat qilish mumkin.

---
# **Python Tuples: Unpacking (Tuple elementlarini ajratib olish)**

## 1️⃣ **Tuple Unpacking nima?**

**Unpacking** — tuple ichidagi elementlarni **alohida o‘zgaruvchilarga ajratib olish** jarayoni.

* Packing — bir nechta qiymatni tuplega joylash
* Unpacking — tuple elementlarini **alohida o‘zgaruvchilarga chiqarish**

Sintaksis:

```python
var1, var2, var3 = my_tuple
```

---

## 2️⃣ **Oddiy tuple unpacking**

```python
my_tuple = (10, 20, 30)

a, b, c = my_tuple
print(a)  # 10
print(b)  # 20
print(c)  # 30
```

* Tuple elementlari **soni** va **o‘zgaruvchilar soni** mos bo‘lishi kerak.
* Agar soni mos kelmasa → `ValueError`:

```python
x, y = (1,2,3)  # ValueError: too many values to unpack
```

---

## 3️⃣ **Unpacking bilan list ham ishlaydi**

```python
numbers = [1,2,3]
a, b, c = numbers
print(a,b,c)  # 1 2 3
```

* Tuple va listni **bir xil tarzda unpack qilish mumkin**.

---

## 4️⃣ **Asterisk `*` operatori bilan unpacking**

Asterisk yordamida **qolgan elementlarni list sifatida olish** mumkin:

```python
my_tuple = (1,2,3,4,5)

a, *b, c = my_tuple
print(a)  # 1
print(b)  # [2,3,4]
print(c)  # 5
```

* Qolgan elementlar har doim **list** ko‘rinishida olinadi.
* Asterisk **faqat bitta joyda ishlatiladi**.

```python
a, *b, *c = (1,2,3,4)  # SyntaxError
```

---

## 5️⃣ **Nested tuple unpacking**

Tuple ichida tuple bo‘lsa, **ichki tuple elementlarini** ham unpack qilish mumkin:

```python
nested = (1, (2,3), 4)
a, (b, c), d = nested
print(a,b,c,d)  # 1 2 3 4
```

* Nested unpacking juda qulay: list/dict yoki tuple ichidagi **ko‘p qavatli ma’lumotlarni ajratish** uchun ishlatiladi.

---

## 6️⃣ **Swapping (qiymatlarni almashtirish) bilan unpacking**

Python-da unpacking yordamida **o‘zgaruvchilarni almashtirish** mumkin:

```python
a = 10
b = 20

a, b = b, a
print(a,b)  # 20 10
```

* Klassik usul: vaqtinchalik o‘zgaruvchi (`temp`) ishlatish shart emas.

---

## 7️⃣ **Unpacking bilan funktsiyalar**

Tuple unpacking **function return** qiymatlari bilan ham ishlatiladi:

```python
def get_point():
    return (10, 20)

x, y = get_point()
print(x,y)  # 10 20
```

* Shu tarzda bir nechta qiymatlarni **bir vaqtning o‘zida** olish mumkin.

---

## 8️⃣ **Amaliy misollar**

```python
# 1. Oddiy unpacking
person = ("Alice", 25, "F")
name, age, gender = person
print(name, age, gender)  # Alice 25 F

# 2. Nested unpacking
coords = (1, (2,3), 4)
x, (y, z), w = coords
print(x,y,z,w)  # 1 2 3 4

# 3. Asterisk bilan
numbers = (1,2,3,4,5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2,3,4]
print(last)    # 5

# 4. Swapping
a, b = 5, 10
a, b = b, a
print(a,b)     # 10 5

# 5. Function return unpacking
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([3,7,1,9])
print(low, high)  # 1 9
```

---
# **Python Tuples: Immutability (O‘zgarmaslik)**

## 1️⃣ **Immutability nima?**

**Immutability** — obyekt yaratgandan keyin uning **ichki qiymatlarini o‘zgartirish mumkin emasligi**.

* **Tuple** immutable
* **List** mutable
* Immutable obyektlarda **element qo‘shish, o‘chirish, almashtirish** mumkin emas

---

## 2️⃣ **Tuple immutable ekanligi**

```python
my_tuple = (1, 2, 3)

# Elementni o'zgartirish mumkin emas
# my_tuple[1] = 99  -> TypeError: 'tuple' object does not support item assignment
```

* Tuple yaratgandan keyin **element qiymatlari o‘zgarmaydi**.

---

## 3️⃣ **Bitta elementli tuple va immutability**

```python
single = (5,)
print(single)        # (5,)
# single[0] = 10     -> TypeError
```

* Tuple immutable, shuning uchun **bitta elementni ham o‘zgartirish mumkin emas**.

---

## 4️⃣ **Tuple bilan listni solishtirish**

```python
# List (mutable)
lst = [1,2,3]
lst[0] = 10
lst.append(4)
print(lst)  # [10, 2, 3, 4]

# Tuple (immutable)
t = (1,2,3)
# t[0] = 10  -> TypeError
# t.append(4) -> AttributeError
```

* **Mutable** obyektlar: list, dict, set
* **Immutable** obyektlar: tuple, str, int, float

---

## 5️⃣ **Tuple ichidagi mutable elementlar**

Tuple o‘zi immutable, lekin **ichidagi element mutable bo‘lsa**, u **o‘zgartirilishi mumkin**.

```python
t = (1, [2,3], 4)
t[1].append(99)
print(t)  # (1, [2, 3, 99], 4)
```

* Tuple o‘zgarmadi, lekin ichidagi **list mutable**, shuning uchun element qo‘shish mumkin.

---

## 6️⃣ **Tuple immutabilityning afzalliklari**

1. **Xavfsizlik**: elementlar tasodifiy o‘zgarmaydi
2. **Hashable** → tuple dict key sifatida ishlatilishi mumkin
3. **Tezroq ishlaydi**: immutable obyektlar **memory-efficient**

```python
t = (1,2,3)
d = {t: "value"}  # tuple dict key sifatida ishlaydi
print(d)          # {(1, 2, 3): 'value'}
```

* List bilan buni qilsa bo‘lmaydi:

```python
lst = [1,2,3]
# d = {lst: "value"}  -> TypeError: unhashable type: 'list'
```

---

## 7️⃣ **Tuple immutability va unpacking**

* Tuple immutable, lekin **unpacking orqali yangi o‘zgaruvchilar yaratish** mumkin:

```python
t = (1, 2, 3)
a, b, c = t
print(a,b,c)  # 1 2 3

# a ni o'zgartirish tuplega ta'sir qilmaydi
a = 99
print(t)      # (1, 2, 3)
```

* Tuple elementlarini o‘zgartirmasdan **yangi qiymatlar bilan tuple yaratish** mumkin:

```python
t = (1, 2, 3)
new_t = (99,) + t[1:]
print(new_t)  # (99, 2, 3)
```

---

## 8️⃣ **Amaliy misollar**

```python
# 1. Oddiy immutability
t = (1,2,3)
# t[0] = 99 -> TypeError

# 2. Ichki mutable element
t = (1, [2,3], 4)
t[1].append(99)
print(t)  # (1, [2, 3, 99], 4)

# 3. Tuple dict key sifatida
t = (1,2)
d = {t: "value"}
print(d)  # {(1, 2): 'value'}

# 4. Tuple + unpacking
t = (5,10,15)
a,b,c = t
a = 99
print(t)  # (5, 10, 15)

# 5. Yangi tuple yaratish immutable tarzda
t = (1,2,3)
new_t = (0,) + t[1:]
print(new_t)  # (0, 2, 3)
```

---
# **Python Sets: Uniqueness & Mathematical Operations**

## 1️⃣ **Set nima?**

**Set** — bu **tartibsiz** va **unique (takrorlanmaydigan) elementlar** to‘plami.

* List yoki tupledan farqi:

  * **Tartibsiz** → elementlarga index orqali murojaat qilish mumkin emas
  * **Unique** → takroriy elementlar avtomatik olib tashlanadi
* Set mutable (element qo‘shish, o‘chirish mumkin)
* Elementlar **hashable** bo‘lishi kerak → list ichida set bo‘lmaydi, lekin tuple bo‘lishi mumkin

```python
my_set = {1,2,3,3,2}
print(my_set)  # {1,2,3}  -> takroriy elementlar olib tashlandi
```

---

## 2️⃣ **Set yaratish**

### 2.1 Qavslar bilan

```python
fruits = {"apple", "banana", "cherry"}
print(fruits)  # {'banana', 'apple', 'cherry'}  -> tartibsiz
```

### 2.2 `set()` funksiyasi bilan

```python
numbers = set([1,2,2,3,4])
print(numbers)  # {1,2,3,4}

letters = set("hello")
print(letters)  # {'e','o','h','l'} -> takroriy 'l' olib tashlandi
```

---

## 3️⃣ **Set elementlarini qo‘shish va o‘chirish**

### 3.1 `add()` — element qo‘shish

```python
s = {1,2,3}
s.add(4)
print(s)  # {1,2,3,4}
```

### 3.2 `update()` — bir nechta element qo‘shish

```python
s.update([5,6])
print(s)  # {1,2,3,4,5,6}
```

### 3.3 `remove()` — element o‘chirish

```python
s.remove(2)
print(s)  # {1,3,4,5,6}
# Agar element mavjud bo‘lmasa -> KeyError
```

### 3.4 `discard()` — element o‘chirish (xatolik bermaydi)

```python
s.discard(10)  # mavjud emas, xatolik yo'q
```

### 3.5 `pop()` — tasodifiy elementni o‘chirish

```python
x = s.pop()
print(x)
print(s)  # tasodifiy element o‘chadi, tartib yo‘q
```

### 3.6 `clear()` — barcha elementlarni o‘chirish

```python
s.clear()
print(s)  # set()
```

---

## 4️⃣ **Set matematik amallari (Set Theory)**

### 4.1 `union()` — birlashtirish (|)

```python
a = {1,2,3}
b = {3,4,5}
print(a.union(b))  # {1,2,3,4,5}
print(a | b)       # {1,2,3,4,5}  -> shorthand
```

### 4.2 `intersection()` — kesish (&)

```python
print(a.intersection(b))  # {3}
print(a & b)              # {3} -> shorthand
```

### 4.3 `difference()` — farq (-)

```python
print(a.difference(b))    # {1,2}
print(a - b)              # {1,2}
```

### 4.4 `symmetric_difference()` — simmetrik farq (^)

```python
print(a.symmetric_difference(b))  # {1,2,4,5}
print(a ^ b)                      # {1,2,4,5} -> shorthand
```

---

## 5️⃣ **Element mavjudligini tekshirish**

```python
fruits = {"apple","banana","cherry"}
print("apple" in fruits)   # True
print("date" in fruits)    # False
```

---

## 6️⃣ **Set va mutable/immutable elementlar**

* Set elementlari **hashable** bo‘lishi kerak → list set ichida bo‘la olmaydi
* Tuple set ichida bo‘lishi mumkin (immutable)

```python
s = {1, (2,3)}
print(s)  # {1, (2,3)}

# s = {1,[2,3]} -> TypeError: unhashable type: 'list'
```

---

## 7️⃣ **Amaliy misollar**

```python
# 1. Takroriy elementlar avtomatik olib tashlanadi
nums = [1,2,2,3,4,4,5]
unique_nums = set(nums)
print(unique_nums)  # {1,2,3,4,5}

# 2. Element qo'shish va o'chirish
fruits = {"apple","banana"}
fruits.add("cherry")
fruits.discard("banana")
print(fruits)  # {'apple','cherry'}

# 3. Set operations
a = {1,2,3,4}
b = {3,4,5,6}
print(a | b)  # {1,2,3,4,5,6} -> union
print(a & b)  # {3,4}         -> intersection
print(a - b)  # {1,2}         -> difference
print(a ^ b)  # {1,2,5,6}     -> symmetric_difference

# 4. Tuple inside set
s = {1, (2,3)}
print(s)  # {1, (2,3)}
```

---

# **Python Sets: Uniqueness (Takrorlanmaslik)**

## 1️⃣ **Unik elementlar nima?**

Setning asosiy xususiyati — **har bir element faqat bir marta uchraydi**.

* Agar list yoki tuple ichida takroriy elementlar bo‘lsa, setga aylantirganda **takrorlar avtomatik olib tashlanadi**.
* Shu sabab set **duplicate-free** ma’lumotlarni saqlash uchun qulay.

---

## 2️⃣ **Listdan setga o‘tkazish**

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

✅ Takroriy elementlar `{}` ichida faqat bir marta saqlanadi.

---

## 3️⃣ **Stringdagi takroriy harflar**

```python
word = "hello"
unique_letters = set(word)
print(unique_letters)  # {'h','e','l','o'}
```

* Shu yerda `'l'` faqat bir marta saqlanadi.
* Tartib **muammo**: set elementlari **unordered**, shuning uchun original tartibni saqlamaydi.

---

## 4️⃣ **Takroriy elementlarni oldini olish**

* Set bilan **data integrity** (takrorlanmas ma’lumotlar) ta’minlanadi.
* Masalan, foydalanuvchi IDlarini saqlash:

```python
user_ids = [101, 102, 103, 101, 104, 102]
unique_user_ids = set(user_ids)
print(unique_user_ids)  # {101, 102, 103, 104}
```

---

## 5️⃣ **Unik elementlarni saqlash va qo‘shish**

```python
fruits = {"apple", "banana", "cherry"}

fruits.add("banana")  # allaqachon mavjud
print(fruits)         # {'apple', 'banana', 'cherry'} -> o'zgarmadi

fruits.add("date")
print(fruits)         # {'apple', 'banana', 'cherry', 'date'}
```

✅ Set **duplicate qo‘shishga yo‘l qo‘ymaydi**.

---

## 6️⃣ **Takroriy elementlarni avtomatik aniqlash**

```python
numbers = [1,2,2,3,3,3,4,5,5]
duplicates = [x for x in numbers if numbers.count(x) > 1]
print(duplicates)  # [2, 2, 3, 3, 3, 5, 5]

unique_numbers = set(numbers)
print(unique_numbers)  # {1,2,3,4,5} -> duplicate removed
```

* Set orqali **takroriy elementlarni filtrlash** juda oson.

---

## 7️⃣ **Amaliy misollar**

```python
# 1. Listni unique qilish
nums = [1,1,2,3,3,4,4,4,5]
unique_nums = set(nums)
print(unique_nums)  # {1,2,3,4,5}

# 2. String ichidagi unique harflar
word = "banana"
unique_letters = set(word)
print(unique_letters)  # {'b','a','n'}

# 3. Takroriy element qo‘shishni oldini olish
fruits = {"apple", "banana"}
fruits.add("apple")
print(fruits)  # {'apple', 'banana'}

# 4. User IDlarni unique qilish
ids = [101,102,103,101,104]
unique_ids = set(ids)
print(unique_ids)  # {101,102,103,104}
```

---
# **Python Sets: Mathematical Operations**

Setlar bilan **matematik to‘plam amallari** bajarish juda oson, chunki Python-da setlar **matematika to‘plamlari (set theory)** ga mos keladi.

---

## 1️⃣ **Union (Birlashtirish) — `union()` yoki `|`**

* **Union** = barcha elementlar, takroriy elementlar faqat bir marta.

```python
A = {1, 2, 3}
B = {3, 4, 5}

# Usul 1: union()
print(A.union(B))  # {1, 2, 3, 4, 5}

# Usul 2: | operatori
print(A | B)       # {1, 2, 3, 4, 5}
```

---

## 2️⃣ **Intersection (Kesish) — `intersection()` yoki `&`**

* **Intersection** = faqat ikkala setda mavjud elementlar

```python
A = {1,2,3}
B = {2,3,4}

# Usul 1: intersection()
print(A.intersection(B))  # {2, 3}

# Usul 2: & operatori
print(A & B)              # {2, 3}
```

---

## 3️⃣ **Difference (Farq) — `difference()` yoki `-`**

* **Difference** = birinchi setda bor, ikkinchi setda yo‘q elementlar

```python
A = {1,2,3}
B = {2,3,4}

# A - B
print(A.difference(B))  # {1}
print(A - B)            # {1}

# B - A
print(B.difference(A))  # {4}
print(B - A)            # {4}
```

---

## 4️⃣ **Symmetric Difference (Simmetrik Farq) — `symmetric_difference()` yoki `^`**

* **Symmetric Difference** = ikkala setda mavjud, lekin faqat **birida** bor elementlar

```python
A = {1,2,3}
B = {2,3,4}

# Usul 1: symmetric_difference()
print(A.symmetric_difference(B))  # {1, 4}

# Usul 2: ^ operatori
print(A ^ B)                      # {1, 4}
```

---

## 5️⃣ **Subset va Superset (Qo‘shimcha)**

* **issubset()** → A set B set ichida to‘liq bo‘lsa True
* **issuperset()** → A set B setni o‘z ichiga olsa True

```python
A = {1,2}
B = {1,2,3,4}

print(A.issubset(B))   # True
print(B.issuperset(A)) # True
```

---

## 6️⃣ **Amaliy misollar**

```python
# 1. Union
a = {1,2,3}
b = {3,4,5}
print(a | b)  # {1,2,3,4,5}

# 2. Intersection
print(a & b)  # {3}

# 3. Difference
print(a - b)  # {1,2}
print(b - a)  # {4,5}

# 4. Symmetric difference
print(a ^ b)  # {1,2,4,5}

# 5. Subset/Superset
x = {1,2}
y = {1,2,3}
print(x.issubset(y))    # True
print(y.issuperset(x))  # True
```

---
# **Python Dictionaries**

## 1️⃣ **Dictionary nima?**

**Dictionary (dict)** — bu **tartibsiz**, **mutable**, **key-value** (kalit-qiymat) asosidagi ma’lumotlar tuzilmasi.

* Har bir element **key-value** juftlik sifatida saqlanadi.
* **Key**: unique, hashable (int, float, string, tuple)
* **Value**: har qanday turdagi ma’lumot bo‘lishi mumkin
* Dictionary **mutable** → element qo‘shish, o‘chirish va o‘zgartirish mumkin

```python
person = {"name": "Alice", "age": 25, "city": "Tashkent"}
print(person)
# {'name': 'Alice', 'age': 25, 'city': 'Tashkent'}
```

---

## 2️⃣ **Dictionary yaratish**

### 2.1 `{}` qavslar bilan

```python
my_dict = {"a": 1, "b": 2, "c": 3}
```

### 2.2 `dict()` funksiyasi bilan

```python
my_dict = dict(a=1, b=2, c=3)
print(my_dict)  # {'a':1, 'b':2, 'c':3}
```

---

## 3️⃣ **Keys va Values**

```python
person = {"name": "Alice", "age": 25, "city": "Tashkent"}

# Keys
print(person.keys())   # dict_keys(['name','age','city'])

# Values
print(person.values()) # dict_values(['Alice',25,'Tashkent'])

# Items (key-value juftliklari)
print(person.items())  # dict_items([('name','Alice'), ('age',25), ('city','Tashkent')])
```

* `keys()`, `values()`, `items()` → iterable object qaytaradi, list emas
* List ko‘rinishida olish uchun `list()` ishlatiladi:

```python
print(list(person.keys()))  # ['name','age','city']
```

---

## 4️⃣ **Dictionary elementlariga murojaat**

```python
person = {"name": "Alice", "age": 25}

# Qiymatni olish
print(person["name"])  # Alice

# Qiymatni o'zgartirish
person["age"] = 26
print(person)          # {'name': 'Alice', 'age': 26}

# Yangi element qo‘shish
person["city"] = "Tashkent"
print(person)          # {'name':'Alice','age':26,'city':'Tashkent'}
```

* Agar mavjud bo‘lmagan keyga murojaat qilsak → `KeyError`
* `get()` metodi xavfsizroq:

```python
print(person.get("country"))  # None
print(person.get("country", "Uzbekistan"))  # Uzbekistan
```

---

## 5️⃣ **Dictionary Methods (Metodlar)**

| Metod                      | Tavsif                                                  |
| -------------------------- | ------------------------------------------------------- |
| `get(key[, default])`      | Key qiymatini olish, bo‘lmasa default qaytaradi         |
| `keys()`                   | Barcha keys                                             |
| `values()`                 | Barcha values                                           |
| `items()`                  | Key-value juftliklari                                   |
| `update(dict2)`            | Dictionaryga boshqa dictionary elementlarini qo‘shish   |
| `pop(key)`                 | Key bo‘yicha elementni o‘chiradi va qaytaradi           |
| `popitem()`                | So‘nggi elementni o‘chiradi va qaytaradi (Python 3.7+)  |
| `clear()`                  | Barcha elementlarni o‘chiradi                           |
| `copy()`                   | Shallow copy (yangi dictionary)                         |
| `setdefault(key, default)` | Key mavjud bo‘lmasa default bilan qo‘shadi va qaytaradi |

### 5.1 `update()`

```python
person = {"name":"Alice","age":25}
person.update({"age":26,"city":"Tashkent"})
print(person)  # {'name':'Alice','age':26,'city':'Tashkent'}
```

### 5.2 `pop()` va `popitem()`

```python
person = {"name":"Alice","age":26,"city":"Tashkent"}

age = person.pop("age")
print(age)     # 26
print(person)  # {'name':'Alice','city':'Tashkent'}

item = person.popitem()
print(item)    # ('city','Tashkent')
print(person)  # {'name':'Alice'}
```

### 5.3 `setdefault()`

```python
person = {"name":"Alice"}
city = person.setdefault("city", "Tashkent")
print(city)    # Tashkent
print(person)  # {'name':'Alice','city':'Tashkent'}
```

---

## 6️⃣ **Hashing Basics**

* Dictionary **key** bo‘lishi uchun **hashable** bo‘lishi kerak
* Mutable elementlar (list, set, dict) key bo‘la olmaydi
* Immutable elementlar (int, float, string, tuple) key bo‘la oladi

```python
d = {(1,2): "tuple key", "a": 10}
print(d)  # {(1,2): 'tuple key', 'a':10}

# d = {[1,2]: "list key"} -> TypeError
```

---

## 7️⃣ **Amaliy misollar**

```python
# 1. Oddiy dict yaratish
person = {"name":"Alice","age":25}
print(person["name"])  # Alice

# 2. Qiymatni o'zgartirish va yangi element qo'shish
person["age"] = 26
person["city"] = "Tashkent"
print(person)  # {'name':'Alice','age':26,'city':'Tashkent'}

# 3. get() va setdefault()
country = person.get("country","Uzbekistan")
person.setdefault("country","Uzbekistan")
print(person)  # {'name':'Alice','age':26,'city':'Tashkent','country':'Uzbekistan'}

# 4. update()
person.update({"age":27, "job":"Engineer"})
print(person)  # {'name':'Alice','age':27,'city':'Tashkent','country':'Uzbekistan','job':'Engineer'}

# 5. pop() va popitem()
age = person.pop("age")
item = person.popitem()
print(age)     # 27
print(item)    # ('job','Engineer')
print(person)  # {'name':'Alice','city':'Tashkent','country':'Uzbekistan'}

# 6. Keys, Values, Items
print(person.keys())   # dict_keys(['name','city','country'])
print(person.values()) # dict_values(['Alice','Tashkent','Uzbekistan'])
print(person.items())  # dict_items([('name','Alice'),('city','Tashkent'),('country','Uzbekistan')])
```

---
# **Python Dictionaries: Keys va Values**

## 1️⃣ **Dictionary key va value nima?**

* **Key**: dictionary ichidagi elementni identifikatsiya qiluvchi noyob kalit.

  * **Unique bo‘lishi kerak**
  * **Hashable bo‘lishi kerak** (int, float, string, tuple)
  * List, set, dict key bo‘la olmaydi (mutable)

* **Value**: keyga tegishli ma’lumot

  * **Har qanday turdagi** bo‘lishi mumkin
  * Takroriy bo‘lishi mumkin

```python
person = {"name": "Alice", "age": 25, "city": "Tashkent"}
```

* Keylar: `"name"`, `"age"`, `"city"`
* Values: `"Alice"`, `25`, `"Tashkent"`

---

## 2️⃣ **Keys**

### 2.1 `keys()` metodi

* Dictionarydagi barcha **keylarni** oladi

```python
person = {"name": "Alice", "age": 25, "city": "Tashkent"}
print(person.keys())  # dict_keys(['name','age','city'])

# List ko‘rinishida olish
print(list(person.keys()))  # ['name','age','city']
```

### 2.2 Key orqali qiymat olish

```python
print(person["name"])  # Alice
print(person.get("age"))  # 25
```

* Agar key mavjud bo‘lmasa:

```python
# print(person["country"]) -> KeyError
print(person.get("country", "Uzbekistan"))  # Uzbekistan
```

---

## 3️⃣ **Values**

### 3.1 `values()` metodi

* Dictionarydagi barcha **value**larni oladi

```python
print(person.values())  # dict_values(['Alice',25,'Tashkent'])
print(list(person.values()))  # ['Alice',25,'Tashkent']
```

* Values **takroriy bo‘lishi mumkin**

```python
grades = {"Math": 90, "Physics": 90, "Chemistry": 80}
print(grades.values())  # dict_values([90, 90, 80])
```

---

## 4️⃣ **Items**

* `items()` — **key-value juftliklarini** oladi
* Har bir element `(key, value)` tuple sifatida qaytadi

```python
print(person.items())  
# dict_items([('name','Alice'),('age',25),('city','Tashkent')])

for key, value in person.items():
    print(f"{key}: {value}")
```

**Natija:**

```
name: Alice
age: 25
city: Tashkent
```

---

## 5️⃣ **Keys va Values bilan ishlash misollari**

```python
# 1. Key orqali value olish
person = {"name":"Alice","age":25,"city":"Tashkent"}
print(person["name"])  # Alice

# 2. get() xavfsizroq
print(person.get("country","Uzbekistan"))  # Uzbekistan

# 3. Barcha keys va values
print(person.keys())   # dict_keys(['name','age','city'])
print(person.values()) # dict_values(['Alice',25,'Tashkent'])

# 4. Items bilan loop
for key, value in person.items():
    print(f"{key} -> {value}")

# 5. Takroriy value bo‘lishi mumkin
grades = {"Math": 90, "Physics": 90, "Chemistry": 80}
print(list(grades.values()))  # [90, 90, 80]

# 6. Keys unique bo‘lishi kerak
d = {"a": 1, "b": 2, "a": 99}
print(d)  # {'a': 99, 'b': 2} -> 'a' key yangilandi
```

---
# **Python Dictionaries: Hashing Basics**

## 1️⃣ **Hashing nima?**

**Hashing** — bu ma’lumotni **integer qiymatga aylantirish** jarayoni, bu qiymat **hash** deb ataladi.

* Python dictionary va setlar **hash table** asosida ishlaydi.
* Har bir **key hashable bo‘lishi kerak** → bu **immutable va o‘zgarmas** bo‘lishi demak.
* Mutable obyektlar (list, set, dict) **key bo‘la olmaydi**, chunki ularning qiymati o‘zgarsa, hash o‘zgarmaydi va dictionary ishlashida muammo yuzaga keladi.

---

## 2️⃣ **Dictionary key va hash**

```python
d = {"name": "Alice", "age": 25}

# string key hashable
print(hash("name"))  # integer qaytaradi

# int key hashable
print(hash(25))      # integer qaytaradi
```

* Hash qiymat **key identifikatsiyasida** ishlatiladi → dictionary elementlarini **tez topish** imkonini beradi.

---

## 3️⃣ **Hashable vs Unhashable Keys**

| Key turi | Hashable?                                            | Misol   |
| -------- | ---------------------------------------------------- | ------- |
| int      | ✅ Ha                                                 | 10      |
| float    | ✅ Ha                                                 | 3.14    |
| string   | ✅ Ha                                                 | "a"     |
| tuple    | ✅ Ha (faqat ichidagi elementlar ham hashable bo‘lsa) | (1,2)   |
| list     | ❌ Yo‘q                                               | [1,2]   |
| set      | ❌ Yo‘q                                               | {1,2}   |
| dict     | ❌ Yo‘q                                               | {"a":1} |

```python
# Hashable key
d = {(1,2): "tuple key", "name": "Alice"}
print(d)  # {(1,2): 'tuple key', 'name': 'Alice'}

# Unhashable key
# d = {[1,2]: "list key"} -> TypeError
```

---

## 4️⃣ **Immutable ichidagi tuple ham hashable**

* Tuple immutable bo‘lsa ham, ichidagi elementlar **mutable bo‘lsa**, tuple **unhashable**

```python
t1 = (1, 2, 3)
print(hash(t1))  # Ha, ishlaydi

t2 = (1, [2,3])
# print(hash(t2)) -> TypeError: unhashable type: 'list'
```

* Shu sabab, dictionary key sifatida **immutable ichidagi immutable elementlar** bo‘lishi kerak.

---

## 5️⃣ **Hashing va Dictionary tezligi**

* Dictionary `O(1)` vaqt ichida **key orqali qiymatni olish** imkonini beradi
* Setlar ham **hash table** orqali ishlaydi, shuning uchun element qo‘shish yoki tekshirish juda tez

```python
d = {i: i*2 for i in range(1000000)}
print(d[999999])  # 1999998  -> tez ishlaydi
```

---

## 6️⃣ **Amaliy misollar**

```python
# 1. Hashable keys
d = {1: "one", 3.14: "pi", "name": "Alice", (1,2): "tuple"}
print(d)
# {1:'one',3.14:'pi','name':'Alice',(1,2):'tuple'}

# 2. Unhashable keys (error)
# d = {[1,2]: "list"} -> TypeError

# 3. Tuple ichida list
# t = (1,[2,3])
# d = {t:"value"} -> TypeError

# 4. Dictionary tezligi hash orqali
import time
d = {i: i*2 for i in range(1000000)}
start = time.time()
val = d[500000]  # O(1)
end = time.time()
print(val, end-start)

# 5. Set hashable elements
s = {1, 2, (3,4)}
print(s)  # {1,2,(3,4)}
```

---
# **Python Dictionaries: Methods**

Python dictionaries bilan ishlashda bir nechta qulay metodlar mavjud. Ular yordamida **element qo‘shish, o‘chirish, yangilash va iteratsiya** qilish mumkin.

---

## 1️⃣ **`get()` — key orqali qiymat olish**

* Key mavjud bo‘lsa, qiymatni qaytaradi
* Key mavjud bo‘lmasa, **default qiymat**ni qaytaradi

```python
person = {"name": "Alice", "age": 25}

print(person.get("name"))         # Alice
print(person.get("city"))         # None
print(person.get("city", "Tashkent"))  # Tashkent
```

---

## 2️⃣ **`keys()` — barcha keys olish**

```python
person = {"name": "Alice", "age": 25, "city": "Tashkent"}
print(person.keys())          # dict_keys(['name','age','city'])
print(list(person.keys()))    # ['name','age','city']
```

---

## 3️⃣ **`values()` — barcha values olish**

```python
print(person.values())        # dict_values(['Alice', 25, 'Tashkent'])
print(list(person.values()))  # ['Alice', 25, 'Tashkent']
```

---

## 4️⃣ **`items()` — key-value juftliklarini olish**

```python
print(person.items())  
# dict_items([('name','Alice'),('age',25),('city','Tashkent')])

for key, value in person.items():
    print(f"{key} -> {value}")
```

**Natija:**

```
name -> Alice
age -> 25
city -> Tashkent
```

---

## 5️⃣ **`update()` — dictionary yangilash**

* Boshqa dictionary yoki key-value juftliklari bilan yangilash

```python
person.update({"age": 26, "country": "Uzbekistan"})
print(person)  
# {'name':'Alice','age':26,'city':'Tashkent','country':'Uzbekistan'}
```

---

## 6️⃣ **`pop(key)` — elementni o‘chirish**

* Key orqali elementni o‘chiradi va qiymatini qaytaradi

```python
age = person.pop("age")
print(age)     # 26
print(person)  # {'name':'Alice','city':'Tashkent','country':'Uzbekistan'}
```

* Agar key mavjud bo‘lmasa → `KeyError`
* Xavfsiz variant: `person.pop("gender", None)`

---

## 7️⃣ **`popitem()` — so‘nggi elementni o‘chirish**

* Python 3.7+ da **dictionary insertion order** saqlanadi
* So‘nggi qo‘shilgan elementni o‘chiradi va `(key, value)` tuple qaytaradi

```python
item = person.popitem()
print(item)    # ('country','Uzbekistan')
print(person)  # {'name':'Alice','city':'Tashkent'}
```

---

## 8️⃣ **`setdefault(key, default)` — key mavjud bo‘lmasa qo‘shish**

* Agar key mavjud bo‘lsa, qiymatni qaytaradi
* Agar key mavjud bo‘lmasa, key va default qo‘shiladi va default qaytariladi

```python
city = person.setdefault("city", "Tashkent")
print(city)    # Tashkent
print(person)  # {'name':'Alice','city':'Tashkent'}

country = person.setdefault("country", "Uzbekistan")
print(country) # Uzbekistan
print(person)  # {'name':'Alice','city':'Tashkent','country':'Uzbekistan'}
```

---

## 9️⃣ **`clear()` — barcha elementlarni o‘chirish**

```python
person.clear()
print(person)  # {}
```

---

## 10️⃣ **`copy()` — shallow copy qilish**

* Yangi dictionary yaratadi, original dictionary o‘zgarmaydi

```python
person = {"name":"Alice","age":25}
person_copy = person.copy()
person_copy["age"] = 26
print(person)       # {'name':'Alice','age':25}
print(person_copy)  # {'name':'Alice','age':26}
```

---

## 11️⃣ **Amaliy misollar**

```python
# 1. get()
person = {"name":"Alice","age":25}
print(person.get("name"))          # Alice
print(person.get("city","Tashkent")) # Tashkent

# 2. keys(), values(), items()
print(list(person.keys()))   # ['name','age']
print(list(person.values())) # ['Alice',25]
print(list(person.items()))  # [('name','Alice'),('age',25)]

# 3. update()
person.update({"age":26,"city":"Tashkent"})
print(person)  # {'name':'Alice','age':26,'city':'Tashkent'}

# 4. pop() va popitem()
age = person.pop("age")
item = person.popitem()
print(age)    # 26
print(item)   # ('city','Tashkent')
print(person) # {'name':'Alice'}

# 5. setdefault()
person.setdefault("country","Uzbekistan")
print(person)  # {'name':'Alice','country':'Uzbekistan'}

# 6. clear() va copy()
person_copy = person.copy()
person.clear()
print(person)       # {}
print(person_copy)  # {'name':'Alice','country':'Uzbekistan'}
```

---
# **Choosing Data Structures (Ma’lumotlar tuzilmasini tanlash)**

Bu mavzuning **asosiy maqsadi** —
👉 **qaysi vaziyatda qaysi data structure (List, Tuple, Set, Dictionary) eng to‘g‘ri tanlov ekanini tushunish**.

---

## 1️⃣ Asosiy mezonlar (tanlash kriteriylari)

Data structure tanlashda quyidagi savollarga javob beriladi:

1. Ma’lumot **tartibli** bo‘lishi kerakmi?
2. Ma’lumot **o‘zgaradimi (mutable)** yoki **o‘zgarmas (immutable)** bo‘lishi kerakmi?
3. **Takroriy elementlar** bo‘lishi mumkinmi?
4. Ma’lumotga **tez murojaat qilish** kerakmi?
5. **Key–Value** ko‘rinishida saqlash kerakmi?

---

## 2️⃣ List qachon tanlanadi?

### ✅ List tanlash shartlari:

* Tartib muhim
* Elementlar **o‘zgaradi**
* Takroriy elementlar bo‘lishi mumkin
* Index orqali ishlash kerak

```python
numbers = [10, 20, 30, 20]
numbers.append(40)
numbers[0] = 99
```

### ❌ List noto‘g‘ri tanlov bo‘ladigan holat:

* Unikal elementlar kerak bo‘lsa
* Juda tez qidirish kerak bo‘lsa

---

## 3️⃣ Tuple qachon tanlanadi?

### ✅ Tuple tanlash shartlari:

* Ma’lumot **o‘zgarmas** bo‘lishi kerak
* Tartib muhim
* Xavfsizlik va barqarorlik muhim

```python
coordinates = (41.31, 69.24)
```

### ❌ Tuple noto‘g‘ri tanlov:

* Elementlarni o‘zgartirish kerak bo‘lsa
* Yangi element qo‘shish kerak bo‘lsa

---

## 4️⃣ Set qachon tanlanadi?

### ✅ Set tanlash shartlari:

* **Unikal elementlar** kerak
* Tartib muhim emas
* Matematik amallar (union, intersection) kerak

```python
ids = {101, 102, 103, 101}
print(ids)  # {101,102,103}
```

### ❌ Set noto‘g‘ri tanlov:

* Tartib saqlanishi kerak bo‘lsa
* Index orqali murojaat qilish kerak bo‘lsa

---

## 5️⃣ Dictionary qachon tanlanadi?

### ✅ Dictionary tanlash shartlari:

* **Key–Value** bog‘lanishi kerak
* Tez qidirish kerak
* Ma’lumotni nom bilan olish kerak

```python
user = {
    "name": "Ali",
    "age": 20,
    "city": "Tashkent"
}
```

### ❌ Dictionary noto‘g‘ri tanlov:

* Faqat oddiy ketma-ket elementlar bo‘lsa
* Index bilan ishlash kerak bo‘lsa

---

## 6️⃣ Tezkor taqqoslash jadvali

| Talab / Strukturа | List | Tuple | Set | Dict     |
| ----------------- | ---- | ----- | --- | -------- |
| Tartib saqlanadi  | ✅    | ✅     | ❌   | ✅ (3.7+) |
| Mutable           | ✅    | ❌     | ✅   | ✅        |
| Unikal elementlar | ❌    | ❌     | ✅   | Keys: ✅  |
| Index mavjud      | ✅    | ✅     | ❌   | ❌        |
| Key–Value         | ❌    | ❌     | ❌   | ✅        |
| Tez qidirish      | ❌    | ❌     | ✅   | ✅        |

---

## 7️⃣ Real vaziyatlar bo‘yicha tanlash

### 🎯 Foydalanuvchi ismlari (takror bo‘lmasin)

```python
usernames = set()
```

### 🎯 Konfiguratsiya (o‘zgarmas)

```python
config = ("localhost", 5432, "admin")
```

### 🎯 Tartibli ma’lumotlar

```python
scores = [90, 85, 88]
```

### 🎯 Profil ma’lumotlari

```python
profile = {
    "username": "ali123",
    "email": "ali@mail.com"
}
```

---

## 8️⃣ Eng muhim qoida (EXAM + REAL CODE)

> ❗ **Agar qaysi strukturani tanlashni bilmasang:**

* Tartib kerak → **List**
* O‘zgarmas bo‘lishi kerak → **Tuple**
* Unikal bo‘lishi kerak → **Set**
* Nomi bilan olish kerak → **Dictionary**

---

## ✅ Yakuniy xulosa

* To‘g‘ri data structure tanlash:

  * Kodni **tezroq**
  * **tozaroq**
  * **xavfsizroq**
  * **kam xatolik bilan**
    yozishga yordam beradi
* Professional dasturchilar uchun bu mavzu **asosiy skill** hisoblanadi

---