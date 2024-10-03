def Multiply(a,b):
    return a * b





def Division(a,b):    
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print("Invalid input you enter 0")
    except TypeError as e:
        print("Invalid input you enter non-digit value")
