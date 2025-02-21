# ============================================================
# Day 52: Multiple and Multilevel Inheritance
# ============================================================

# --- MULTIPLE INHERITANCE ---
class Flyable:
    def fly(self):
        return f"{self.name} is flying! ✈️"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming! 🏊"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    def quack(self):
        return f"{self.name}: Quack! 🦆"

d = Duck("Donald")
print(d.fly())
print(d.swim())
print(d.quack())
print("MRO:", [c.__name__ for c in Duck.__mro__])

# --- MULTILEVEL INHERITANCE ---
class LivingThing:
    def breathe(self):
        return "Breathing..."

class Animal(LivingThing):
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} is eating."

class Mammal(Animal):
    def feed_young(self):
        return f"{self.name} feeds its young with milk."

class Human(Mammal):
    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession
    def work(self):
        return f"{self.name} works as a {self.profession}."

h = Human("Alice", "Software Engineer")
print(f"\n{h.breathe()}")         # 3 levels up
print(h.eat())                     # 2 levels up
print(h.feed_young())              # 1 level up
print(h.work())                    # own method
print("MRO:", [c.__name__ for c in Human.__mro__])
