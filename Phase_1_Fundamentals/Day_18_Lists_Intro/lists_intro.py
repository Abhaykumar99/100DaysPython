# ============================================================
# Day 18: Introduction to Lists — Creating & Indexing
# ============================================================
# Lists: ordered, mutable, allow duplicates, any data type
# ============================================================

# --- CREATING LISTS ---
fruits  = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed   = [42, "hello", 3.14, True]
empty   = []

print(fruits)
print(numbers)
print(mixed)

# --- INDEXING (same as strings) ---
print("\nFirst item :", fruits[0])    # apple
print("Last item  :", fruits[-1])    # cherry

# --- NESTED LISTS ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatrix row 1  :", matrix[0])
print("Element [1][2]:", matrix[1][2])   # 6

# --- SLICING ---
nums = [10, 20, 30, 40, 50, 60]
print("\nSlice [1:4] :", nums[1:4])    # [20, 30, 40]
print("Slice [::2] :", nums[::2])     # [10, 30, 50]
print("Reversed    :", nums[::-1])    # [60, 50, 40, 30, 20, 10]

# --- LIST IS MUTABLE (can change values) ---
fruits[1] = "mango"
print("\nAfter change:", fruits)

# --- USEFUL OPERATIONS ---
print("\nLength      :", len(fruits))
print("Contains 'apple'?", "apple" in fruits)
print("Max:", max(numbers), "  Min:", min(numbers))
print("Sum:", sum(numbers))

# --- CONCATENATION & REPETITION ---
a = [1, 2, 3]
b = [4, 5, 6]
print("\na + b =", a + b)
print("a * 3 =", a * 3)
