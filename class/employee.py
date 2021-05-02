class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def printval(self):
        print("empid:",self.empid)
        print("name:",self.name)
        print("salary:",self.salary)

obj=Employee(101,"sandeep",25000)
obj.printval()