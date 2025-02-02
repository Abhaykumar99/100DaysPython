# ============================================================
# Day 33: Short Hand if-else (Ternary Operators)
# ============================================================
# Syntax: value_if_true if condition else value_if_false
# ============================================================

# --- BASIC TERNARY ---
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# --- IN PRINT ---
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# --- WITH FUNCTIONS ---
def abs_value(n):
    return n if n >= 0 else -n

print(abs_value(-5))   # 5
print(abs_value(7))    # 7

# --- CHAINED TERNARY ---
marks = int(input("Enter marks: "))
grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "D"
print(f"Grade: {grade}")

# --- TERNARY IN LIST COMPREHENSION ---
numbers = list(range(1, 11))
labels  = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(list(zip(numbers, labels)))

# --- TERNARY WITH NONE CHECK ---
name = None
display = name if name else "Guest"
print(f"Hello, {display}!")

# --- ASSIGNMENT VARIATIONS ---
a, b = 10, 20
maximum = a if a > b else b
print(f"Max of {a} and {b} is {maximum}")
