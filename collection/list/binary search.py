lst=[3,5,11,22,2,6,13]
lst.sort()
print(lst)
low=0
upper=len(lst)-1
element=int(input("enter element to "))
flag=0
while(low<=upper):
    mid=(low+upper)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upper=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag==1):
    print("element found")
else:
    print("element not found")