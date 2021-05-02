#Linear search
lst=[10,20,21,22,23,24,33]
num=int(input("enter number"))
flag=0
for i in lst:
    if(i==num):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("found")
else:
    print("not found")

