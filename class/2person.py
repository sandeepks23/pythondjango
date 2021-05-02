class Person:
    def setVal(self,name,age):
        self.age=age
        self.name=name
    def printValue(self):
        print("name:",self.name)
        print("age:",self.age)
obj=Person()
obj.setVal('ram',23)
obj.printValue()