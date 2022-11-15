class User:		
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def make_withdraw(self, amount):	
    	self.account_balance -= amount	



Abdelhafiz = User("Mohammed Abdelhafiz", "abd@python.com" , 200)
nasri = User("Nasri Ladaa", "nasrii@python.com" , 400)
ibrahim = User("Ibrahim Ahmad", "barhoom@python.com" , 900)


Abdelhafiz.make_withdraw(70)
nasri.make_withdraw(98)
ibrahim.make_withdraw(120)



print(Abdelhafiz.name, Abdelhafiz.account_balance)
print(nasri.name , nasri.account_balance)
print(ibrahim.name , ibrahim.account_balance)

