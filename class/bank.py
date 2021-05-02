class Bank:
    bname="sbi"        #static variable
    def accCreat(self,accno,name):
        self.accno=accno
        self.name=name

        self.minimum=5000
        self.balance=self.minimum
    def deposit(self,amt):
        self.balance+=amt
        print("Your",Bank.bname," account is credited with",amt)
        print("Balance is ",self.balance)
    def withdraw(self,amt):
        if(amt>self.balance):
            print("Insufficient balance")
        else:
            print("account debited with",amt)
            self.balance-=amt
            print("Balance is ",self.balance)

obj=Bank()
obj.accCreat(101,"sandeep")
obj.deposit(5000)
obj.withdraw(1000)


