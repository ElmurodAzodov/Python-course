# =========================================
# 🚀 1-PROYEKT: Smart Data Cleaner System
# =========================================


# Maqsad: Berilgan datasetni decoratorlar orqali tozalash va analiz qilish

# 📌 Vazifa:
# List ichida aralash ma’lumotlar bo‘ladi:
# data = [10, "20", None, 30, "hello", 40, -5, 0, "50"]
# 🎯 Talablar:

# Decoratorlar orqali:

# @remove_invalid → None va stringlarni olib tashlash (filter)
# @to_int → string sonlarni int ga o‘tkazish (map)
# @only_positive → faqat musbat sonlar qolsin (filter)
# @calculate_stats →
# sum (reduce)
# average
# unique values (set)
# 🧠 Natija:
# {
#     "clean_data": [...],
#     "sum": ...,
#     "avg": ...,
#     "unique": {...}
# }
from functools import reduce

data = [10, "20", None, 30, "hello", 40, -5, 0, "50"]

def remove_invalid(func):
    def wrapper(data):
        cleaned = list(filter(lambda x: x is not None and (isinstance(x, int) or str(x).isdigit()), data))
        return func(cleaned)
    return wrapper

def to_int(func):
    def wrapper(data):
        converted = list(map(lambda x: int(x), data))
        return func(converted)
    return wrapper

def only_positive(func):
    def wrapper(data):
        positive = list(filter(lambda x: x > 0, data))
        return func(positive)
    return wrapper

def calculate_stats(func):
    def wrapper(data):
        result = func(data)
        total = reduce(lambda a, b: a + b, data, 0)
        avg = total / len(data) if data else 0
        unique = set(data)

        return {
            "clean_data": data,
            "sum": total,
            "avg": avg,
            "unique": unique
        }
    return wrapper

@remove_invalid
@to_int
@only_positive
@calculate_stats
def process_data(data):
    return data


print("1-PROJECT RESULT:")
print(process_data(data))