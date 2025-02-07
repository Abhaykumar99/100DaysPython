# ============================================================
# Day 38: OS Module — Automating Folder/File Creation
# ============================================================

import os
import os.path

# --- CURRENT DIRECTORY ---
print("Current directory:", os.getcwd())

# --- LIST DIRECTORY CONTENTS ---
print("\nFiles in current dir:")
for item in os.listdir("."):
    print(f"  {item}")

# --- PATH OPERATIONS ---
base    = os.getcwd()
subdir  = os.path.join(base, "test_folder")
file_p  = os.path.join(subdir, "hello.txt")

print(f"\nBase path  : {base}")
print(f"Joined path: {subdir}")

# --- CREATE DIRECTORIES ---
os.makedirs("test_folder/sub1/sub2", exist_ok=True)
print("✅ Directories created!")

# --- CHECK EXISTENCE ---
print(f"\nDoes 'test_folder' exist? {os.path.exists('test_folder')}")
print(f"Is it a dir?             {os.path.isdir('test_folder')}")
print(f"Is it a file?            {os.path.isfile('test_folder')}")

# --- CREATE FILE ---
with open("test_folder/hello.txt", "w") as f:
    f.write("Hello from OS module!")
print("✅ File created: test_folder/hello.txt")

# --- FILE INFO ---
stats = os.stat("test_folder/hello.txt")
print(f"\nFile size: {stats.st_size} bytes")

# --- RENAME ---
os.rename("test_folder/hello.txt", "test_folder/renamed.txt")
print("✅ File renamed to renamed.txt")

# --- WALK (traverse directory tree) ---
print("\n--- Directory Tree ---")
for root, dirs, files in os.walk("test_folder"):
    level = root.replace("test_folder", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}📁 {os.path.basename(root)}/")
    for file in files:
        print(f"{indent}  📄 {file}")

# --- REMOVE ---
os.remove("test_folder/renamed.txt")
os.removedirs("test_folder/sub1/sub2")
print("\n✅ Cleanup done!")

# --- ENVIRONMENT VARIABLES ---
print(f"\nHOME / USERPROFILE: {os.environ.get('USERPROFILE') or os.environ.get('HOME', 'N/A')}")
print(f"PATH (first 50 chars): {os.environ.get('PATH', '')[:50]}...")
