# ============================================================
# Day 41: File I/O — writelines(), seek(), tell(), truncate()
# ============================================================

# --- writelines() — write a list of strings ---
lines = ["Apple\n", "Banana\n", "Cherry\n", "Date\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)
print("✅ Written with writelines()")

with open("fruits.txt", "r") as f:
    print(f.read())

# --- tell() — get current file position (byte offset) ---
with open("fruits.txt", "r") as f:
    print("Position after open:", f.tell())   # 0
    f.read(6)                                  # read 6 bytes
    print("Position after read(6):", f.tell())
    content = f.read()
    print("Position at end:", f.tell())

# --- seek() — move file pointer to a specific position ---
with open("fruits.txt", "r") as f:
    f.seek(7)                   # move to byte 7
    print("\nFrom byte 7:", f.read())

    f.seek(0)                   # go back to beginning
    print("From start:", f.readline().strip())

# --- truncate() — shrink file to specified size (bytes) ---
with open("fruits.txt", "r+") as f:   # r+ = read AND write
    content = f.read()
    print(f"\nOriginal size: {len(content)} bytes")
    f.seek(0)
    f.truncate(14)              # Keep only first 14 bytes
print("✅ Truncated to 14 bytes")

with open("fruits.txt", "r") as f:
    print("After truncate:", f.read())

# --- REAL WORLD: Log rotation simulation ---
def append_log(filename, message):
    """Append a log entry with a timestamp."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

append_log("app.log", "Application started.")
append_log("app.log", "User logged in: Alice")
append_log("app.log", "Data processed successfully.")

with open("app.log") as f:
    print("\n--- app.log ---")
    print(f.read())

# Cleanup
import os
os.remove("fruits.txt")
os.remove("app.log")
