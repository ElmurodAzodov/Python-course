
# **STAGE 4 — Control Flow & Logic**
---

# **Python’da Boolean Expressions**

## **1. Boolean nima?**

* **Boolean** — bu **mantiqiy tip** (`bool`) bo‘lib, qiymatlari faqat **`True`** yoki **`False`** bo‘ladi.
* Python’da `True` va `False` katta harf bilan yoziladi.

```python
a = True
b = False
print(type(a))  # <class 'bool'>
```

---

## **2. Boolean Expressions nima?**

**Boolean expression** — bu **mantiqiy qiymat qaytaradigan ifoda**.

* Misol: `5 > 3`
* Natija: `True`

```python
print(5 > 3)   # True
print(2 == 2)  # True
print(4 < 1)   # False
```

> 🔑 Har qanday ifoda, natijasi **`True` yoki `False` bo‘lsa**, boolean expression hisoblanadi.

---

## **3. Solishtirish operatorlari (Comparison Operators)**

| Operator | Ma’nosi          | Misol           |
| -------- | ---------------- | --------------- |
| `==`     | Tengmi?          | `5 == 5` → True |
| `!=`     | Teng emasmi?     | `5 != 3` → True |
| `>`      | Katta            | `5 > 3` → True  |
| `<`      | Kichik           | `2 < 1` → False |
| `>=`     | Katta yoki teng  | `3 >= 3` → True |
| `<=`     | Kichik yoki teng | `2 <= 5` → True |

---

## **4. Mantiqiy operatorlar (Logical Operators)**

| Operator | Ma’nosi | Misol                    |
| -------- | ------- | ------------------------ |
| `and`    | va      | `True and False` → False |
| `or`     | yoki    | `True or False` → True   |
| `not`    | inkor   | `not True` → False       |

**Misol:**

```python
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

---

## **5. Boolean Expressions bilan ishlash misollari**

```python
x = 10
y = 5

# 1. Solishtirish
print(x > y)   # True
print(x == y)  # False

# 2. Mantiqiy operatorlar
print((x > y) and (y > 0))  # True
print((x < y) or (y == 5))  # True
print(not(x == 10))         # False

# 3. Murakkab boolean expression
age = 25
has_ticket = True
can_enter = (age >= 18) and has_ticket
print(can_enter)  # True
```

---

## **6. Booleans va shart operatorlari**

* Boolean expressions **if** statement bilan birga ishlatiladi:

```python
x = 15
if x > 10:
    print("x 10 dan katta")
else:
    print("x 10 dan kichik yoki teng")
```

**Natija:**

```
x 10 dan katta
```

> 🔑 Har qanday boolean expression **`if`**, **`while`**, yoki **`assert`** bilan ishlaydi.

---
# **Python’da Truthy va Falsy Values**

## **1. Truthy va Falsy nima?**

* Python’da **har qanday obyekt** Boolean kontekstida (`if`, `while`, `bool()`) ishlatilganda **`True` yoki `False`** qiymatga aylanadi.
* **Truthy** — Boolean kontekstida **`True`** deb hisoblanadigan qiymatlar.
* **Falsy** — Boolean kontekstida **`False`** deb hisoblanadigan qiymatlar.

---

## **2. Falsy qiymatlar**

Python’da quyidagi qiymatlar **False** hisoblanadi:

| Qiymat                | Misol                           |
| --------------------- | ------------------------------- |
| `None`                | `x = None`                      |
| `False`               | `x = False`                     |
| 0 (int)               | `x = 0`                         |
| 0.0 (float)           | `x = 0.0`                       |
| 0j (complex)          | `x = 0j`                        |
| Bo‘sh ketma-ketliklar | `[]`, `()`, `{}`, `set()`, `""` |

**Misol:**

```python
values = [None, False, 0, 0.0, 0j, "", [], {}, set()]

for v in values:
    if v:
        print(f"{v} is Truthy")
    else:
        print(f"{v} is Falsy")
```

**Natija:**

```
None is Falsy
False is Falsy
0 is Falsy
0.0 is Falsy
0j is Falsy
 is Falsy
