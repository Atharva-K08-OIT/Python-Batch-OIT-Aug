def double(num):
    return num * 2

def square(num):
    return num ** 2

def powerOf(num,power):
    return num ** power

def cubeRootOf(num):
    return round(num ** (1. / 3))

def FindMyAge(BirthYear):
    return 2024 - BirthYear 

def Fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * Fact(num - 1)
    
