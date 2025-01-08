# ============================================================
# Day 8: String Methods
# ============================================================
# Common methods: upper, lower, strip, replace, split, etc.
# ============================================================

text = "  Hello, Python World!  "

# Case methods
print(text.upper())          # ALL CAPS
print(text.lower())          # all lowercase
print(text.title())          # Title Case
print(text.swapcase())       # sWAP cASE

# Strip (remove whitespace or characters)
print(text.strip())          # Remove both sides
print(text.lstrip())         # Remove left side
print(text.rstrip())         # Remove right side
print("***hello***".strip("*"))  # Remove specific chars

# Replace
print(text.replace("Python", "Java"))
print(text.replace("l", "L"))       # Replace all occurrences

# Split & Join
sentence = "apple,banana,cherry"
fruits = sentence.split(",")        # ['apple', 'banana', 'cherry']
print(fruits)
print(type(fruits))                 # list

joined = " - ".join(fruits)         # Back to string
print(joined)

# Find & Count
msg = "Python is great and Python is popular"
print(msg.find("Python"))           # 0 (first occurrence index)
print(msg.rfind("Python"))          # 22 (last occurrence)
print(msg.count("Python"))          # 2
print(msg.count("is"))              # 2

# Check methods (return True/False)
print("hello123".isalnum())         # True
print("hello".isalpha())            # True
print("123".isdigit())              # True
print("  ".isspace())               # True
print("Hello World".startswith("Hello"))  # True
print("Hello World".endswith("World"))    # True

# Center / ljust / rjust
print("Python".center(20, "-"))     # -------Python-------
print("Python".ljust(20, "."))      # Python..............
print("Python".rjust(20, "."))      # ..............Python
