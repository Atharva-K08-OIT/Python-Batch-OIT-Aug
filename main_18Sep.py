# Operator Overload
# Ex.1
# class Vector():
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __str__(self):
#         return f"({self.x}î + {self.y}ĵ + {self.z}k)"
#     def __repr__(self) -> str:
#         return f"Vector({self.x}î + {self.y}ĵ + {self.z}k)"
#     def __len__(self):
#         return int((self.x**2 + self.y**2 + self.z**2)**(0.5))
#     def __add__(self,v):
#         return Vector(self.x + v.x , self.y + v.y , self.z + v.z)
#     def __sub__(self,v):
#         return Vector(self.x - v.x , self.y - v.y , self.z - v.z)
#     def __mul__(self,k):
#         return Vector(self.x*k , self.y*k , self.z*k)
# v1 = Vector(3, 5, 4)
# v2 = Vector(2, 2, 2)
# v3 = v1 + v2
# print(v3)
# print(type(v1 + v2))
# print(v1 - v2)
# print(v1*2)

# --------------------------------------------------------------------

class QuadracticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}x² + {self.b}x + {self.c}"

    def __repr__(self):
        return f"Qurd({self.a}, {self.b}, {self.c})"

    def __add__(self, e):
        return QuadracticEquation(self.a + e.a, self.b + e.b, self.c + e.c)

    def roots(self):
        if self.a == 0:
            print("Root doesn't exist")
            return []

        delta = ((self.b**2) - (4*self.a*self.c))
        print(delta)

        if (delta >= 0):
            r1 = (-self.b + (delta**0.5))/(2*self.a)
            r2 = (-self.b - (delta**0.5))/(2*self.a)
            return [r1, r2]
        else:
            print("Root are imaginary")
            return -1


e1 = QuadracticEquation(2, 4, 2)
print(e1.roots())
