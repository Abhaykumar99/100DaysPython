# ============================================================
# Day 13: for Loops — Iterating Sequences & range()
# ============================================================

# --- BASIC for LOOP ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# --- LOOP THROUGH A STRING ---
print()
for char in "Python":
    print(char, end=" ")
print()

# --- range() FUNCTION ---
# range(stop)          → 0 to stop-1
# range(start, stop)   → start to stop-1
# range(start, stop, step)

print("\nrange(5):")
for i in range(5):            # 0, 1, 2, 3, 4
    print(i, end=" ")

print("\nrange(1, 6):")
for i in range(1, 6):         # 1, 2, 3, 4, 5
    print(i, end=" ")

print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):     # 0, 2, 4, 6, 8
    print(i, end=" ")

print("\nrange(10, 0, -2):")
for i in range(10, 0, -2):    # 10, 8, 6, 4, 2
    print(i, end=" ")

# --- PRACTICAL EXAMPLES ---
print("\n\n--- Sum of 1 to 100 ---")
total = 0
for i in range(1, 101):
    total += i
print(f"Sum = {total}")

print("\n--- Multiplication Table ---")
n = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")

# --- NESTED for LOOP ---
print("\n--- Star Pattern ---")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
