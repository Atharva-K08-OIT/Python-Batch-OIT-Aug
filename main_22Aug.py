# For loop in python:

# Defination:
# The for loop is used to iterate over a well defined sequence

# (such as a list, tuple, dictionary,such as strings, files, or generator expressions or set) or other iterable objects

# perfect iteration: execute a block of code for each item in it.

# Syntax:

# for variable in iterable:  // variable dependent loop
#     # code to be executed

# Example:

# loop: repeation/iteration


# funtion: range()
# syntax: range(start, end, jump)
# syntax: range(start:0, end:n-1, jump:1)
'''
print(range(0, 5))  # range(): iterable object
# start (inclusive)
# end (exclusive)

# Ex: print 1 --> 10 using range in for loop
for i in range(-10, 11):
    print(i)

# Ex: print -10 --> 10 using range in for loop
for i in range(-10, 11):
    print(i)

# Ex: print 11 --> 11 using range in for loop
for i in range(11, 11):
    print(i)

# Ex: print 11 --> 1 using range in for loop
for i in range(11, 1):
    print(i)

# Ex: print 11 --> 1 using range in for loop with jump:3
for i in range(1, 11, 3):
    print(i)

# Ex: print 1 --> 10 using range in for loop with jump:-1
for i in range(10, 0,-1):
    print(i)
'''

# Basic Examples:
'''
# Ex.1
# accept the number of iteration form user and print hello
n = int(input("Enter your number: "))
for i in range(1, n+1):
    print(i)

# Ex.2
# accept the number of iteration form user and print sum of all number
# (form 1 to n)
n = int(input("Enter your number: "))
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)

# Ex.3
# accept the number form user and print factorial for given number

# 5! = 5*4*3*2*1 = 120
# n! = n*(n-1)*(n-2)*(n-3)*....*3*2*1

# 1! = 1
# 0! = 1

n = int(input("Enter your number : "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(n, "! : ", factorial,sep="")
'''
