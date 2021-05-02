num1=int(input("enter no."))
num2=int(input("enter no."))
try:
    res=num1/num2
    print("res=",res)
except:
    print("Exception occured")

finally:
    print("Program executed")