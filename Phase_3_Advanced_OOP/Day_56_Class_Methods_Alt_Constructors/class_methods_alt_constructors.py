# ============================================================
# Day 56: Class Methods and Alternative Constructors
# ============================================================
# @classmethod: receives the CLASS (cls) instead of instance (self)
# Used for factory methods / alternative constructors
# ============================================================

class Date:
    """Date class demonstrating class methods as alternate constructors."""

    def __init__(self, day, month, year):
        self.day   = day
        self.month = month
        self.year  = year

    @classmethod
    def from_string(cls, date_str):
        """Alternate constructor: create Date from 'DD-MM-YYYY' string."""
        day, month, year = map(int, date_str.split("-"))
        return cls(day, month, year)

    @classmethod
    def today(cls):
        """Alternate constructor: create Date from current date."""
        from datetime import date
        t = date.today()
        return cls(t.day, t.month, t.year)

    @staticmethod
    def is_valid_date(day, month, year):
        """Validate a date (static — no class or instance needed)."""
        return 1 <= month <= 12 and 1 <= day <= 31 and year > 0

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"

# Normal constructor
d1 = Date(20, 2, 2026)
print("Normal:", d1)

# Alternative constructors via class methods
d2 = Date.from_string("15-08-1947")
print("From string:", d2)

d3 = Date.today()
print("Today:", d3)

print("Valid?", Date.is_valid_date(31, 13, 2024))  # False
print("Valid?", Date.is_valid_date(15, 8, 1947))   # True

# --- Singleton pattern using class method ---
class Config:
    _instance = None

    def __init__(self):
        self.debug   = False
        self.version = "1.0.0"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

cfg1 = Config.get_instance()
cfg2 = Config.get_instance()
print(f"\nSame object? {cfg1 is cfg2}")   # True (singleton)
