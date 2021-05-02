class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)

f=open("student","r")
for lines in f:
    data=lines.split(",")

    name=data[0]
    age=data[1]
    obj=Student(name,age)
    obj.printval()


