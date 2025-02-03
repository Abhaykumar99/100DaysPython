# ============================================================
# Day 34: enumerate — Getting Index and Value Simultaneously
# ============================================================

fruits = ["apple", "banana", "cherry", "date"]

# --- WITHOUT enumerate (old way) ---
print("Without enumerate:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

# --- WITH enumerate (Pythonic way) ---
print("\nWith enumerate:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# --- enumerate with start index ---
print("\nStarting from 1:")
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")

# --- PRACTICAL EXAMPLES ---
print("\n--- Menu Display ---")
menu = ["Burger", "Pizza", "Pasta", "Salad", "Soup"]
for idx, item in enumerate(menu, 1):
    print(f"  {idx}. {item}")

choice = int(input("Choose item number: "))
print(f"You chose: {menu[choice - 1]}")

# --- enumerate with strings ---
print("\n--- Character positions ---")
for i, char in enumerate("Python"):
    print(f"  [{i}] = '{char}'")

# --- Use enumerate to find an item's index ---
colors = ["red", "green", "blue", "yellow"]
target = "blue"
for i, color in enumerate(colors):
    if color == target:
        print(f"\n'{target}' is at index {i}")
        break

# --- Convert enumerate to list ---
indexed = list(enumerate(fruits, 1))
print("\nAs list:", indexed)
