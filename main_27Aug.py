'''
# dict:
# defination:
# 1. A collection of key-value pairs where each key is unique and each value is immutable

Flist = {
    "a": "apple",
    "b": "banana",
    "c": "cherry",
    "d": "date",
    "e": "elderberry",
    "A": "apple"
}

print(type(Flist))
# <class 'dict'>
print(Flist)
# {'a': 'apple', 'b': 'banana', 'c': 'cherry'}


print(Flist["A"])
print(Flist["b"])
print(Flist["c"])


print("By using for loop: ")
for key in Flist:
    print(key , ": ",Flist[key])

'''

# Ex.2
mydict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

'''
print(mydict)

mydict.update({
    "country": "USA",
    "phone": "1234567890"
})
print(mydict)

print("conName:",mydict.get("country"))


print("Keys: ",mydict.keys())
# dict_keys(['name', 'age', 'city', 'country', 'phone'])

print("Values: ",mydict.values())
# dict_values(['John', 30, 'New York', 'USA', '123456789

print("Items: ",mydict.items())
# dict_items([('name', 'John'), ('age', 30), ('city', 'New York')]

mydict.clear()
print(mydict)

'''

# Ex.3
mydict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(mydict["name"])

mydict['name'] = "Mona"

print(mydict["name"])
# Output: Mona
print(mydict)

del mydict["age"]

print(mydict)

print("Lenght : ",len(mydict))
# Output: 2