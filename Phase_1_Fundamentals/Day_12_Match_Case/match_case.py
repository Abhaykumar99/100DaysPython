# ============================================================
# Day 12: Match Case Statements (Python 3.10+)
# ============================================================
# Python's version of switch-case from other languages
# ============================================================

# --- BASIC MATCH CASE ---
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:           # default (like else)
        print("Invalid day number!")

# --- MATCH WITH MULTIPLE VALUES (OR pattern) ---
print("\n--- Weekend Check ---")
match day:
    case 6 | 7:
        print("It's the Weekend! 🎉")
    case 1 | 2 | 3 | 4 | 5:
        print("It's a Weekday 💼")
    case _:
        print("Invalid!")

# --- MATCH WITH STRINGS ---
command = input("\nEnter command (start/stop/pause): ").lower()
match command:
    case "start":
        print("▶ Starting the process...")
    case "stop":
        print("⏹ Stopping the process...")
    case "pause":
        print("⏸ Pausing the process...")
    case _:
        print("❌ Unknown command!")
