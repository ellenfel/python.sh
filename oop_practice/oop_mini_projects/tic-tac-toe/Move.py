class Move:
    def __init__(self, value):
            self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        return 1 <= self._value <= 9

    def get_row(self):
        if self._value in (1,2,3):
            return 0  # First row
        elif self._value in (4,5,6):
            return 1  # Second row
        else:
            return 2  # Third row

    def get_column(self):
        if self._value in (1,4,7):
            return 0  # First column
        elif self._value in (2,5,8):
            return 1  # Second column
        else:
            return 2  # Third column



# # # # # # T E S T I N G # # # # # #

# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |

#move = Move(1)
#print(move.value)
#print(move.is_valid())

#move1 = Move(0)
#print(move1.value)
#print(move1.is_valid())

#move = Move(3)
#print(move.get_row())
#print(move.get_column())