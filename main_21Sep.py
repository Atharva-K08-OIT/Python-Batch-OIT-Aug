# map function
# filter function
# reduce function

# -----------------------------
# Ex.1

# i/p: myList = [2, 4, 3, 7, 1, 9]
# o/p: newL = [4, 8, 6, 14, 2, 18]

# aam jindagi:
# myList = [2, 4, 3, 7, 1, 9]
# newList = []
# for i in myList:
#     newList.append(i*2)
# print(newList)

# mentor jindagi:
# myList = [2, 4, 3, 7, 1, 9]
# newList = list(map(lambda mark:mark*2,myList))
# print(newList)

# --------------------------------------
# Ex.2
# i/p: myList = [2, 4, 3, 7, 1, 8]
# o/p: newL = [2, 4, 8]

# aam jindagi:
# mylist = [2, 4, 3, 7, 1, 8]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)

# mentor jingadi:
# mylist = [2, 4, 3, 7, 1, 8]
# newlist = list(filter(lambda x:x%2==0,mylist))
# print(newlist)


# ---------------------------------------------
# Ex.3
# i/p: myList = [2, 4, 3, 7, 1]
# o/p: newL = 17

# aam jindagi:
# mylist = [2, 4, 3, 7, 1]
# sum = 0
# for i in mylist:
#     sum += i
# print(sum)

# mentor jindagi
from functools import reduce
mylist = [2, 4, 3, 7, 1]
sum = reduce(lambda a,b:a+b,mylist)
print(sum)