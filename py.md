# **THE COMPLETE PYTHON ROADMAP 2026**

### _Backend-Focused Edition | Core Python Only_

<div align="center">
  <img src="./py.png" width="200" alt="Python Logo">
  <br>
  <h3>🐍 Python Programming Language 🐍</h3>
  <p><strong>Version 3.9 → 3.13 | Backend Core Edition</strong></p>
  <br>
  <p><strong>Elmurod Azodov</strong></p>
  <p>@the_elmurod</p>
</div>

<br>

---

## 📑 **TABLE OF CONTENTS**

- [📘 THE COMPLETE PYTHON ROADMAP 2026](#-the-complete-python-roadmap-2026)
  - [From Zero to Backend Developer](#from-zero-to-backend-developer)
  - [📑 TABLE OF CONTENTS](#-table-of-contents)
  - [🎯 ROADMAP OVERVIEW](#-roadmap-overview)
    - [**Learning Path Summary**](#learning-path-summary)
    - [**📊 Time Distribution**](#-time-distribution)
  - [🎯 STAGE 0 — Programming & Python Foundations](#-stage-0--programming--python-foundations)
  - [🎯 STAGE 1 — Core Syntax & Expressions](#-stage-1--core-syntax--expressions)

---

## 🎯 ROADMAP OVERVIEW

### **Learning Path Summary**

| Level               | Stages | Time   | Outcome                             |
| ------------------- | ------ | ------ | ----------------------------------- |
| 🟢 **Beginner**     | 0-7    | 1.5 oy | Python sintaksisi, asosiy dasturlar |
| 🔵 **Intermediate** | 8-13   | 2 oy   | Funksiyalar, OOP, modullar          |
| 🟠 **Advanced**     | 14-17  | 2 oy   | Standart kutubxona, generatsiyalar  |
| 🔴 **Expert**       | 18-20  | 1.5 oy | Performans, konkurentlik            |

### **📊 Time Distribution**

```
Jami vaqt: 7 oy (28 hafta)
Haftalik yuklama: 10-12 soat
Jami soat: ~150 soat

Beginner    (0-7)   ██████████░░░░ 1.5 oy
Intermediate (8-13) ████████████░░ 2 oy
Advanced    (14-17) ████████████░░ 2 oy
Expert      (18-20) ████████░░░░░░ 1.5 oy
```

---

## 🎯 STAGE 0 — Programming & Python Foundations

**Goal**: Understand what programming and Python are before writing code.  
**Time**: 4 soat | 2 dars

#### 📚 Topics

- **⚙️ What Programming Is** (algorithms, problem solving)
- **🐍 What Python Is** (high-level, interpreted, dynamic)
- **🔄 Interpreter vs Compiler** (Python is interpreted)
- **🏃 Python Execution Model** (source → bytecode → PVM)
- **📄 Python Source Files** (.py files)
- **📊 Python Versions** (3.9 → 3.13, focus on 3.11+)
- **📥 Installing Python** (official installer, pyenv)
- **💻 Python REPL** (interactive mode for experimentation)
- **🚀 Running Scripts** (`python script.py`)
- **✏️ Code Editors** (VS Code, PyCharm)
- **📝 Syntax Rules** (case sensitivity, statement termination)
- **↪️ Indentation** (4 spaces, no tabs)
- **💬 Comments** (`#` single-line)
- **📄 Docstrings** (`"""triple quotes"""` for documentation)

---

## 🎯 STAGE 1 — Core Syntax & Expressions

**Goal**: Write correct Python statements and understand basic expressions.  
**Time**: 6 soat | 3 dars

#### 📚 Topics

- **📊 Variables and Assignment** (naming rules: letters, digits, underscore)
- **🏷️ Identifiers and Keywords** (`if`, `else`, `for`, `def`, etc.)
- **🔤 Built-in Data Types** (overview: int, float, str, bool, None)
- **🌀 Dynamic Typing** (type is determined at runtime)
- **✅ Type Checking** (`type()`, `isinstance()`)
- **🔄 Type Conversion** (`int()`, `str()`, `float()`, `bool()`)
- **⌨️ Input Handling** (`input()`, always returns string)
- **🖨️ Output Formatting** (`print()`, `sep`, `end`, f-strings preview)
- **🔧 Operators:**
  - ➕➖ Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
  - ⚖️ Comparison (`==`, `!=`, `>`, `<`, `>=`, `<=`)
  - 🔗 Logical (`and`, `or`, `not`)
  - 📝 Assignment (`=`, `+=`, `-=`, `*=`, `/=`)
  - 👥 Membership (`in`, `not in`)
  - 🆔 Identity (`is`, `is not`)
- **📝 Expressions** (how Python evaluates them)
- **📊 Operator Precedence** (PEMDAS, parentheses override)

---

<br>
<br>
<br>
<br>
<br>

# 🎯 STAGE 2 — Primitive Types & Data Fundamentals

**Goal**: Master Python's core data types and understand how values are stored.  
**Time**: 6 soat | 3 dars

---

#### 📚 Topics

##### **🔢 Numeric Types**

- **🔢 Integers (`int`)**
  - Unlimited precision
  - Binary (`0b1010`), octal (`0o12`), hexadecimal (`0xA`)
  - Common operations: `abs()`, `pow()`, `divmod()`
- **🔟 Floating-Point Numbers (`float`)**
  - IEEE 754 standard (binary floating-point)
  - Precision limitations (`0.1 + 0.2 != 0.3`)
  - Special values: `inf`, `-inf`, `nan`
  - `math.isclose()` for comparisons
- **🔷 Complex Numbers (`complex`)**
  - `3 + 4j`, `complex(3, 4)`
  - Real and imaginary parts: `.real`, `.imag`
- **📏 Decimal for Precision**
  - `from decimal import Decimal`
  - When to use: financial calculations, exact decimal arithmetic
  - `Decimal('0.1') + Decimal('0.2') == Decimal('0.3')` ✅

##### **✅ Boolean Type**

- **📊 `bool` Type**
  - `True` and `False` (subclass of `int`)
  - `True == 1`, `False == 0`
  - Boolean operations: `and`, `or`, `not`
  - Short-circuit evaluation

##### **🚫 NoneType**

- **❓ `None`**
  - Represents absence of value
  - Singleton object (only one `None` exists)
  - Use `is None` for comparison (not `==`)
  - Default return value for functions without `return`

##### **🎯 Truthy and Falsy Values**

- **⚖️ Truth Value Testing**
  - **Falsy values**: `False`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`
  - **Truthy values**: everything else
  - Used in `if`, `while`, and logical operations

##### **🆔 Object Identity & References**

- **🎯 Variables Are References**
  - Variables point to objects, not containers
  - Assignment creates reference, not copy
- **🆔 `id()` Function**
  - Returns unique identifier for object
  - Useful for debugging reference behavior
- **🆔 `is` Operator**
  - Checks if two references point to same object
  - Use for `None` comparison, not for value equality

##### **🔄 Mutability vs Immutability**

- **🔒 Immutable Types** (cannot change after creation)
  - `int`, `float`, `bool`, `str`, `tuple`, `frozenset`
  - Any operation creates a new object
- **📝 Mutable Types** (can be modified)
  - `list`, `dict`, `set`, custom objects
  - Changes affect all references

##### **📦 Type Conversion**

- **🔄 Explicit Conversion Functions**
  - `int()`, `float()`, `str()`, `bool()`
  - `list()`, `tuple()`, `set()`, `dict()`
- **⚠️ Conversion Rules**
  - String to number: `int("123")` works, `int("12.3")` fails
  - Float to int: truncates (not rounds)
  - Boolean conversion: `bool(0) → False`, `bool(1) → True`

##### **🔢 Numeric Operations & Functions**

- **🧮 `math` Module Basics**
  - `math.floor()`, `math.ceil()`, `math.trunc()`
  - `math.sqrt()`, `math.pow()`, `math.pi`, `math.e`
- **🎲 `random` Module**
  - `random.random()` (0 to 1)
  - `random.randint(a, b)` (inclusive)
  - `random.choice(seq)` (random element)

##### **📊 Type Information**

- **🔍 `type()` Function**
  - Returns type object
  - `type(x) is int` (exact type check)
- **✅ `isinstance()` Function**
  - Checks inheritance hierarchy
  - Preferred over `type()` for type checking
  - `isinstance(True, int)` → `True` (bool is subclass of int)

---

<br>
<br>
<br>
<br>
<br>

# 🎯 STAGE 3 — Strings & Text Processing

**Goal**: Master text manipulation — a core skill for backend development.  
**Time**: 6 soat | 3 dars

---

#### 📚 Topics

##### **📝 String Creation**

- **🆕 String Literals**
  - Single quotes: `'Hello'`
  - Double quotes: `"Hello"` (useful for strings with apostrophes)
  - Triple quotes: `'''...'''` or `"""..."""` (multi-line strings)
  - Raw strings: `r'C:\Users\name'` (ignores escape characters)
- **📊 String Type**
  - `str` type (immutable sequence of Unicode characters)
  - `len()` function for length

##### **📍 Indexing**

- **0-based indexing**
  - First character: `s[0]`
  - Last character: `s[-1]`
  - Access any position: `s[index]`
- **⚠️ IndexError** (index out of range)

##### **🔪 Slicing**

- **🔪 Slice Syntax**: `s[start:stop:step]`
  - `s[0:5]` → first 5 characters
  - `s[:5]` → from start to index 5
  - `s[5:]` → from index 5 to end
  - `s[::-1]` → reverse string
- **📊 Slice Behavior**
  - Returns new string (immutability)
  - Start inclusive, stop exclusive
  - Negative indices work

##### **🔒 String Immutability**

- **❌ Cannot Modify Strings**
  - `s[0] = 'a'` → TypeError
- **✅ Operations Create New Strings**
  - `s = s + '!'` → new string
  - `s = s.upper()` → new string

##### **🛠️ Essential String Methods**

| Method                 | Example                                        | Description                    |
| ---------------------- | ---------------------------------------------- | ------------------------------ |
| **Case Conversion**    |
| `upper()`              | `"hello".upper()` → `"HELLO"`                  | All uppercase                  |
| `lower()`              | `"HELLO".lower()` → `"hello"`                  | All lowercase                  |
| `capitalize()`         | `"hello world".capitalize()` → `"Hello world"` | First letter uppercase         |
| `title()`              | `"hello world".title()` → `"Hello World"`      | Each word capitalized          |
| `swapcase()`           | `"Hello".swapcase()` → `"hELLO"`               | Swap case                      |
| **Whitespace Removal** |
| `strip()`              | `"  hello  ".strip()` → `"hello"`              | Remove both ends               |
| `lstrip()`             | `"  hello".lstrip()` → `"hello"`               | Remove left whitespace         |
| `rstrip()`             | `"hello  ".rstrip()` → `"hello"`               | Remove right whitespace        |
| **Search & Find**      |
| `find(sub)`            | `"hello".find("e")` → `1`                      | Returns index or -1            |
| `index(sub)`           | `"hello".index("e")` → `1`                     | Raises ValueError if not found |
| `count(sub)`           | `"hello".count("l")` → `2`                     | Count occurrences              |
| `startswith(prefix)`   | `"hello".startswith("he")` → `True`            | Check prefix                   |
| `endswith(suffix)`     | `"hello".endswith("lo")` → `True`              | Check suffix                   |
| **Validation**         |
| `isalpha()`            | `"hello".isalpha()` → `True`                   | Only letters                   |
| `isdigit()`            | `"123".isdigit()` → `True`                     | Only digits                    |
| `isalnum()`            | `"hello123".isalnum()` → `True`                | Letters or digits              |
| `isspace()`            | `"   ".isspace()` → `True`                     | Only whitespace                |
| `isupper()`            | `"HELLO".isupper()` → `True`                   | All uppercase                  |
| `islower()`            | `"hello".islower()` → `True`                   | All lowercase                  |

##### **🔧 String Manipulation Methods**

| Method                  | Example                                      | Description             |
| ----------------------- | -------------------------------------------- | ----------------------- |
| **Split & Join**        |
| `split(sep)`            | `"a,b,c".split(",")` → `["a","b","c"]`       | Split into list         |
| `split()`               | `"a b c".split()` → `["a","b","c"]`          | Split on whitespace     |
| `rsplit()`              | `"a,b,c".rsplit(",", 1)` → `["a,b","c"]`     | Split from right        |
| `join(iterable)`        | `",".join(["a","b","c"])` → `"a,b,c"`        | Join with separator     |
| `partition(sep)`        | `"a=b=c".partition("=")` → `("a","=","b=c")` | Split into 3 parts      |
| **Replace & Translate** |
| `replace(old, new)`     | `"hello".replace("l","x")` → `"hexxo"`       | Replace all occurrences |
| `translate(table)`      | Advanced character mapping                   | Map characters          |
| **Alignment**           |
| `center(width)`         | `"hi".center(5)` → `"  hi "`                 | Center align            |
| `ljust(width)`          | `"hi".ljust(5)` → `"hi   "`                  | Left align              |
| `rjust(width)`          | `"hi".rjust(5)` → `"   hi"`                  | Right align             |
| `zfill(width)`          | `"42".zfill(5)` → `"00042"`                  | Pad with zeros          |

##### **🎨 String Formatting**

- **🎯 f-strings (Python 3.6+, RECOMMENDED)**

  ```python
  name = "Alice"
  age = 30
  f"{name} is {age} years old"
  f"{age:05d}"  # → "00030" (zero padding)
  f"{price:.2f}"  # → "12.34" (2 decimal places)
  f"{value:>10}"  # → right align 10 spaces
  f"{value:<10}"  # → left align
  f"{value:^10}"  # → center
  ```

- **🎨 `format()` Method**

  ```python
  "{} is {} years old".format(name, age)
  "{name} is {age} years old".format(name=name, age=age)
  ```

- **📜 %-formatting (Legacy)**
  ```python
  "%s is %d years old" % (name, age)  # C-style, avoid when possible
  ```

##### **🔤 Escape Characters**

| Escape | Meaning         |
| ------ | --------------- |
| `\n`   | Newline         |
| `\t`   | Tab             |
| `\\`   | Backslash       |
| `\'`   | Single quote    |
| `\"`   | Double quote    |
| `\r`   | Carriage return |
| `\b`   | Backspace       |

##### **🌐 Unicode Support**

- **🔤 Unicode Characters**
  - Python strings are Unicode by default
  - `ord('A')` → 65 (get Unicode code point)
  - `chr(65)` → 'A' (get character from code point)
  - Unicode escape: `"\u0041"` → 'A' (4-digit hex)
  - Unicode escape: `"\U0001F600"` → '😀' (8-digit hex)
- **📝 Encoding & Decoding**
  - `encode()`: string → bytes (`"hello".encode('utf-8')`)
  - `decode()`: bytes → string (`b'hello'.decode('utf-8')`)

##### **🔍 Regular Expressions (re module)**

- **📚 Basic Patterns**

  ```python
  import re

  # Search
  re.search(r'\d+', 'abc123')  # find digits
  re.match(r'^\d+', '123abc')  # match from start

  # Find all
  re.findall(r'\w+', 'hello world')  # → ['hello', 'world']

  # Replace
  re.sub(r'\d+', 'X', 'a1b2c3')  # → 'aXbXcX'

  # Split
  re.split(r'[,;]', 'a,b;c')  # → ['a', 'b', 'c']
  ```

- **📊 Common Patterns**
  - `\d` → digit, `\D` → non-digit
  - `\w` → word character (letter, digit, underscore)
  - `\s` → whitespace
  - `.` → any character (except newline)
  - `*` → 0 or more, `+` → 1 or more, `?` → 0 or 1
  - `{n}` → exactly n times
  - `^` → start of string, `$` → end of string

---

<br>
<br>
<br>
<br>
<br>

# 🎯 STAGE 4 — Control Flow & Logic

**Goal**: Control program execution with conditions and decision-making structures.  
**Time**: 4 soat | 2 dars

---

#### 📚 Topics

##### **✅ Boolean Expressions**
- **⚖️ Comparison Operators**
  - Equality: `==`, `!=`
  - Relational: `>`, `<`, `>=`, `<=`
  - Returns `True` or `False`
- **🔗 Logical Operators**
  - `and`: both must be True
  - `or`: at least one must be True
  - `not`: negates boolean value
- **⚡ Short-Circuit Evaluation**
  - `and` stops at first False
  - `or` stops at first True
  - Useful for safe chaining: `if user and user.is_active:`

##### **⚖️ Truthy and Falsy Values**
- **📊 Falsy Values** (evaluate to False in boolean context)
  - `False`, `0`, `0.0`, `0j`
  - `""` (empty string)
  - `[]` (empty list), `()` (empty tuple), `{}` (empty dict)
  - `set()` (empty set)
  - `None`
- **✅ Truthy Values**
  - Everything else (non-empty collections, non-zero numbers, True)

##### **🔀 if Statements**
- **📝 Basic Syntax**
  ```python
  if condition:
      # executed if condition is True
  ```
- **⛓️ if-else**
  ```python
  if condition:
      # executed if True
  else:
      # executed if False
  ```
- **🔢 elif Chains**
  ```python
  if condition1:
      # condition1 True
  elif condition2:
      # condition2 True
  elif condition3:
      # condition3 True
  else:
      # none of the above
  ```
- **📦 Nested Conditions**
  ```python
  if outer_condition:
      if inner_condition:
          # both True
  ```

##### **🎭 match / case** (Structural Pattern Matching - Python 3.10+)

- **📝 Basic Syntax**
  ```python
  match value:
      case pattern1:
          # action for pattern1
      case pattern2:
          # action for pattern2
      case _:
          # default (wildcard)
  ```

- **📊 Literal Patterns**
  ```python
  match status_code:
      case 200:
          print("OK")
      case 404:
          print("Not Found")
      case 500:
          print("Server Error")
      case _:
          print("Unknown status")
  ```

- **🔍 Capture Patterns** (variable binding)
  ```python
  match point:
      case (0, 0):
          print("Origin")
      case (x, 0):
          print(f"On X-axis at {x}")
      case (0, y):
          print(f"On Y-axis at {y}")
      case (x, y):
          print(f"Point at ({x}, {y})")
  ```

- **🔢 OR Patterns**
  ```python
  match status:
      case 200 | 201 | 204:
          print("Success")
      case 400 | 404 | 403:
          print("Client error")
      case _:
          print("Other")
  ```

- **🎯 Guard Clauses** (additional condition)
  ```python
  match value:
      case int(x) if x > 0:
          print(f"Positive integer: {x}")
      case int(x) if x < 0:
          print(f"Negative integer: {x}")
      case int(x):
          print(f"Zero")
  ```

- **📦 Sequence Patterns**
  ```python
  match items:
      case []:
          print("Empty list")
      case [first]:
          print(f"Single item: {first}")
      case [first, second]:
          print(f"Two items: {first}, {second}")
      case [first, *rest]:
          print(f"First: {first}, Rest: {rest}")
  ```

- **📖 Mapping Patterns** (dictionaries)
  ```python
  match config:
      case {"debug": True, "port": port}:
          print(f"Debug mode on port {port}")
      case {"port": port}:
          print(f"Port: {port}")
      case _:
          print("No port configured")
  ```

- **🏷️ Class Patterns**
  ```python
  match obj:
      case Point(x=0, y=0):
          print("Origin")
      case Point(x=x, y=y):
          print(f"Point at ({x}, {y})")
      case Circle(center=Point(0,0), radius=r):
          print(f"Circle at origin with radius {r}")
  ```

##### **🔄 Conditional Expressions**

- **📝 Ternary Operator**
  ```python
  # value_if_true if condition else value_if_false
  status = "active" if user.is_active else "inactive"
  max_value = a if a > b else b
  ```
- **🎯 Use Cases**
  - Simple conditional assignments
  - Default values with fallback
  - Not for complex logic (use if-else)

##### **🔄 Walrus Operator** (`:=`) - Python 3.8+

- **📝 Assignment Expression**
  ```python
  # Assign and use in same expression
  if (n := len(data)) > 10:
      print(f"Data is long: {n} characters")
  
  # In while loops
  while (line := file.readline()) != "":
      process(line)
  
  # In list comprehensions
  [y for x in data if (y := process(x)) is not None]
  ```
- **⚠️ Best Practices**
  - Use when it improves readability
  - Avoid nesting too deep
  - Wrap in parentheses for clarity

##### **⚡ Condition Chaining**

- **📊 Comparison Chaining**
  ```python
  # Python allows chained comparisons
  if 0 < x < 10:
      print("x is between 0 and 10")
  
  # Equivalent to:
  if 0 < x and x < 10:
      print("x is between 0 and 10")
  
  # Works with other operators
  if a == b == c:
      print("All equal")
  ```

##### **🎯 De Morgan's Laws**

- **📝 Logical Transformations**
  ```python
  # not (A and B) == (not A) or (not B)
  # not (A or B) == (not A) and (not B)
  
  # Simplify complex conditions
  if not (user and user.is_active):  # ❌ Hard to read
  if not user or not user.is_active:  # ✅ Clearer
  ```

---

#### 📝 Practice Exercises

1. **Grade Calculator**: Input score (0-100), output grade (A, B, C, D, F) using if-elif-else
2. **Leap Year Checker**: Check if year is leap year (divisible by 4, but not by 100 unless also by 400)
3. **Number Classifier**: Classify number as positive/negative/zero, even/odd, using match-case
4. **Command Parser**: Parse CLI-like commands using match-case patterns
5. **Safe Division**: Calculate division with guard against division by zero
6. **Login System**: Validate username and password with truthy/falsy checks

---

#### ⚠️ Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| `if x = 5:` vs `if x == 5:` | Use `==` for comparison, `=` is assignment (syntax error) |
| Comparing with `None` using `==` | Always use `is None` or `is not None` |
| Forgetting colon `:` | Required after if, elif, else, match, case |
| Indentation errors | Use 4 spaces consistently, no mixing with tabs |
| `elif` instead of `else if` | Python uses `elif`, not `else if` |
| Complex nested if-else | Extract to functions or use match-case |
| `is` vs `==` confusion | `is` for identity (same object), `==` for value equality |
| Truthy confusion | Empty collections are falsy, but explicitly check when needed |

---

#### 🔧 Code Examples

```python
# Ternary operator with multiple conditions
status = "critical" if error_count > 10 else "warning" if error_count > 0 else "ok"

# Match-case for HTTP status handling
def handle_http_status(code: int) -> str:
    match code:
        case 200 | 201 | 204:
            return "Success"
        case 400 | 404 | 403:
            return "Client error"
        case 500 | 502 | 503:
            return "Server error"
        case _:
            return f"Unknown status: {code}"

# Walrus operator for efficient validation
def validate_input(data):
    if (length := len(data)) < 3:
        return f"Too short: {length} characters"
    if (length := len(data)) > 100:
        return f"Too long: {length} characters"
    return "Valid input"

# Guard clauses (early returns)
def process_user(user):
    if not user:  # Guard clause
        return None
    if not user.is_active:  # Guard clause
        return None
    if not user.has_permission:  # Guard clause
        return None
    
    # Main logic
    return user.process()

# De Morgan's law application
# Instead of:
if not (is_valid and is_authorized):
    return "Invalid"
    
# Better:
if not is_valid or not is_authorized:
    return "Invalid"
```

---

#### 🎯 Decision Tree

```
Need to make decision?
        │
        ├── Simple assignment based on condition?
        │   └── Use ternary operator: x if condition else y
        │
        ├── Multiple conditions with patterns?
        │   └── Use match-case (Python 3.10+)
        │
        └── Complex logic flow?
            └── Use if-elif-else chains
                │
                ├── Early exit conditions?
                │   └── Use guard clauses (return early)
                │
                └── Multiple nested conditions?
                    └── Extract to separate functions
```

---
