# formulations:

# ----------------------------------------
# (a+b)^2 = a*a + b*b + 2*a*b

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))

# ans = (a*a) + (b*b) + (2*a*b)

# print("(a + b)^2 : ", ans)

# ----------------------------------------
# Area of Circle = 3.14*r*r

# r = int(input("Enter radius of circle: "))

# ans = 3.14 * r * r

# print("Area of Circle :", ans,"sq.cm.")
# print(f"Area of Circle : {ans} sq.cm.")

# ----------------------------------------
# Volume of Sphere = (4/3) * 3.14 *r*r*r

# from math import *
# r = int(input("Enter radius of sphere: "))

# ans = (4/3) * 3.14 * (r**3)
# print(f"Volume of Sphere : {round(ans, 4)} cu.cm.")

# ---------------------------------------

# num = int(input("Enter your number : "))
# flag = 1

# for i in range(2, (num//2)+1):
#     if (num % i == 0):
#         flag = 0
#         break

# if (flag == 1):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# --------------------------------------

# num = 3456

# temp = '3456'
#         0123


num = int(input("Enter your number : "))

temp = str(num)
rev = int(temp[::-1])

# rev = int(str(num)[::-1])

print(f"Num : {num}")
print(f"Rev : {rev}")

if (num == rev):
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")
