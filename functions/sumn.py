def sumN(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum

num=int(input("enter number"))
print(sumN(num))