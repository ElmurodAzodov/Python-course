
# **STAGE 5 — Loops & Iteration**
---

# **Python’da for Loops**

## **1. for loop nima?**

* **for loop** — bu **ma’lum bir iterable (ketma-ketlik) bo‘ylab takroriy ishlov berish** usuli.
* Iterable: list, tuple, string, dictionary, set, range va boshqa takrorlanadigan obyektlar.
* Sintaksis:

```python
for element in iterable:
    # element bilan bajariladigan kod
    print(element)
```

> 🔑 Python’da **for loop** C/C++ yoki Java’dagi an’anaviy for loopdan farq qiladi:
> u **index emas, iterable elementlari bo‘yicha ishlaydi**.

---

## **2. Oddiy misol: list bo‘yicha takrorlash**

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")
```

**Natija:**

```
I like apple
I like banana
I like cherry
```

---

## **3. String bo‘yicha for loop**

* String ham iterable, har bir harf alohida element sifatida olinadi:

```python
word = "Python"

for letter in word:
    print(letter)
```

**Natija:**

```
P
y
t
h
o
n
```

---

## **4. range() bilan for loop**

* Ko‘pincha **sonlar bo‘yicha takrorlash** uchun `range()` ishlatiladi.
* Sintaksis:

```python
range(start, stop, step)
```

* `start` — boshlang‘ich son (default 0)
* `stop` — tugash soni (exclusive)
* `step` — qadam (default 1)

**Misollar:**

```python
# 0 dan 4 gacha
for i in range(5):
    print(i)
```

**Natija:**

```
0
1
2
3
4
```

```python
# 1 dan 10 gacha 2 qadam bilan
for i in range(1, 11, 2):
    print(i)
```

**Natija:**

```
1
3
5
7
9
```

---

## **5. list comprehension bilan for loop**

* For loop yordamida **yangi list yaratish** mumkin:

```python
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]

print(squares)
```

**Natija:**

```
[1, 4, 9, 16, 25]
```

---

## **6. Dictionary bo‘yicha for loop**

* Dictionary iterable bo‘lib, **key yoki value bo‘yicha** takrorlanadi:

```python
person = {"name": "Alice", "age": 25}

# Keys bo‘yicha
for key in person:
    print(key, person[key])

# Items bo‘yicha
for key, value in person.items():
    print(key, ":", value)
```

**Natija:**

```
name Alice
age 25
name : Alice
age : 25
```

---

## **7. Nested for loop**

* For loop ichida yana for loop yozish mumkin:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
```

**Natija:**

```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3
```

---

## **8. for loop va else**

* **else block** for loop **normal tugaganda** bajariladi (break ishlatilmasa):

```python
for i in range(3):
    print(i)
else:
    print("Loop tugadi")
```

**Natija:**

```
0
1
2
Loop tugadi
```

* Agar loop **break bilan to‘xtatilsa**, else bajarilmaydi:

```python
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop tugadi")
```

**Natija:**

```
0
```

---

## **9. Amaliy misol: listdagi musbat sonlar yig‘indisi**

```python
numbers = [3, -1, 7, -5, 2]
total = 0

for n in numbers:
    if n > 0:
        total += n

print(f"Musbat sonlar yig‘indisi: {total}")
```

**Natija:**

```
Musbat sonlar yig‘indisi: 12
```

---
# **Python’da while Loops**

## **1. while loop nima?**

* **while loop** — bu **shart True bo‘lganda kod blokini takroriy bajarish** usuli.
* Sintaksis:

```python
while shart:
    # shart True bo‘lsa bajariladigan kod
    print("Shart True")
```

> 🔑 Shart False bo‘lganda loop to‘xtaydi.

---

## **2. Oddiy misol**

```python
count = 0

while count < 5:
    print("Count:", count)
    count += 1
```

**Natija:**

```
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
```

* `count += 1` bo‘lmasa, **infinite loop** hosil bo‘ladi.

---

## **3. while loop va break**

* **break** — loopni **darhol to‘xtatish** uchun ishlatiladi:

```python
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
```

**Natija:**

```
0
1
2
3
4
```

> 🔑 break ishlatilganda loop **darhol tugaydi**, else bajarilmaydi.

---

## **4. while loop va continue**

* **continue** — loopni **keyingi iteratsiyaga o‘tkazish**:

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

**Natija:**

```
1
2
4
5
```

> 🔑 i==3 bo‘lganda print bajarilmadi, lekin loop davom etdi.

---

## **5. while loop va else**

