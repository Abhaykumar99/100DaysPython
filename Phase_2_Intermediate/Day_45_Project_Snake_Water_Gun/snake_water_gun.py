# ============================================================
# Day 45: Project — Snake, Water, Gun Game 🐍💧🔫
# ============================================================
# Rules: Snake drinks Water (Snake wins)
#        Water douses Gun (Water wins)
#        Gun shoots Snake (Gun wins)
# ============================================================

import random

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["snake", "water", "gun"])

def determine_winner(player, computer):
    """Determine the winner based on choices."""
    if player == computer:
        return "draw"

    wins = {
        "snake": "water",   # snake beats water
        "water": "gun",     # water beats gun
        "gun":   "snake",   # gun beats snake
    }

    if wins[player] == computer:
        return "player"
    else:
        return "computer"

def play_game():
    """Main game loop."""
    print("=" * 40)
    print("  🎮 Snake, Water, Gun Game 🎮")
    print("=" * 40)

    player_score   = 0
    computer_score = 0
    rounds = 0

    while True:
        print(f"\n📊 Score — You: {player_score} | Computer: {computer_score}")
        print("Options: snake | water | gun | quit")
        player = input("Your choice: ").strip().lower()

        if player == "quit":
            break

        if player not in ["snake", "water", "gun"]:
            print("❌ Invalid choice! Please enter snake, water, or gun.")
            continue

        computer = get_computer_choice()
        rounds += 1
        print(f"💻 Computer chose: {computer}")

        winner = determine_winner(player, computer)

        if winner == "draw":
            print("🤝 It's a Draw!")
        elif winner == "player":
            print("🏆 You Win this round!")
            player_score += 1
        else:
            print("💻 Computer Wins this round!")
            computer_score += 1

    print(f"\n{'='*40}")
    print(f"  Final Score after {rounds} rounds:")
    print(f"  You      : {player_score}")
    print(f"  Computer : {computer_score}")

    if player_score > computer_score:
        print("  🥇 Overall Winner: YOU! 🎉")
    elif computer_score > player_score:
        print("  🤖 Overall Winner: Computer!")
    else:
        print("  🤝 Overall: It's a Tie!")
    print("=" * 40)

if __name__ == "__main__":
    play_game()
