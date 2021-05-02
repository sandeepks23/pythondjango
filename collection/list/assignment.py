lst=[5,10,20]
lst1=[]
sum=0
diff=0
for i in lst:
    sum=sum+i
for i in lst:
    diff=sum-i
    lst1.append(diff)
print(lst1)