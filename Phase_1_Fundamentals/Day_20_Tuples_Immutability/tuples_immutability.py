# ============================================================
# Day 20: Tuples — Understanding Immutability
# ============================================================
# Tuples: ordered, IMMUTABLE, allow duplicates, any data type
# ============================================================

# --- CREATING TUPLES ---
coordinates = (10.5, 20.3)
rgb         = (255, 128, 0)
single      = (42,)         # NOTE: trailing comma needed for single-element tuple
empty       = ()

print(coordinates)
print(rgb)
print(single)
print(type(single))   # <class 'tuple'>

# --- INDEXING & SLICING (same as lists) ---
colors = ("red", "green", "blue", "yellow")
print("\nFirst:", colors[0])
print("Last :", colors[-1])
print("Slice:", colors[1:3])

# --- IMMUTABLE = cannot change ---
# colors[0] = "purple"   # ← TypeError: 'tuple' object does not support item assignment

# --- WHY USE TUPLES? ---
# ✅ Faster than lists
# ✅ Safer (data cannot be accidentally changed)
# ✅ Can be used as dictionary keys (lists cannot)
# ✅ Used for returning multiple values from functions

# --- TUPLE METHODS ---
numbers = (1, 2, 3, 2, 4, 2, 5)
print("\nCount of 2 :", numbers.count(2))    # 3
print("Index of 4 :", numbers.index(4))    # 4

# --- USEFUL OPERATIONS ---
print("\nLength :", len(colors))
print("Max    :", max(numbers))
print("Min    :", min(numbers))
print("Sum    :", sum(numbers))
print("Sorted :", sorted(numbers))   # Returns a new list, tuple unchanged

# --- TUPLE vs LIST ---
# Tuple: ()  immutable  → use for fixed data (GPS, RGB, DB records)
# List:  []  mutable    → use for data you need to modify
print("\nIs 'red' in colors?", "red" in colors)
