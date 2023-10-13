"""
Define a new class called BankAccount
- Each BankAccount should have an owner, specified when a new BankAccount is
created like BankAccount("Charlie")
- Each BankAccount should have a balance attribute that always starts out as
0.0
- Each instance should have a deposit method that accepts a number and adds it
to the balance - It should return the new balance
- Each instance should have a withdraw method that accepts a number and
subtracts it from the balance - It should return the new balance
- The following code should work:
    acct = BankAccount("Darcy")
    acct.owner  # Darcy
    acct.balance  # 0.0
    acct.deposit(10)  # 10.0
    acct.withdraw(3)  # 7.0
    acct.balance  # 7.0
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount: int | float) -> float:
        self.balance += deposit_amount
        return self.balance

    def withdraw(self, withdraw_amount: int | float) -> float:
        self.balance -= withdraw_amount
        return self.balance


acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)
