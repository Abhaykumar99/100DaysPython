# ============================================================
# Day 7: Strings — Indexing and Slicing
# ============================================================
# Syntax: string[start : stop : step]
# Index starts at 0 (positive) or -1 (negative from end)
# ============================================================

text = "Python Programming"

# --- INDEXING ---
print(text[0])    # P  (first character)
print(text[6])    # (space)
print(text[-1])   # g  (last character)
print(text[-7])   # m

# --- SLICING [start:stop]  (stop is exclusive) ---
print(text[0:6])    # Python
print(text[7:18])   # Programming
print(text[:6])     # Python   (start defaults to 0)
print(text[7:])     # Programming (stop defaults to end)
print(text[:])      # Full string

# --- SLICING WITH STEP [start:stop:step] ---
print(text[::2])    # Every 2nd character: Pto rgamn
print(text[::-1])   # Reverse the string: gnimmargorP nohtyP
print(text[0:6:1])  # Python
print(text[0:6:2])  # Pto

# --- NEGATIVE SLICING ---
print(text[-11:])   # Programming
print(text[-11:-5]) # Progra

# --- STRING IS IMMUTABLE ---
# text[0] = "J"  ← This would raise a TypeError!
# You must create a new string instead:
new_text = "J" + text[1:]
print(new_text)    # Jython Programming

# --- LENGTH OF STRING ---
print(len(text))   # 18
