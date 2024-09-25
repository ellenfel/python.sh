# Modules are files containing Python code that can define functions, 
# classes, and variables, and can also include runnable code.

from math import pi
import sys
import random as rdm
from enum import Enum
import os
import argparse

# Add the directory containing rps.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'rsp-game'))

try:
    from rps import RPSGame
except ImportError:
    sys.exit(1)

# Set up argument parsing
parser = argparse.ArgumentParser(description="Play Rock-Paper-Scissors game.")
parser.add_argument(
    "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
)
args = parser.parse_args()

print(pi)

# for item in dir(rdm):
#     print(item)

# Create an instance of RPSGame and start the game
game = RPSGame(name=args.name)
game.play_rps_game()