'''
ATM
using a <class>, create an ATM
'''

class ATM:
    def __init__(self, balance = 0, interest_rate= .1, transactions = []):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions

    def check_balance(self):
         return self.balance

    def deposit(self, amount):
        self.balance += amount
        # self.transactions.append(+)
        self.transactions.append(amount)
        # print()
        
    def check_withdrawl(self, amount):
        for amount in self.balance:
            self.balance != amount
            if amount < self.balance:
                return False
            else:
                return True

    def withdrawl(self, amount):
        self.balance -= amount
        # self.transactions.append(-)
        self.transactions.append(amount)
        return self.balance

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance
    
    def call_transactions(self):
        print(self.transactions)

atm = ATM()
print("\n Welcome to Bank ATM")
while True:
    command = input("\n Select a command: ")
    if command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions- check recent transactions')
        print('exit     - exit the program')
    
    elif command == 'balance':
        my_balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${my_balance}')
    
    elif command == 'deposit':
        amount = float(input('Enter deposit amount: '))
        atm.deposit(amount)
        print(f'Deposited ${amount}')

    elif command == 'withdraw':
        amount = float(input('How much you want: '))
        if atm.check_balance():
            atm.withdrawl(amount)
            print(f'Withdrew ${amount}')
        else:
            print('Cant afford it')
    
    elif command == 'interest':
        amount = atm.calc_interest()
        # atm.deposit(amount)
        print(f"New balance is ${amount} from interest owed")
    
    elif command == 'transactions':
        print(atm.call_transactions())

    elif command == 'exit':
        break
    
    else:
        print('Command not recognized')