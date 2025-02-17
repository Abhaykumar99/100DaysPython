# ============================================================
# Day 48: Decorators — Modifying Function Behavior
# ============================================================
# A decorator wraps a function to add extra behavior.
# Syntax: @decorator_name above the function definition.
# ============================================================

import time
import functools

# --- HOW DECORATORS WORK (manually) ---
def shout(func):
    """A simple decorator that shouts the output."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() + "!!!"
    return wrapper

def greet(name):
    return f"hello, {name}"

# Manual decoration:
shouting_greet = shout(greet)
print(shouting_greet("Alice"))    # HELLO, ALICE!!!

# Syntactic sugar with @:
@shout
def welcome(name):
    return f"welcome, {name}"

print(welcome("Bob"))             # WELCOME, BOB!!!

# --- PRACTICAL DECORATOR 1: Timer ---
def timer(func):
    """Measure execution time of a function."""
    @functools.wraps(func)        # Preserve original function's metadata
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f"⏱ {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

result = slow_sum(1_000_000)
print(f"Sum = {result}")

# --- PRACTICAL DECORATOR 2: Login Check ---
is_logged_in = True

def require_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("❌ Please log in first!")
            return None
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_dashboard():
    print("✅ Welcome to your dashboard!")

view_dashboard()

# --- DECORATOR WITH ARGUMENTS ---
def repeat(times):
    """Repeat function n times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

print()
say_hello()
