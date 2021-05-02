class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def printval(self):
        print("Name",self.name)
        print("age",self.age)
obj=Person("sandeep",22)
obj.printval()