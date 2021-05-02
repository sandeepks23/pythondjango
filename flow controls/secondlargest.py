num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print(num2,"is second highest")
    else:
        print(num3,"is second highest")

elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print(num1, "is second highest")
    else:
        print(num3, "is second highest")

elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print(num1,"is second highest")
    else:
        print(num2,"is second highest")
