birthmonth=int(input("Enter birthmonth month"))
birthdate=int(input("Enter birthdate"))
birthyear=int(input("Enter birthyear "))

prmonth=int(input("Enter present month month"))
prdate=int(input("Enter present date"))
pryear=int(input("Enter present year"))

age=pryear-birthyear
if(prmonth<birthmonth):
    age=age-1
    print(age)
elif((prmonth==birthmonth)&(prdate<birthdate)):
    age=age-1
    print(age)
else:
    print(age)