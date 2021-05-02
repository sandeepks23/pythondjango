#3rd method
def factorial3(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
print(factorial3(3))

#2nd method
def factorial2(num):
    f = 1
    for i in range(1, num + 1):
        f=f*i
    print(f)
factorial2(5)

#1st method

def factorial1():
    num=int(input("enter number"))
    f=1
    for i in range(1,num+1):
        f=f*i
    print(f)
factorial1()


