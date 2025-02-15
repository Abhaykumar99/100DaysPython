# ============================================================
# Day 46: Introduction to OOPs — Classes and Objects
# ============================================================
# OOP models real-world entities as objects with data and behavior.
# Class: A blueprint.  Object (Instance): A real item from that blueprint.
# ============================================================

# --- DEFINING A CLASS ---
class Dog:
    # Class attribute (shared by ALL instances)
    species = "Canis lupus familiaris"

    # Instance method
    def bark(self):
        return "Woof! 🐶"

    def describe(self):
        return f"I am {self.species}"

# --- CREATING OBJECTS (Instantiation) ---
dog1 = Dog()
dog2 = Dog()

print(dog1.bark())
print(dog2.describe())
print(dog1.species)    # Accessed via instance
print(Dog.species)     # Accessed via class

# --- MORE REALISTIC CLASS ---
class Car:
    """Represents a car."""

    # Class variable
    total_cars = 0

    def __init__(self, brand, model, year, fuel="petrol"):
        """Initialize a Car object."""
        self.brand = brand       # Instance attribute
        self.model = model
        self.year  = year
        self.fuel  = fuel
        self.speed = 0
        Car.total_cars += 1

    def accelerate(self, amount):
        self.speed += amount
        return f"{self.brand} {self.model} speed: {self.speed} km/h"

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        return f"Braking! Speed: {self.speed} km/h"

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} ({self.fuel})"

# Create instances
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla",  "Model 3", 2023, fuel="electric")
car3 = Car("Honda",  "Civic",  2021)

print(f"\n{car1}")
print(f"{car2}")
print(f"Total cars: {Car.total_cars}")

print(car1.accelerate(60))
print(car1.accelerate(40))
print(car1.brake(30))
