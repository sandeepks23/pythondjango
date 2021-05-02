#dictionary
student1={"roll":1001,"name":"arun","age":25,"cpp":30}      #does not support duplicate key
print(student1)
print(student1["age"])
for i in student1:
    print(i,":",student1[i])

del student1["cpp"]
print(student1)
print("age" in student1)

student1["total"]=150
print(student1)