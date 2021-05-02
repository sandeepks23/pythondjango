class Student:
    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(1,"sandeep","btech",240)
s2=Student(2,"alan","bca",210)
s3=Student(3,"allen","bcom",230)
student=[]
student.append(s1)
student.append(s2)
student.append(s3)
studtotal=list(map(lambda stud:stud.total,student))
print(studtotal)
print(max(studtotal))
