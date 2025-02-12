# ============================================================
# Day 43: Functional Programming — map, filter, reduce
# ============================================================
# These functions apply operations on iterables in a functional style
# ============================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- map(function, iterable) ---
# Applies function to EVERY element; returns a map object.
squares = list(map(lambda x: x**2, numbers))
print("map (squares)  :", squares)

doubled = list(map(lambda x: x * 2, numbers))
print("map (doubled)  :", doubled)

# With multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print("map (a + b)    :", sums)

# --- filter(function, iterable) ---
# Keeps elements where function returns True.
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("\nfilter (evens) :", evens)

positives = list(filter(lambda x: x > 0, [-3, -1, 0, 2, 5, -7, 8]))
print("filter (>0)    :", positives)

# --- reduce(function, iterable) ---
# Reduces iterable to a SINGLE value by applying function cumulatively.
total    = reduce(lambda acc, x: acc + x, numbers)     # sum
product  = reduce(lambda acc, x: acc * x, [1,2,3,4,5]) # factorial of 5
maximum  = reduce(lambda a, b: a if a > b else b, numbers)

print(f"\nreduce (sum)   : {total}")
print(f"reduce (5!)    : {product}")
print(f"reduce (max)   : {maximum}")

# --- COMPARISON: for loop vs map vs list comprehension ---
data = [3, 1, 4, 1, 5, 9, 2, 6]

# Traditional:
result1 = []
for x in data:
    result1.append(x**2)

# map:
result2 = list(map(lambda x: x**2, data))

# List comprehension (most Pythonic):
result3 = [x**2 for x in data]

print(f"\nAll equal: {result1 == result2 == result3}")
print(f"Result   : {result3}")
