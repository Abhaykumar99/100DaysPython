# ============================================================
# Day 14: while Loops — Logic & Infinite Loop Prevention
# ============================================================

# --- BASIC while LOOP ---
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1   # IMPORTANT: update variable to avoid infinite loop

# --- while with a CONDITION ---
print("\n--- Countdown ---")
n = 10
while n > 0:
    print(n, end=" ")
    n -= 1
print("Liftoff! 🚀")

# --- INFINITE LOOP with break (controlled) ---
print("\n--- Guess the Number ---")
secret = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("✅ Correct! You got it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

# --- while with COUNTER (avoiding infinite loop) ---
print("\n--- ATM PIN (3 attempts) ---")
correct_pin = "1234"
attempts = 0
while attempts < 3:
    pin = input("Enter PIN: ")
    attempts += 1
    if pin == correct_pin:
        print("✅ Access Granted!")
        break
    else:
        remaining = 3 - attempts
        print(f"❌ Wrong PIN. {remaining} attempt(s) left.")
else:
    print("🔒 Card blocked after 3 failed attempts.")
