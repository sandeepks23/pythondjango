lst=[1,2,3,4,5,6]
num=int(input("enter number"))
for i in lst:
    for j in lst:
        if((i+j)==num):
            print((i,j))