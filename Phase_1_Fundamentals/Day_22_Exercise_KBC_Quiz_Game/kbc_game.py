# ============================================================
# Day 22: Exercise — KBC (Kaun Banega Crorepati) Quiz Game
# ============================================================
# A simple quiz game using Lists and if-elif logic
# ============================================================

questions = [
    "Which planet is known as the Red Planet?",
    "What is the capital of Japan?",
    "Who wrote 'Romeo and Juliet'?",
    "How many sides does a hexagon have?",
    "What is the chemical symbol for Gold?",
]

options = [
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok"],
    ["A. Dickens", "B. Hemingway", "C. Shakespeare", "D. Chaucer"],
    ["A. 5", "B. 6", "C. 7", "D. 8"],
    ["A. Gd", "B. Ag", "C. Au", "D. Pt"],
]

answers    = ["B", "C", "C", "B", "C"]
prize_money = [1000, 10000, 50000, 100000, 1000000]

print("=" * 40)
print("    🎉 Welcome to KBC! 🎉")
print("=" * 40)

score = 0

for i in range(len(questions)):
    print(f"\nQ{i+1}: {questions[i]}")
    for opt in options[i]:
        print(f"   {opt}")

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == answers[i]:
        score += 1
        print(f"✅ Correct! Prize: ₹{prize_money[i]:,}")
    else:
        print(f"❌ Wrong! Correct answer was: {answers[i]}")
        print(f"   Better luck next time!")
        break

print(f"\n{'='*40}")
print(f"  Final Score   : {score} / {len(questions)}")
print(f"  Total Winning : ₹{prize_money[score-1]:,}" if score > 0 else "  Total Winning : ₹0")
print("=" * 40)
