# ============================================================
# Day 40: File I/O — Reading and Writing Text Files
# ============================================================
# Modes: 'r' read, 'w' write (overwrite), 'a' append, 'x' create
# ============================================================

# --- WRITING to a file ---
with open("day40_notes.txt", "w") as f:
    f.write("Hello, File I/O!\n")
    f.write("Python makes file handling easy.\n")
    f.write("Line 3: This is appended.\n")
print("✅ File written.")

# --- READING entire file ---
with open("day40_notes.txt", "r") as f:
    content = f.read()
print("\n--- read() ---")
print(content)

# --- READING line by line ---
with open("day40_notes.txt", "r") as f:
    print("--- readline() ---")
    line = f.readline()           # reads ONE line at a time
    while line:
        print(repr(line))
        line = f.readline()

# --- READLINES (all lines as a list) ---
with open("day40_notes.txt", "r") as f:
    lines = f.readlines()
print(f"\n--- readlines() --- {lines}")

# --- ITERATING FILE directly (most memory-efficient) ---
print("\n--- Iterating file ---")
with open("day40_notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# --- APPEND mode (adds to end, doesn't overwrite) ---
with open("day40_notes.txt", "a") as f:
    f.write("Line 4: Added via append mode.\n")
print("✅ Appended to file.")

# --- READ after append ---
with open("day40_notes.txt", "r") as f:
    print("\n--- Final content ---")
    print(f.read())

# Clean up
import os
os.remove("day40_notes.txt")
