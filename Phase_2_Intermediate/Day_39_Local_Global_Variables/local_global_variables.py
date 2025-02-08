# ============================================================
# Day 39: Local vs Global Variables & the global keyword
# ============================================================

# --- LOCAL VARIABLE ---
# Defined inside a function; only accessible inside it.
def my_func():
    local_var = "I am local"
    print(local_var)

my_func()
# print(local_var)  # ← NameError: name 'local_var' is not defined

# --- GLOBAL VARIABLE ---
# Defined outside functions; accessible everywhere (read-only inside functions).
count = 0

def show_count():
    print("Count:", count)    # Can READ global variable

show_count()

# --- MODIFYING GLOBAL INSIDE FUNCTION (use 'global' keyword) ---
total = 100

def add_bonus(amount):
    global total          # Declare intent to modify global
    total += amount

print(f"\nBefore: total = {total}")
add_bonus(50)
print(f"After:  total = {total}")

# --- WITHOUT global keyword (common mistake) ---
score = 0

def update_score():
    # score += 10   ← UnboundLocalError! Python thinks it's local
    pass

# --- NESTED FUNCTIONS & nonlocal ---
def outer():
    message = "Hello"

    def inner():
        nonlocal message        # Modify outer function's variable
        message = "Modified!"
        print("Inner:", message)

    inner()
    print("Outer:", message)

outer()

# --- BEST PRACTICE ---
# ✅ Minimize global variables → pass data via arguments and return values
# ✅ Use global only when truly necessary (e.g., config flags, counters)
# ✅ Use classes to group state instead of globals for complex programs

def counter_demo():
    """Shows passing state through arguments instead of globals."""
    def increment(n):
        return n + 1
    
    val = 0
    for _ in range(5):
        val = increment(val)
    return val

print(f"\nCounter (no globals): {counter_demo()}")
