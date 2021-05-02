lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
eve=0
odd=0
for i in range(lower,upper+1):
    if(i%2==0):
        eve=eve+i
    else:
        odd=odd+i

print("Even number sum",eve)
print("odd number sum",odd)