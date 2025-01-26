# ============================================================
# Day 26: Sets — Unique Collections & Set Operations
# ============================================================
# Sets: unordered, NO duplicates, mutable, no indexing
# ============================================================

# --- CREATING SETS ---
fruits = {"apple", "banana", "cherry", "apple"}  # duplicates removed
print("Set:", fruits)
print("Type:", type(fruits))

empty_set = set()   # NOTE: {} creates an empty DICT, not a set!

# --- SET OPERATIONS ---
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# Union (|) → all elements from both sets
print("\nA | B (Union)        :", A | B)
print("A.union(B)           :", A.union(B))

# Intersection (&) → only common elements
print("A & B (Intersection) :", A & B)
print("A.intersection(B)    :", A.intersection(B))

# Difference (-) → in A but NOT in B
print("A - B (Difference)   :", A - B)
print("B - A                :", B - A)

# Symmetric Difference (^) → in either but NOT both
print("A ^ B (Sym Diff)     :", A ^ B)

# --- SET RELATIONSHIPS ---
X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}

print(f"\nX.issubset(Y)   : {X.issubset(Y)}")     # True (X ⊆ Y)
print(f"Y.issuperset(X) : {Y.issuperset(X)}")   # True (Y ⊇ X)
print(f"A.isdisjoint(B) : {A.isdisjoint(B)}")   # False (they share 3,4,5)

# --- PRACTICAL USE: Remove duplicates from a list ---
items = [1, 2, 3, 2, 4, 3, 5, 1]
unique = list(set(items))
print(f"\nOriginal: {items}")
print(f"Unique  : {sorted(unique)}")
