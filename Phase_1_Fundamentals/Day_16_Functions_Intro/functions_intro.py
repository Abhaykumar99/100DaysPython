# ============================================================
# Day 16: Introduction to Functions — Defining & Calling
# ============================================================
# A function is a reusable block of code.
# Syntax: def function_name():
# ============================================================

# --- DEFINING AND CALLING ---
def greet():
    print("Hello! Welcome to Python Functions!")

greet()   # Calling the function

# --- FUNCTION WITH PARAMETERS ---
def greet_user(name):
    print(f"Hello, {name}! 👋")

greet_user("Alice")
greet_user("Bob")

# --- FUNCTION WITH RETURN VALUE ---
def add(a, b):
    return a + b

result = add(5, 3)
print(f"\n5 + 3 = {result}")

# --- MULTIPLE RETURN VALUES ---
def min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 7, 1, 9, 4]
minimum, maximum = min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")

# --- WHY FUNCTIONS? ---
# ✅ Avoid code repetition (DRY: Don't Repeat Yourself)
# ✅ Makes code modular and readable
# ✅ Easy to test and debug

# --- PRACTICAL EXAMPLE ---
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

for temp in [0, 25, 37, 100]:
    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.1f}°F")
