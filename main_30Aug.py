# // String
# Defination :
# A string is a sequence of characters, such as a word or phrase.
# Strings are enclosed in quotes, either single quotes or double quotes.

# str1 = "Hello, Good Morning!"
# str2 = 'Hello, Good Morning!'
# str3 = '''Hello, Good Morning!'''
# str4 = """Hello, Good Morning!"""
# print(str1) # Hello, Good Morning!


# print("Rohan, Say's,\"Hello\"")
# print('Rohan, Say\'s,"Hello"')
# print('''Rohan, Say's,"Hello"''')

#    0123456789  ...    19
# s = "Hello, Good Morning!"

# print("Lenght : ", len(s))

# for i in range(0, len(s)):
#     print(s[i], end="")

# print("\n")

# for ch in s:
#     print(ch, end="")

# print("\n")

# print("--> ", s[0:20:1])
# print("--> ", s[19::-1])


a = 20
b = 30

# Addition of 20 and 30 is 50
print("Addition of", a, "and", b, "is", (a+b))
print(f"Addition of {a} and {b} is {a+b}")
print("Addition if {} and {} is {}".format(a,b,a+b))
print("Addition of %d and %d is %d" %(a,b,a+b))