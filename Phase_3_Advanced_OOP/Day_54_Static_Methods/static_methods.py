# ============================================================
# Day 54: Static Methods using @staticmethod
# ============================================================
# Static methods: belong to the class, NOT to any instance.
# No 'self' or 'cls' parameter.  Called on class or instance.
# Use when logic is related to the class but doesn't need class/instance state.
# ============================================================

class MathUtils:
    """Utility class with purely static methods."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# Called on class (no instance needed):
print(MathUtils.add(3, 4))
print(MathUtils.is_prime(17))
print(MathUtils.factorial(6))

# Can also be called on an instance (but unnecessary):
m = MathUtils()
print(m.add(10, 20))

# --- COMPARISON: static vs class vs instance method ---
class MyClass:
    class_var = "I am a class variable"

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        """Has access to instance (self) and class."""
        return f"Instance: {self.value}, Class: {MyClass.class_var}"

    @classmethod
    def class_method(cls):
        """Has access to class but NOT instance."""
        return f"Class var: {cls.class_var}"

    @staticmethod
    def static_method():
        """No access to instance OR class. Pure utility."""
        return "I am a static method!"

obj = MyClass(42)
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())

# --- REAL WORLD: Date validator ---
class DateValidator:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if month == 2 and DateValidator.is_leap_year(year):
            return 29
        return days[month - 1]

print(f"\n2024 leap year? {DateValidator.is_leap_year(2024)}")
print(f"Feb 2024 days? {DateValidator.days_in_month(2, 2024)}")
