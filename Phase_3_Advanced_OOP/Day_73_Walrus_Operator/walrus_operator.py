# ============================================================
# Day 73: The Walrus Operator (:=) — Python 3.8+
# ============================================================
# := (walrus operator) assigns AND returns a value in one step.
# Also called "assignment expressions".
# ============================================================

# --- BASIC USAGE ---
# Without walrus (old way):
numbers = [1, 2, 3, 4, 5]
n = len(numbers)
if n > 3:
    print(f"List has {n} elements — that's a lot!")

# With walrus:
if (n := len(numbers)) > 3:
    print(f"Walrus: List has {n} elements — that's a lot!")

# --- IN while LOOPS (most common use) ---
print("\n--- Input loop (type 'quit' to exit) ---")
# Old way (repeat yourself):
# user = input("Enter command: ")
# while user != "quit":
#     print(f"You said: {user}")
#     user = input("Enter command: ")

# Walrus way (no repetition):
while (user := input("Enter command (or 'quit'): ")) != "quit":
    print(f"  Processing: '{user}'")
print("Exited loop.")

# --- IN LIST COMPREHENSIONS ---
import math

# Without walrus:
results1 = [math.sqrt(x) for x in range(1, 11) if math.sqrt(x) > 2]

# With walrus (compute sqrt only once):
results2 = [y for x in range(1, 11) if (y := math.sqrt(x)) > 2]
print(f"\nSqrt > 2: {[round(v,2) for v in results2]}")

# --- IN if/elif CHAINS ---
import re

text = "Call us at 987-654-3210 for support."

if m := re.search(r"\d{3}-\d{3}-\d{4}", text):
    print(f"\nPhone found: {m.group()}")
else:
    print("No phone found.")

# --- FILE READING ---
with open(__file__, "r") as f:    # Read this script itself
    lines = []
    while (line := f.readline()):
        if "walrus" in line.lower():
            lines.append(line.strip())

print(f"\nLines mentioning 'walrus': {len(lines)}")

# --- WHEN TO USE vs WHEN NOT TO ---
# ✅ Use when assignment inside a condition avoids repetition
# ✅ Use in loops where re-computing a value would be needed twice
# ❌ Avoid in simple cases where it reduces readability
