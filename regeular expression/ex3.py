import re
x='[a-zA-z]{8,15}'
n=input("enter value")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