* **while else** — loop **normal tugaganda** else ishlaydi (break ishlatilmasa):

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop normal tugadi")
```

**Natija:**

```
0
1
2
Loop normal tugadi
```

* Agar break ishlatilsa, **else bajarilmaydi**:

```python
i = 0
while i < 3:
    if i == 1:
        break
    print(i)
    i += 1
else:
    print("Loop normal tugadi")
```

**Natija:**

```
0
```

---

## **6. Amaliy misol: foydalanuvchi son kiritish**

```python
while True:
    num = int(input("Musbat son kiriting: "))
    if num > 0:
        print(f"Siz musbat son kirdingiz: {num}")
        break
    else:
        print("Xato! Musbat son kiriting.")
```

* Loop **faqat musbat son kiritilganda** to‘xtaydi.

---

## **7. Nested while loops**

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```

**Natija:**

```
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
i=3, j=1
i=3, j=2
```

---
# **Python’da Loop Control Statements**

Python’da loopni boshqarish uchun 3 asosiy statement mavjud:

1. **break** — loopni darhol to‘xtatadi
2. **continue** — loopni keyingi iteratsiyaga o‘tkazadi
3. **pass** — loopda hech narsa qilmasdan o‘tadi (placeholder)

---

## **1. break**

* **break** — loopni **darhol to‘xtatish** uchun ishlatiladi, else blok ishlamaydi.

### Misol: 1 dan 10 gacha bo‘lgan sonlarni chop etish, lekin 5 ga yetganda to‘xtatish

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

**Natija:**

```
1
2
3
4
```

* **while loop bilan:**

```python
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1
```

**Natija:**

```
1
2
3
4
5
6
```

---

## **2. continue**

* **continue** — loopni **shu iteratsiyani tashlab keyingisiga o‘tkazadi**.

### Misol: 1 dan 5 gacha bo‘lgan sonlarni chop etish, 3 ni tashlab

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Natija:**

```
1
2
4
5
```

* **while loop bilan:**

```python
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)
```

**Natija:**

```
1
3
4
5
```

> 🔑 i == 2 bo‘lganda print bajarilmadi, lekin loop davom etdi.

---

## **3. pass**

* **pass** — loop ichida hech narsa qilmasdan o‘tish uchun ishlatiladi.
* Asosan **placeholder** sifatida ishlatiladi: keyinchalik kod yoziladi.

### Misol:

```python
for i in range(5):
    if i % 2 == 0:
        pass  # keyinchalik ishlov beriladi
    else:
        print(i)
```

**Natija:**

```
1
3
```

* **while loop bilan:**

```python
i = 0
while i < 3:
    i += 1
    pass  # hech narsa qilmaydi
```

* Bu kod **infinite loop bo‘lmaydi**, chunki i oshiriladi.

---

## **4. break, continue va pass birlashtirilgan misol**

```python
for i in range(1, 10):
    if i == 3:
        continue  # 3 ni tashlab o'tadi
    elif i == 7:
        break     # 7 ga yetganda to‘xtaydi
    else:
        pass      # boshqa holatlarda hech narsa qilmaydi
    print(i)
```

**Natija:**

```
1
2
4
5
6
```

* 3 tashlandi (`continue`)
* 7 ga yetganda loop to‘xtadi (`break`)
* pass boshqa holatlarda ishladi, lekin hech narsa qilmaydi.

---

## **5. Xulosa**

1. **break** — loopni darhol to‘xtatadi, else bajarilmaydi
2. **continue** — hozirgi iteratsiyani tashlab keyingisiga o‘tkazadi
3. **pass** — hech narsa qilmaydi, placeholder sifatida ishlatiladi
4. Bu statements **for va while loop**larda ishlaydi
5. **Real misollar:**

   * break → foydalanuvchi to‘g‘ri ma’lumot kiritganda loopni to‘xtatish
   * continue → ma’lum holatdagi elementlarni tashlab o‘tish
   * pass → kodni keyinroq to‘ldirish yoki bo‘sh loop yaratish

---
# **Python’da Nested Loops (Ichma-ich looplar)**

## **1. Nested loop nima?**

* **Nested loop** — bu **loop ichida boshqa loop yozish**.
* Maqsad: **murakkab iteratsiyalar**, masalan, 2D array, ko‘p o‘lchamli strukturalar, kombinatsiyalarni yaratish.

Sintaksis:

```python
for outer in iterable1:
    for inner in iterable2:
        # outer va inner bilan bajariladigan kod
        print(outer, inner)
```

> 🔑 Ichki loop **tashqi loop har bir iteratsiyasida ishlaydi**.

---

