# ============================================================
# Day 47: Constructors — __init__ method and self
# ============================================================
# __init__: called automatically when object is created.
# self: reference to the current instance of the class.
# ============================================================

class BankAccount:
    """A simple bank account class."""

    # Class variable
    bank_name = "PyBank"

    def __init__(self, owner, initial_balance=0):
        """Constructor: runs on object creation."""
        # self.attribute assigns INSTANCE attributes
        self.owner   = owner
        self.balance = initial_balance
        self._transactions = []   # private-ish list
        print(f"✅ Account created for {self.owner}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._transactions.append(("deposit", amount))
        return f"Deposited ₹{amount}. New balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"❌ Insufficient funds! Balance: ₹{self.balance}"
        self.balance -= amount
        self._transactions.append(("withdraw", amount))
        return f"Withdrew ₹{amount}. New balance: ₹{self.balance}"

    def get_statement(self):
        print(f"\n--- {self.bank_name} Statement for {self.owner} ---")
        for txn_type, amount in self._transactions:
            symbol = "+" if txn_type == "deposit" else "-"
            print(f"  {symbol} ₹{amount}")
        print(f"  Current Balance: ₹{self.balance}")

    def __str__(self):
        return f"BankAccount({self.owner}, ₹{self.balance})"

# --- CREATING INSTANCES ---
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob")          # uses default balance=0

print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.withdraw(2000))         # insufficient funds

acc1.get_statement()
print(f"\n{acc1}")
print(f"{acc2}")

# --- UNDERSTANDING self ---
# When you call: acc1.deposit(500)
# Python translates it to: BankAccount.deposit(acc1, 500)
# 'self' is the acc1 object inside the method.

# Multiple instances are INDEPENDENT
acc2.deposit(750)
print(f"\n{acc1.balance} vs {acc2.balance}")  # Different balances
