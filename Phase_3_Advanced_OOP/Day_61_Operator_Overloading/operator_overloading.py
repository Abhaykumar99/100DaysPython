# ============================================================
# Day 61: Operator Overloading — Adding Two Objects
# ============================================================
# Customize how Python operators work on your custom objects.
# ============================================================

class Fraction:
    """Fraction class with full operator overloading."""

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")
        from math import gcd
        g = gcd(abs(numerator), abs(denominator))
        self.num = numerator // g
        self.den = denominator // g

    def __str__(self):
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den,
                        self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self == other or self < other

    def __float__(self):
        return self.num / self.den

a = Fraction(1, 2)
b = Fraction(1, 3)

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a == b: {a == b}")
print(f"a > b : {a > b}")
print(f"float(a) = {float(a)}")

fractions = [Fraction(3,4), Fraction(1,2), Fraction(2,3), Fraction(1,4)]
print(f"\nSorted: {sorted(fractions)}")
