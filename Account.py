class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        # Encapsulation: Making balance private
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive and greater than zero.")

    def withdraw(self, amount):
        """Base withdraw method to be overridden (Polymorphism)"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        """Public getter for the private __balance"""
        return self.__balance



