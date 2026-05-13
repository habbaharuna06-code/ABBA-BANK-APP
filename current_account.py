from Account import Account

class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    # Polymorphism: Different implementation of withdraw
    def withdraw(self, amount):
        available_funds = self.get_balance() + self.overdraft_limit
        if 0 < amount <= available_funds:
            # Note: We'd need a protected setter or specialized logic
            # to handle negative balances in a real app
            print(f"Withdrawal of ${amount} approved (using overdraft if necessary).")
            # Logic simplified for demonstration
        else:
            print("Withdrawal denied: Exceeds overdraft limit.")
print("\n--- Current Account ---")
current = CurrentAccount("Bob", 100)
current.withdraw(400) # This would fail in a standard Account but works here