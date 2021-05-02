class Person:
    def m1(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Student(Person):         #single inheritance
    def m2(self,stid,mark):
        self.stid=stid
        self.markmark
        print(self.name)
        print(self.stid)
        print(self.age)
        print(self.mark)

class Child(Student):          #multilevel inheritance
    def m3(self):
        print(self.stid)
        print(self.age)

class Employee(Person,Student):   #multiple inheritance
    def m4(self,empid,salary):
        self.empid=empid
        self.salary=salary
        print(self.empid)
        print(self.name)
        print(self.age)
        print(self.mark)
        print(self.salary)


