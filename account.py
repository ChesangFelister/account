class Account:
    def __init__(self,first_name,second_name):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0.00
        
        
    def greetings(self):
            return"Hello {} {} welcome to the your banking account you balance is{}".format(self.first_name,self.second_name,self.balance)

    def deposit(self,x):
        self.balance=self.balance+x
        return("you have deposited {}".format(x))

    def withdraw(self,v):
        if v < self.balance:
            self.balance=self.balance-v
       
            return("Hello {} {} you have successfully withdrawn  {}".format(self.first_name,self.second_name,v))
        else:
            return("Hello {} {} you have insufficient balance".format(self.first_name,self.second_name,v))