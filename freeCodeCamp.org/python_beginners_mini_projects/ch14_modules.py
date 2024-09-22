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

from rps import RPSGame



import kansas

print(pi)

# for item in dir(rdm):
#     print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

RPSGame()