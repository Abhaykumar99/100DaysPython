# ============================================================
# Day 42: Lambda Functions — Anonymous One-Liner Functions
# ============================================================
# Syntax: lambda arguments: expression
# Lambdas have no name; they're used for short, throwaway functions
# ============================================================

# --- BASIC LAMBDA ---
square = lambda x: x ** 2
print(square(5))    # 25

add = lambda a, b: a + b
print(add(3, 4))    # 7

greet = lambda name: f"Hello, {name}!"
print(greet("Alice"))

# --- LAMBDA vs REGULAR FUNCTION ---
# Regular:
def multiply(a, b):
    return a * b

# Lambda equivalent:
multiply_l = lambda a, b: a * b

print(multiply(3, 4))    # 12
print(multiply_l(3, 4))  # 12

# --- LAMBDA WITH CONDITIONAL ---
even_odd = lambda n: "even" if n % 2 == 0 else "odd"
print(even_odd(7))   # odd
print(even_odd(8))   # even

# --- LAMBDA WITH BUILT-INS (sort, sorted, filter, map) ---
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]

# Sort by grade (second element):
sorted_students = sorted(students, key=lambda s: s[1])
print("\nSorted by grade:", sorted_students)

# Sort descending:
sorted_desc = sorted(students, key=lambda s: s[1], reverse=True)
print("Top students  :", sorted_desc)

# --- IMMEDIATELY INVOKED LAMBDA ---
result = (lambda x, y: x * y)(6, 7)
print(f"\n6 × 7 = {result}")

# --- WHEN TO USE LAMBDA ---
# ✅ Short, simple operations passed as arguments
# ✅ Sorting, filtering, mapping
# ❌ Complex logic → use a named def function instead
