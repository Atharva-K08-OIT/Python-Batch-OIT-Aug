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

# sqr = list(map(lambda x:x**2,mylist))
# print(sqr)

# # # # ----------------------------------------------------
# # # Ex.2 : to find even numbered list form give list
# even = [x for x in mylist if x % 2 == 0]
# print(even)

# newEvens = list(filter(lambda x: x%2==0,mylist))
# print(newEvens)

# # # ----------------------------------------------------
# # # Ex.3 : to find (x,x**2) list form give list
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
# # # Ex.5 : we have list of string (word,length)
# words = ["apple", "banana", "cherry", "date", "berry"]

# # wordAndLength = [(word,len(word)) for word in words]
# # print(wordAndLength)

# # # --------------------------------------------
# # # Ex.6 : we have list of string and get list of words having lenght > 5

# mylist = [f"{word}:{len(word)}" for word in words if len(word) > 5]
# print(mylist)

# ---------------------------------------------------
# Ex.7 : We Have To creat list of "string" having "A" as prefix from other list a = []
# a = ["apple", "Ant", "Paper", "Table", "Chair",
#      "Atul", "Airpods", "Atul", "appu ghar"]

# b = {word for word in a if word.startswith("A")}

# print(b)
# ---------------------------------------------------

# Ex.8 : we have list of pallandroms from given list
# a = ["1234", "456","1221","454","997899","2013","191"]

# b = [num for num in a if num == num[::-1]]

# print(b)
# ---------------------------------------------------
# Ex.9 : we have list all numbers occured in give string
# s = "Today at 9:30 we a our python lecture for 1/2 hour"
# # o/p : num = [9,3,0,1,2]

# num = [int(n) for n in s if n.isdigit()]
# num.sort()
# print(num)

# ---------------------------------------------------

# set comprehension:
# syntax :
# {expression for variable in iterable if condition}
# ---------------------------------------------------
# Ex.1 : we have list of numbers and get set of even numbers from it
# a = [1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 6, 3, 7, 8]
# even = {x for x in a if x % 2 == 0}
# print(even)

# ---------------------------------------------------
# Dict Comprehention:
# syntax :
# {key : value for variable in iterable if condition}
# -----------------------------------------------------
# Ex.1
# we have list of numbers and get dict of squares of numbers from it
# a = [1, 2, 3, 4, 5, 6]
# # o/p : {1:1,2:4,3:9,4:16}
# squares = {x: x**2 for x in a}
# print(squares)

# -----------------------------------------------------
# Ex.2 : dict of {city:temp ℃} --> {city:temp ℉}
# import math
# a = {"delhi": 30, "mumbai": 35, "chennai": 40, "bangal": 38}


# t = {city: temp*(9/5)+32 for city, temp in a.items()}
# print(t)

# # -----------------------------------------------------
# # Ex.3 make a dict of factorial form give list
# a = [1, 2, 3, 4, 5, 6]
# f = {x: math.factorial(x) for x in a}  # math
# print(f)

# -------------------------------------------------
# a = ["a", "b", "c"]
# b = ["Airpods", "Batman", "Captain"]

# d = {a[i]:b[i] for i in range(len(a))}
# print(d)


# s = {key:value for key,value in zip(a,b)}
# print(s)