import re

x="[^abc]"   #either a,b or c
matcher=re.finditer(x,"abt AVc@5kz")
for match in matcher:
    print(match.start())
    print(match.group())
