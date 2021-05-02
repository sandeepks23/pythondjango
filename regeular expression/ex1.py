#combination of uppercase and lower case ending with a number
import re
x='[a-zA-Z]+\d{1}$'
n=input("enter value")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")