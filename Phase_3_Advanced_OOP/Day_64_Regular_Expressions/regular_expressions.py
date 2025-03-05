# ============================================================
# Day 64: Regular Expressions (Regex) for Pattern Matching
# ============================================================
# import re — Python's regex module
# ============================================================

import re

text = "My phone is 987-654-3210 and email is user@example.com. Call 123-456-7890!"

# --- BASIC PATTERNS ---
# .      → any character except newline
# *      → 0 or more of preceding
# +      → 1 or more of preceding
# ?      → 0 or 1 of preceding
# \d     → digit [0-9]
# \w     → word char [a-zA-Z0-9_]
# \s     → whitespace
# [...]  → character set
# ^      → start of string
# $      → end of string
# |      → OR

# re.search() — find FIRST match
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print("Phone found:", match.group())
    print("At position:", match.start(), "-", match.end())

# re.findall() — find ALL matches (returns list)
phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print("\nAll phones:", phones)

emails = re.findall(r"[\w.]+@[\w.]+\.\w+", text)
print("Emails:", emails)

# re.sub() — replace matches
clean = re.sub(r"\d{3}-\d{3}-\d{4}", "***-***-****", text)
print("\nRedacted:", clean)

# re.split() — split on pattern
words = re.split(r"\s+", "  Hello   World  Python  ")
print("Split:", words)

# re.match() — match at BEGINNING of string only
print("\nMatch at start:", re.match(r"My", text))

# --- GROUPS ---
date_text = "Today is 2026-02-20 and tomorrow is 2026-02-21"
pattern   = r"(\d{4})-(\d{2})-(\d{2})"
for m in re.finditer(pattern, date_text):
    print(f"Full: {m.group(0)}, Year:{m.group(1)}, Month:{m.group(2)}, Day:{m.group(3)}")

# --- COMPILED PATTERNS (more efficient for repeated use) ---
email_pattern = re.compile(r"[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.[a-zA-Z]+")
print("\nCompiled find:", email_pattern.findall("a@b.com and x@y.org"))

# --- FLAGS ---
print("\nCase insensitive:", re.findall(r"python", "Python PYTHON python", re.IGNORECASE))
