class person:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

class User(person):
    def __init__(self,name,email,password,address,accountType):
        super().__init__(name,email,password)
        self.address=address
        self.accountType=accountType
        self.accountNo= self.name+self.email
        self.balance=0
        self.loan=0
        self.depositebal=0
        self.withdrawbal=0
    
    def deposite(self,amount,bank):
        if amount>0:
            self.balance=self.balance+amount
            self.depositebal=self.depositebal+amount
            bank.balance=bank.balance+amount
            print(f'Successfully deposite.')
    
    def withdraw(self,amount,bank):
        if bank.bankrupt==True:
            print(f'The bank is bankrupt.')
        elif amount>self.balance:
            print(f'You have not enough balance to withdraw.')
        else:
            self.balance=self.balance-amount
            self.withdrawbal=self.withdrawbal+amount
            bank.balance=bank.balance-amount
            print(f'Successfully withdraw.')
    
    def check_balance(self):
        print(f'Your account balance is {self.balance}')
    
    def History(self):
        print(f'Your Total Deposite Amount is {self.depositebal}')
        print(f'Your Total Withdraw Amount is {self.withdrawbal}')
    
    def take_loan(self,amount,bank):
        if bank.loan=='off':
            print(f'This bank can not give loan.')
        elif self.loan<2:
            self.balance=self.balance+amount
            bank.loan_amount=bank.loan_amount+amount
            self.loan=self.loan+1
            print(f'loan get successfully.')
        else:
            print(f'You can not get loan.')

    def tansfer(self,user,bank,amount):
        if bank.bankrupt==True:
            print(f'The bank is bankrupt.')
        elif user not in bank.accounts:
            print(f'This account is not exists.')
        elif amount>self.balance:
            print(f'Withdrawal amount exceeded')
        else:
            user.balance=user.balance+amount
            user.depositebal=user.depositebal+amount
            self.balance=self.balance-amount
            self.withdrawbal=self.withdrawbal+amount
            print(f'Transfer Successfully.')

class admin(person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    
    def delet_account(self,useraccno,bank):
        dell=False
        for acnt in bank.accounts:
            if acnt.accountNo==useraccno:
                bank.accounts.remove(acnt)
                dell=True
                print(f'account deleted successfully.')
        if dell==False:
            print(f'account does not exists.')
    
    def user_account_list(self,bank):
        if len(bank.accounts)>0:
            print(f'Account Lists:')
            for acnt in bank.accounts:
                print(f'User Name:{acnt.name},Account type:{acnt.accountType}')
        else:
            print(f'Have no account.')
    
    def available_balance(self,bank):
        print(f'The available balance of the Bank is :{bank.balance}')
    
    def loan_amount(self,bank):
        print(f'The Total loan amount is :{bank.loan_amount}')
    
    def change_loan_feather(self,bank,status):
        bank.loan=status
    
    def change_bank_status(self,bank,status):
        bank.bankrupt=status

class Bank:
    def __init__(self,name):
        self.name=name
        self.accounts=[]
        self.balance=0
        self.loan_amount=0
        self.loan='on'
        self.bankrupt=False
        self.admin=None
    
    def create_account(self,name,email,password,address,accountType):
        user=User(name,email,password,address,accountType)
        self.accounts.append(user)
        print(f'account created successfully.')
    
    def create_admin(self,name,email,password):
        adm=admin(name,email,password)
        self.admin=adm
        print(f'Admin added successfully.')

