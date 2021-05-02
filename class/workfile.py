class Employee:
    def __init__(self,name,roll,course,mark):
        self.name=name
        self.roll=roll
        self.course=course
        self.mark=mark
    def printVal(self):
        print("name:",self.name)
        print("rollno:",self.roll) 
        print("course",self.course)
        print("mark:",self.mark)
f=open("work","r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    roll=data[1]
    course=data[2]
    mark=int(data[3])
    emp=Employee(name,roll,course,mark)
    if(mark>190):
        emp.printVal()


