# ============================================================
# Day 67: Shutil Module — High-Level File Operations
# ============================================================
# shutil: shell utilities for copying, moving, and archiving files
# ============================================================

import shutil
import os

# Setup: create test files
os.makedirs("shutil_demo/source_dir", exist_ok=True)
os.makedirs("shutil_demo/dest_dir", exist_ok=True)

with open("shutil_demo/source_dir/file1.txt", "w") as f:
    f.write("Hello from file1!")
with open("shutil_demo/source_dir/file2.txt", "w") as f:
    f.write("Hello from file2!")
with open("shutil_demo/single.txt", "w") as f:
    f.write("A single file.")

# --- COPY FILE ---
shutil.copy("shutil_demo/single.txt", "shutil_demo/dest_dir/single_copy.txt")
print("✅ copy: file copied")

# copy2: also preserves metadata (timestamps)
shutil.copy2("shutil_demo/single.txt", "shutil_demo/dest_dir/single_copy2.txt")
print("✅ copy2: file copied with metadata")

# --- COPY ENTIRE DIRECTORY ---
shutil.copytree("shutil_demo/source_dir", "shutil_demo/dest_dir/source_backup")
print("✅ copytree: directory copied recursively")

# --- MOVE FILE ---
shutil.move("shutil_demo/dest_dir/single_copy.txt", "shutil_demo/dest_dir/moved.txt")
print("✅ move: file moved/renamed")

# --- DISK USAGE ---
total, used, free = shutil.disk_usage(".")
print(f"\nDisk: Total={total//1e9:.1f}GB, Used={used//1e9:.1f}GB, Free={free//1e9:.1f}GB")

# --- CREATE ARCHIVE (zip/tar) ---
shutil.make_archive("shutil_demo/backup", "zip", "shutil_demo/source_dir")
print("✅ make_archive: zip created")

# --- EXTRACT ARCHIVE ---
os.makedirs("shutil_demo/extracted", exist_ok=True)
shutil.unpack_archive("shutil_demo/backup.zip", "shutil_demo/extracted")
print("✅ unpack_archive: zip extracted")

# --- REMOVE DIRECTORY TREE ---
shutil.rmtree("shutil_demo")
print("✅ rmtree: all demo files cleaned up")

# --- SUMMARY ---
print("""
shutil key functions:
  shutil.copy(src, dst)          → copy file
  shutil.copy2(src, dst)         → copy with metadata
  shutil.copytree(src, dst)      → copy directory recursively
  shutil.move(src, dst)          → move/rename file or dir
  shutil.rmtree(path)            → delete directory tree
  shutil.make_archive(name, fmt) → create zip/tar archive
  shutil.unpack_archive(file)    → extract archive
  shutil.disk_usage(path)        → disk space info
  shutil.which(cmd)              → find executable path
""")
