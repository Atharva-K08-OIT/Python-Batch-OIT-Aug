'''
# print("Hello Good Morning...", end="\n")
# print("Bye Bye", "TaTa", "See U!", sep=" ")

# print("Samosa",end=" ")
# print("Pizza")

# print("Pizza" , "Samosa" ,sep=" - ")

# age = 18
# print("Age : ", age)

# implicitly or explicitly
# age = int(input("Enter your age : ")) # "8"
# print(type(age))
# print(age)


# operators:
# 1. Arithmetic Operators: +, -, *, /, //, %, **
# if a = 20 and b = 10
a = int(input("Enter your 1st number :"))
b = int(input("Enter your 2nd number :"))

print("a + b : ", a+b)  # a + b :  30
print("a - b : ", a-b)  # a - b :  10
print("a * b : ", a*b)  # a * b :  200
print("a / b : ", a/b)  # a / b :  2.0
print("a // b : ", a//b)  # a // b :  2
print("a % b : ", a % b)  # a % b :  0
print("a ** b : ", a**b)  # a ** b :  200

# 2. Comparison Operators: ==, !=, >, <, >=, <=
# if a = 20 and b = 10
a = int(input("Enter your 1st number :"))
b = int(input("Enter your 2nd number :"))

print("a == b : ", a == b)  # a == b :  False
print("a != b : ", a != b)  # a != b :  True
print("a > b : ", a > b)  # a > b :  True
print("a < b : ", a < b)  # a < b :  False
print("a >= b : ", a >= b)  # a >= b :  True
print("a <= b : ", a <= b)  # a <= b :  False


# 3. Logical Operators: and, or, not
a = 20
b = 10

# True and True --> True   otherwise : false

print(a > b and a != b)

# False or False --> False   otherwise : true

print(a < b or a == b)

# not True ---> False
# not False ---> True

print(not (a > b))


# 4. Assignment Operators: =, +=, -=, *=, /=, //=, %=, **

# a = 20
# print("a : ", a)
# a += 5
# print("a : ", a)  # a :  25
# a -= 10
# print("a : ", a)  # a :  15
# a *= 2
# print("a : ", a)  # a :  30
# a //= 3
# print("a : ", a)  # a :  10
# a %= 4
# print("a : ", a)  # a :  2
# a **= 3
# print("a : ", a)  # a :  8

# 5. Membership Operators: in, not in
# 6. Identity Operators: is, is not
# 7. Bitwise Operators: &, |, ^, ~, <<, >>

print("a & b : ", 13 & 12)

# 0 & 0 --> 0
# 0 & 1 --> 0
# 1 & 0 --> 0
# 1 & 1 --> 1

#  13 = 1101
#  12 = 1100
#       1100 --> 12

print("a | b : ", 9 | 6)

# 0 | 0 --> 0
# 0 | 1 --> 1
# 1 | 0 --> 1
# 1 | 1 --> 1

# 9 = 1001
# 6 = 0110
#     1111 --> 15


print("a ^ b : ", 5 ^ 7)

# 0 ^ 0 --> 0
# 0 ^ 1 --> 1
# 1 ^ 0 --> 1
# 1 ^ 1 --> 0

# 5 = 0101
# 7 = 0111
#     0010 --> 2

print("~a : ", ~4)

# 000000000000000000...00100
# 111111111111111111...11011


a = 4
print("a>>1 : ", a >> 1)
print("a<<1 : ", a << 1)


# 4 = 0100
#     0010  --> 2
#     1000  --> 8
'''
