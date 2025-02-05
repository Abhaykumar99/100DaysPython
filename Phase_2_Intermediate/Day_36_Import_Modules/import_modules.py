# ============================================================
# Day 36: How import Works — math, random & Custom Modules
# ============================================================

# --- IMPORTING STANDARD LIBRARY MODULES ---
import math
import random

# --- math module ---
print("=== math module ===")
print(f"math.pi     = {math.pi}")
print(f"math.e      = {math.e}")
print(f"sqrt(144)   = {math.sqrt(144)}")
print(f"ceil(4.2)   = {math.ceil(4.2)}")
print(f"floor(4.9)  = {math.floor(4.9)}")
print(f"factorial(6)= {math.factorial(6)}")
print(f"log(100,10) = {math.log(100, 10)}")
print(f"sin(90°)    = {math.sin(math.radians(90)):.2f}")

# --- random module ---
print("\n=== random module ===")
print(f"random()          = {random.random()}")        # float 0.0-1.0
print(f"randint(1,10)     = {random.randint(1, 10)}")  # int inclusive
print(f"randrange(0,100,5)= {random.randrange(0, 100, 5)}")

fruits = ["apple", "banana", "cherry", "date"]
print(f"choice(fruits)    = {random.choice(fruits)}")

random.shuffle(fruits)
print(f"shuffle(fruits)   = {fruits}")

print(f"sample 2 from list= {random.sample([1,2,3,4,5], 2)}")

# --- IMPORT STYLES ---
from math import pi, sqrt, factorial  # import specific names
print(f"\nDirect pi  = {pi}")
print(f"Direct sqrt= {sqrt(81)}")

import math as m                      # alias
print(f"Alias m.e  = {m.e}")

from random import *                  # import everything (not recommended)

# --- HOW MODULES WORK ---
# When you do: import math
# Python searches:
#   1. Built-in modules
#   2. sys.path directories (current dir, PYTHONPATH, standard lib, site-packages)
import sys
print(f"\nSearch path (first 3): {sys.path[:3]}")
