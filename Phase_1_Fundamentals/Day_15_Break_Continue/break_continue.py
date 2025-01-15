# ============================================================
# Day 15: break and continue Statements
# ============================================================

# --- break: exits the loop early ---
print("--- break Example ---")
for i in range(1, 11):
    if i == 6:
        print("Breaking at 6!")
        break
    print(i, end=" ")
print()

# --- continue: skips current iteration ---
print("\n--- continue Example (skip even numbers) ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i, end=" ")
print()

# --- break in while loop ---
print("\n--- Search in a list ---")
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target = input("Enter a name to find: ")

for name in names:
    if name.lower() == target.lower():
        print(f"✅ Found: {name}")
        break
else:
    # This runs only if loop completed WITHOUT break
    print(f"❌ '{target}' not found in the list.")

# --- continue with while ---
print("\n--- Skip multiples of 3 from 1 to 15 ---")
n = 0
while n < 15:
    n += 1
    if n % 3 == 0:
        continue
    print(n, end=" ")
print()
