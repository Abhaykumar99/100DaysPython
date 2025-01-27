# ============================================================
# Day 27: Set Methods
# ============================================================
# add, update, remove, discard, pop, clear, copy
# ============================================================

colors = {"red", "green", "blue"}

# add() → adds a single element
colors.add("yellow")
print("add('yellow')   :", colors)

# update() → adds multiple elements (from any iterable)
colors.update(["purple", "orange"])
print("update(...)     :", colors)

# remove() → removes element; raises KeyError if not found
colors.remove("green")
print("remove('green') :", colors)

# discard() → removes element; does NOT raise error if not found
colors.discard("pink")       # 'pink' doesn't exist — no error!
colors.discard("red")
print("discard(...)    :", colors)

# pop() → removes and returns a RANDOM element (sets are unordered)
popped = colors.pop()
print(f"pop() removed   : {popped}, remaining: {colors}")

# copy() → shallow copy
backup = colors.copy()
print("copy()          :", backup)

# clear() → removes ALL elements
backup.clear()
print("clear()         :", backup)

# --- frozenset (immutable set) ---
immutable = frozenset([1, 2, 3, 4])
print("\nfrozenset:", immutable)
# immutable.add(5)  ← AttributeError! frozensets cannot be modified

# --- PRACTICAL: Common interests between two users ---
user1_interests = {"Python", "Gaming", "Music", "Travel"}
user2_interests = {"Gaming", "Travel", "Cooking", "Reading"}

common = user1_interests & user2_interests
only_u1 = user1_interests - user2_interests
only_u2 = user2_interests - user1_interests

print(f"\nCommon interests  : {common}")
print(f"Only User1 likes  : {only_u1}")
print(f"Only User2 likes  : {only_u2}")
