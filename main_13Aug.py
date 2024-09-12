# Data Type In Python:
# Number:
a = 32
print(type(a))  # Output: <class 'int'>

b = 3.14
print(type(b))  # Output: <class 'float'>

c = 4+5j
print(type(c))  # Output: <class 'complex'>

# Text:

# Single line comment
"Hello Bollo"
'Bye'

# Multiple line comment
'''Hello Good 
Morning'''
"""Hello 
ji"""

name = "Atharva"
print(type(name))  # Output: <class 'str'>

# sequence type
# List
my_list = [1, 2, 3, 4, 5]
print(type(my_list))  # Output: <class 'list'>
# Tuple
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))  # Output: <class 'tuple'>
# Dictionary : Map
my_dict = {
    "name": "Atharva",
    "age": 20
}
print(type(my_dict))  # Output: <class 'dict'>
# Set
my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>


# Boolean
is_admin = True
print(type(is_admin))  # Output: <class 'bool'>