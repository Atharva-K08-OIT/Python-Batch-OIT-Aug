# Strings:
# defination:
# A string is a sequence of characters, such as a word or a sentence.
# Example: "Hello, World!"
'''
# Ex.1 
str1 = "Hello, Good Morning!"
str2 = 'Hello, Good Morning!'
str3 = \'''Hello, Good Morning!\'''
str4 = """Hello, Good Morning!"""
print(str1) # Output: Hello, Good Morning!
print(str2) # Output: Hello, Good Morning!
print(str3) # Output: Hello, Good Morning!
print(str4) # Output: Hello, Good Morning!
'''
# Ex.2
# Escape Sequence Character. : \", \', \n, \t
str1 = "Hello, Good Morning!"  # string literal

d1 = 'Ramesh Said,"I want apple".'
print(d1)  # Output: Ramesh Said,"I want apple".
d2 = "Ramesh Said,\"I want apple\"."
print(d2)  # Output: Ramesh Said,"I want apple".
d3 = "Ramesh Say's,\"I want apple\"."
print(d3)  # Output: Ramesh Say's,"I want apple".
d4 = 'Ramesh Say\'s,"I want apple".'
print(d4)  # Output: Ramesh Say's,"I want apple".
d5 = 'Ramesh Say\'s,"Hello Ji\nKese ho".'
print(d5)  # Output: Ramesh Say's,"Hello Ji
d6 = 'Ramesh Say\'s,"Hello Ji\tKese ho".'
print(d6)  # Output: Ramesh Say's,"Hello Ji	Kese ho".


# Ex.3
# String Concatenation
str1 = "Hello,"
str2 = "Good Morning!"
str3 = str1 + " " + str2
print(str3)  # Output: Hello, Good Morning!


# Ex.4
# Formated Strings: (f-string):
# f-string is a feature in Python that allows you to embed expressions inside string literals, using the
# f prefix before the string. This is a more readable and efficient way to format strings.

a = 30
b = 40

ans1 = "Addition of ", a, " and ", b, " is ", a+b
print(ans1)  # Output: Addition of  30  and  40  is 70

ans2 = "Addition of a and b is a+b"
print(ans2)  # Output: Addition of a and b is a+b

ans3 = f"Addition of {a} and {b} is {a+b}"
print(ans3)  # Output: Addition of 30 and 40 is 70

ans4 = "Addition of {} and {} is {}".format(a, b, a+b)
print(ans4)  # Output: Addition of 30 and 40 is 70
