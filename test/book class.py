import re
x='[A-Z]{1}[a-z]+'
n=input("enter value")
matcher=re.finditer(x,n)
for match in matcher:
    print(match.start())
    print(match.group())

