"""
Rock paper scissors
"""
import random

choice_list = ["Rock", "Paper", "Scissors"]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
ai_choice = random.randint(0, 2)

print(f"You chose {choice_list[choice]}")
print(f"Computer chose {choice_list[ai_choice]}")

if choice < 0 or choice > 2:
    print("You chose a number outside the range of 0 and 2, you lose")
elif choice == 0 and ai_choice == 2:
    print("You win")
elif ai_choice == 0 and ai_choice == 2:
    print("You lose")
elif ai_choice > choice:
    print("You lose")
elif ai_choice < choice:
    print("You win")
elif choice == ai_choice:
    print("You tie")
