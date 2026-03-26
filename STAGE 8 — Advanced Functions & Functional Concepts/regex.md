
# **Regular Expressions**

---

# 🔹 1. `re` nima?

`re` — bu Python moduli bo‘lib:

* matndan ma’lum pattern topadi
* validatsiya qiladi (email, telefon, parol)
* replace (almashtirish) qiladi

```python
import re
```

---

# 🔹 2. ENG ASOSIY FUNKSIYALAR

## ✅ `re.search()`

Matnda pattern bor yoki yo‘qligini tekshiradi

```python
text = "hello python"

result = re.search("python", text)

print(result)  # Match object yoki None
```

✔ Agar topsa → match
❌ topmasa → None

---

## ✅ `re.match()`

Faqat **string boshidan** tekshiradi

```python
re.match("hello", "hello world")  # ✔
re.match("world", "hello world")  # ❌
```

---

## ✅ `re.findall()`

Hammasini list qilib qaytaradi

```python
text = "cat dog cat"

print(re.findall("cat", text))
# ['cat', 'cat']
```

---

## ✅ `re.sub()`

Replace qilish

```python
text = "hello 123"

result = re.sub(r'\d', '*', text)

print(result)  # hello ***
```

---

## ✅ `re.split()`

Bo‘lish (split)

```python
text = "one,two;three"

print(re.split(r'[;,]', text))
# ['one', 'two', 'three']
```

---

# 🔹 3. REGEX BELGILARI (MUHIM!)

## 🔤 Harflar

| Pattern | Ma’nosi             |
| ------- | ------------------- |
| `a`     | aynan 'a'           |
| `.`     | istalgan 1 ta belgi |

---

## 🔢 Maxsus belgilar

| Pattern | Ma’nosi              |
| ------- | -------------------- |
| `\d`    | raqam (0-9)          |
| `\D`    | raqam emas           |
| `\w`    | harf + raqam + _     |
| `\W`    | yuqoridagidan boshqa |
| `\s`    | bo‘sh joy            |
| `\S`    | bo‘sh joy emas       |

---

## 🔁 Takrorlash

| Pattern | Ma’nosi       |
| ------- | ------------- |
| `+`     | 1 yoki ko‘p   |
| `*`     | 0 yoki ko‘p   |
| `?`     | 0 yoki 1      |
| `{3}`   | aynan 3 ta    |
| `{2,5}` | 2 dan 5 gacha |

```python
re.findall(r'\d+', "a12b345")
# ['12', '345']
```

---

## 🎯 To‘plamlar (sets)

```python
[abc]   # a yoki b yoki c
[a-z]   # kichik harflar
[A-Z]   # katta harflar
[0-9]   # raqamlar
```

```python
re.findall(r'[a-z]', "AbC1")
# ['b']
```

---

## 🚫 Inkori

```python
[^a-z]  # a-z dan boshqa hamma narsa
```

---

## 📍 Chegaralar

| Pattern | Ma’nosi  |
| ------- | -------- |
| `^`     | boshidan |
| `$`     | oxiridan |

```python
re.match(r'^hello', "hello world")  # ✔
re.search(r'world$', "hello world") # ✔
```

---

# 🔹 4. REAL MISOLLAR

## 📧 Email tekshirish

```python
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

email = "test@gmail.com"

print(bool(re.match(pattern, email)))
```

---

## 📱 Telefon tekshirish

```python
pattern = r'^\+?\d{9,15}$'

print(bool(re.match(pattern, "+998901234567")))
```

---

## 🔐 Parol tekshirish

```python
password = "Abc123!"

valid = (
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'\d', password) and
    re.search(r'[!@#$%]', password)
)

print(bool(valid))
```

---

## 🔍 Faqat harflar

```python
re.match(r'^[A-Za-z]+$', "Hello")  # True
```

---

# 🔹 5. GROUPLAR (Juda muhim 🔥)

```python
text = "my email is test@gmail.com"

match = re.search(r'(\w+)@(\w+\.\w+)', text)

print(match.group(1))  # username
print(match.group(2))  # domain
```

---

# 🔹 6. RAW STRING (r"")

```python
r'\d'
```

❗ Nega kerak:

* `\` bilan muammo bo‘lmaydi
* regex uchun DOIM ishlat

---

# 🔹 7. FLAGS (qo‘shimcha imkoniyat)

```python
re.search("hello", "HELLO", re.IGNORECASE)
```

---

# 🔥 QISQA XULOSA

`re` bilan siz:

* 🔍 qidirasiz (`search`)
* ✔ tekshirasiz (`match`)
* 📋 hammasini olasiz (`findall`)
* 🔁 almashtirasiz (`sub`)
* ✂ bo‘lasiz (`split`)

---