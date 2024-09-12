
# class Employee:
#     def __init__(self, Id, Name, Salary):
#         self.id = Id
#         self.name = Name
#         self.__salary = Salary

#     def printDetails(self):
#         print(f"Employee ID: {self.id}")
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Salary: {self.__salary}")

#     @property
#     def getSalary_value(self):
#         return self.__salary

#     @getSalary_value.setter
#     def setSalary_value(self, newValue):
#         self.__salary = newValue


# emp = Employee(101, "Rakesh", 10000)

# print(emp.getSalary_value)

# emp.setSalary_value = 30000

# print(emp.getSalary_value)

# emp.printDetails()

class DigitalWatch:
    def __init__(self, id, Price, GST=0.28):
        self.id = id
        self.__price = Price
        self.__gst = GST

    @property #getter
    def printBill(self):
        return self.__price+(self.__price*self.__gst)
    
    @printBill.setter
    def updatePrice(self,newPrice):
        self.__price = newPrice


w1 = DigitalWatch(3004, 1000)

print(w1.printBill)
w1.updatePrice = 2000
print(w1.printBill)