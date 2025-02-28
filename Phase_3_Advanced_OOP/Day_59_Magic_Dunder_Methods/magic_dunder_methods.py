# ============================================================
# Day 59: Magic/Dunder Methods — __str__, __repr__, __len__, __call__
# ============================================================
# Dunder (double-underscore) methods let you customize how your
# objects behave with Python's built-in operations.
# ============================================================

class Vector:
    """2D vector demonstrating dunder methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """User-friendly string (used by print and str())."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Developer representation (used in REPL, logging)."""
        return f"Vector(x={self.x!r}, y={self.y!r})"

    def __len__(self):
        """Return 'length' of the vector (used by len())."""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

    def __abs__(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        """v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """v * scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """v1 == v2"""
        return self.x == other.x and self.y == other.y

    def __bool__(self):
        """bool(v) — False if zero vector"""
        return self.x != 0 or self.y != 0

    def __call__(self, factor):
        """Makes the object callable like a function."""
        return Vector(self.x * factor, self.y * factor)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(str(v1))           # __str__
print(repr(v1))          # __repr__
print(len(v1))           # __len__  → 5
print(abs(v1))           # __abs__  → 5.0
print(v1 + v2)           # __add__
print(v1 - v2)           # __sub__
print(v1 * 3)            # __mul__
print(v1 == Vector(3,4)) # __eq__
print(bool(v1))          # __bool__
print(v1(2))             # __call__ → Vector(6, 8)

# --- __enter__ / __exit__ (Context Manager protocol) ---
class ManagedResource:
    def __enter__(self):
        print("Resource acquired.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released.")
        return False   # Don't suppress exceptions

with ManagedResource() as r:
    print("Using resource...")
