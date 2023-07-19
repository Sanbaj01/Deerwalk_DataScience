'''
Create a class BankAccount
open account --> first_name, last_name, address, balance = 0
check balance() --> print current balance
deposit balance() --> takes deposit amount from user and deposit it in the account
withdrawl balance() --> takes withdrawl amount from the user and withdraw it from the BankAccount
check interest rate() --> displays the bank's current interest rate
print govt holidays --> displays government holidays list
'''

class BankAccount():
    __interst_rate = 12
    __bank_name = 'Bro Bank Pvt. Ltd.'

    def __init__(self, first_name, last_name, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__balance = 0

    def get_balance(self):
        return self.__balance
    
    def deposit_balance(self, deposit_amount):
        if deposit_amount <= 0:
            print('invalid amount')
            return
        self.__balance = self.__balance + deposit_amount

    def withdraw_balance(self, withdraw_amount):
        if withdraw_amount < 0:
            print('invalid amount')
        elif withdraw_amount > self.__balance:
            print(f'You can withdraw only upto {self.__balance}')
        else:
            self.__balance = self.__balance - withdraw_amount
    
    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name
    
    @classmethod
    def get_interest_rate(cls):
        return cls.__interst_rate 
    
    @classmethod
    def set_interest_rate(cls, new_rate):
        if new_rate <= 0:
            print('Invalid rate')
            return
        BankAccount.__interst_rate = new_rate
    
    @staticmethod
    def print_gov_holidays():
        print('Dashain bida is for 10 days.')
        print('Tihar holidays is for 5 days.')
    
account = None
while True:
    print('*' * 50)
    print(f'Welcome to {BankAccount.get_bank_name()}')
    user_choice = input('Enter 1 to open account. \nEnter 2 to check balance. \nEnter 3 to deposit balance. \nEnter 4 to withdraw balance. \nEnter 5 to check interest rate. \nEnter 6 to change interest rate. \nEnter 7 to list holidays.\n ')

    if user_choice == '1':
        first_name = input('Enter first name - ')
        last_name = input('Enter last name - ')
        address = input('Enter address - ')

        account = BankAccount(first_name=first_name, last_name=last_name, address=address)
        print('Yayyyy! An account has been created for you.')

    elif user_choice == '2' and account is not None:
        print(f'Current balance is {account.get_balance()}')    
    
    elif user_choice == '3' and account is not None:
        deposit_amount = int(input('Enter balance : '))
        account.deposit_balance(deposit_amount)
        print(f'Updated balance is {account.get_balance()}')
    
    elif user_choice == '4' and account is not None:
        withdrawl_amount = int(input('Enter withdrawl amount : '))
        account.withdraw_balance(withdrawl_amount)
        print(f'Updated balance is {account.get_balance()}')

    elif user_choice == '5':
        Current_rate = BankAccount.get_interest_rate()
        print(f"Bank's current interest rate is {Current_rate}")
    
    elif user_choice == '6':
        print('!!WARNING!!')
        change_rate_choice = input('Enter 0 to exit. Enter 1 to continue.')
        if change_rate_choice == '0':
            continue
        else:
            new_rate = int(input('Enter new rate : '))
            BankAccount.set_interest_rate(new_rate)
            print(f'Updated rate is {BankAccount.get_interest_rate()}')
        
    elif user_choice == '7':
        BankAccount.print_gov_holidays()
    
    elif account is None:
        print('Please open an account first.')

    else:
        print('Invalid Option')
        