# ============================================================
# Day 23: f-Strings — Advanced String Formatting
# ============================================================
# f-strings (formatted string literals) — Python 3.6+
# Syntax: f"text {expression}"
# ============================================================

name  = "Arjun"
age   = 22
pi    = 3.14159265
price = 1999.50

# --- BASIC f-string ---
print(f"Hello, {name}! You are {age} years old.")

# --- EXPRESSIONS INSIDE f-strings ---
print(f"5 + 3 = {5 + 3}")
print(f"Age in 5 years: {age + 5}")
print(f"Name uppercase: {name.upper()}")

# --- NUMBER FORMATTING ---
print(f"\nPi (2 decimals)  : {pi:.2f}")
print(f"Pi (5 decimals)  : {pi:.5f}")
print(f"Price (currency) : ₹{price:,.2f}")
print(f"Price (no comma) : {price:.0f}")

# --- WIDTH & ALIGNMENT ---
# :<  left-align   :>  right-align   :^  center
items = [("Apple", 30), ("Banana", 15), ("Cherry", 50)]
print(f"\n{'Item':<10} {'Price':>8}")
print("-" * 20)
for item, p in items:
    print(f"{item:<10} ₹{p:>6}")

# --- BINARY, HEX, OCTAL ---
n = 255
print(f"\n{n} in binary : {n:b}")
print(f"{n} in hex    : {n:x}")
print(f"{n} in octal  : {n:o}")

# --- f-string with conditional expression ---
score = 85
print(f"\nResult: {'Pass ✅' if score >= 40 else 'Fail ❌'}")

# --- Debugging with = (Python 3.8+) ---
x = 42
print(f"\n{x = }")           # x = 42
print(f"{x * 2 = }")         # x * 2 = 84
