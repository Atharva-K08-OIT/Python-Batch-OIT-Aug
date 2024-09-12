# Functions:
# defination:
'''
# .Ex.1
def greet():   # function declaration
    print("Good Morning!")   # function body
    print("Have a nice day")
    print("Welcome")
    

greet() # funtion call 
greet()
greet()
greet()
# Ex.2
def add():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum is: ", a + b)

add()
add()
add()
add()

# Ex.3

def AreaOfCuboid():
    l = int(input("Enter lenght: "))
    b = int(input("Enter breadth: "))
    h = int(input("Enter height: "))
    Area = 2*(l*b + b*h + h*l)
    print(f"The area of cuboid is: {Area} cu.cm.")

for i in range(5):
    AreaOfCuboid() # calling the function 5 times

# Ex.4
def evenOdd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

evenOdd()
evenOdd()
evenOdd()
# Ex.5
def calculateBill():
    item = input("Enter the item name: ")
    price = float(input("Enter the price of the item: "))
    tax = float(input("Enter the tax percentage: "))
    tax_amount = (price * tax) / 100
    total_bill = price + tax_amount
    print(f"Your total bill is for {item} : {total_bill} Rs")

calculateBill()
'''