class Parent:
    def m1(self):
        print("Inside parent class")
class Child(Parent):
    def m2(self):
        print("Inside Child class")
class Subchild(Child):
    def m3(self):
        print("Inside Subchild class")

sub=Subchild()
sub.m1()
sub.m2()
sub.m3()