class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount

    def print(self):
        print(f"Current balance: ${self.balance}, Interest Rate: {self.interest_rate}%")


# Create an instance of BankAccount
bank_account = BankAccount("123456789", "John Doe")

# Perform a deposit of $1000
bank_account.deposit(1000)
print("After deposit of $1000, current balance:", bank_account.get_balance())

# Perform a withdrawal of $500
bank_account.withdraw(500)
print("After withdrawal of $500, current balance:", bank_account.get_balance())

# Create an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "Jane Doe", 5)  # 5% interest rate

# Perform a deposit of $2000
savings_account.deposit(2000)
print("\nAfter deposit of $2000, current balance and interest rate:")
savings_account.print()

# Apply interest
savings_account.apply_interest()
print("\nAfter applying interest, current balance and interest rate:")
savings_account.print()
