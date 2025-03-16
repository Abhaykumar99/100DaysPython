# ============================================================
# Day 75: Revision — Refactoring Old Code to Follow PEP-8
# ============================================================
# PEP-8 is Python's official style guide.
# ============================================================

"""
PEP-8 KEY RULES:
=================
1. Indentation      : 4 spaces (not tabs)
2. Max line length  : 79 characters
3. Imports          : one per line, at top of file, grouped
4. Blank lines      : 2 between top-level, 1 between methods
5. Spaces           : around operators, after commas
6. Naming           :
    - variables/functions : snake_case
    - class names         : PascalCase
    - constants           : ALL_CAPS
    - private             : _single_underscore
7. Docstrings       : for all public modules/functions/classes
8. No trailing whitespace
9. f-strings over % or .format() (Python 3.6+)
"""

# ============================================================
# BAD CODE (violates PEP-8):
# ============================================================

# BadExample — don't write code like this
class badbank:
    def __init__(self,n,b): self.name=n; self.b=b
    def deposit(self,a):
        if a>0: self.b+=a
        else: print("invalid")
    def getBalance(self): return self.b

x=badbank("alice",1000)
x.deposit(500)
print(x.getBalance())

# ============================================================
# GOOD CODE (follows PEP-8):
# ============================================================

MAX_DEPOSIT = 1_000_000   # Constant in ALL_CAPS


class BankAccount:
    """A simple bank account with PEP-8 compliant code."""

    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        """Initialize a bank account.

        Args:
            owner_name: Name of the account holder.
            initial_balance: Starting balance (default 0).
        """
        self.owner_name = owner_name
        self._balance   = initial_balance

    def deposit(self, amount: float) -> str:
        """Deposit money into the account."""
        if 0 < amount <= MAX_DEPOSIT:
            self._balance += amount
            return f"Deposited ₹{amount:.2f}. New balance: ₹{self._balance:.2f}"
        return "❌ Invalid deposit amount."

    def withdraw(self, amount: float) -> str:
        """Withdraw money from the account."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrawn ₹{amount:.2f}. Remaining: ₹{self._balance:.2f}"
        return "❌ Insufficient funds or invalid amount."

    @property
    def balance(self) -> float:
        """Return the current balance."""
        return self._balance

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner_name!r}, balance=₹{self._balance:.2f})"


# Main execution
if __name__ == "__main__":
    account = BankAccount("Alice", initial_balance=1000.0)
    print(account)
    print(account.deposit(500.0))
    print(account.withdraw(200.0))
    print(f"Balance: ₹{account.balance:.2f}")

# TOOLS FOR AUTOMATIC PEP-8:
# pip install pycodestyle  → checks PEP-8 compliance
# pip install autopep8     → auto-fixes PEP-8 issues
# pip install black        → opinionated code formatter
# pip install flake8       → linter (style + errors)
# pip install pylint       → comprehensive linter
