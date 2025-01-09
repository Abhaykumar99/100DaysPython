# ============================================================
# Day 9: Conditional Statements — if / else
# ============================================================

# --- BASIC if / else ---
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult. ✅")
else:
    print("You are a minor. ❌")

# --- COMPARISON OPERATORS ---
# == equal to        != not equal to
# >  greater than    <  less than
# >= greater or eq   <= less or eq

num = int(input("\nEnter a number: "))

if num > 0:
    print("Positive number")
else:
    print("Non-positive number (zero or negative)")

# --- LOGICAL OPERATORS: and / or / not ---
x = int(input("\nEnter a value (1-100): "))

if x >= 1 and x <= 100:
    print("Valid range")
else:
    print("Out of range")

# Using 'or'
char = input("Enter a vowel (a,e,i,o,u): ").lower()
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(f"'{char}' is a vowel ✅")
else:
    print(f"'{char}' is NOT a vowel ❌")

# Using 'not'
logged_in = False
if not logged_in:
    print("Please log in first.")
