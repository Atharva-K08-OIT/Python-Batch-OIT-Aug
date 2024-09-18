# Dunder Methods:

# Ex.1

# x+yj == 3+5j

# class Complex_number:
#     def __init__(self, X, Y):
#         self.x = X
#         self.y = Y

#     def __str__(self):
#         return f"({self.x}+{self.y}j)"

#     def __repr__(self):
#         return f"Real Part:{self.x}\nImaginary Part:{self.y}\n"


# a = Complex_number(2, 5)  # 2+5j

# print(a)                  # 2 + 5i
# print(str(a))             # 2 + 5i
# print(repr(a))            #Real Part:2
#                           # Imaginary Part:5

# -----------------------------------------------------------------------------

# Ex.2

# Vector: 5i + 3j + 6k

class Vector:
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z

    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

v1 = Vector(4,5,3)

print(v1)