## **2. Oddiy misol: ikki list kombinatsiyasi**

```python
colors = ["red", "green"]
fruits = ["apple", "banana"]

for color in colors:
    for fruit in fruits:
        print(f"{color} {fruit}")
```

**Natija:**

```
red apple
red banana
green apple
green banana
```

* Tashqi loop har bir rang uchun ichki loopni to‘liq ishlaydi.

---

## **3. Tuple ichida nested loop**

```python
pairs = [(1, 2), (3, 4)]

for x, y in pairs:
    for i in range(x):
        for j in range(y):
            print(f"x={x}, y={y}, i={i}, j={j}")
```

**Natija:**

```
x=1, y=2, i=0, j=0
x=1, y=2, i=0, j=1
x=3, y=4, i=0, j=0
x=3, y=4, i=0, j=1
x=3, y=4, i=0, j=2
x=3, y=4, i=1, j=0
x=3, y=4, i=1, j=1
...
```

* Ichki looplar **har bir tashqi iteratsiya uchun** qayta ishlaydi.

---

## **4. while loop ichida while loop**

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```

**Natija:**

```
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
i=3, j=1
i=3, j=2
```

---

## **5. Nested loop bilan amaliy misol: Multiplication table**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

**Natija:**

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

* Bu **ko‘p o‘lchamli iteratsiya**ning oddiy misoli.

---

## **6. break va continue bilan nested loop**

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue  # j=2 bo‘lganda skip
        if i == 3 and j == 1:
            break     # i=3 va j=1 bo‘lganda inner loopni to‘xtat
        print(f"i={i}, j={j}")
```

**Natija:**

```
i=1, j=1
i=1, j=3
i=2, j=1
i=2, j=3
i=3, j=3
```

* `continue` → j=2 tashlandi
* `break` → i=3, j=1 bo‘lganda inner loop to‘xtadi

---

## **7. Nested loop bilan list comprehension**

```python
numbers = [1, 2, 3]
letters = ["a", "b"]

combinations = [(n, l) for n in numbers for l in letters]
print(combinations)
```

**Natija:**

```
[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

* Nested loop **yangi kombinatsiyalar yaratish**da foydali.

---

## **8. Xulosa**

1. **Nested loops** — loop ichida boshqa loop.
2. Tashqi loop **har bir iteratsiya uchun ichki loopni** to‘liq ishlatadi.
3. **for va while** har ikkisi ichma-ich ishlatilishi mumkin.
4. **break va continue** nested looplarda ham ishlaydi, lekin **faqat shu loopga ta’sir qiladi**.
5. List comprehension va tuple/list kombinatsiyalarini yaratishda juda qulay.
6. **Real misollar:** multiplication table, 2D array ishlovi, kombinatsiyalar, chess board yaratish.

---
# **Python’da Loop else Clause**

## **1. Loop else nima?**

* **Loop else** — bu **loop normal tugaganda bajariladigan kod bloki**.
* Agar loop **break bilan to‘xtatilsa**, else bloki ishlamaydi.
* Sintaksis:

```python
for element in iterable:
    if shart:
        break
else:
    # loop normal tugasa bajariladi
    print("Loop to‘liq bajarildi")
```

* **while loop** uchun ham xuddi shunday ishlaydi:

```python
while shart:
    if shart2:
        break
else:
    print("Loop normal tugadi")
```

> 🔑 else blok **faqat loop oxiriga yetganda** bajariladi.

---

## **2. Oddiy misol: for loop else**

```python
for i in range(5):
    print(i)
else:
    print("Loop to‘liq bajarildi")
```

**Natija:**

```
0
1
2
3
4
Loop to‘liq bajarildi
```

* Hech break ishlatilmagani sababli else bajarildi.

---

## **3. for loop else + break**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop to‘liq bajarildi")
```

**Natija:**

```
0
1
2
```

* i==3 bo‘lganda break ishladi → **else bajarilmadi**

---

## **4. while loop else**

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop normal tugadi")
```

**Natija:**

```
0
1
2
Loop normal tugadi
```

* Loop shart False bo‘lganda else ishlaydi.

---

## **5. while loop else + break**

```python
i = 0
while i < 3:
    if i == 1:
        break
    print(i)
    i += 1
else:
    print("Loop normal tugadi")
```

**Natija:**

```
0
```

* i==1 bo‘lganda break ishladi → else bajarilmadi.

---

## **6. Amaliy misol: foydalanuvchi son tekshiruvi**

* Maqsad: foydalanuvchi musbat son kiritsa break bilan to‘xtatish, else agar **hech musbat son kiritilmasa**:

```python
numbers = [-3, -5, -2]

