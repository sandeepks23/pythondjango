age=int(input("enter age"))
sex=input("enter sex(m/f)")
status=input("Married(y/n)")
if(sex=='f'):
    print("she will work only in urban areas")
elif(sex=='m'):
    if((age>20)&(age<40)):
        print("He may work anywhere")
    elif((age>40)&(age<40)):
        print("he will work in urban areas only")
    else:
        print("ERROR")