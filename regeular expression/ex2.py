#starting with a and ending with b
import re
x='(^a[a-zA-Z0-9\W]*b$)'
n=input("enter value")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
