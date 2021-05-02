import re
lst=[]
x='\w{2}\d{2}\w{2}\d{4}'
f=open("vehicle","r")
for lines in f:
    match=re.fullmatch(x,lines.rstrip("\n"))
    if match is not None:
        lst.append(lines.rstrip("\n"))
print(lst)