[] is Falsy
{} is Falsy
set() is Falsy
```

---

## **3. Truthy qiymatlar**

Python’da **boshqa barcha obyektlar** **True** hisoblanadi, masalan:

* Ijobiy sonlar: `1`, `3.14`
* Manfiy sonlar: `-1`, `-2.5`
* To‘ldirilgan ketma-ketliklar: `[1,2]`, `"Python"`, `(1,)`, `{1: "a"}`, `{1,2}`
* Ob’ektlar (`object()`)

**Misol:**

```python
values = [1, -1, 3.14, "Python", [0], (1,), {1:"a"}, {1,2}, object()]

for v in values:
    if v:
        print(f"{v} is Truthy")
    else:
        print(f"{v} is Falsy")
```

**Natija:**

```
1 is Truthy
-1 is Truthy
3.14 is Truthy
Python is Truthy
[0] is Truthy
(1,) is Truthy
{1: 'a'} is Truthy
{1, 2} is Truthy
<some object> is Truthy
```

---

## **4. Boolean kontekstida ishlatish**

* `if`, `while` va `bool()` har doim **Truthy/Falsy** qiymatni tekshiradi:

```python
x = []

if x:
    print("x is Truthy")
else:
    print("x is Falsy")
```

**Natija:**

```
x is Falsy
```

```python
y = [1,2,3]

if y:
    print("y is Truthy")
```

**Natija:**

```
y is Truthy
```

---

## **5. Foydali amaliy misol: foydalanuvchi kiritgan matn**

```python
user_input = input("Enter something: ")

if user_input:
    print(f"You entered: {user_input}")
else:
    print("You entered nothing!")
```

* Bo‘sh matn: `""` → Falsy
* Noto‘la bo‘sh matn: `Hello` → Truthy

---

## **6. Xulosa**

1. **Falsy** qiymatlar: `None`, `False`, `0`, `0.0`, `0j`, bo‘sh ketma-ketliklar (`[]`, `()`, `{}`, `""`, `set()`)
2. **Truthy** qiymatlar: qolgan barcha obyektlar
3. Boolean kontekstida (`if`, `while`, `bool()`) **har qanday obyekt** True/False sifatida ishlaydi
4. Truthy/Falsy tushunchasi **shart operatorlari va mantiqiy ifodalarni** to‘g‘ri ishlatish uchun muhim

---
# **Python’da if Statements**

## **1. if statement nima?**

* **if statement** — bu **shart bajarilsa kod blokini ishga tushirish** usuli.
* Sintaksis:

```python
if shart:
    # shart True bo'lsa bajariladigan kod
    print("Shart to'g'ri")
```

> 🔑 Python’da **blok ichidagi kodni** har doim **indentation (4 bo‘shliq yoki tab)** bilan yozish kerak.

---

## **2. Oddiy misol**

```python
x = 10

if x > 5:
    print("x 5 dan katta")
```

**Natija:**

```
x 5 dan katta
```

* Agar `x > 5` **False** bo‘lsa, kod bajarilmaydi.

---

## **3. else bilan ishlatish**

* Agar shart **False** bo‘lsa, **else** bloki ishlatiladi:

```python
x = 3

if x > 5:
    print("x 5 dan katta")
else:
    print("x 5 dan kichik yoki teng")
```

**Natija:**

```
x 5 dan kichik yoki teng
```

---

## **4. elif (else if) bilan ishlatish**

* Bir nechta shartni tekshirish uchun **elif** ishlatiladi:

```python
x = 7

if x > 10:
    print("x 10 dan katta")
elif x > 5:
    print("x 5 dan katta, 10 dan kichik yoki teng")
else:
    print("x 5 dan kichik yoki teng")
```

**Natija:**

```
x 5 dan katta, 10 dan kichik yoki teng
```

> 🔑 `elif` shartlari yuqoridan pastga qarab tekshiriladi. Birinchi True bo‘lgan shart bajariladi va qolganlari e’tiborga olinmaydi.

---

## **5. Nested if (Ichma-ich shartlar)**

* Kod ichida yana `if` yozish mumkin:

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Siz kinoga kira olasiz")
    else:
        print("Sizga chipta kerak")
else:
    print("Siz kichik yoshda, kino uchun ruxsat yo'q")
```

**Natija:**

