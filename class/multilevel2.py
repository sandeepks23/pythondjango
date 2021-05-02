class Parent:
    parent_name="abc"
    def m1(self,age):
        self.age=age
class Child(Parent):
    child_name="sandeep"
    def m2(self):
        print("Parent name ",Parent.parent_name)
        print("child name",Child.child_name)
class Subchild(Child):
    def m3(self):
        print("parent name",Parent.parent_name)
        print("Child name",Child.child_name)
sub=Subchild()
sub.m1(42)
sub.m2()
sub.m3()