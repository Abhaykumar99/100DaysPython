# ============================================================
# Day 17: Function Arguments
# ============================================================
# Types: Required, Default, Keyword, Variable-length (*args, **kwargs)
# ============================================================

# --- REQUIRED ARGUMENTS (positional) ---
def full_name(first, last):
    print(f"Full Name: {first} {last}")

full_name("John", "Doe")

# --- DEFAULT ARGUMENTS ---
def power(base, exponent=2):   # exponent has a default value
    return base ** exponent

print(power(3))        # 3^2 = 9  (uses default)
print(power(3, 3))     # 3^3 = 27 (overrides default)

# --- KEYWORD ARGUMENTS (named arguments, order doesn't matter) ---
def student_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

student_info(age=20, city="Mumbai", name="Priya")  # Order doesn't matter

# --- *args (Variable-length positional arguments) ---
def add_all(*args):
    print(f"Arguments: {args}")    # args is a tuple
    return sum(args)

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40, 50))

# --- **kwargs (Variable-length keyword arguments) ---
def show_profile(**kwargs):
    print(f"Profile: {kwargs}")   # kwargs is a dict
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_profile(name="Aarav", age=22, role="Developer")

# --- COMBINING ALL TYPES ---
# Order must be: required → default → *args → **kwargs
def demo(a, b=10, *args, **kwargs):
    print(f"a={a}, b={b}, args={args}, kwargs={kwargs}")

demo(1, 2, 3, 4, x=5, y=6)
