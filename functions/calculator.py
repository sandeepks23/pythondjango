#calculator
def add(num1,num2):
    sum=num1+num2
    return sum
def sub(num1,num2):
    diff=num1-num2
    return diff
def mul(num1,num2):
    pro=num1*num2
    return pro
def div(num1,num2):
    res=num1/num2
    return res
num1=int(input("enter num1"))
num2=int(input("enter num2"))
print("1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division")
choice=int(input("enter your choice"))
if(choice==1):
    print(add(num1,num2))
elif(choice==2):
    print(sub(num1,num2))
elif(choice==3):
    print(mul(num1,num2))
elif(choice==4):
    print(div(num1,num2))