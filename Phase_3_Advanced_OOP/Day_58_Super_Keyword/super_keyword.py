# ============================================================
# Day 58: The super() Keyword
# ============================================================
# super() returns a proxy object that delegates method calls to
# the parent class, following the MRO (Method Resolution Order).
# ============================================================

class Shape:
    def __init__(self, color="white"):
        self.color = color

    def describe(self):
        return f"A {self.color} shape"

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height, color="blue"):
        super().__init__(color)     # Call Shape.__init__
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        base = super().describe()    # Call Shape.describe()
        return f"{base} (rectangle {self.width}×{self.height})"

class Square(Rectangle):
    def __init__(self, side, color="red"):
        super().__init__(side, side, color)   # Call Rectangle.__init__

    def describe(self):
        return f"Square with side {self.width}, color={self.color}"

r = Rectangle(4, 6, "green")
print(r.describe())
print("Area:", r.area())

s = Square(5)
print(f"\n{s.describe()}")
print("Area:", s.area())

# --- super() in Multiple Inheritance ---
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")
        super().method()

class C(A):
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    def method(self):
        print("D.method")
        super().method()

print("\nMRO for D:", [cls.__name__ for cls in D.__mro__])
D().method()
# Follows MRO: D → B → C → A
