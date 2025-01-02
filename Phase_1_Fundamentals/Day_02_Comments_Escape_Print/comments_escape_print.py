# ============================================================
# Day 2: Comments, Escape Sequences & Print Parameters
# ============================================================

# --- COMMENTS ---
# This is a single-line comment (starts with #)

"""
This is a multi-line comment (docstring).
It can span multiple lines.
Useful for explaining blocks of code.
"""

# --- ESCAPE SEQUENCES ---
print("Hello\tWorld")        # \t → Tab space
print("Hello\nWorld")        # \n → New line
print("He said \"Python\"")  # \" → Double quote inside string
print("C:\\Users\\Python")   # \\ → Literal backslash
print("Line1\rLine2")        # \r → Carriage return

# --- PRINT PARAMETERS ---
# sep: separator between multiple values (default is space)
print("Python", "is", "fun", sep="-")
print("A", "B", "C", sep=", ")

# end: what to print at the end (default is \n newline)
print("Hello", end=" ")
print("World")   # prints on same line: Hello World

# Combining sep and end
print("one", "two", "three", sep=" | ", end="!\n")
