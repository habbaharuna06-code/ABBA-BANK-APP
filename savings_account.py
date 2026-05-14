from Account import Account


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02, withdraw_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdraw_limit = withdraw_limit

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} applied.")

    
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal denied: Amount exceeds withdraw limit of ${self.withdraw_limit}.")
        elif 0 < amount <= self.get_balance():
            super().withdraw(amount)
        else:
            print("Invalid withdrawal amount or insufficient funds.")


print("--- Savings Account ---")
savings = SavingsAccount("Alice", 1000)
print(f"Initial balance: ${savings.get_balance()}\n")


print("Test 1: Withdraw $50 (within $100 limit)")
savings.withdraw(50)
print(f"Balance: ${savings.get_balance()}\n")


print("Test 2: Withdraw $100 (at the limit)")
savings.withdraw(100)
print(f"Balance: ${savings.get_balance()}\n")


print("Test 3: Attempt to withdraw $150 (exceeds $100 limit)")
savings.withdraw(150)
print(f"Balance: ${savings.get_balance()}\n")


print("Test 4: Attempt to withdraw $200 (more than balance)")
savings.withdraw(200)
print(f"Balance: ${savings.get_balance()}\n")


print("Test 5: Apply interest")
savings.apply_interest()
