class Parent:
    def marry(self):
        print("with A")

class Child(Parent):
    def marry(self):
        print("with B")
c=Parent()
c.marry()