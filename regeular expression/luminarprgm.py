import re
x='[A-Z]{3}[0-9]{2}[P][Y]\d{3}'
f=open("luminar","r")
s=open("python","w")
for lines in f:
    match=re.fullmatch(x,lines.rstrip("\n"))
    if match is not None:
        s.write(lines)
