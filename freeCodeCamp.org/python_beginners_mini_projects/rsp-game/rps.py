#rock paper scissors game

import sys
import random
from enum import Enum

game_count = 0

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")

# Initialize scores
player_score = 0
computer_score = 0
def get_player_choice():
    player_choice = input(
        "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
    player = int(player_choice)
    if player not in [1, 2, 3]:
        sys.exit("Invalid input. You must enter 1, 2, or 3.")
    return player

def get_computer_choice():
    computer_choice = random.choice("123")
    return int(computer_choice)

def determine_winner(player, computer):
    if player == 1 and computer == 3:
        return "player"
    elif player == 2 and computer == 1:
        return "player"
    elif player == 3 and computer == 2:
        return "player"
    elif player == computer:
        return "tie"
    else:
        return "computer"

def print_choices(player, computer):
    print("")
    print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

def print_winner(winner):
    if winner == "player":
        print("🎉 You win!")
    elif winner == "computer":
        print("🐍 Python wins!")
    else:
        print("😲 Tie game!")

def print_final_scores(player_score, computer_score):
    print("\nFinal Scores:")
    print("You: " + str(player_score))
    print("Python: " + str(computer_score))

    if player_score > computer_score:
        print("🎉 You win the game!")
    elif player_score < computer_score:
        print("🐍 Python wins the game!")
    else:
        print("😲 It's a tie!")

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

def play_again():
    choice = input("\nDo you want to play again? (Y to play again, Q to quit): ").strip().upper()
    if choice == 'Y':
        play_rps_game()
    elif choice == 'Q':
        print("Thanks for playing!")
        sys.exit()
    else:
        print("Invalid input. Please enter Y to play again or Q to quit.")
        play_again()

def play_rps_game():
    player_score = 0
    computer_score = 0

    for _ in range(3):
        player = get_player_choice()
        computer = get_computer_choice()

        print_choices(player, computer)

        winner = determine_winner(player, computer)
        print_winner(winner)

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

    print_final_scores(player_score, computer_score)
    play_again()

# Call the function to play the game
play_rps_game()