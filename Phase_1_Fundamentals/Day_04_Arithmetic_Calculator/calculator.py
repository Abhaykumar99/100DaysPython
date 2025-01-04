# ============================================================
# Day 4: Arithmetic Operators — Basic Calculator
# ============================================================
# Operators: +  -  *  /  //  %  **
# ============================================================

# --- ALL ARITHMETIC OPERATORS ---
a = 10
b = 3

print("Addition       :", a + b)    # 13
print("Subtraction    :", a - b)    # 7
print("Multiplication :", a * b)    # 30
print("Division       :", a / b)    # 3.333...  (always float)
print("Floor Division :", a // b)   # 3         (drops decimal)
print("Modulus        :", a % b)    # 1         (remainder)
print("Exponentiation :", a ** b)   # 1000      (10^3)

# --- BASIC CALCULATOR PROGRAM ---
print("\n===== Basic Calculator =====")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))
op   = input("Choose operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")
