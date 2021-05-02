class Manager:
    mname="Sandeep"
    def mval(self,mid,age,salary):
        self.mid=mid
        self.age=age
        self.salary=salary
        print("Manager name",Manager.mname)
        print(self.mid)
        print(self.age)
        print(self.salary)
class Employee(Manager):
    ename="arun"
    def eval(self,empid,eage,esalary):
        self.empid=empid
        self.eage=eage
        self.esalary=esalary
        print("employee name",Employee.ename)
        print("Manager name",Manager.mname)
        print(self.empid)
        print(self.eage)
        print(self.esalary)
emp=Employee()
emp.mval(101,27,35000)
emp.eval(201,20,20000)