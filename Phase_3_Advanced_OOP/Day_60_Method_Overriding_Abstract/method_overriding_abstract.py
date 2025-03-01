# ============================================================
# Day 60: Method Overriding and @abstractmethod
# ============================================================
# Method Overriding: child class provides its own implementation
# of a method defined in the parent class.
# ABC / @abstractmethod: force subclasses to implement methods.
# ============================================================

from abc import ABC, abstractmethod

# --- ABSTRACT BASE CLASS ---
class Shape(ABC):
    """Abstract base class — cannot be instantiated directly."""

    def __init__(self, color="black"):
        self.color = color

    @abstractmethod
    def area(self):
        """Must be implemented by every subclass."""
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        """Concrete method shared by all subclasses."""
        return f"{type(self).__name__} | Color: {self.color} | Area: {self.area():.2f}"

# Cannot instantiate ABC:
try:
    s = Shape()
except TypeError as e:
    print(f"❌ {e}")

# --- CONCRETE SUBCLASSES ---
import math

class Circle(Shape):
    def __init__(self, radius, color="red"):
        super().__init__(color)
        self.radius = radius

    def area(self):             # MUST override
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, w, h, color="blue"):
        super().__init__(color)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def describe(self):         # OVERRIDE concrete method too
        return f"Rectangle {self.w}×{self.h} | {super().describe()}"

shapes = [Circle(5), Rectangle(4, 6), Circle(3, "green")]

for shape in shapes:
    print(shape.describe())
    print(f"  Perimeter: {shape.perimeter():.2f}")

# --- POLYMORPHISM in action ---
print("\n--- Polymorphism ---")
for shape in shapes:
    print(f"  type={type(shape).__name__}, area={shape.area():.2f}")
