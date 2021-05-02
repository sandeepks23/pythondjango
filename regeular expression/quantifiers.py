import re

x="a$"
r="aaa abc aaaa cya"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
