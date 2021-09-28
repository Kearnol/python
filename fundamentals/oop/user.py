class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_addres = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
        
    def display_user_balance(self):
        print(f"User {self.first_name} {self.last_name}'s Balance is: ${self.account_balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("After transfer:")
        self.display_user_balance()
        other_user.display_user_balance()
        print("Transfer end.")
        return self

devin = User("Devin","Kearns","dkearn@fake.com")
troy = User("Troy", "Mild", "TMild@fake.com")
bob = User("Bob", "Lanchuck", "BobyFlay@yahooper.com")

devin.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(300).display_user_balance().transfer_money(bob, 100)
troy.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(75).display_user_balance()
bob.make_deposit(500).make_withdrawal(175).make_withdrawal(100).make_withdrawal(25).display_user_balance()


