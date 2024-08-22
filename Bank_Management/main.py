from Bank import person,User,admin,Bank

def main_page():
    print(f'Main Page:')
    print(f'press 1 for sign up as a user')
    print(f'press 2 for sign up as a admin')
    print(f'press 3 for log in')
    print(f'press 4 for log out')

def login(bank):
    print(f'Please Log in')
    print(f'press 1 for user')
    print(f'press 2 for admin')
    op=int(input('Enter your option:'))
    u=None
    if op==1:
        ck=False
        e=input('Enter your email:')
        p=input('Enter your password:')
        for acc in bank.accounts:
            if acc.email==e and acc.password==p:
                ck=True
                u=acc
                print(f'Logged in successfully.')
                break
        if ck==False:
            main_page()
        else:
            print(f'1.Deposite Money')
            print(f'2.withdraw amount:')
            print(f'3.check balance')
            print(f'4.check transation history')
            print(f'5.take loan')
            print(f'6.transfer money')
            print(f'7.back to main page')
            while(True):
                opp=int(input('Enter the option:'))
                if opp==1:
                    amt=int(input('Enter the amount:'))
                    u.deposite(amt,bank)
                elif opp==2:
                    amt=int(input('Enter the amount:'))
                    u.withdraw(amt,bank)
                elif opp==3:
                    u.check_balance()
                elif opp==4:
                    u.History()
                elif opp==5:
                    amt=int(input('Enter the amount:'))
                    u.take_loan(amt,bank)
                elif opp==6:
                    accno=input('Enter the account number:')
                    amt=int(input('Enter the amount:'))
                    ck=False
                    for acc in bank.accounts:
                        if acc.accountNo==accno:
                            u.tansfer(acc,bank,amt)
                            ckk=True
                    if ck==False:
                        print(f'Account does not exist')
                else:
                    main_page()
                    break
    elif op==2:
        ck=False
        e=input('Enter your email:')
        p=input('Enter your password:')
        if bank.admin.email==e and bank.admin.password==p:
            u=bank.admin
            ck=True
            print(f'Admin Logged in successfully.')

        if ck==False:
            main_page()
        else:
            print(f'1.delete user account')
            print(f'2.see all user account')
            print(f'3.total balance of the bank:')
            print(f'4.total loan amount')
            print(f'5.change loan feature')
            print(f'6.back to main page')
            while(True):
                opp=int(input('Enter your option:'))
                if opp==1:
                    accno=input('Enter your account no:')
                    u.delet_account(accno,bank)
                elif opp==2:
                    u.user_account_list(bank)
                elif opp==3:
                    u.available_balance(bank)
                elif opp==4:
                    u.loan_amount(bank)
                elif opp==5:
                    status=input('Loan Feature (on/off):')
                    u.change_loan_feather(bank,status)
                else:
                    main_page()
                    break

def main():
    print(f'Main Function Started.........')
    bank=Bank('Sonali Bank Ltd')
    main_page()
    while(True):
        option=int(input('Enter the option:'))
        if option==1:
            # name,email,password,address,accountType
            n=input('Enter your name:')
            e=input('Enter your email:')
            p=input('Enter your password:')
            a=input('Enter your address:')
            at=input('Enter your account type:(Savings/Cuurent)')
            bank.create_account(n,e,p,a,at)
            login(bank)
        elif option==2:
            n=input('Enter your name:')
            e=input('Enter your email:')
            p=input('Enter your password:')
            bank.create_admin(n,e,p)
            login(bank)
        elif option==3:
            login(bank)
        else:
            break

if __name__=='__main__':
    main()