```
Siz kinoga kira olasiz
```

---

## **6. Boolean expressions va if statement**

* Har qanday **Boolean expression** if statement sharti sifatida ishlaydi:

```python
x = 10
y = 5

if x > y and y > 0:
    print("Ikki shart ham True")
```

**Natija:**

```
Ikki shart ham True
```

* **Truthy/Falsy** qiymatlar ham ishlatiladi:

```python
my_list = [1,2,3]

if my_list:  # Bo'sh emas → True
    print("Ro'yxat bo'sh emas")
```

**Natija:**

```
Ro'yxat bo'sh emas
```

---

## **7. Amaliy misol: foydalanuvchi yoshini tekshirish**

```python
age = int(input("Yoshingizni kiriting: "))

if age < 0:
    print("Xato! Yoshingiz manfiy bo'lishi mumkin emas")
elif age < 18:
    print("Siz kichik yoshda, kirish mumkin emas")
elif age <= 65:
    print("Siz kirishingiz mumkin")
else:
    print("Siz kattalar uchun maxsus chegirma olasiz")
```

* Bu misol **if → elif → else** zanjirini ko‘rsatadi.

---
# **Python’da elif Chains**

## **1. elif nima?**

* **elif** — bu “else if” degan ma’noni beradi.
* **Bir nechta shartlarni tekshirish** imkonini beradi.
* Foydasi: bir nechta shartni **bitta if → elif → else zanjiri** orqali tartib bilan tekshirish.

Sintaksis:

```python
if shart1:
    # shart1 True bo'lsa bajariladi
    kod1
elif shart2:
    # shart1 False va shart2 True bo'lsa bajariladi
    kod2
elif shart3:
    # shart1 va shart2 False va shart3 True bo'lsa bajariladi
    kod3
else:
    # hammasi False bo'lsa bajariladi
    kod_else
```

> 🔑 Python’da **elif zanjiri yuqoridan pastga qarab tekshiriladi**. Birinchi True bo‘lgan shart bajariladi va qolganlari e’tiborga olinmaydi.

---

## **2. Oddiy misol**

```python
x = 15

if x > 20:
    print("x 20 dan katta")
elif x > 10:
    print("x 10 dan katta, 20 dan kichik yoki teng")
elif x > 5:
    print("x 5 dan katta, 10 dan kichik yoki teng")
else:
    print("x 5 dan kichik yoki teng")
```

**Natija:**

```
x 10 dan katta, 20 dan kichik yoki teng
```

> 🔑 `x > 10` sharti True bo‘lganligi sababli, **qolgan eliflar tekshirilmaydi**.

---

## **3. Nested elif Chains**

* Ichma-ich shartlar bilan birlashtirish mumkin:

```python
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Siz kinoga kira olasiz")
    elif not has_ticket:
        print("Sizga chipta kerak")
else:
    print("Siz kichik yoshda, kino uchun ruxsat yo'q")
```

**Natija:**

```
Siz kinoga kira olasiz
```

---

## **4. Foydali misol: bahoni tekshirish**

```python
score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Ball: {score}, Bahosi: {grade}")
```

**Natija:**

```
Ball: 78, Bahosi: C
```

> 🔑 Ball 78, shuning uchun birinchi mos keladigan shart (`score >= 70`) bajariladi.

---

## **5. Boolean expressions bilan ishlash**

* `elif` zanjirida **mantiqiy operatorlar** va **Truthy/Falsy** qiymatlar ishlatilishi mumkin:

```python
x = 10
y = 5

if x > y and y > 0:
    print("Ikki shart ham True")
elif x > 0 or y < 0:
    print("Kamida bitta shart True")
else:
    print("Hech narsa True emas")
```

**Natija:**

```
Ikki shart ham True
```

---
# **Python’da else Blocks**

## **1. else block nima?**

* **else block** — bu **if/elif shartlari False bo‘lganda bajariladigan kod bloki**.
* Syntax:

```python
if shart1:
    # shart1 True bo'lsa bajariladi
    kod1
elif shart2:
    # shart2 True bo'lsa bajariladi
    kod2
else:
    # hammasi False bo'lsa bajariladi
    kod_else
```

