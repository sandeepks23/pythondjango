employee={
        1001:{"name":"arun","desig":"python","exp":5},
        1002:{"name":"sanjay","desig":"c++","exp":4},
        1003:{"name":"divakar","desig":"java","exp":6}
}
def emp_details(**kwargs):#kwargs={eid:1001,prop:desig}
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if(id in employee):
        print(employee[id]["name"])
        print(employee[id][prop])

emp_details(eid=1001,prop="desig")