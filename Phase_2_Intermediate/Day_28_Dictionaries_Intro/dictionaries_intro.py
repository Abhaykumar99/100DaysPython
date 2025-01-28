# ============================================================
# Day 28: Dictionaries — Key-Value Pairs & Initialization
# ============================================================
# Dicts: ordered (3.7+), mutable, keys must be unique & hashable
# ============================================================

# --- CREATING DICTIONARIES ---
student = {
    "name"   : "Aarav",
    "age"    : 20,
    "grade"  : "A",
    "marks"  : 95.5,
}
print(student)

# Alternative creation
person = dict(name="Bob", city="Delhi", age=25)
print(person)

# Empty dictionary
empty = {}
print(type(empty))   # <class 'dict'>

# --- ACCESSING VALUES ---
print("\nName  :", student["name"])         # KeyError if missing
print("Grade :", student.get("grade"))     # None if missing (safe)
print("Score :", student.get("score", 0)) # Default value if missing

# --- MODIFYING ---
student["age"] = 21                        # Update existing key
student["city"] = "Mumbai"                 # Add new key
print("\nUpdated:", student)

# --- DELETING ---
del student["city"]
print("After del:", student)

# --- NESTED DICTIONARIES ---
school = {
    "class_10A": {"strength": 40, "teacher": "Mr. Sharma"},
    "class_10B": {"strength": 38, "teacher": "Ms. Gupta"},
}
print("\nClass 10A teacher:", school["class_10A"]["teacher"])

# --- ITERATING ---
print("\nKeys   :", list(student.keys()))
print("Values :", list(student.values()))
print("Items  :", list(student.items()))

for key, value in student.items():
    print(f"  {key:8}: {value}")
