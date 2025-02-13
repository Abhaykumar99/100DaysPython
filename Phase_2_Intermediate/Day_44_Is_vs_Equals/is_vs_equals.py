# ============================================================
# Day 44: is vs == — Identity vs Equality
# ============================================================
# == checks if VALUES are equal
# is checks if they are the SAME OBJECT in memory
# ============================================================

# --- == (Equality) ---
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a == b : {a == b}")    # True  (same values)
print(f"a is b : {a is b}")   # False (different objects in memory)
print(f"id(a)  : {id(a)}")
print(f"id(b)  : {id(b)}")

# --- is (Identity) ---
c = a                           # c points to SAME object as a
print(f"\na is c : {a is c}")  # True (same object!)
print(f"id(a)={id(a)}, id(c)={id(c)}")

# --- INTEGERS: Small int caching (Python optimization) ---
x = 256
y = 256
print(f"\nx is y ({x}) : {x is y}")    # True (Python caches -5 to 256)

p = 1000
q = 1000
print(f"p is q ({p}) : {p is q}")    # May be False (not cached!)

# --- STRINGS: String interning ---
s1 = "hello"
s2 = "hello"
print(f"\ns1 is s2 : {s1 is s2}")   # True (Python interns short strings)

s3 = "hello world!"
s4 = "hello world!"
# Long strings with spaces may not be interned

# --- None comparison (use 'is' NOT '==') ---
value = None
print(f"\nvalue is None     : {value is None}")     # ✅ correct way
print(f"value is not None : {value is not None}")  # ✅ correct way
# print(value == None)   # Works but not recommended (PEP8 warning)

# --- BEST PRACTICE SUMMARY ---
# ✅ Use == for comparing VALUES (numbers, strings, lists, etc.)
# ✅ Use is for checking against None, True, False
# ❌ Never use is to compare integers or strings (unreliable due to caching)
