# ============================================================
# Day 24: Docstrings & the help() Function
# ============================================================
# Docstrings document your functions/classes/modules.
# They are accessible via help() and .__doc__
# ============================================================

# --- SINGLE-LINE DOCSTRING ---
def square(n):
    """Return the square of a number."""
    return n ** 2

print(square(5))
print(square.__doc__)

# --- MULTI-LINE DOCSTRING (Google Style) ---
def calculate_bmi(weight_kg, height_m):
    """
    Calculate the Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m  (float): Height in meters.

    Returns:
        float: The BMI value rounded to 2 decimal places.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

print(calculate_bmi(70, 1.75))
help(calculate_bmi)    # Displays the full docstring nicely

# --- CLASS DOCSTRING ---
class Dog:
    """Represents a dog with a name and breed."""

    def __init__(self, name, breed):
        """Initialize a Dog instance."""
        self.name  = name
        self.breed = breed

    def bark(self):
        """Make the dog bark and return the sound."""
        return f"{self.name} says: Woof! 🐶"

help(Dog)

d = Dog("Buddy", "Labrador")
print(d.bark())

# --- help() on built-ins ---
# help(print)   # Uncomment to see print's documentation
# help(str)
# help(list)
