# # tuple

# mylist = [2, 4, 7, 9]
# print(mylist)
# # Output: [2, 4, 7, 9]

# print(type(mylist))
# # Output: <class 'list'>

# print(mylist)
# mylist[0] = 8
# print(mylist)

# ---------------------
'''
# tuple: is immutable(unchangeble) data type in python
# it is similar to list but it is immutable
mytuple = (3, 5, 8, 1)
print("My Tuple : ", mytuple)
# Output: (3, 5, 8, 1)
print(type(mytuple))
# Output: <class 'tuple'>

# mytuple[0] = 55 // error
# Output: TypeError: 'tuple' object does not support item assignment
# Ex.1
a = (2, 5, 77, 2, 2, "hello", "vadapav")

print("Tuple: ", a)
print(a.index(77))
print(a.count(2))
# set:
# set is an unordered collection of unique elements

myset = {2, 4, 6, 2, 7, 4, 5, 7}
print("Set : ", myset)

myset.add(44)
myset.add(44)
print(myset)

myset.remove(5)
print(myset)

myset.discard(15)
print(myset)

myset.update({33, 55, 99, 4})
print(myset)


'''
# Ex.2
A = {2, 4, 6, 8, 7, 5}
B = {4, 6, 9, 1, 3}

C = A.copy()

A.remove(6)
print(A)
print(C)

print("A U B : ", A.union(B))
print("A n B : ", A.intersection(B))
print("A D B : ", A.difference(B))
print("B D A : ", B.difference(A))

