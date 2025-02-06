# ============================================================
# Day 37: The if __name__ == "__main__" Idiom
# ============================================================

"""
EXPLANATION:
Every Python file has a built-in variable: __name__

When you RUN a file directly:     __name__ == "__main__"
When you IMPORT the file:         __name__ == "filename" (the module name)

The guard: if __name__ == "__main__":
  → Code inside ONLY runs when the file is executed directly.
  → Code inside does NOT run when the file is imported.

WHY?
  ✅ Allows a file to be both a reusable module AND a standalone script.
  ✅ Prevents unintended code execution on import.
  ✅ Standard practice in every professional Python project.
"""

# --- FUNCTIONS (reusable by other modules) ---
def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}! 👋"

# --- TEST / DEMO code (only runs when executed directly) ---
if __name__ == "__main__":
    print("Running as main script!")
    print(f"__name__ = '{__name__}'")

    # Tests / demos
    print(f"\nadd(3, 4)       = {add(3, 4)}")
    print(f"multiply(5, 6)  = {multiply(5, 6)}")
    print(f"greet('Alice')  = {greet('Alice')}")

    # Interactive section
    name = input("\nEnter your name: ")
    print(greet(name))
