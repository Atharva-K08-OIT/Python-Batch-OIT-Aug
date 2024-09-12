# if - else
# explan:
# if condition is true, then do this else, do that
# example

# res = input("What is your Result ? ")
# if ('condition'):
#     print("Yes")  # if True
# else:
#     print("No")  # if False


# if ():   ---> if False:
# -------------------------------------


# n ->>> 7 divide hoto ki nahi

# n = int(input("Enter your fav num : "))
# if (n % 7 == 0):
#     print("Yes, it is divisible by 7")
# else:
#     print("No, it is not divisible by 7")

# ------------------------------------------
# n -->> odd / even
# n % 2 == 0  ---> even
# n % 2 != 0 ---> odd

# n = int(input("Enter your Number : "))
# if (n % 2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")
# -------------------------------------------
# if - elif - else

# n -->> positive / negative / zero
# n > 0 ---> positive
# n < 0 ---> negative
# n == 0 ---> zero

# n = int(input("Enter your Number : "))
# if n > 0:
#     print("Positive Number")
# elif n < 0:
#     print("Negative Number")
# else:
#     print("Zero")

# -------------------------------------------
# n -->> greater than / less than / equal to 18
# n > 18 ---> can vote
# n < 18 ---> can't vote
# n == 18 ---> appled for card

# n = int(input("Enter your Age : "))
# if n > 18:
#     print("You can vote")
# elif n < 18:
#     print("You can't vote")
# else:
#     print("Applied for card")

# --------------------------------------------------

# if - else
# a , b find max

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))

# if (a > b):
#     print("a is greater")
# else:
#     print("b is greater")

# --------------------

# nested if - else

# a, b, c  find max

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))


# if (a > b):
#     if (a > c):
#         print("a is greater")
#     else:
#         print("c is greater than a,b")
# else:
#     if (b > c):
#         print("b is greater")
#     else:
#         print("c is greater than b,a")

# ***** ----

password = int(input("Enter your password: "))
# if password == 1234:
#     print("Welcome")
# else:
#     print("Invalid password")

# short hand: (for if-else)

print("Welcome!") if password == 1234 else print("Invalid Password")
