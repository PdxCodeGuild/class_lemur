# Class Lemur Day Course
# Lab 13, ATM
# Scott Cormack
# Python 3.9.6

class ATM:
    def __init__(self, balance=0, interest_rate=0.1, transactions=[]):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions

    def check_balance(self):
        """return the account balance"""
        self.transactions.append('Checked balance.')
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount
        self.transactions.append(f'Deposited ${amount}.')
        return self.balance

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        funds = False
        if self.balance >= amount:
            funds = True
        return funds
        

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance = self.balance - amount
        self.transactions.append(f'Withdrew ${amount}')
        return self.balance

    def calc_interest(self):
        """calculate and return interest gained on account"""
        int_amount = (self.balance * self.interest_rate) / 100
        return int_amount

    def print_transactions(self):
        """Display transactions made during banking session"""
        print(self.transactions)



atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        atm.print_transactions()
        break
    else:
        print('Command not recognized')