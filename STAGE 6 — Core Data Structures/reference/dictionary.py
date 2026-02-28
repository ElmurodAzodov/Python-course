
#^ Ditionary {} => {"key": "value", ..., }

# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "Tashkent",
#     12: [1, "bir", True, False],
#     12.5: {1, 2, 3},
#     (1, 2, 3): "bu tuple",
#     # [1,2,3]: "string" #bu yerda kalit xatoligi mavjud, chunki kalit tipi list bolishi mumkin emas!
# }
# #^ Kalit faqat - int, float, string, tuple tipda bo'lishi kerak, boshqa tipda mumkin emas!
# #^ Qiymati - turli tipda bo'lishi mumkin!
# #^ Dictionary mutable

# print(person)
# print(type(person))

# -----------------------------------------------------------------------------------------------

# my_dict = {"a": 1, "b": 2, "c": 3}
# my_dict1 = dict(a=1, b=2, c=3)

# print(my_dict, type(my_dict))
# print(my_dict1, type(my_dict1))

# -----------------------------------------------------------------------------------------------

#^ .keys(), .values(), .items()

person = {"name": "Alice", "age": 25, "city": "Tashkent"}

# print(person.keys(), type(person.keys()))
# print(list(person.keys()), type(list(person.keys())))
# print(person.values())
# print(person.items())

# print(person["city"])
# person["city"] = "Samarkand"
# print(person["city"])

# person["jobs"] = "Developer"
# print(person)

# print(person["village"]) #KeyError
# print(person.get("village")) #default holatida - None
# print(person.get("village", "Bunday kalit mavjud emas!")) # Bunday kalit mavjud emas!

# data = {"time": "12:00", "date": "28.02.2026"}
# person.update(data)
# print(person)

# print(person.pop("date"))
# print(person)

# print(person.popitem())
# print(person)

# print(person.clear())
# print(person)

# data = person.copy()
# print(data)

# person.setdefault("date", "27.02.2026", "time")
# print(person)

print(hash("name"))
print(hash(12))
print(hash(12.5))
print(hash((1,2,3)))
