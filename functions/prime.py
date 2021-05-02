def prime(num):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
        else:
            flag=0
    if(flag==0):
        print("Prime")
    else:
        print("not prime")

num=int(input("enter number"))
prime(num)