# ============================================================
# Day 3: Variables and Data Types
# ============================================================
# Data Types: int, float, str, bool, complex
# ============================================================

# --- VARIABLES ---
# A variable is a named container that stores a value.
name = "Alice"        # str  (string)
age = 25              # int  (integer)
height = 5.7          # float (decimal)
is_student = True     # bool (True or False)
score = 3 + 4j        # complex (real + imaginary)

# Print variables and their types
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(score, type(score))

# --- MULTIPLE ASSIGNMENT ---
x = y = z = 10         # All three point to same value
a, b, c = 1, 2, 3      # Unpack multiple values

print(x, y, z)
print(a, b, c)

# --- NAMING RULES ---
# ✅ Valid: my_var, _var, var1
# ❌ Invalid: 1var, my-var, class (reserved keyword)

# --- DYNAMIC TYPING ---
# Python allows changing type of a variable
data = 42
print(type(data))   # int
data = "now a string"
print(type(data))   # str
