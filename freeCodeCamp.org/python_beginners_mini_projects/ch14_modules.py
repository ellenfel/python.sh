# Modules are files containing Python code that can define functions, 
# classes, and variables, and can also include runnable code.

from math import pi
import sys
import random as rdm
from enum import Enum
import kansas
from rsp import rock_paper_scissors

print(pi)

# for item in dir(rdm):
#     print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

rock_paper_scissors()