#to return list with only salary
class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def printDet(self):
        print(self.ename)
f=open("emplo","r")
employee=[]

for lines in f:
    data=lines.rstrip("\n").split(",")
    eid=data[0]
    ename=data[1]
    desig=data[2]
    salary=data[3]
    emp=Employee(eid,ename,desig,salary)
    employee.append(emp)

    salary=list(map(lambda e:e.salary,employee))
    designation=list(filter(lambda e:e.desig=="qa",employee))
print(designation)

