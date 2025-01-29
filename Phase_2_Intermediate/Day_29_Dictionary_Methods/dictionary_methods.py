# ============================================================
# Day 29: Dictionary Methods
# ============================================================
# get, update, keys, values, items, pop, setdefault, fromkeys
# ============================================================

info = {"name": "Priya", "age": 22, "city": "Pune"}

# get(key, default) — safe access
print(info.get("name"))           # Priya
print(info.get("email"))          # None
print(info.get("email", "N/A"))   # N/A

# update() — merge another dict (overwrites existing keys)
info.update({"age": 23, "email": "priya@example.com"})
print("\nAfter update:", info)

# keys(), values(), items()
print("\nKeys  :", list(info.keys()))
print("Values:", list(info.values()))
print("Items :", list(info.items()))

# pop(key) — remove and return value
removed = info.pop("city")
print(f"\nPopped 'city': {removed}")
print("After pop:", info)

# popitem() — remove and return LAST inserted (key, value) pair
last = info.popitem()
print(f"popitem(): {last}")

# setdefault(key, default) — adds key if not present, returns value
info.setdefault("country", "India")
print("\nAfter setdefault:", info)

# fromkeys() — create dict from a list of keys with same value
keys      = ["name", "age", "city"]
template  = dict.fromkeys(keys, "Unknown")
print("\nfromkeys:", template)

# copy()
backup = info.copy()

# clear()
info.clear()
print("After clear:", info)

# --- Dict Comprehension ---
squares = {x: x**2 for x in range(1, 6)}
print("\nSquares dict:", squares)

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)
