# Multiple Inheritance:
# In Python, we can inherit from multiple classes using the (,) operator.
# Hirarchical Inheritance:
# Hybrid Inheritance:

class Person:
    pass

class Employee(Person):
    pass

class Student(Person):
    def __init__(self, Name, Rollno):
        self.name = Name
        self.rollno = Rollno


class Marks:
    def __init__(self, Math, Science, English):
        self.math = Math
        self.science = Science
        self.english = English

    def TotalMarks(self):
        return self.math + self.science + self.english


class Result(Student, Marks):
    def __init__(self, Name, Rollno, Math, Science, English):
        Student.__init__(self, Name, Rollno)
        Marks.__init__(self, Math, Science, English)

    def percentage(self):
        result = (self.TotalMarks()/3)
        print(f"Result: {round(result,2)}%")

    def ShowResult(self):
        print(f"Roll No.: {self.rollno}")
        print(f"Name Of Student: {self.name}")
        print(f"Math Marks: {self.math}")
        print(f"Science Marks: {self.science}")
        print(f"English Marks: {self.english}")
        print(f"Total mark obtained {self.TotalMarks()} Outof 300")
        self.percentage()

student = Result("Rahul", 21, 98, 97, 91)
student1 = Result("Rahul", 21, 98, 97, 91)
student.ShowResult()
student1.ShowResult()


