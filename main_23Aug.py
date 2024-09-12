# While loop:
#   - The while loop will continue to execute as long as the condition is true.


'''
# Ex.1
i = 0
while i < 10:
    print(i)
    i += 1
    # Output: 0, 1, 2, 3, 4

# Ex.2
i = 1
while i <= 10:
    print(i)
    i += 1
    # Output: 1, 2, 3, 4, 5, 6... 10

# Ex.3 // print table for 5 using while loop
i = 1
while i <= 10:
    print("5 x",i,"=", i*5)
    i += 1

# Ex.4: print series of number with gap of 2 digits
i = 2
while i <= 50:
    print(i)
    i += 3
    # Ex.5:    1 4 7 10 13 16 19

# Ex.5 print series of powers of 2
# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8

i = 0
while i <= 10:
    print("2 ^",i, "=", 2**i)
    i += 1


# break and continue

i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print(i)

print("Done")
# ---------------------------
i = 0
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i)

print("Done")

'''
# Ex. 8: do-while loop using while

while True:
    password = input("Enter your PassKey: ")
    if password == "1234":
        break

print("Your Device is Unlocked")