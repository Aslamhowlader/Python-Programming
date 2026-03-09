class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    # Getter for owner
    @property
    def owner(self):
        return self.__owner

    # Getter for balance
    @property
    def balance(self):
        return self.__balance

    # Setter for balance (deposit)
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance += amount  # deposit
        else:
            print("Balance can't be negative")

ob = BankAccount("Aslam", 500)
print(ob.owner)    # Aslam
print(ob.balance)  # 500

ob.balance = 200   # deposit 200
print(ob.balance)  # 700

ob.balance = -50   # Balance can't be negative