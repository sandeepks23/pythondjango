class College:
    collegename="LT"

    def __init__(self,name,roll):
        self.roll=roll
        self.name=name
    def printDetails(self):
        print("college name",College.collegename)
        print("name of student",self.name)
        print("rollno",self.rollno)

    def __str__(self):
        return self.name+str(self.roll)

obj=College("anu",4)
print(obj)
