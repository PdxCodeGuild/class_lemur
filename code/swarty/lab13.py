"""Lab 13 David Swartwood
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
Fill in the methods for the ATM class:
"""
import datetime
class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.int=interest_rate
        self.balance=balance
        self.accounting=''

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance+=amount
        self.accounting += f'{datetime.datetime.now()}\nDeposit ${amount}\nBalance ${self.balance}\n'

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if self.balance>=amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount
        self.accounting += f'{datetime.datetime.now()}\nWithdrawl ${amount}\nBalance ${self.balance}\n'

    def calc_interest(self):
        """calculate and return interest gained on account"""
        interest=self.balance*.01
        self.balance+=interest
        self.accounting += f'{datetime.datetime.now()}\nInterest Accrued ${interest}\nBalance ${self.balance}\n'
        return interest

    def history(self):
        return self.accounting

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
    elif command == 'history':
        print(atm.history())

    elif command == 'help':
        print('Available commands:')
        print('balance  - get current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history - Get account history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')