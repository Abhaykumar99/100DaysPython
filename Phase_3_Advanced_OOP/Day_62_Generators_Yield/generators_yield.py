# ============================================================
# Day 62: Generators and the yield Keyword
# ============================================================
# Generators produce values ONE AT A TIME using yield.
# They are memory-efficient — they don't store all values at once.
# ============================================================

# --- NORMAL FUNCTION vs GENERATOR ---
def get_squares_list(n):
    """Normal function: builds entire list in memory."""
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def get_squares_gen(n):
    """Generator: yields one value at a time."""
    for i in range(n):
        yield i**2         # Pauses here, returns value, resumes later

# Using them:
squares_list = get_squares_list(5)
print("List:", squares_list)          # [0, 1, 4, 9, 16]

squares_gen = get_squares_gen(5)
print("Generator object:", squares_gen)
print("Next:", next(squares_gen))     # 0
print("Next:", next(squares_gen))     # 1
print("Iterate rest:", list(squares_gen))  # [4, 9, 16]

# --- GENERATOR EXPRESSION (like list comp but with ()) ---
gen_expr = (x**3 for x in range(1, 6))
print("\nCube generator:", list(gen_expr))

# --- INFINITE GENERATOR ---
def counting(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = counting(10)
print("\nInfinite counter (first 5):", [next(counter) for _ in range(5)])

# --- FIBONACCI GENERATOR ---
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("Fibonacci (first 10):", [next(fib) for _ in range(10)])

# --- MEMORY COMPARISON ---
import sys
list_data = [i**2 for i in range(100_000)]
gen_data  = (i**2 for i in range(100_000))

print(f"\nList size: {sys.getsizeof(list_data):,} bytes")
print(f"Gen  size: {sys.getsizeof(gen_data):,} bytes")

# --- yield from (delegating to sub-generator) ---
def chain(*iterables):
    for it in iterables:
        yield from it

print("\nchain:", list(chain([1,2], [3,4], [5,6])))
