class Person:
    def show(self,num):
        self.num=num
        print(self.num)
class Student(Person):
    def show(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("num1=",self.num1,"num2=",self.num2)
obj=Student()
obj.show(2)
