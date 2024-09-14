# rock paper scissors game

import sys
import random
from enum import Enum

# Enum for Rock, Paper, Scissors choices
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Class to handle the Rock, Paper, Scissors game logic
class RPSGame:
    def __init__(self):
        # Initialize game counters
        self.game_count = 0
        self.player_wins = 0
        self.computer_wins = 0

    # Get player's choice
    def get_player_choice(self):
        player_choice = input(
            "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
        player = int(player_choice)
        if player not in [1, 2, 3]:
            sys.exit("Invalid input. You must enter 1, 2, or 3.")
        return player

    # Get computer's choice
    def get_computer_choice(self):
        computer_choice = random.choice("123")
        return int(computer_choice)

    # Closure to determine and print the winner
    def determine_winner_closure(self):
        def determine_winner(player, computer):
            if player == 1 and computer == 3:
                winner = "player"
            elif player == 2 and computer == 1:
                winner = "player"
            elif player == 3 and computer == 2:
                winner = "player"
            elif player == computer:
                winner = "tie"
            else:
                winner = "computer"
            
            return winner

        def print_winner(winner):
            if winner == "player":
                print("🎉 You win!")
            elif winner == "computer":
                print("🐍 Python wins!")
            else:
                print("😲 Tie game!")

        return determine_winner, print_winner

    # Print the choices made by player and computer
    def print_choices(self, player, computer):
        print("")
        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        print("")

    # Print the final scores of the game
    def print_final_scores(self, player_score, computer_score):
        print("\nFinal Scores:")
        print("You: " + str(player_score))
        print("Python: " + str(computer_score))

        if player_score > computer_score:
            print("\n🎉 You win the game!")
        elif player_score < computer_score:
            print("🐍 Python wins the game!")
        else:
            print("😲 It's a tie!")

        self.game_count += 1
        print("\nGame count: " + str(self.game_count))

    # Print the overall scores of all games played
    def print_overall_scores(self):
        print(f"\nOverall Scores -> Player: {self.player_wins}, Computer: {self.computer_wins}")

    # Ask the player if they want to play again
    def play_again(self):
        choice = input("\nDo you want to play again? (Y to play again, Q to quit): ").strip().upper()
        if choice == 'Y':
            self.play_rps_game()
        elif choice == 'Q':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter Y to play again or Q to quit.")
            self.play_again()

    # Main game loop for playing Rock, Paper, Scissors
    def play_rps_game(self):
        player_score = 0
        computer_score = 0

        determine_winner, print_winner = self.determine_winner_closure()

        for _ in range(3):
            player = self.get_player_choice()
            computer = self.get_computer_choice()

            self.print_choices(player, computer)

            winner = determine_winner(player, computer)
            print_winner(winner)

            if winner == "player":
                player_score += 1
            elif winner == "computer":
                computer_score += 1

        if player_score > computer_score:
            self.player_wins += 1
        elif player_score < computer_score:
            self.computer_wins += 1

        self.print_final_scores(player_score, computer_score)
        self.print_overall_scores()
        self.play_again()

# Create an instance of the game and start it
game = RPSGame()
game.play_rps_game()