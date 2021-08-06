'''
ATM
using a <class>, create an ATM
'''

class ATM:
    def __init__(self, balance = 0, interest_rate= -.4):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        print()
        
    def check_withdrawl(self, amount):
        for amount in self.balance:
            

    def withdrawl(self, amount):
        self.balance -= amount
        print(self.balance)

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        print(interest)

atm = ATM()
print("Welcome to Communist Chase ATM")
while True:
    command = input("Select a command: ")
    if command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    
    elif command == 'deposit':
        amount = float(input('Enter deposit amount: '))
        atm.deposit(amount)
        print(f'Deposited ${amount}')

    elif command == 'withdraw':
        amount = float(input('How much you want: '))
        if atm.check_balance(amount):
            atm.withdrawl(amount)
            print(f'Withdrew ${amount}')
        else:
            print('Cant afford it')
    elif command == 'interest':
        amount = atm.calc_interest()
        atm.deposit(amount)
        print(f"Managed ${amount} in interest")
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
