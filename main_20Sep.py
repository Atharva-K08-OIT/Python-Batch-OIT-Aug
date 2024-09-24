# function parameters
# default arguments

# def addition(a, b = 0, c = 0):
#     return a+b+c

# print(addition(4,5,8))
# print(addition(4,5))
# print(addition(a=3,c=5))

# ---------------------------------
# *args and kwargs

# Ex.1
# def add(*digits):
#     print(digits)
#     sum = 0
#     for i in digits:
#         sum += i

#     print(sum)


# add(3, 4, 5, 4, 5, 6, 7, 8, 34)

# ------------------------------------

# Ex.2
# def percetage(*args,**marks):
#     print(args)
#     print(marks)
#     total = 0
#     for sub in marks:
#         total += marks[sub]
#     print(f"Total marks:{total} outoff 600")

#     per = (total/600)*100

#     print(f"Percentage: {round(per,2)}%")

# percetage(math=99, eng=85, sci=92, marathi=71, hindi=81, socialSci=86)
# percetage(math=99, eng=85, sci=92, it=180, evs=98)
# percetage(1,2,3,4)

# lambda Expression:

sqr = lambda x: [x**2 for x in x]
print(sqr([2,3,4,5,6]))


# def isEven(x): return "Given num is even" if (
#     x % 2 == 0) else "Given num is odd"


# print(isEven(36))


# def add(mylist): return sum(mylist)


# print(add([2, 4, 6]))
