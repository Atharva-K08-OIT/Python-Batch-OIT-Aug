# List in Python:
#   - A list is a collection of items that can be of any data type
#   - Lists are denoted by square brackets `[]` and are ordered, meaning that items
#     have a specific position in the list.
#   - Lists are mutable, meaning that they can be modified after creation.

# ----------------------------------------------------
'''
# Ex.1
nums = [2, 4, 5, 7, 9, 0]
print(type(nums))
# Output: <class 'list'>

# Ex.2
mylist = [23, 4.23, True, "Atharva", "923"]
print(mylist)
# Output: [23, 4.23, True, 'Atharva', '923']

# Ex.3
#     0   1   2   3   4    +ve indexing
a = [33, 55, 77, 99, 88]
#    -5  -4  -3  -2  -1    -ve indexing
print("List : ", a)

print(a[1])
# Output: 55
print(a[-4])
# Output: 55


# Ex.4
# Sorting of list in A/D order:
b = [33, 11, 77, 99, 88]
print("List : ", b)
print("Sorted list : ", b.sort())
print("List : ", b)
print("Sorted list : ", b.sort(reverse=True))
print("List : ", b)


# Ex.5
# removal of element:
mylist = [2, 4, 3, 6, 7]
print("Original list : ", mylist)
mylist[2] = 8
print("List after modify : ", mylist)
mylist.remove(6)
mylist.remove(4)
# mylist.remove(12) error
print("List after remove : ", mylist)


# Ex. 5:
# To Add the new element in list:
mylist = [2, 4, 3, 6, 7]
print("Original list : ", mylist)

# append:
mylist.append(9)
print("List after append : ", mylist)

# insert
mylist.insert(2, 8)
print("List after insert : ", mylist)


# Ex.6
# To find the index of element in list
mylist = [2, 4, 3, 6, 7, 4, 7, 9, 2, 5]
print("Index of 9 : ", mylist.index(9))

# Ex.7
# To find the count of element in list
mylist = [2, 4, 3, 6, 7, 4, 7, 3, 2, 7, 4, 8]
print("Count of 4 : ", mylist.count(4))

# Ex.8
# To find the max/min element in list
mylist = [2, 4, 3, 6, 7, 4]
print("Max element : ", max(mylist))
print("Min element : ", min(mylist))

# Ex.9
# To find the sum of all element in list
mylist = [2, 4, 3, 6, 7, 4]
print("Sum of all element : ", sum(mylist))

# Ex.10
# reverse:
mylist = [2, 4, 3, 6, 7, 4]
print("Original list : ", mylist)
mylist.reverse()
print("List after reverse : ", mylist)

'''
