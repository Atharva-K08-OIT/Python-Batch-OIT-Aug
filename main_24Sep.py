# # list Comprehension
# # defination
# # list comprehension is a compact way to create lists using consized syntax in python.


# # square = []

# # for i in mylist:
# #     square.append(i**2)
# # print("Using Convention Method: ")
# # print(square)

# # # --------------------------------
# # # using map

# # square = lambda x : x**2
# # newList = list(map(square,mylist))
# # print("Using Convention Method: ")
# # print(newList)
# # --------------------------------
# mylist = [22, 44, 77, 88, 99]
# # syntax for list comprehension:
# # [(expression/elem/format) for elem in iterable_reference if condition]

# # Ex.1 : to find square of item in give in another list
# square = [x**2 for x in mylist]
# print(square)

# # ----------------------------------------------------
# # Ex.2 : to find even numbered list form give list
# even = [x for x in mylist if x % 2 == 0]
# print(even)

# # ----------------------------------------------------
# # Ex.3 : to find (x,x**2) list form give list
# numAndSqu = [[x, x**2] for x in mylist]
# print(numAndSqu)

# ----------------------------------------------------
# Ex.4 : to find frqu(x) list form give list
# a = [2, 3, 6, 3, 7, 2, 6, 2]
# freq = []
# for i in a:
#     count = a.count(i)
#     freq.append((i, count))

# print(freq)
# print(set(freq))
# print(list(set(freq)))

# freq = list(set([(x,a.count(x)) for x in a]))
# print(freq)

# -------------------------------------------
# Ex.5 : we have list of string (word,length)
words = ["apple", "banana", "cherry", "date", "berry"]

# wordAndLength = [(word,len(word)) for word in words]
# print(wordAndLength)

# --------------------------------------------
# Ex.6 : we have list of string and get list of words having lenght > 5

mylist = [f"{word}:{len(word)}" for word in words if len(word) > 5]
print(mylist)

