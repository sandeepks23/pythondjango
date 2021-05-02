f=open("numbers","r")
lst=[]
for numbers in f:
    lst.append(int(numbers.rstrip("\n")))
print(lst)
print(sum(lst))

