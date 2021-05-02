#employee
employee={"id":1001,"ename":"sandeep","designation":"manager","salary":50000}
print(employee["ename"])
print("company" in employee)
employee["company"]="luminar"
employee["salary"]+=50000
for i in employee:
    print(i,":",employee[i])