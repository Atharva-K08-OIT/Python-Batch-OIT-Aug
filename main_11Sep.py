# Multi-level inheritance:

class Person:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age

    def personalDetails(self):
        print(f"{self.name} is {self.age} years old")


class Employee(Person):
    def __init__(self, Name, Age, Id, Salary):
        super().__init__(Name, Age)
        self.id = Id
        self.salary = Salary

    def employeeDetails(self):
        print(f"Emp No.{self.id}: {self.name} has {self.salary} per month")


class Developer(Employee):
    def __init__(self, Name, Age, Id, Salary, Dept, Project):
        super().__init__(Name, Age, Id, Salary)
        self.dept = Dept
        self.project = Project

    def developerDetails(self):
        print(f"Developer is working in {
              self.dept} department on project:{self.project}")

    def RecordOfDeveloper(self):
        print(f"Emp No. Of Developer: {self.id}")
        print(f"Name Of Developer: {self.name}")
        print(f"Department Of Developer: {self.dept}")
        print(f"Project Of Developer: {self.project}")
        print(f"Salary Of Developer: {self.salary}")


d1 = Developer("Rakesh", 28, 21, 60000, "AI", "GPT-5")
d1.RecordOfDeveloper()
