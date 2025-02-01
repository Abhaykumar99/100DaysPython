# ============================================================
# Day 32: finally keyword & Raising Custom Errors
# ============================================================

# --- finally: ALWAYS runs (cleanup code) ---
try:
    f = open("test.txt", "w")
    f.write("Hello, World!")
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("❌ Division by zero!")
finally:
    f.close()
    print("✅ File closed (finally block ran)")

# --- try / except / else / finally ---
try:
    num = int(input("\nEnter a number: "))
    result = 100 / num
except ValueError:
    print("❌ Not a valid number!")
except ZeroDivisionError:
    print("❌ Can't divide by zero!")
else:
    # runs only if no exception occurred
    print(f"✅ 100 / {num} = {result}")
finally:
    print("🔁 This always runs.")

# --- RAISING BUILT-IN EXCEPTIONS ---
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    print(f"Age set to: {age}")

try:
    set_age(-5)
except ValueError as e:
    print(f"❌ {e}")

# --- CUSTOM EXCEPTIONS (Custom Error Classes) ---
class InsufficientFundsError(Exception):
    """Raised when bank balance is too low."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount
        super().__init__(f"Cannot withdraw ₹{amount}. Balance is ₹{balance}.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    balance = withdraw(500, 1000)
except InsufficientFundsError as e:
    print(f"❌ {e}")
