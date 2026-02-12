class BankAccount():
    bank_name = "SBI"
    bank_code = 6754
    bank_location = "Hyd"
    minimum_balance = 500
    def __init__(self, customer_name, initial_deposit=0, account_balance=0):
        self.customer_name = customer_name
        self.initial_deposit = initial_deposit
        self.account_balance = account_balance
    def withdraw(self, amount):
        if amount > 0:
            if self.account_balance - amount > BankAccount.minimum_balance:
                print("Withdraw successful", self.account_balance)
            else:
                print("Exceeding minimum balance")
        else:
            print("Invalid amount")
    def deposit(self, amount):
        if amount < 0:
            print("Invalid deposit amount")
        else:
            self.account_balance += amount
            print(self.account_balance)
    def display_account_details(self):
        print(self.customer_name,
              self.account_balance,
              self.initial_deposit,
              self.minimum_balance)
    @classmethod
    def update_minimum_balance(cls, new_min_balance):
        cls.minimum_balance = new_min_balance
        print("Updated Minimum Balance:", cls.minimum_balance)
b1 = BankAccount("Priya", 1000, 5000)
b2 = BankAccount("Neha", 500, 3000)
b1.update_minimum_balance(1000)
b1.display_account_details()
b2.display_account_details()
b1.withdraw(1500)
print(b1.account_balance, b1.initial_deposit)
