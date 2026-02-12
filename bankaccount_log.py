import logging

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BankAccount:
    bank_name = "SBI"
    bank_code = 6754
    bank_location = "Hyd"
    minimum_balance = 500

    def __init__(self, customer_name, initial_deposit=0, account_balance=0):
        self.customer_name = customer_name
        self.initial_deposit = initial_deposit
        self.account_balance = account_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            logging.error("Invalid withdraw attempt: %s", amount)
        elif self.account_balance - amount >= BankAccount.minimum_balance:
            self.account_balance -= amount
            print("Withdraw successful:", self.account_balance)
            logging.info("Withdraw successful: %s", self.account_balance)
        else:
            print("Exceeding minimum balance")
            logging.error("Exceeding minimum balance. Current balance: %s", self.account_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            logging.warning("Invalid deposit attempt: %s", amount)
        else:
            self.account_balance += amount
            print("Deposit successful:", self.account_balance)
            logging.info("Deposit successful: %s", self.account_balance)

    def display_account_details(self):
        print(self.customer_name,
              self.account_balance,
              self.initial_deposit,
              self.minimum_balance)

    @classmethod
    def update_minimum_balance(cls, new_min_balance):
        cls.minimum_balance = new_min_balance
        print("Updated Minimum Balance:", cls.minimum_balance)
        logging.info("Minimum balance updated to: %s", cls.minimum_balance)


b1 = BankAccount("Priya", 1000, 5000)
b2 = BankAccount("Neha", 500, 3000)

b1.update_minimum_balance(1000)
b1.display_account_details()
b2.display_account_details()

b1.withdraw(-1500)  
b1.withdraw(4500)   
b1.withdraw(3000)   

b1.deposit(-500)    
b1.deposit(1000)    

print(b1.account_balance, b1.initial_deposit)
