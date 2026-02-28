
# List []
# Tuple ()
# Set {} , set() => ()
# Dictionary {}

#Dict
# print(type({"qwe":123, "qwe":"qwe"}))


# Set

# my_set = {1, 2, 3, 3, 4, 5, 6, 5}
# print(my_set)


# fruits = {"apple", "banana", "cherry"}
# print(fruits)

# numbers = set([1,2,2,3,4])
# numbers_1 = [1,2,2,3,4]

# print(numbers)
# print(numbers_1)

# s = {1,2,3}
# s.add(4)
# s.update([5, 6, 6])
# s.remove(4)
# # s.remove(7)
# s.discard(1)
# s.pop()
# s.clear()
# print(s)


# set matematik amallar

a = {1,2,3,4}
b = {3,4,5,6}

print(f"Union: {a.union(b)}")
print(f"Intersection: {a.intersection(b)}")
print(f"Difference: {a.difference(b)}")
print(f"Symmetric difference: {a.symmetric_difference(b)}")


A = {1,2}
B = {1,2,3,4}

print(A.issubset(B))

print(B.issuperset(A))