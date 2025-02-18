# ============================================================
# Day 49: Getters and Setters using @property
# ============================================================
# @property provides controlled access to attributes.
# Avoids direct attribute modification.
# ============================================================

class Temperature:
    """Temperature class with Celsius and Fahrenheit conversion."""

    def __init__(self, celsius=0):
        self._celsius = celsius    # Convention: _ means "private"

    # Getter: access like an attribute (no parentheses)
    @property
    def celsius(self):
        return self._celsius

    # Setter: validates before setting
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible!")
        self._celsius = value

    # Deleter
    @celsius.deleter
    def celsius(self):
        print("Deleting temperature...")
        del self._celsius

    # Derived property (read-only)
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15

    def __str__(self):
        return f"{self._celsius}°C = {self.fahrenheit:.2f}°F = {self.kelvin:.2f}K"

# Usage
t = Temperature(25)
print(t)
print(f"Celsius   : {t.celsius}")
print(f"Fahrenheit: {t.fahrenheit}")
print(f"Kelvin    : {t.kelvin}")

t.celsius = 100             # Uses the setter
print(f"\nBoiling point: {t}")

try:
    t.celsius = -300        # ← raises ValueError
except ValueError as e:
    print(f"❌ {e}")

# --- WITHOUT @property (bad way) ---
class BadAccount:
    def __init__(self):
        self.balance = 0    # Direct access — no validation!

# --- WITH @property (good way) ---
class GoodAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount

acc = GoodAccount()
acc.balance = 500
print(f"\nAccount balance: ₹{acc.balance}")
try:
    acc.balance = -100
except ValueError as e:
    print(f"❌ {e}")
