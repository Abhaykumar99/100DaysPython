# ============================================================
# Day 31: Exception Handling — try / except
# ============================================================
# Prevent your program from crashing on runtime errors.
# ============================================================

# --- BASIC try / except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")

# --- CATCHING SPECIFIC EXCEPTIONS ---
try:
    num = int(input("Enter a number: "))
    print(f"100 / {num} = {100 / num}")
except ValueError:
    print("❌ Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("❌ Division by zero is not allowed!")

# --- CATCHING MULTIPLE EXCEPTIONS IN ONE LINE ---
try:
    items = [1, 2, 3]
    print(items[10])    # IndexError
except (IndexError, KeyError) as e:
    print(f"❌ Error: {e}")

# --- GENERIC EXCEPTION (catch all) ---
try:
    x = int("abc")
except Exception as e:
    print(f"❌ An error occurred: {type(e).__name__}: {e}")

# --- NESTED try / except ---
print("\n--- File Read Example ---")
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("❌ File not found!")
except PermissionError:
    print("❌ No permission to read file!")

# --- COMMON BUILT-IN EXCEPTIONS ---
# ValueError     → wrong value type (int("abc"))
# TypeError      → wrong type (1 + "a")
# IndexError     → list index out of range
# KeyError       → dict key not found
# FileNotFoundError → file doesn't exist
# ZeroDivisionError → division by zero
# AttributeError → object has no such attribute
# NameError      → variable not defined
