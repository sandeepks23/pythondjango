class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        sum=self.num1+self.num2
        print(sum)

    def sub(self):
        diff=self.num1-self.num2
        print(diff)
    def mul(self):
        prod=self.num1*self.num2
        print(prod)
    def div(self):
        res=self.num1/self.num2
        print(res)

obj=Calculator(8,2)
obj.add()
obj.sub()
obj.mul()
obj.div()
