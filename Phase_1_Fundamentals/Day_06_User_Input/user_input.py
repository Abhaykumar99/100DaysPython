# ============================================================
# Day 6: Taking User Input using input()
# ============================================================

# --- BASIC INPUT ---
name = input("What is your name? ")      # Always returns a string
print("Hello,", name + "!")

# --- INPUT WITH TYPE CONVERSION ---
age    = int(input("Enter your age: "))
height = float(input("Enter your height (in cm): "))

print(f"\nName   : {name}")
print(f"Age    : {age}")
print(f"Height : {height} cm")

# --- BUILDING A SIMPLE PROFILE ---
print("\n--- Student Profile ---")
roll    = int(input("Roll Number : "))
subject = input("Favourite Subject: ")
marks   = float(input("Marks obtained (out of 100): "))
grade   = "A" if marks >= 90 else ("B" if marks >= 75 else ("C" if marks >= 60 else "D"))

print(f"\nRoll    : {roll}")
print(f"Subject : {subject}")
print(f"Marks   : {marks}")
print(f"Grade   : {grade}")
