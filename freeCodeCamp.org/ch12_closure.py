#closure
"""
This module demonstrates the concept of closures in Python.

A closure is a function object that has access to variables 
in its lexical scope, even when the function is called outside 
that scope. Closures are created by defining a function inside 
another function and returning the inner function.

"""


def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()