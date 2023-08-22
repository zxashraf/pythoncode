class Bank:
    acno:int
    balance:int
    ac_type:str
    p_name:str

    def create_account(self,acno,balance,ac_type,p_name):
        self.acno=acno
        self.balance=balance
        self.ac_type=ac_type
        self.p_name=p_name
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"you sbi bank account")

    def withdraw(self,amount):
        self.balance-amount