class Account(object):
    def __init__(self, holder, number, balance):
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance

    def deposit(self, amount):
        self.__Balance += amount

    def withdraw(self, amount):
        self.__Balance -= amount

    def balance(self):
        return self.__Balance


ben = Account('B FRANKLIN', 5478936, 45000)
print(ben.balance())

ben.deposit(500)
print(ben.balance())

