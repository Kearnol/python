class BankAccount:
    all_accounts = []

    def __init__(self, rate=0.0, amount=0):
        self.account_balance = amount
        self.int_rate = rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        print(f"After deposit, new account balance = ${self.account_balance}")
        return self

    def withdraw(self, amount):
        if self.account_balance - amount < 0:
            print("Insufficient funds: Charging $5 fee")
            self.account_balance -= 5
            print(f"Account balance = ${self.account_balance}")
        else:
            self.account_balance -= amount
            print(f"After withdraw, account balance = ${self.account_balance}")
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self

    def yeild_interest(self):
        if self.account_balance > 0:
            self.account_balance *= (1 + self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.all_accounts:
            print(f"Balance: ${accounts.account_balance}, Interest: {accounts.int_rate}")


account1 = BankAccount(0.05, 100)
account2 = BankAccount(0.03, 100)
BankAccount.print_all_accounts()
print("")
account1.deposit(200).deposit(100).deposit(50).yeild_interest().display_account_info().withdraw(475)
account2.deposit(300).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yeild_interest().display_account_info()
print("")

