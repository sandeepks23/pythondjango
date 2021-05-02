#multiple inheritance
class Parent():
    parent_name="Arun"
    def m1(self,age):
        self.age=age
        print("My name is ",Parent.parent_name)
        print(self.age)

class Mobile:
    def mob(self):
        print("I have a poco")

class Child(Parent,Mobile):
    def m2(self):
        print("Parent name is ",Parent.parent_name)
        print(self.age)

c=Child()
c.m1(23)
c.m2()
c.mob()