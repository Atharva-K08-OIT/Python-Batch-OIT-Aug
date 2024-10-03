# def NameValidation(username):
#     if len(username) >= 8:
#         return True


# def PassValidation(password):
#     if len(password) >= 6:
#         return True


filename = "user.txt"

# with open(filename, "a") as fp:
#     username = input("Create your username: ")
#     password = input("Create your password: ")

#     while True:
#         if NameValidation(username) and PassValidation(password):
#             fp.write("username: "+username + "\n" + "password: "+password + "\n")
#             break
#         else:
#             print("Invalid username or password")
#             username = input("re-enter your username: ")
#             password = input("re-enter your password: ")


import re
with open(filename,"r") as fp:
    text = fp.read()

matches = re.findall(r"username: ([^\n]+)\npassword: ([^\n]+)",text)

print(matches)
# ----------------------------------------------------------

# filename = "zoo.txt"

# with open(filename, "r") as fp:
#     fp.seek(50)
#     info = fp.read(30)
#     print(info)
#     info = fp.read(5)
#     print(info)
#     print(fp.tell())

# -------------------------------------------

# read()
# readlines()
# readline()
# seek()
# tell()
# write()
# writelines()
# truncate()

# mode : x,r,w,a

# -------------------------------------------
