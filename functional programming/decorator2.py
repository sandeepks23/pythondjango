def decorator_div(fun):
    def wrapper(num1,num2):
        if(num1<num2):
            (num1,num2)=(num2,num1)
        return fun(num1,num2)
    return wrapper

@decorator_div
def div(num1,num2):
    return num1/num2

res=div(2,50)
print(res)