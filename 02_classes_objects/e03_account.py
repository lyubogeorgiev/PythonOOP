class Account:
    def __init__(self, account_id: int, name: str, balance: float = 0):
        self.id = account_id
        self.name = name
        self.balance = balance

    def credit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def debit(self, amount: float) -> [str, float]:
        if self.balance < amount:
            return 'Amount exceeded balance'
        else:
            self.balance -= amount
            return self.balance

    def info(self) -> str:
        return f'User {self.name} with account {self.id} has {self.balance} balance'


a = Account(1, "A", 10)
print(a.id)
print(a.name)
print(a.balance)

a = Account(1, "A")
print(a.id)
print(a.name)
print(a.balance)

a = Account(123, "B", 10)
print(a.credit(10))
print(a.balance)

a = Account(333444, "X", 1000)
print(a.debit(999))
print(a.balance)

a = Account(5555, "N", 500)
print(a.debit(1000))
print(a.balance)


a = Account(4321, "ABC", 400)
print(a.info())
