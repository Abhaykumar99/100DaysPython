# ============================================================
# Day 11: Exercise — Time Greeting Program
# ============================================================
# Based on the current hour, greet the user appropriately.
# ============================================================

import datetime

current_hour = datetime.datetime.now().hour
print(f"Current Hour: {current_hour}:00")

if 5 <= current_hour < 12:
    greeting = "Good Morning 🌅"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon ☀️"
elif 17 <= current_hour < 21:
    greeting = "Good Evening 🌆"
else:
    greeting = "Good Night 🌙"

name = input("Enter your name: ")
print(f"\n{greeting}, {name}!")
print("Welcome to your Python journey!")
