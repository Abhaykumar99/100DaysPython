# ============================================================
# Day 57: Introspection — dir(), __dict__, help()
# ============================================================
# Introspection: examining objects at runtime to see their structure
# ============================================================

class Person:
    """Represents a person."""
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def greet(self):
        return f"Hi, I'm {self.name}!"

    def _private_method(self):
        return "private"

p = Person("Alice", 30)

# --- dir() — lists all attributes and methods ---
print("dir(p):")
all_attrs = dir(p)
# Filter to non-dunder for readability
user_attrs = [a for a in all_attrs if not a.startswith("__")]
print(user_attrs)

print(f"\ndir() count: {len(all_attrs)} attributes/methods")

# --- __dict__ — instance's attribute dictionary ---
print(f"\np.__dict__   : {p.__dict__}")
print(f"Person.__dict__: (subset)")
for k, v in Person.__dict__.items():
    if not k.startswith("__"):
        print(f"  {k}: {v}")

# --- type() and isinstance() ---
print(f"\ntype(p)              : {type(p)}")
print(f"type(p).__name__     : {type(p).__name__}")
print(f"isinstance(p, Person): {isinstance(p, Person)}")

# --- hasattr, getattr, setattr, delattr ---
print(f"\nhasattr(p, 'name')  : {hasattr(p, 'name')}")
print(f"hasattr(p, 'email') : {hasattr(p, 'email')}")

print(f"getattr(p, 'name')  : {getattr(p, 'name')}")
print(f"getattr(p, 'email', 'N/A') : {getattr(p, 'email', 'N/A')}")

setattr(p, 'email', 'alice@example.com')
print(f"After setattr email : {p.email}")

delattr(p, 'email')
print(f"After delattr email : {hasattr(p, 'email')}")

# --- __class__, __name__, __module__ ---
print(f"\np.__class__      : {p.__class__}")
print(f"Person.__name__  : {Person.__name__}")
print(f"Person.__module__: {Person.__module__}")
print(f"Person.__doc__   : {Person.__doc__}")

# help(Person)   # Uncomment to see full help
