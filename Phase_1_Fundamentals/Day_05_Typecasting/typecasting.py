# ============================================================
# Day 5: Typecasting — Explicit vs Implicit Conversion
# ============================================================

# --- IMPLICIT TYPECASTING (Python does it automatically) ---
num_int = 10
num_float = 3.5
result = num_int + num_float   # Python auto-converts int → float
print("Implicit:", result, type(result))

# --- EXPLICIT TYPECASTING (You do it manually) ---
# int() → converts to integer
print(int(3.9))        # 3   (truncates, does NOT round)
print(int("42"))       # 42
print(int(True))       # 1
print(int(False))      # 0

# float() → converts to float
print(float(5))        # 5.0
print(float("3.14"))   # 3.14

# str() → converts to string
print(str(100))        # "100"
print(str(3.14))       # "3.14"
print(str(True))       # "True"

# bool() → converts to boolean
print(bool(0))         # False  (0 is always False)
print(bool(1))         # True
print(bool(""))        # False  (empty string is False)
print(bool("hi"))      # True

# --- COMMON USECASE: input() always returns str ---
age = input("Enter your age: ")
print(type(age))             # <class 'str'>
age = int(age)               # Explicit cast to int
print("Next year you'll be", age + 1)
