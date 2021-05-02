#2 Function with argument and no return type
def addition(num1,num2):
    sum=num1+num2
    print(sum)
addition(50,30)

def difference(num1,num2):
    diff=num1-num2
    print(diff)

def multiplication(num1,num2):
    mul=num1*num2
    print(mul)
difference(50,30)
multiplication(50,30)

#3 Function with argument and return type
def sumN(num1,num2):
    sum=num1+num2
    return sum
print(sumN(30,80))

def diffN(num1,num2):
    diff=num1-num2
    return diff
print(diffN(30,80))

def mulN(num1,num2):
    pro=num1+num2
    return pro
print(mulN(30,80))