> 🔑 Python’da **else** **shartni tekshirmaydi**, faqat oldingi shartlar False bo‘lganda ishlaydi.

---

## **2. Oddiy misol**

```python
x = 3

if x > 5:
    print("x 5 dan katta")
else:
    print("x 5 dan kichik yoki teng")
```

**Natija:**

```
x 5 dan kichik yoki teng
```

* `x > 5` False bo‘lgani sababli, **else** ichidagi kod bajarildi.

---

## **3. if → else bilan ishlash**

* Faqat **if** va **else** bo‘lishi mumkin:

```python
age = 17

if age >= 18:
    print("Siz kirishingiz mumkin")
else:
    print("Siz kichik yoshda, kirish mumkin emas")
```

**Natija:**

```
Siz kichik yoshda, kirish mumkin emas
```

---

## **4. if → elif → else bilan ishlash**

```python
score = 72

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Ball: {score}, Bahosi: {grade}")
```

**Natija:**

```
Ball: 72, Bahosi: C
```

* Agar ball 70-79 bo‘lmasa, else **F** bahoni beradi.

---

## **5. Nested else (Ichma-ich else)**

```python
age = 20
has_ticket = False

if age >= 18:
    if has_ticket:
        print("Siz kinoga kira olasiz")
    else:
        print("Sizga chipta kerak")
else:
    print("Siz kichik yoshda, kino uchun ruxsat yo'q")
```

**Natija:**

```
Sizga chipta kerak
```

> 🔑 Nested else — ichki shart False bo‘lganda bajariladi.

---

## **6. Boolean expressions bilan ishlash**

```python
x = 0

if x:
    print("x Truthy")
else:
    print("x Falsy")
```

**Natija:**

```
x Falsy
```

* Bo‘sh list, `0`, `""`, `None` kabi Falsy qiymatlar else blokini ishga tushiradi.

---

## **7. Foydali amaliy misol: foydalanuvchi kiritgan son**

```python
num = int(input("Son kiriting: "))

if num > 0:
    print("Musbat son")
elif num < 0:
    print("Manfiy son")
else:
    print("Son nolga teng")
```

* `else` bu yerda **num == 0** holatini qamrab oladi.

---
# **Python’da Nested Conditions (Ichma-ich shartlar)**

## **1. Nested condition nima?**

* **Nested condition** — bu **if yoki elif ichida yana if/elif/else yozish**.
* Maqsad: **bir shart bajarilganda boshqa shartlarni tekshirish**.

Sintaksis:

```python
if shart1:
    if shart2:
        # shart1 va shart2 True bo‘lsa bajariladi
        kod1
    else:
        # shart1 True, shart2 False
        kod2
else:
    # shart1 False bo‘lsa
    kod3
```

> 🔑 Python’da **indentation** juda muhim. Ichki if **tashqi if blokiga kiradi**.

---

## **2. Oddiy misol**

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Siz kinoga kira olasiz")
    else:
        print("Sizga chipta kerak")
else:
    print("Siz kichik yoshda, kino uchun ruxsat yo'q")
```

**Natija:**

```
Siz kinoga kira olasiz
```

* Tashqi shart (`age >= 18`) True
* Ichki shart (`has_ticket`) True → ichki blok ishlaydi

---

## **3. Nested elif chains**

```python
score = 85

if score >= 90:
    print("Bahosi: A")
elif score >= 75:
    if score >= 80:
        print("Bahosi: B+")
    else:
        print("Bahosi: B")
else:
    print("Bahosi: C yoki past")
```

**Natija:**

```
Bahosi: B+
```

> 🔑 Ichki if yordamida **bir shartni yanada nozik tekshirish** mumkin.

---

## **4. Multiple nested conditions**

```python
x = 10
y = 5
z = -1

if x > 0:
    if y > 0:
        if z > 0:
            print("Hammasi musbat")
        else:
            print("z manfiy yoki nol")
    else:
        print("y manfiy yoki nol")
else:
    print("x manfiy yoki nol")
```

**Natija:**

```
z manfiy yoki nol
```

---

## **5. Boolean expressions bilan nested if**

```python
user_logged_in = True
has_permission = False

