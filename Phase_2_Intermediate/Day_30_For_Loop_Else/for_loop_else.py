# ============================================================
# Day 30: for loop with else (Special Python syntax)
# ============================================================
# The else block runs ONLY if the loop completed without 'break'
# ============================================================

# --- BASIC for-else ---
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num % 2 != 0:
        print(f"Found odd number: {num}")
        break
else:
    # This runs because no 'break' was triggered
    print("All numbers are even! ✅")

# --- SEARCH with for-else pattern (very Pythonic!) ---
students = ["Alice", "Bob", "Charlie", "Diana"]
target   = input("Search for name: ")

for student in students:
    if student.lower() == target.lower():
        print(f"✅ Found '{student}'!")
        break
else:
    print(f"❌ '{target}' not found in list.")

# --- PRIME NUMBER CHECK using for-else ---
def is_prime(n):
    """Check if a number is prime using for-else."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break          # Not prime — break triggered
    else:
        return True        # No divisors found — it's prime!
    return False

print("\n--- Prime Numbers from 1 to 30 ---")
primes = [n for n in range(1, 31) if is_prime(n)]
print(primes)

# --- while-else ---
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop finished normally (while-else)!")
