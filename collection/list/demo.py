#list
lst=[]  #square bracket #empty list
st=list()
print(type(lst))
print(type(st))

lst1=[10,10.5,"sandeep",True]   #support heterogeneous data
print(lst1)

lst2=[10,10,10,'sandeep']  #support duplicate values
print(lst2)

lst3=[10,23,33,11,44]
#0 to n-1
#index value
print(lst3[1],lst3[0])
lst3[0]=11  #mutable
print(lst3)
lst3[4]="sandeep"
print(lst3)