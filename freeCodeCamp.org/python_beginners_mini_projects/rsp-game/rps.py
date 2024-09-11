#rock paper scissors game

import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")

# Initialize scores
player_score = 0
computer_score = 0

# Run the game for 3 rounds
for _ in range(3):
    playerchoice = input(
        "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)
    if player not in [1, 2, 3]:
        sys.exit("Invalid input. You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("")
    # Convert the 'computer' enum value to a string without the 'RPS.' prefix
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    if player == 1 and computer == 3:
        print("🎉 You win!")
        player_score += 1
    elif player == 2 and computer == 1:
        print("🎉 You win!")
        player_score += 1
    elif player == 3 and computer == 2:
        print("🎉 You win!")
        player_score += 1
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")
        computer_score += 1

# Print final scores
print("\nFinal Scores:")
print("You: " + str(player_score))
print("Python: " + str(computer_score))

# Determine the winner
if player_score > computer_score:
    print("🎉 You win the game!")
elif player_score < computer_score:
    print("🐍 Python wins the game!")
else:
    print("😲 It's a tie!")