**ASCII jadvali** — bu kompyuterlar matnni tushunishi uchun harflar, raqamlar va belgilarni **raqamlar bilan ifodalovchi kodlash tizimi**.

ASCII — **American Standard Code for Information Interchange** degani.

---

## 🔢 ASCII qanday ishlaydi?

Kompyuter faqat **0 va 1 (binary)** ni tushunadi.
Shuning uchun har bir belgi (masalan, `A`, `a`, `1`, `@`) ga **raqam biriktirilgan**.

Masalan:

| Belgi             | ASCII kodi | Binary ko‘rinishi |
| ----------------- | ---------- | ----------------- |
| A                 | 65         | 01000001          |
| a                 | 97         | 01100001          |
| 0                 | 48         | 00110000          |
| !                 | 33         | 00100001          |
| Bo‘sh joy (space) | 32         | 00100000          |

---

## 📌 ASCII nechta belgidan iborat?

Standart ASCII — **0 dan 127 gacha** (jami 128 ta belgi)

Ular 2 ga bo‘linadi:

### 1️⃣ 0–31 → Boshqaruv belgilar

Masalan:

* 10 → New Line (`\n`)
* 9 → Tab (`\t`)

### 2️⃣ 32–127 → Ko‘rinadigan belgilar

* 32–47 → Belgilar (`! @ # $ %`)
* 48–57 → Raqamlar (`0–9`)
* 65–90 → Katta harflar (`A–Z`)
* 97–122 → Kichik harflar (`a–z`)

---

## 💻 Python’da ASCII

```python
print(ord('A'))   # 65
print(chr(65))    # A
```

* `ord()` → belgini raqamga aylantiradi
* `chr()` → raqamni belgiga aylantiradi

---

## 🎯 Oddiy qilib aytganda

ASCII — bu:

> "Har bir harf va belgining kompyuter tilidagi raqami"

Masalan:

* `A` = 65
* `B` = 66
* `a` = 97

Shuning uchun Python’da:

```python
print(ord('B') - ord('A'))  # 1
```

---
Quyida **0 dan 127 gacha to‘liq ASCII jadvali** berilgan.

> Eslatma: 0–31 va 127 — boshqaruv (ko‘rinmaydigan) belgilar.

---

## 🔹 0–31 (Boshqaruv belgilar)

| Dec | Belgi | Nomi                 |
| --- | ----- | -------------------- |
| 0   | NUL   | Null                 |
| 1   | SOH   | Start of Heading     |
| 2   | STX   | Start of Text        |
| 3   | ETX   | End of Text          |
| 4   | EOT   | End of Transmission  |
| 5   | ENQ   | Enquiry              |
| 6   | ACK   | Acknowledge          |
| 7   | BEL   | Bell                 |
| 8   | BS    | Backspace            |
| 9   | TAB   | Horizontal Tab       |
| 10  | LF    | Line Feed (\n)       |
| 11  | VT    | Vertical Tab         |
| 12  | FF    | Form Feed            |
| 13  | CR    | Carriage Return (\r) |
| 14  | SO    | Shift Out            |
| 15  | SI    | Shift In             |
| 16  | DLE   | Data Link Escape     |
| 17  | DC1   | Device Control 1     |
| 18  | DC2   | Device Control 2     |
| 19  | DC3   | Device Control 3     |
| 20  | DC4   | Device Control 4     |
| 21  | NAK   | Negative Acknowledge |
| 22  | SYN   | Synchronous Idle     |
| 23  | ETB   | End of Trans Block   |
| 24  | CAN   | Cancel               |
| 25  | EM    | End of Medium        |
| 26  | SUB   | Substitute           |
| 27  | ESC   | Escape               |
| 28  | FS    | File Separator       |
| 29  | GS    | Group Separator      |
| 30  | RS    | Record Separator     |
| 31  | US    | Unit Separator       |

---

## 🔹 32–47 (Belgilar)

| Dec | Belgi   |
| --- | ------- |
| 32  | (space) |
| 33  | !       |
| 34  | "       |
| 35  | #       |
| 36  | $       |
| 37  | %       |
| 38  | &       |
| 39  | '       |
| 40  | (       |
| 41  | )       |
| 42  | *       |
| 43  | +       |
| 44  | ,       |
| 45  | -       |
| 46  | .       |
| 47  | /       |

---

## 🔹 48–57 (Raqamlar)

| Dec | Belgi |
| --- | ----- |
| 48  | 0     |
| 49  | 1     |
| 50  | 2     |
| 51  | 3     |
| 52  | 4     |
| 53  | 5     |
| 54  | 6     |
| 55  | 7     |
| 56  | 8     |
| 57  | 9     |

---

## 🔹 58–64

| Dec | Belgi |
| --- | ----- |
| 58  | :     |
| 59  | ;     |
| 60  | <     |
| 61  | =     |
| 62  | >     |
| 63  | ?     |
| 64  | @     |

---

## 🔹 65–90 (Katta harflar)

| Dec | Belgi |
| --- | ----- |
| 65  | A     |
| 66  | B     |
| 67  | C     |
| 68  | D     |
| 69  | E     |
| 70  | F     |
| 71  | G     |
| 72  | H     |
| 73  | I     |
| 74  | J     |
| 75  | K     |
| 76  | L     |
| 77  | M     |
| 78  | N     |
| 79  | O     |
| 80  | P     |
| 81  | Q     |
| 82  | R     |
| 83  | S     |
| 84  | T     |
| 85  | U     |
| 86  | V     |
| 87  | W     |
| 88  | X     |
| 89  | Y     |
| 90  | Z     |

---

## 🔹 91–96

| Dec | Belgi |
| --- | ----- |
| 91  | [     |
| 92  | \     |
| 93  | ]     |
| 94  | ^     |
| 95  | _     |
| 96  | `     |

---

## 🔹 97–122 (Kichik harflar)

| Dec | Belgi |
| --- | ----- |
| 97  | a     |
| 98  | b     |
| 99  | c     |
| 100 | d     |
| 101 | e     |
| 102 | f     |
| 103 | g     |
| 104 | h     |
| 105 | i     |
| 106 | j     |
| 107 | k     |
| 108 | l     |
| 109 | m     |
| 110 | n     |
| 111 | o     |
| 112 | p     |
| 113 | q     |
| 114 | r     |
| 115 | s     |
| 116 | t     |
| 117 | u     |
| 118 | v     |
| 119 | w     |
| 120 | x     |
| 121 | y     |
| 122 | z     |

---

## 🔹 123–127

| Dec | Belgi |
| --- | ----- |
| 123 | {     |
| 124 | |     |
| 125 | }     |
| 126 | ~     |
| 127 | DEL   |

---