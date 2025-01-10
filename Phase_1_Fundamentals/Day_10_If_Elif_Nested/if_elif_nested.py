# ============================================================
# Day 10: if-elif-else Ladder & Nested Conditionals
# ============================================================

# --- if-elif-else LADDER ---
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print(f"Your grade is: {grade}")

# --- NESTED CONDITIONALS ---
print("\n--- Nested Example: Loan Eligibility ---")
age    = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("✅ Eligible for loan!")
    else:
        print("❌ Salary too low (need ≥ ₹25,000).")
else:
    print("❌ Must be at least 21 years old.")

# --- REAL WORLD: BMI Calculator ---
print("\n--- BMI Calculator ---")
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi    = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight ✅")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
