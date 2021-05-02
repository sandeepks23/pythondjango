class Employee:
    def __init__(self,name,empid):
        self.empid=empid
        self.name=name
    def printDetails(self):
        print("empid", self.empid)
        print("name of employee",self.name)

    def __str__(self):
        return str(self.empid)

emp=Employee("sandeep",101)
print(emp)
