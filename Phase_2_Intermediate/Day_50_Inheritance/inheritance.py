# ============================================================
# Day 50: Inheritance — Reusing Code from Parent Classes
# ============================================================
# Inheritance: a child class acquires attributes and methods of parent.
# ============================================================

# --- BASE (PARENT) CLASS ---
class Animal:
    """Base class for all animals."""

    def __init__(self, name, age, sound):
        self.name  = name
        self.age   = age
        self.sound = sound

    def speak(self):
        return f"{self.name} says: {self.sound}!"

    def __str__(self):
        return f"{type(self).__name__}({self.name}, age={self.age})"

    def breathe(self):
        return f"{self.name} breathes."

# --- CHILD CLASSES ---
class Dog(Animal):
    """Dog inherits from Animal."""

    def __init__(self, name, age, breed):
        super().__init__(name, age, "Woof")  # Call parent's __init__
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetched the {item}! 🎾"

    def __str__(self):
        return f"Dog({self.name}, breed={self.breed})"


class Cat(Animal):
    """Cat inherits from Animal."""

    def __init__(self, name, age, indoor=True):
        super().__init__(name, age, "Meow")
        self.indoor = indoor

    def purr(self):
        return f"{self.name} purrs contentedly... 😸"


class Bird(Animal):
    """Bird inherits from Animal."""

    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age, "Tweet")
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying! 🐦"
        return f"{self.name} cannot fly."

# --- USING INHERITED CLASSES ---
dog  = Dog("Buddy", 3, "Labrador")
cat  = Cat("Whiskers", 5)
bird = Bird("Tweety", 2)

print(dog)
print(dog.speak())      # Inherited from Animal
print(dog.breathe())    # Inherited from Animal
print(dog.fetch("ball"))

print(f"\n{cat}")
print(cat.speak())
print(cat.purr())

print(f"\n{bird}")
print(bird.speak())
print(bird.fly())

# --- isinstance() and issubclass() ---
print(f"\ndog is Animal?  {isinstance(dog, Animal)}")   # True
print(f"dog is Cat?     {isinstance(dog, Cat)}")       # False
print(f"Dog subclass?   {issubclass(Dog, Animal)}")    # True

# --- METHOD RESOLUTION ORDER ---
print(f"\nDog MRO: {[c.__name__ for c in Dog.__mro__]}")
