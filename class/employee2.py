class Employee:
    cname="luminar"
    def insert(self,empid,ename,salary):
        self.empid=empid
        self.ename=ename
        self.salary=salary
    def printval(self):
        print("Employee name:",self.ename)
        print("Employee id:",self.empid)
        print("company name:   ",Employee.cname)
        print("Salary:",self.salary)
emp=Employee()
emp.insert(101,"sandeep",10000)
emp.printval()