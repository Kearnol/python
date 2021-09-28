class User:
    all_accounts = []
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_addres = email_address
        self.accounts = {
            "checking": BankAccount(0.02, 0),
            "saving": BankAccount(0.02, 0),
            "investment": BankAccount(0.02, 0)
        }
        User.all_accounts.append(self)

    def make_deposit(self, amount, bankID="checking"):
        self.accounts[bankID].deposit(amount)
        return self

    def make_withdrawal(self, amount, bankID="checking"):
        self.accounts[bankID].withdraw(amount)
        return self
        
    def display_user_balance(self, bankID="checking"):
        print(f"User {self.first_name} {self.last_name}'s Balance is: ${self.accounts[bankID].account_balance}")
        return self
    
    def transfer_money(self, other_user, amount, bankIDfrom="checking", bankIDto="saving"):
        self.make_withdrawal(amount, bankIDfrom)
        other_user.make_deposit(amount, bankIDto)
        print("After transfer:")
        self.display_user_balance()
        other_user.display_user_balance()
        print("Transfer end.")
        return self

    @classmethod
    def print_all_account_data(cls):
        for x in cls.all_accounts:
            print(f"{x.first_name} {x.last_name} | Account Balances:")
            for key, value in x.accounts.items():
                print(key, value.account_balance)

    

class BankAccount:
    all_accounts = []

    def __init__(self, rate=0.0, amount=0):
        self.account_balance = amount
        self.int_rate = rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance - amount < 0:
            print("Insufficient funds: Charging $5 fee")
            self.account_balance -= 5
            print(f"Account balance = ${self.account_balance}")
        else:
            self.account_balance -= amount
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

#make Users:
devin = User("Devin","Kearns","dkearn@fake.com")
troy = User("Troy", "Mild", "TMild@fake.com")
bob = User("Bob", "Lanchuck", "BobyFlay@yahooper.com")

print(f"Account = {bob.accounts}")

# bob.make_deposit(200, "checking").display_user_balance()

#Process Transactions
devin.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(300).display_user_balance().transfer_money(troy,200, "checking", "investment")
troy.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(75).display_user_balance()
bob.make_deposit(500).make_withdrawal(175).make_withdrawal(100).make_withdrawal(25).display_user_balance()

#Print Account details
User.print_all_account_data()