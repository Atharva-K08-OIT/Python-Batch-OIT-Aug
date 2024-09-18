# # public
# # private
# # protected

# class MainDemo:
#     def __init__(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30


#     def fun():
#         pass


# a = MainDemo()
# print(a.a) # 10
# print(a._b) # 20
# # print(a.__c)
# # # AttributeError: 'A' object has no attribute
# # '__c'
# # '_A__c'
# print(a._MainDemo__c)


# Overriding:

class Parent:
    def giveIntro(self):
        print("Hello, I am Parent class")

    def add(self, a, b):
        print("Add: ", a+b)


class Child(Parent):
    def giveIntro(self):
        print("Hello, I am Child class")

    def add(self, nums):
        sum = 0
        for n in nums:
            sum += n
        print("Add: ", sum)


rajesh = Parent()
raju = Child()

rajesh.add(2,5)
raju.add([34,23,100,45,78])