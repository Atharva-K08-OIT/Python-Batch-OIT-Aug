from array import *

arr = array("i", [12, 56, 12, 67, 12])
print(type(arr))
print(arr)
print(arr.typecode)
print(arr.tolist())
# replace:
arr[arr.index(67)] = 40
print(arr.tolist())
# append:
arr.append(100)
print(arr.tolist())
# insert on any index
arr.insert(len(arr), 4)
print(arr.tolist())
# list,tuple,set of element : add in array
arr.extend({23, 45})
print(arr.tolist())
# remove any item:
arr.remove(100)
print(arr.tolist())
# remove item using index:
arr.pop(1)
print(arr.tolist())
# count:
print("Occurance (12):", arr.count(12))
# slicing od array:

print("array:", arr)
print("Slicing of array:", arr[0:80:2])
print("reverse of array:", arr[len(arr)::-1])
arr.reverse()
print("Rev: ", arr.tolist())

