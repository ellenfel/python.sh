# Modules are files containing Python code that can define functions, 
# classes, and variables, and can also include runnable code.

from math import pi
import sys
import random as rdm
from enum import Enum
import os

# Add the directory containing rps.py to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'rsp-game'))

try:
    from rps import RPSGame
except ImportError:
    print("Module rps not found. Please ensure 'Desktop/workenv/python/python_roadmap.sh/freeCodeCamp.org/python_beginners_mini_projects/rsp-game/rps.py' exists.")
    sys.exit(1)

print(pi)

# for item in dir(rdm):
#     print(item)

# Create an instance of RPSGame and start the game
game = RPSGame()
game.play_rps_game()