for num in numbers:
    if num > 0:
        print(f"Musbat son topildi: {num}")
        break
else:
    print("Musbat son topilmadi")
```

**Natija:**

```
Musbat son topilmadi
```

* Agar listda musbat son bo‘lsa, else bajarilmaydi.

---

## **7. Nested loop + else**

```python
for i in range(1, 4):
    for j in range(1, 4):
        if i*j == 4:
            break
    else:
        continue  # ichki loop break bo‘lmasa tashqi loop davom etadi
    break  # ichki loop break bo‘lganda tashqi loop ham to‘xtaydi

print("Loop tugadi")
```

* Nested loop else **ichki loop break bo‘lmasa** ishlaydi.

---

## **8. Xulosa**

1. **Loop else** — loop normal tugaganda bajariladi.
2. Agar loop **break bilan to‘xtatilsa**, else ishlamaydi.
3. For va while looplarda ishlaydi.
4. Foydasi: **loopda ma’lum shart topilmaganini tekshirish** (masalan, musbat son, element mavjudligi).
5. Nested looplarda else ichki loopni tekshirish uchun ishlatiladi.

---
# **Python’da Common Loop Patterns (Odatdagi loop naqshlari)**

Python’da looplar ko‘pincha **ma’lum naqshlar** bo‘yicha ishlatiladi. Quyida eng ko‘p ishlatiladigan patternlar va misollarini ko‘rib chiqamiz.

---

## **1. Traversal (Elementlarni birma-bir o‘tkazish)**

* Iterable elementlarini **birma-bir tekshirish**.
* Ko‘p ishlatiladi: list, tuple, string, dictionary.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")
```

**Natija:**

```
I like apple
I like banana
I like cherry
```

* String bo‘yicha:

```python
word = "Python"
for letter in word:
    print(letter)
```

---

## **2. Index orqali traversal**

* **range()** bilan **index bo‘yicha** elementlarga murojaat qilish:

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
```

**Natija:**

```
Index 0: apple
Index 1: banana
Index 2: cherry
```

---

## **3. Accumulator Pattern (Yig‘ish naqshi)**

* Sonlarni yig‘ish, mahsulotni hisoblash.

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for n in numbers:
    total += n

print("Yig‘indisi:", total)
```

**Natija:**

```
Yig‘indisi: 15
```

---

## **4. Filtering Pattern (Filtrlash naqshi)**

* Ma’lum shartga mos elementlarni ajratish:

```python
numbers = [1, -2, 3, -4, 5]
positives = []

for n in numbers:
    if n > 0:
        positives.append(n)

print(positives)
```

**Natija:**

```
[1, 3, 5]
```

* **List comprehension bilan:**

```python
positives = [n for n in numbers if n > 0]
```

---

## **5. Search Pattern (Qidiruv naqshi)**

* Loop ichida shart topilganda break ishlatish:

```python
numbers = [1, 2, 3, 4, 5]
target = 3

for n in numbers:
    if n == target:
        print("Topildi:", n)
        break
else:
    print("Topilmadi")
```

**Natija:**

```
Topildi: 3
```

* else ishlatilsa, topilmasa xabar beradi.

---

## **6. Enumeration Pattern (Index + element)**

* `enumerate()` yordamida **index va element** bir vaqtda olinadi:

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
```

**Natija:**

```
1 apple
2 banana
3 cherry
```

---

## **7. Nested Loop Pattern (Ichma-ich loop)**

* 2D strukturalar uchun ishlatiladi:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
```

**Natija:**

```
1 2 3 
4 5 6 
7 8 9
```

---

## **8. Loop with Conditionals Pattern (Shart bilan loop)**

* Ma’lum shartga qarab ishlash:

```python
numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n % 2 == 0:
        print(n, "juft")
    else:
        print(n, "toq")
```

**Natija:**

```
1 toq
2 juft
3 toq
4 juft
5 toq
```

---

## **9. Loop Reversal Pattern (Teskari iteratsiya)**

* List yoki range bo‘yicha teskari yurish:

```python
numbers = [1, 2, 3, 4, 5]

for n in reversed(numbers):
    print(n)
```

**Natija:**

```
5
4
3
2
1
```

* range bilan:

```python
for i in range(5, 0, -1):
    print(i)
```

---

## **10. Xulosa**

