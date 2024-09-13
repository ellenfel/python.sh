#scope
"""
This module demonstrates the concept of scope in Python.

Scopes in Python:
- Global Scope: Variables defined at the top level of a script or module.
- Local Scope: Variables defined inside a function.
- Enclosing Scope: Variables in the local scope of enclosing functions.
- Built-in Scope: Names preassigned in the built-in names module.

Functions:
- another(): Demonstrates the use of global and nonlocal keywords to modify variables in different scopes.
"""


# global scope
name = "Dave"
count = 1


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()