if user_logged_in:
    if has_permission:
        print("Siz ma’lumotlarni o‘zgartira olasiz")
    else:
        print("Sizda ruxsat yo‘q")
else:
    print("Login qiling")
```

**Natija:**

```
Sizda ruxsat yo‘q
```

---

## **6. Foydali amaliy misol: foydalanuvchi kirish tizimi**

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "1234":
        print("Xush kelibsiz, admin!")
    else:
        print("Parol noto‘g‘ri")
else:
    print("Foydalanuvchi topilmadi")
```

* Nested conditions yordamida **tashqi shart (username)** va **ichki shart (password)** alohida tekshiriladi.

---
# **Python’da match / case (Structural Pattern Matching)**

## **1. match / case nima?**

* **match / case** — bu **Python 3.10+** versiyada paydo bo‘lgan yangi **control flow** konstruktsiyasi.
* Maqsad: **biror qiymat yoki obyekt strukturasi bo‘yicha turli hollarni tekshirish**.
* Sintaksis **switch-case** ga o‘xshaydi, lekin **Python’dagi pattern matching** ko‘proq quvvatli.

```python
match expression:
    case pattern1:
        # pattern1 mos kelsa bajariladi
    case pattern2:
        # pattern2 mos kelsa bajariladi
    case _:
        # hech narsa mos kelmasa bajariladi (default)
```

> 🔑 `_` — bu **wildcard**, ya’ni default case.

---

## **2. Oddiy misol (qiymat bo‘yicha tekshirish)**

```python
day = "Monday"

match day:
    case "Monday":
        print("Bugun Dushanba")
    case "Tuesday":
        print("Bugun Seshanba")
    case _:
        print("Bugun boshqa kun")
```

**Natija:**

```
Bugun Dushanba
```

> 🔑 `day` qiymati `"Monday"` ga mos kelgani sababli, birinchi case ishladi.

---

## **3. Bir nechta qiymatlarni tekshirish (OR operator)**

```python
grade = "B"

match grade:
    case "A" | "B":
        print("A'lo va Yaxshi")
    case "C":
        print("O‘rta")
    case "D" | "F":
        print("Qoniqarsiz")
```

**Natija:**

```
A'lo va Yaxshi
```

> 🔑 `|` operatori yordamida **bir nechta patternlarni birga tekshirish** mumkin.

---

## **4. Pattern matching bilan list va tuple**

```python
point = (0, 0)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y o‘qi: {y}")
    case (x, 0):
        print(f"X o‘qi: {x}")
    case (x, y):
        print(f"Point: x={x}, y={y}")
```

**Natija:**

```
Origin
```

* Tuple ichidagi qiymatlar **pattern orqali** ajratildi.
* `x` va `y` — bu **pattern variables** bo‘lib, keyin ishlatiladi.

---

## **5. Dictionary pattern matching**

```python
data = {"name": "Alice", "age": 25}

match data:
    case {"name": name, "age": age} if age >= 18:
        print(f"{name} kattalar")
    case {"name": name, "age": age}:
        print(f"{name} kichik yoshda")
```

**Natija:**

```
Alice kattalar
```

> 🔑 `if` bilan **case guard** qo‘shish mumkin: shart qo‘shimcha tekshiruv sifatida ishlaydi.

---

## **6. Nested match / case**

```python
point = (0, 5)

match point:
    case (0, y):
        print(f"Y o‘qi: {y}")
    case (x, 0):
        print(f"X o‘qi: {x}")
    case _:
        print("Boshqa nuqta")
```

**Natija:**

```
Y o‘qi: 5
```

* Nested structures (tuple ichida tuple) ham ishlaydi:

```python
nested = (0, (1, 2))

match nested:
    case (0, (a, b)):
        print(f"a={a}, b={b}")
```

**Natija:**

```
a=1, b=2
```

---

## **7. Foydali misol: foydalanuvchi roli tekshiruvi**

```python
user = {"role": "admin", "active": True}

match user:
    case {"role": "admin", "active": True}:
        print("Admin tizimga kirdi")
    case {"role": "user", "active": True}:
        print("Oddiy foydalanuvchi tizimga kirdi")
    case _:
        print("Foydalanuvchi faol emas")
```

**Natija:**

```
Admin tizimga kirdi
```

---