1. **Traversal** — iterable elementlarini tekshirish
2. **Index orqali traversal** — elementlarni index bo‘yicha olish
3. **Accumulator** — yig‘ish, ko‘paytirish
4. **Filtering** — ma’lum shartga mos elementlarni ajratish
5. **Search** — ma’lum elementni qidirish (break bilan)
6. **Enumeration** — index + element
7. **Nested Loop** — 2D yoki murakkab strukturani ishlash
8. **Conditional Loop** — shart bilan elementni ishlash
9. **Reversal** — teskari iteratsiya

> 🔑 Bu naqshlar **real hayotdagi Python kodlari**da eng ko‘p ishlatiladi.

---
# **Python’da Avoiding Infinite Loops (Cheksiz looplardan qochish)**

## **1. Infinite loop nima?**

* **Infinite loop** — bu loop **hech qachon tugamaydigan holat**.
* Sababi: loop sharti **doim True** bo‘lib qoladi yoki **increment/decrement** ishlatilmaydi.

### Oddiy misol:

```python
i = 0
while i < 5:
    print("Hello")  # i oshirilmayapti → loop cheksiz davom etadi
```

> 🔑 Bu **console’ni to‘sib qo‘yishi yoki dastur ishlashini to‘xtatmasligi** mumkin.

---

## **2. Infinite loop sabablari**

1. **Shartni o‘zgartirmaslik**:

```python
while True:
    print("Loop cheksiz")
```

2. **Counter (son hisoblagich) oshirilmaydi / kamaytirilmaydi**:

```python
i = 0
while i < 5:
    print(i)
    # i += 1 yo‘q → cheksiz loop
```

3. **Break ishlatilmaydi** va shart doim True:

```python
while True:
    # hech qanday break yo‘q → cheksiz loop
    pass
```

---

## **3. Cheksiz looplarni oldini olish usullari**

### **a) Counter bilan shartni boshqarish**

```python
i = 0
while i < 5:
    print(i)
    i += 1  # counterni oshirish shart
```

**Natija:**

```
0
1
2
3
4
```

---

### **b) break statement bilan boshqarish**

```python
while True:
    n = int(input("Musbat son kiriting: "))
    if n > 0:
        print("Rahmat!")
        break  # loopni tugatish
```

* `break` bo‘lmasa, `while True` → cheksiz loop.

---

### **c) shartni to‘g‘ri yozish**

* Loops uchun **shartni aniq va o‘zgartiriladigan** qilganingizga ishonch hosil qiling:

```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1  # har iteratsiyada count oshadi
```

---

### **d) Input/validation bilan loop**

```python
while True:
    password = input("Parol kiriting (kamida 6 ta belgi): ")
    if len(password) >= 6:
        print("Parol qabul qilindi")
        break
```

* Input shart bajarilguncha loop davom etadi → xavfsiz va cheksiz bo‘lmaydi.

---

### **e) Timeout / max attempts qo‘llash**

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Parol kiriting: ")
    if password == "1234":
        print("Xush kelibsiz!")
        break
    attempts += 1
else:
    print("Urinishlar tugadi, tizim bloklandi")
```

* Bu usul **infinite loopni oldini olishning eng yaxshi amaliyoti**.

---

### **f) for loop bilan xavfsiz iteratsiya**

* For loop odatda **range()** yoki iterable bilan ishlatiladi → cheksiz bo‘lmaydi:

```python
for i in range(5):
    print(i)  # faqat 0 dan 4 gacha ishlaydi
```

> 🔑 while loopda esa **shart va increment**ga e’tibor berish kerak.

---

## **4. Nested loops va infinite loop xavfi**

* Nested while yoki for looplarda ham **har bir loopning sharti to‘g‘ri** bo‘lishi kerak:

```python
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(i, j)
        j += 1  # ichki loop counterni oshirish shart
    i += 1  # tashqi loop counterni oshirish shart
```

* Agar `i += 1` yoki `j += 1` yo‘q bo‘lsa → cheksiz loop bo‘ladi.

---

## **5. Xulosa / Tips**

1. **While loop** ishlatishda shart **oxirida False bo‘lishini tekshiring**.
2. **Break** orqali loopni xavfsiz tugating.
3. **Counter yoki increment** — har iteratsiyada loop shartini o‘zgartirish zarur.
4. **Max attempts** — foydalanuvchi input looplarini xavfsiz qilish.
5. **For loop** odatda xavfsiz, chunki range yoki iterable **cheklangan**.
6. **Nested looplarda** har bir loop counter yoki shartini to‘g‘ri boshqaring.

> 🔑 Cheksiz looplar dastur ishini to‘xtatishi yoki resurslarni egallashi mumkin, shuning uchun **shart va boshqaruv elementlarini aniqlik bilan yozish** juda muhim.

---