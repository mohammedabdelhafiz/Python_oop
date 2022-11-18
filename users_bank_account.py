class BankAccount:
    def __init__(self, first_name, balance):
        self.name = first_name
        self.balance = balance




    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -=amount
        return self

    def display_account_info(self):
        print("Balance:" , self.balance)




ahmad_account = BankAccount("Ahmad",2550)
tayseer_account=BankAccount("Tayseer",3220)

ahmad_account.withdraw(500).deposit(400)
ahmad_account.deposit(2000)
tayseer_account.deposit(3500)
y=ahmad_account.balance
z=tayseer_account.balance
print(y , z)
