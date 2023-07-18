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
    __bank_name = 'Bro Bank'

    def __init__(self, first_name, last_name, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__balance = 0

    def get_balance(self):
        return self.balances
    
    def deposit_balance(self, deposit_amount):
        if deposit_amount <= 0:
            print('invalid amount')
            return
        self.__balance

        