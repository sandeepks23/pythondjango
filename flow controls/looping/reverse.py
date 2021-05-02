#123
#321

num=int(input("enter the number"))
s=0
temp=num
while(temp>0):
    a=temp%10
    s=s*10+a
    temp=temp//10
print(s)

